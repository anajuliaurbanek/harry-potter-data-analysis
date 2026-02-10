"""
analysis_hp.py

Data analysis and visualization script for the cleaned Harry Potter characters dataset.

Goals:
- Perform descriptive analysis on key categorical variables
- Generate plots for portfolio documentation
- Save figures as image files for use in the project README

Technologies:
- Python
- pandas
- matplotlib
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def load_clean_data(csv_path: str) -> pd.DataFrame:
    """
    Load the cleaned CSV dataset into a pandas DataFrame.

    Parameters:
    - csv_path (str): Path to the cleaned CSV file.

    Returns:
    - pd.DataFrame: Loaded dataset.
    """
    return pd.read_csv(csv_path)

def ensure_output_dir(dir_path: str) -> None:
    """
    Ensure that the output directory for plots exists.

    Parameters:
    - dir_path (str): Path to the directory.
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"📁 Created directory: {dir_path}")

def plot_bar(series: pd.Series, title: str, xlabel: str, ylabel: str, output_path: str) -> None:
    """
    Generate and save a bar chart from a pandas Series.

    Parameters:
    - series (pd.Series): Value counts to plot
    - title (str): Plot title
    - xlabel (str): Label for x-axis
    - ylabel (str): Label for y-axis
    - output_path (str): File path to save the plot
    """
    plt.figure(figsize=(8, 5))
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"📊 Plot saved: {output_path}")

def analyze_house_distribution(df: pd.DataFrame, output_dir: str) -> None:
    """
    Analyze and plot the distribution of characters by house.
    """
    house_counts = df["house"].value_counts()
    plot_bar(
        series=house_counts,
        title="Character Distribution by House",
        xlabel="House",
        ylabel="Number of Characters",
        output_path=os.path.join(output_dir, "characters_by_house.png")
    )

def analyze_gender_distribution(df: pd.DataFrame, output_dir: str) -> None:
    """
    Analyze and plot the distribution of characters by gender.
    """
    gender_counts = df["gender"].value_counts()
    plot_bar(
        series=gender_counts,
        title="Character Distribution by Gender",
        xlabel="Gender",
        ylabel="Number of Characters",
        output_path=os.path.join(output_dir, "characters_by_gender.png")
    )

def analyze_species_distribution(df: pd.DataFrame, output_dir: str) -> None:
    """
    Analyze and plot the top 10 most common species.
    """
    species_counts = df["species"].value_counts().head(10)
    plot_bar(
        series=species_counts,
        title="Top 10 Most Common Species",
        xlabel="Species",
        ylabel="Number of Characters",
        output_path=os.path.join(output_dir, "top_species.png")
    )

def analyze_alive_distribution(df: pd.DataFrame, output_dir: str) -> None:
    """
    Analyze and plot the distribution of alive vs deceased characters.
    """
    alive_counts = df["alive"].value_counts()
    plot_bar(
        series=alive_counts,
        title="Alive vs Deceased Characters",
        xlabel="Status",
        ylabel="Number of Characters",
        output_path=os.path.join(output_dir, "alive_vs_deceased.png")
    )

def analyze_house_vs_alive(df: pd.DataFrame, output_dir: str) -> None:
    """
    Analyze and plot house vs survival status.
    """
    cross_tab = pd.crosstab(df["house"], df["alive"])
    cross_tab.plot(kind="bar", stacked=True, figsize=(9, 6))
    plt.title("House vs Survival Status")
    plt.xlabel("House")
    plt.ylabel("Number of Characters")
    plt.tight_layout()
    output_path = os.path.join(output_dir, "house_vs_alive.png")
    plt.savefig(output_path)
    plt.close()
    print(f"📊 Plot saved: {output_path}")

def main():
    """
    Main function to run all analyses and generate plots.
    """
    CLEAN_CSV_PATH = "harry_potter_characters_clean.csv"
    OUTPUT_DIR = "images"

    print("🔍 Loading cleaned dataset...")
    df = load_clean_data(CLEAN_CSV_PATH)

    print("📁 Ensuring output directory exists...")
    ensure_output_dir(OUTPUT_DIR)

    print("📊 Generating plots...")
    analyze_house_distribution(df, OUTPUT_DIR)
    analyze_gender_distribution(df, OUTPUT_DIR)
    analyze_species_distribution(df, OUTPUT_DIR)
    analyze_alive_distribution(df, OUTPUT_DIR)
    analyze_house_vs_alive(df, OUTPUT_DIR)

    print("🎉 Analysis and visualization completed successfully!")

if __name__ == "__main__":
    main()
