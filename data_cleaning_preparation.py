"""
clean_hp_data.py

Data cleaning and preparation script for the Harry Potter characters dataset.

Goals:
- Handle missing values in key categorical columns
- Standardize text values (e.g., house names, gender)
- Select relevant columns for analysis
- Create a clean dataset ready for analysis and visualization

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
    return pd.read_csv(csv_path)

def clean_categorical_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize key categorical columns:
    - Fill missing values with 'Unknown'
    - Strip whitespace
    - Standardize text to title case where applicable

    Parameters:
    - df (pd.DataFrame): Original dataset.

    Returns:
    - pd.DataFrame: Cleaned dataset.
    """
    categorical_cols = ["house", "gender", "species"]

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")
            df[col] = df[col].astype(str).str.strip()

    return df

def select_relevant_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Select only the columns relevant for the analysis phase.

    Parameters:
    - df (pd.DataFrame): Cleaned dataset.

    Returns:
    - pd.DataFrame: Dataset with selected columns.
    """
    selected_columns = ["name", "house", "gender", "species", "alive"]

    existing_columns = [col for col in selected_columns if col in df.columns]
    df_selected = df[existing_columns].copy()

    return df_selected

def save_clean_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save the cleaned dataset to a new CSV file.

    Parameters:
    - df (pd.DataFrame): Cleaned dataset.
    - output_path (str): Output CSV file path.
    """
    df.to_csv(output_path, index=False)
    print(f"✅ Clean dataset saved to: {output_path}")

def main():
    """
    Main function to execute the data cleaning workflow.
    """
    INPUT_CSV_PATH = "harry_potter_characters.csv"
    OUTPUT_CSV_PATH = "harry_potter_characters_clean.csv"

    print("🔍 Loading raw dataset...")
    df = load_data(INPUT_CSV_PATH)

    print("🧹 Cleaning categorical columns...")
    df_cleaned = clean_categorical_columns(df)

    print("✂️ Selecting relevant columns for analysis...")
    df_selected = select_relevant_columns(df_cleaned)

    print("💾 Saving cleaned dataset...")
    save_clean_data(df_selected, OUTPUT_CSV_PATH)

    print("🎉 Data cleaning step completed successfully!")

if __name__ == "__main__":
    main()
