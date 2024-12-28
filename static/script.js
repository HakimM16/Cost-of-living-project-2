/* Dropdown Function */
const input = document.getElementById("city2");
const dropdown = document.getElementById("city2-list");

input.addEventListener("click", function () {
  dropdown.style.display = "block";
});

dropdown.addEventListener("click", function (e) {
  if (e.target && e.target.matches(".city-option")) {
    input.value = e.target.innerText;
    dropdown.style.display = "none";
  }
});

document.addEventListener("click", function (event) {
  if (!input.contains(event.target) && !dropdown.contains(event.target)) {
    dropdown.style.display = "none";
  }
});

/* Tooltips section */
const tooltips = {
  rent: "Cost of your monthly accommodation.",
  fitness: "Gym memberships or other fitness-related expenses.",
  food: "Grocery bills or eating out expenses.",
  clothes: "Clothing, shoes, and other wearable items.",
  transport: "Public transport, fuel, or car maintenance costs.",
  debts: "Loan repayments, credit card payments, etc.",
  luxuries: "Non-essential items like entertainment or gadgets.",
  utilities: "Electricity, water, internet, and other household utilities.",
};

// Add tooltips dynamically
document.querySelectorAll("label").forEach((label) => {
  const forAttr = label.getAttribute("for");
  if (tooltips[forAttr]) {
    const tooltip = document.createElement("span");
    tooltip.className = "tooltip";
    tooltip.setAttribute("data-tooltip", tooltips[forAttr]);
    tooltip.textContent = "?";
    label.appendChild(tooltip);
  }
});


// Real-Time Expense Calculation
const expenseFields = document.querySelectorAll("#rent, #fitness, #food, #clothes, #transport, #debts, #luxuries, #utilities");

// Create and display real-time total summary card
const summaryCard = document.createElement("div");
summaryCard.id = "summaryCard";
summaryCard.style.marginTop = "20px";
summaryCard.style.padding = "20px";
summaryCard.style.borderRadius = "8px";
summaryCard.style.backgroundColor = "#00abf0"; // Bright blue background
summaryCard.style.color = "#fff"; // White text
summaryCard.style.boxShadow = "0 4px 6px rgba(0, 0, 0, 0.1)";
summaryCard.style.maxWidth = "400px";
summaryCard.style.margin = "20px auto";
summaryCard.style.fontFamily = "Arial, sans-serif";
summaryCard.style.fontSize = "1rem";
summaryCard.style.lineHeight = "1.5";

document.body.appendChild(summaryCard);

function calculateTotal() {
  let total = 0;
  let breakdown = "";

  expenseFields.forEach((field) => {
    const value = parseFloat(field.value) || 0; // Default to 0 if no value entered
    total += value;

    breakdown += `<li><strong>${field.previousElementSibling.textContent}</strong> £${value.toFixed(2)}</li>`;
  });

  summaryCard.innerHTML = `
    <h3>Expense Summary</h3>
    <ul style="list-style-type: none; padding: 0; margin: 0;">
      ${breakdown}
    </ul>
    <p style="margin-top: 10px; font-weight: bold; text-align: center;">Total Expenses: £${total.toFixed(2)}</p>
  `;
}

// Add input event listener to each expense field
expenseFields.forEach((field) => {
  field.addEventListener("input", calculateTotal);
});

// Run calculation on load to show default summary
calculateTotal();

// Weather fetching function
const apiKey = "99ff24c012144fb4582bdbb87e7f6612"; // Replace with your OpenWeatherMap API key

async function fetchWeather(city) {
  try {
    const response = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`
    );
    if (!response.ok) {
      throw new Error(`Error fetching weather for ${city}`);
    }
    const data = await response.json();
    return {
      temperature: data.main.temp,
      weather: data.weather[0].description,
      icon: `https://openweathermap.org/img/wn/${data.weather[0].icon}.png`,
    };
  } catch (error) {
    console.error(error);
    return null;
  }
}


// Function to render the comparison chart
function renderComparisonChart(city1, city2, city1Data, city2Data) {
  const categories = Object.keys(city1Data); // Ensure consistent order of categories
  const city1Values = categories.map((key) => city1Data[key]); // Values in order
  const city2Values = categories.map((key) => city2Data[key]); // Ensure same order as categories

  const ctx = document.getElementById("comparisonChart").getContext("2d");

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: categories, // Expense categories
      datasets: [
        {
          label: `Expenses in ${city1}`,
          data: city1Values,
          backgroundColor: "rgba(54, 162, 235, 0.6)",
          borderColor: "rgba(54, 162, 235, 1)",
          borderWidth: 1,
        },
        {
          label: `Expenses in ${city2}`,
          data: city2Values,
          backgroundColor: "rgba(255, 99, 132, 0.6)",
          borderColor: "rgba(255, 99, 132, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}


// Event listener for form submission
document.getElementById("comparisonForm").addEventListener("submit", async (event) => {
  event.preventDefault();

  // Gather inputs
  const city1 = document.getElementById("city1").value;
  const city2 = document.getElementById("city2").value;

  const expenses = {
    rent: parseFloat(document.getElementById("rent").value),
    fitness: parseFloat(document.getElementById("fitness").value),
    food: parseFloat(document.getElementById("food").value),
    clothes: parseFloat(document.getElementById("clothes").value),
    transport: parseFloat(document.getElementById("transport").value),
    debts: parseFloat(document.getElementById("debts").value),
    luxuries: parseFloat(document.getElementById("luxuries").value),
    utilities: parseFloat(document.getElementById("utilities").value),
  };

  // Fetch weather data for both cities
  const weatherCity1 = await fetchWeather(city1);
  const weatherCity2 = await fetchWeather(city2);

  // Send data to backend
  const response = await fetch("/compare", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ city1, city2, expenses_city1: expenses }),
  });

  const result = await response.json();

  // Display results and render chart
  if (response.ok) {
    document.getElementById("result").innerHTML = `
      <h2>Comparison</h2>
      <table>
        <thead>
          <tr>
            <th>Expense</th>
            <th>${result.city1}</th>
            <th>${result.city2}</th>
          </tr>
        </thead>
        <tbody>
          ${Object.keys(expenses)
            .map(
              (key) => `
              <tr>
                <td>${key}</td>
                <td>${expenses[key]}</td>
                <td>${result.average_city2[key]}</td>
              </tr>
            `
            )
            .join("")}
        </tbody>
        <tfoot>
          <tr>
            <th>Total (£)</th>
            <th>${result["totals"].city1}</th>
            <th>${result["totals"].city2}</th>
          </tr>
        </tfoot>
      </table>

      <div id="weather">
        <h3>Weather</h3>
        <div style="display: flex; justify-content: space-around;">
          <div>
            <h4>${result.city1}</h4>
            ${
              weatherCity1
                ? `<p>Temperature: ${weatherCity1.temperature}°C</p>
                  <p>${weatherCity1.weather}</p>
                  <img src="${weatherCity1.icon}" alt="${weatherCity1.weather}" />`
                : `<p>Weather data not available.</p>`
            }
          </div>
          <div>
            <h4>${result.city2}</h4>
            ${
              weatherCity2
                ? `<p>Temperature: ${weatherCity2.temperature}°C</p>
                  <p>${weatherCity2.weather}</p>
                  <img src="${weatherCity2.icon}" alt="${weatherCity2.weather}" />`
                : `<p>Weather data not available.</p>`
            }
          </div>
        </div>
      </div>
    `;

    // Render the comparison chart
    renderComparisonChart(result.city1, result.city2, expenses, result.average_city2);
  } else {
    document.getElementById("result").innerText = "Error: " + result.error;
  }
});


