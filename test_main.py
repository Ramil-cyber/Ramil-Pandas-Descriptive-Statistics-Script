from main import read_csv, get_descriptive_stats, get_histogram, get_line_graph
import pandas as pd

file_path = "Health_Sleep_Statistics.csv"


def test_main():
    df = read_csv(file_path)

    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 100
    assert not df.empty

    # Check if all required columns are present
    expected_columns = [
        "User ID",
        "Age",
        "Gender",
        "Sleep Quality",
        "Bedtime",
        "Wake-up Time",
        "Daily Steps",
        "Calories Burned",
        "Physical Activity Level",
        "Dietary Habits",
        "Sleep Disorders",
        "Medication Usage",
    ]
    assert all(column in df.columns for column in expected_columns)
    # Check if 'Age' is within a realistic range
    assert df["Age"].between(0, 120).all()
    # Check if 'Sleep Quality' is between 1 and 10
    assert df["Sleep Quality"].between(1, 10).all()
    # Check for missing values in required columns
    required_columns = ["User ID", "Age", "Gender", "Sleep Quality"]
    assert df[required_columns].notnull().all().all()
