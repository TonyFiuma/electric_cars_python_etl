import pandas as pd
import os

# Direct URL of the CSV file
csv_url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'

# Path of the destination folder
output_dir = r"C:\Users\antonio.fiumano\******\ETL_Pandas_ElectricCar_USA\data_file"

# Create the folder if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Full path for the output CSV file
output_file = os.path.join(output_dir, 'Electric_Vehicle_Population_Data.csv')

# Extract the CSV file into a DataFrame
try:
    df = pd.read_csv(csv_url)
    print("Data extracted successfully!")

    # Save the DataFrame to a CSV file in the specified folder
    df.to_csv(output_file, index=False)
    print(f"CSV file saved as '{output_file}'")
except Exception as e:
    print(f"Error during extraction: {e}")
