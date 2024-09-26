import pandas as pd
from extract import output_file  # Import the path to the saved CSV
from transform import transform, test_output

# Load your DataFrame from the CSV file
df = pd.read_csv(output_file)

# Transform the DataFrame
transformed_data = transform(df)

# Test the output
test_output(transformed_data)

print("Transformation completed successfully!")
