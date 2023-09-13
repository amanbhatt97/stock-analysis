# Stock Analysis Project

This is a project for analyzing stock data using Python. It includes various directories and files for data processing, modeling, and analysis.

## Project Structure

The project is organized into the following directories:

- `data`: Contains data related to the project.
- `models`: Stores trained machine learning models for stock prediction.
- `notebooks`: Jupyter notebooks for conducting analysis and experiments.
- `src`: Source code files for data fetching, data processing, and model training.
- `stock_env`: Environment directory for managing project dependencies.

## Contents

Here's a brief overview of the main contents of each directory:

### `data`

- `raw_data`: Raw stock data files.
- `processed_data`: Processed and cleaned data files.

### `models`

- Trained machine learning models for stock prediction, named by the day of prediction (e.g., `model_day1.pkl`, `model_day2.pkl`, etc.).

### `notebooks`

- Jupyter notebooks for stock analysis and experiments, including `analysis.ipynb`.

### `src`

- `data_fetch.py`: Python script for fetching stock data.
- `paths.py`: Configuration file for defining file paths.
- `symbols.py`: Configuration file for defining stock symbols and tickers.
- Other source code files for data processing and modeling.

### `stock_env`

- Environment directory for managing Python dependencies.

## Getting Started

1. Clone this repository to your local machine: git clone https://github.com/yourusername/stock-analysis-project.git
2. Set up a Python virtual environment (recommended): python -m venv stock_env
3. Activate the virtual environment:

- On Windows:

  ```
  stock_env\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source stock_env/bin/activate
  ```

4. Install project dependencies: pip install -r requirements.txt

## Usage

- Use the provided Jupyter notebooks in the `notebooks` directory for conducting stock analysis and experiments.

- The `src` directory contains source code for data fetching, data processing, and model training. You can modify and extend this code as needed.
