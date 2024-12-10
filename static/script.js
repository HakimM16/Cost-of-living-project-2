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
                        <th>Total</th>
                        <th>${result.totals.city1}</th>
                        <th>${result.totals.city2}</th>
                    </tr>
                </tfoot>
            </table>
        `;
    } else {
        document.getElementById("result").innerText = "Error: " + result.error;
    }
});
