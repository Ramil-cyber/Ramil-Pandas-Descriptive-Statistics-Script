# Descriptive Statistics Script with Pandas

This project contains a Python script that uses Pandas to compute descriptive statistics for a dataset and generate data visualizations. The script reads data from a CSV or Excel file and provides key summary statistics such as the mean, median, and standard deviation.

## Features

- Reads a dataset from a CSV or Excel file.
- Generates summary statistics:
  - Mean
  - Median
  - Standard Deviation
- Produces at least one data visualization (e.g., histogram, boxplot, etc.).
- Continuous Integration/Continuous Deployment (CI/CD) pipeline integrated with a build status badge.

## Visualizations

- **Histogram**:  
  ![Histogram](https://github.com/nogibjj/Ramil-Pandas-Descriptive-Statistics-Script/blob/d74cda0b22c4c8af5769c23a238e6abf22bbbb0f/image/histogram.png)
  
- **Line Graph**:  
  ![Line Graph](https://github.com/nogibjj/Ramil-Pandas-Descriptive-Statistics-Script/blob/d74cda0b22c4c8af5769c23a238e6abf22bbbb0f/image/linegraph.png)




## Summary Statistics Report

You can view the detailed summary statistics report generated in PDF format here:
- [Summary Statistics Report (PDF)](https://github.com/nogibjj/Ramil-Pandas-Descriptive-Statistics-Script/blob/70640a6208f36e5eefc99eb1a5544ae82d2f1eb4/Summary-Statistics.pdf)


## Requirements

- Python 3.x
- Pandas
- Matplotlib or Seaborn (for visualization)
- pytest (for testing)

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/repo-name.git
    cd repo-name
    ```

2. **Install required dependencies**:
    You can install all required packages by running:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**:
    To run the descriptive statistics script, use the following command:
    ```bash
    python main.py
    ```

## Usage

- Place your dataset in the project directory.
- Modify the script (`main.py`) to specify the path to your CSV or Excel file.
  
The script will automatically compute and display the descriptive statistics, and generate the data visualization.

## Running Tests

The project includes tests to ensure the correctness of the script. To run the tests, use:

```bash
make test
```

## Linting
To ensure code quality, Pylint is used. You can check for linting issues by running:

```bash
make lint
```
