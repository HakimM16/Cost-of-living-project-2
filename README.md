# 🌍 Cost of Living Comparison

**Cost of Living Comparison** is a web-based application that helps users evaluate and compare living expenses between two cities. Whether you're planning a move, budgeting for travel, or simply curious, this tool offers an intuitive way to make informed, data-driven financial decisions.

---

## ✨ Key Features

* 💰 **Custom Expense Input** – Enter your personal expenses (e.g., rent, groceries, transport) for a selected city.
* 🔁 **City-to-City Comparison** – Compare your expenses against average costs in another city.
* 📊 **Visual Cost Breakdown** – Get a clear, visual summary of cost differences.
* 🧠 **Smarter Decisions** – Use data insights to guide relocation, job changes, or budgeting.

---

## 🛠️ Tech Stack

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python (Flask)
* **API Integration**: OpenWeatherMap (for city-based weather context)

---

## 🚀 How It Works

1. **Enter Your Expenses** – Provide your monthly costs for your current city.
2. **Choose a Comparison City** – Select another city to compare against.
3. **Analyse the Difference** – The app fetches average living cost data and calculates the variance.
4. **View Results** – Explore an intuitive breakdown of cost categories to understand key differences.

---

## 🧪 Installation & Setup

To run the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/HakimM16/Cost-of-living-project-2.git
   cd cost-of-living-project-2
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   flask run
   ```

5. Open your browser and go to `http://localhost:5000`

---

## 📌 Notes

* API key for OpenWeatherMap is required (add it to your environment or config file).
* Default average cost data may be mocked or simplified — real-time integration is planned for future releases.

---
