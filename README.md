# Quantium Dash Data Visualisation Project

A data processing and visualisation project for **Soul Foods’ Pink Morsel sales**, built using **Python, Pandas, and Dash**.  
This project transforms raw transactional CSV data into actionable insights through interactive charts and region-based filters.

---

## 📊 Project Overview

**Goal:**  
To answer the business question —  
> “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?”

This project:
1. Cleans and processes multiple raw CSV datasets.
2. Combines them into a single structured dataset (`sales`, `date`, `region`).
3. Builds an interactive Dash dashboard for visual analysis.
4. Includes automated testing and CI integration for reliability.

---

## 🧩 Tech Stack

- **Python 3.9+**
- **Pandas** — data cleaning and transformation  
- **Plotly Dash** — data visualisation and interactivity  
- **Pytest** + **dash[testing]** — automated testing  
- **Git + CI/CD** — version control and automation  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/quantium-starter-repo.git
cd quantium-starter-repo
```
```bash
python3 -m venv .quantium
source .quantium/bin/activate     # On Windows: .quantium\Scripts\activate
```
```bash
pip install dash pandas plotly pytest "dash[testing]"
```

<h1>🧮 Data Processing</h1><br>

All raw data is located in the data/ folder.<br>
The preprocessing script:<br>

1.Filters only Pink Morsel products<br>
2.Computes total sales (price × quantity)<br>
3.Retains only the sales, date, and region fields<br>
4.Merges all three CSVs into one clean dataset<br>

<h1>Resulting output:</h1><br>

output_data.csv<br>

<h1>📈 Dash App</h1><br>

```bash
Run the app with:

python app.py


Access at http://127.0.0.1:8050
```
<h1>Features:</h1><br>

1. Header: “Pink Morsel Sales Dashboard”<br>
2. Interactive Line Chart: Sales over time<br>
3. Region Filter: Radio buttons for North, East, South, West, or All<br>
4. Annotation: Highlights the 15 Jan 2021 price increase<br>

<h1>🧪 Testing</h1><br>

All tests are located in test_app.py.<br>

```bash
To run tests manually

pytest -v

```

<h1>Tests verify:</h1><br>

Header is present<br>

Graph renders correctly<br>

Region picker exists<br>

<h1>🤖 Continuous </h1>><br>

The included Bash script run_tests.sh automates testing for CI environments.<br>

```bash
Run locally:
./run_tests.sh
```
```bash
<h1>🗂️ Repository Structure</h1><br>
quantium-starter-repo/<br>
│
├── data/                     # Raw input CSV files<br>
├── output_data.csv            # Processed dataset<br>
├── app.py                     # Main Dash application<br>
├── test_app.py                # Automated Dash tests<br>
├── run_tests.sh               # CI-compatible test runner<br>
├── requirements.txt           # Python dependencies<br>
└── README.md                  # Project documentation<br>
```
<h1>🧠 Insights</h1><br>

After visualisation, it becomes evident whether sales increased or decreased following the Pink Morsel price hike on 15 Jan 2021.<br>
This dashboard demonstrates how data processing + visualisation can turn raw data into clear business insights.<br>

<h1>🏁 Author</h1><br>

Gaurav Sharma<br>
Backend & Data Developer (Python + Flask)<br>