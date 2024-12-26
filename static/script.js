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

  // Send data to backend
  const response = await fetch("/compare", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ city1, city2, expenses_city1: expenses }),
  });

  const result = await response.json();

  // Display results
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
    `;
  } else {
    document.getElementById("result").innerText = "Error: " + result.error;
  }
});
