# Oil Price Statistical Modeling

A comprehensive project analyzing the impact of significant political and economic events on Brent oil prices. This repository includes data preprocessing scripts, statistical modeling using ARIMA and LSTM, exploratory data analysis (EDA) visualizations, and an interactive dashboard built with Flask and React. The goal is to provide actionable insights for investors, policymakers, and energy companies navigating the complexities of the oil market.

## Project Directory Structure

The repository is organized as follows:

- **`.github/workflows/`**: Contains GitHub Actions for CI/CD and automated testing.
- **`.vscode/`**: Development configuration for Visual Studio Code.
- **`notebooks/`**: Jupyter notebooks for data exploration, feature engineering, and model prototyping.
- **`scripts/`**: Scripts for data preprocessing, visualization, and model building.
- **`tests/`**: Unit tests for model integrity and data processing functions.

---

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/epythonlab/oil-price-statistical-modeling.git
   cd oil-price-statistical-modeling
   ```

2. **Set Up a Virtual Environment**

   **For Linux/MacOS:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **For Windows:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

---