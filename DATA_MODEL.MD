# Entity-Relationship Diagram

## Entities

### Electric Vehicle Dim
| Column Name            | Description                             |
|-----------------------|-----------------------------------------|
| vehicle_id (PK)      | Unique identifier for each vehicle     |
| VIN (1-10)           | Vehicle Identification Number           |
| Make                  | Manufacturer of the vehicle            |
| Model                 | Model of the vehicle                   |
| Electric Vehicle Type  | Type of electric vehicle                |
| Electric Range        | Maximum distance the vehicle can travel on electric power |
| county_id (FK)       | Foreign key referencing County Dim      |

### County Dim
| Column Name            | Description                             |
|-----------------------|-----------------------------------------|
| county_id (PK)       | Unique identifier for each county      |
| County                | Name of the county                     |

### Fact Table
| Column Name            | Description                             |
|-----------------------|-----------------------------------------|
| VIN (1-10) (FK)      | Foreign key referencing Electric Vehicle Dim |
| Model Year            | Year of the vehicle model              |
| Base MSRP             | Manufacturer's suggested retail price   |
| vehicle_id (FK)      | Foreign key referencing Electric Vehicle Dim |

## Relationships
- **Electric Vehicle Dim** (1) ⟶ (N) **Fact Table**
- **County Dim** (1) ⟶ (N) **Electric Vehicle Dim**
