import pandas as pd

def transform(df):
    """
    Transformation logic for the DataFrame.

    Args:
        df: The input DataFrame containing electric vehicle data.

    Returns:
        A dictionary of transformed dimensions and fact table.
    """
    # Print the DataFrame columns for verification
    print("DataFrame columns:", df.columns.tolist())

    # Filter data to include only vehicles from 2023 onwards
    df = df[df['Model Year'] >= 2023]

    # Limit the records to a maximum of 1000
    df = df.head(1000)

    # Convert 'Electric Range' to numeric using .loc to avoid SettingWithCopyWarning
    df.loc[:, 'Electric Range'] = pd.to_numeric(df['Electric Range'], errors='coerce')

    # Creating dimensions
    electric_vehicle_dim = df[['VIN (1-10)', 'Make', 'Model', 'Electric Vehicle Type', 'Electric Range', 'County']].drop_duplicates().reset_index(drop=True)
    electric_vehicle_dim['vehicle_id'] = electric_vehicle_dim.index  # Create vehicle_id after dropping duplicates

    # Create county_dim and assign county_id
    county_dim = df[['County']].drop_duplicates().reset_index(drop=True)
    county_dim['county_id'] = county_dim.index

    # Merge to get county_id in electric_vehicle_dim
    electric_vehicle_dim = electric_vehicle_dim.merge(county_dim[['County', 'county_id']], on='County')

    # Retain only the county_id in electric_vehicle_dim
    electric_vehicle_dim = electric_vehicle_dim[['VIN (1-10)', 'Make', 'Model', 'Electric Vehicle Type', 'Electric Range', 'county_id', 'vehicle_id']]

    # Fact table
    fact_table = df[['VIN (1-10)', 'Model Year', 'Base MSRP']].copy()
    fact_table = fact_table.merge(electric_vehicle_dim[['vehicle_id', 'VIN (1-10)']], on='VIN (1-10)', how='left')

    # Save the transformed data to CSV files
    output_dir = r"C:\Users\antonio.fiumano\OneDrive - We-Plus S.p.A\Desktop\ETL_Pandas_ElectricCar_USA\data_file"
    electric_vehicle_dim.to_csv(f"{output_dir}\\electric_vehicle_dim.csv", index=False)
    county_dim.to_csv(f"{output_dir}\\county_dim.csv", index=False)
    fact_table.to_csv(f"{output_dir}\\fact_table.csv", index=False)

    return {
        "electric_vehicle_dim": electric_vehicle_dim.to_dict(orient="records"),
        "county_dim": county_dim.to_dict(orient="records"),
        "fact_table": fact_table.to_dict(orient="records")
    }

def test_output(output) -> None:
    """
    Template code for testing the output of the transform function.
    """
    assert output is not None, 'The output is undefined'
