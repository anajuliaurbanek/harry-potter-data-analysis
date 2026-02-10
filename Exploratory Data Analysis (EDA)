"""
eda_hp.py

Exploratory Data Analysis (EDA) script for the Harry Potter characters dataset.

Goals:
- Understand the dataset structure
- Inspect available columns
- Identify missing values
- Explore unique values in key categorical columns

Technologies:
- Python
- pandas
"""

import pandas as pd

def load_data(csv_path: str) -> pd.DataFrame:
    """
    Load the CSV dataset into a pandas DataFrame.

    Parameters:
    - csv_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded dataset.
    """
    df = pd.read_csv(csv_path)
    return df

def basic_info(df: pd.DataFrame) -> None:
    """
    Display basic information about the dataset:
    - Shape (rows and columns)
    - Data types
    - First rows of the dataset
    """
    print("\n📌 Dataset shape (rows, columns):")
    print(df.shape)

    print("\n📌 Data types by column:")
    print(df.dtypes)

    print("\n📌 First 5 rows of the dataset:")
    print(df.head())

def missing_values_report(df: pd.DataFrame) -> None:
    """
    Display the number and percentage of missing values per column.
    """
    print("\n📌 Missing values report:")
    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100

    missing_df = pd.DataFrame({
        "Missing Values": missing_count,
        "Percentage (%)": missing_percent.round(2)
    })

    print(missing_df.sort_values(by="Missing Values", ascending=False))

def unique_values_report(df: pd.DataFrame, columns: list) -> None:
    """
    Display unique values and their counts for selected columns.

    Parameters:
    - df (pd.DataFrame): Dataset
    - columns (list): List of column names to analyze
    """
    for col in columns:
        if col in df.columns:
            print(f"\n📌 Unique values in column '{col}':")
            print(df[col].value_counts(dropna=False))
        else:
            print(f"\n⚠️ Column '{col}' not found in the dataset.")

def main():
    """
    Main function to run the EDA workflow.
    """
    CSV_PATH = "harry_potter_characters.csv"  # Adjust path if needed

    print("🔍 Loading dataset...")
    df = load_data(CSV_PATH)

    print("📊 Basic dataset information:")
    basic_info(df)

    print("🧹 Missing values analysis:")
    missing_values_report(df)

    print("🔎 Unique values analysis (key columns):")
    columns_to_analyze = ["house", "gender", "species", "alive"]
    unique_values_report(df, columns_to_analyze)

    print("\n✅ EDA completed successfully!")

if __name__ == "__main__":
    main()
