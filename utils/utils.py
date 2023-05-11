import pandas as pd
import os


def export_data(data_folder):
    year_to_data = {}
    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):
            filepath = os.path.join(data_folder, filename)
            df = pd.read_csv(filepath)

            year = int(filename.split("_")[0][:-4])

            if year not in year_to_data:
                year_to_data[year] = df
            else:
                year_to_data[year] = pd.concat([year_to_data[year], df])
    return dict(sorted(year_to_data.items()))


def bring_to_common_column_name(year_to_data, year_to_column_name, replace_to):
    for year, df in year_to_data.items():
        rank_column_name = year_to_column_name[year]
        if rank_column_name in df.columns:
            df.rename(columns={rank_column_name: replace_to}, inplace=True)
    return year_to_data
