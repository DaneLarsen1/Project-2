# Uber AI Data Preprocessing

## Brief Project Description
This project preprocesses Uber trip data to prepare it for building an AI model that predicts Uber ride costs. The primary objectives include cleaning and transforming the data to ensure it is suitable for accurate and meaningful analysis. Key preprocessing steps involve handling missing values, removing duplicates, validating coordinates, and engineering features such as pickup hour, day of the week, season, and trip distance in miles.
It then uses this data to train a predictive model so the user can determine what their fare will be based off of time and location. 
---

## Table of Contents
- [Introduction](#introduction)
- [Data Information](#data-information)
- [Getting Started](#getting-started)
- [Methodology](#methodology)
- [Results](#results)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

---

## Introduction
Predicting the cost of Uber rides requires high-quality data. This project focuses on preprocessing Uber trip data to ensure it is clean, well-structured, and enriched with meaningful features. The key steps include:

1. **Cleaning the Data**:
   - Handling missing values.
   - Removing duplicate records.
   - Validating coordinates to ensure accurate geospatial data.

2. **Transforming the Data**:
   - Extracting new features such as pickup hour, day of the week, and season.
   - Calculating trip distances in miles using geospatial data.

By preparing raw data effectively, this project lays the foundation for building a robust AI model capable of accurately predicting ride costs.

---

## Data Information

### Source
The data for this project comes from Uber’s trip records.

### Description
The dataset contains information about Uber trips, including pickup and dropoff locations, times, fare amounts, and passenger counts.

### Structure
Key features/variables in the dataset include:
- **pickup_datetime**: The date and time when the trip started.
- **pickup_latitude**: The latitude of the pickup location.
- **pickup_longitude**: The longitude of the pickup location.
- **dropoff_latitude**: The latitude of the dropoff location.
- **dropoff_longitude**: The longitude of the dropoff location.
- **fare_amount**: The fare amount for the trip.
- **passenger_count**: The number of passengers in the trip.

---

## Getting Started

### Prerequisites
Ensure you have Python installed along with the following libraries:
- pandas
- numpy
- geopy

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <repository-directory>
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Methodology

### Data Loading
Load the raw Uber trip data from a CSV file.

### Data Cleaning
- Handle missing values in key features.
- Remove duplicate records to ensure data integrity.
- Validate geospatial coordinates to filter out invalid locations.

### Data Transformation
- Extract temporal features such as:
  - Pickup hour.
  - Day of the week.
  - Season (spring, summer, fall, winter).
- Calculate trip distances in miles using the geopy library.

### Data Saving
Save the processed data into CSV files for subsequent analysis:
- `uber_data_cleaned.csv`
- `uber_data_transformed.csv`

---

## Results
The cleaned and transformed dataset is stored in the `processed` directory. This data is ready for use in building and training AI models to predict Uber ride costs accurately.

---

## Dependencies
This project uses the following libraries:
- pandas
- numpy
- geopy

Install them with:
```bash
pip install pandas numpy geopy
```

---

## Usage
To preprocess the data, run the `data_preprocessing.py` script:
```bash
python data_preprocessing.py
```
This will generate cleaned and transformed datasets saved in the `processed` directory.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## Acknowledgments
None

