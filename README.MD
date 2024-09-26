# Electric Vehicle Data Transformation

## Overview
This project is an ETL (Extract, Transform, Load) process built using Python and Pandas. It transforms electric vehicle data from a CSV file and an API into structured dimensions and a fact table, enabling better data analysis and relationships between different entities.

![Overview Image](images/PythonEtlChartJ.jpg)

## Data Source
The data used in this project is sourced from the Washington State open data portal. You can download the dataset [here](https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD).

## Usage Instructions
After executing the [`extract.py`](pandas_api_csv/extract.py) file, run the [`load.py`](pandas_api_csv/load.py) file to call the [`transform.py`](pandas_api_csv/transform.py) fufile and functions, which will extract the data and generate a CSV file.

![CSV](images/load_to_csv.jpg)

If you wish to load the transformed data into Google BigQuery (using your own credentials), you should execute the [`load_bigquery.py`](pandas_api_bigquery/load_bigquery.py) file after running the [`extract.py`](pandas_api_csv/extract.py) file.

![BIG QUERY](images/load_to_bigquery.jpg)

### Loading to CSV or to BIG QUERY
The transformed data will be saved in the following files:
- `electric_vehicle_dim.csv`
- `county_dim.csv`
- `fact_table.csv`

### Loading to BigQuery
In addition to CSV output, this project also supports loading the transformed data directly into Google BigQuery. Ensure you have your credentials set up properly for this to work.

## Contact
For further questions, please contact:
**Antonio Fiumanò**  
Data Engineer  
Email: [axelfiumano@gmail.com](mailto:axelfiumano@gmail.com)
# Electric Vehicle Data Transformation

## Overview
This project is an ETL (Extract, Transform, Load) process built using Python and Pandas. It transforms electric vehicle data from a CSV file and an API into structured dimensions and a fact table, enabling better data analysis and relationships between different entities.

![Overview Image](images/PythonEtlChartJ.jpg)

## Data Source
The data used in this project is sourced from the Washington State open data portal. You can download the dataset [here](https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD).

## Usage Instructions
After executing the [`extract.py`](pandas_api_csv/extract.py) file, run the [`load.py`](pandas_api_csv/load.py) file to call the [`transform.py`](pandas_api_csv/transform.py) file and functions, which will extract the data and generate a CSV file.

![CSV](images/load_to_csv.jpg)

If you wish to load the transformed data into Google BigQuery (using your own credentials), you should execute the [`load_bigquery.py`](pandas_api_bigquery/load_bigquery.py) file after running the [`extract.py`](pandas_api_csv/extract.py) file.

![BIG QUERY](images/load_to_bigquery.jpg)

### Loading to CSV or to BIG QUERY
The transformed data will be saved in the following files:
- `electric_vehicle_dim.csv`
- `county_dim.csv`
- `fact_table.csv`

### Loading to BigQuery
In addition to CSV output, this project also supports loading the transformed data directly into Google BigQuery. Ensure you have your credentials set up properly for this to work.

## Contact
For further questions, please contact:  
**Antonio Fiumanò**  
Data Engineer  
[axelfiumano@gmail.com](mailto:axelfiumano@gmail.com)
[LinkedIn](https://www.linkedin.com/in/antonio-fiumano-68aab419a)  
[Personal Website](https://tonyfiuma.github.io)

