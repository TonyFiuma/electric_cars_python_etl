# module
import os
from google.cloud import bigquery
from google.oauth2 import service_account

# Path to the Service Account JSON credentials file
key_path = "/home/axel_unix/projectetlpython1-3c975c20a048.json"

# Create credentials using the JSON file
credentials = service_account.Credentials.from_service_account_file(key_path)

# Create a BigQuery client using the credentials
client = bigquery.Client(credentials=credentials, project='projectetlpython1')

# Define the target table for loading data
target_table = 'projectetlpython1.sample_dataset.Electric_Population_Data.csv'

# Configure the job for loading data
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,            # Skip the header row in the CSV file
    source_format=bigquery.SourceFormat.CSV,  # Specify that the source file is a CSV
    autodetect=True,                # Automatically detect the schema of the CSV
    write_disposition='WRITE_TRUNCATE'
)

# File variables
cur_path = os.getcwd()                          # Get the current working directory
file_name = 'Electric_Vehicle_Population_Data.csv'                     # Name of the CSV file
file_path = os.path.join(cur_path, 'data_files', file_name)  # Construct the full file path

# Load the CSV file into the BigQuery table
try:
    with open(file_path, 'rb') as source_file:  # Open the file in binary mode
        load_job = client.load_table_from_file(
            source_file,
            target_table,
            job_config=job_config
        )

    load_job.result()  # Wait for the job to complete

    # Retrieve and print the number of rows in the destination table
    destination_table = client.get_table(target_table)
    print(f"You have {destination_table.num_rows} rows in your table")

except Exception as e:
    print("An error occurred while loading the CSV file:", e)
