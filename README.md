# NYC Taxi Analytics Platform

## Overview

An end-to-end data engineering and analytics platform built using NYC Yellow Taxi trip data. The project processes over 3.4 million taxi trip records, performs ETL transformations, automates workflows with Apache Airflow, stores analytics-ready data in PostgreSQL, and visualizes key metrics through an interactive Power BI dashboard connected directly to PostgreSQL.

---

## Architecture

```
NYC Taxi Dataset (Parquet)
        ↓
Python ETL Pipeline
        ↓
Data Cleaning & Feature Engineering
        ↓
PySpark Processing
        ↓
Apache Airflow
        ↓
PostgreSQL Database
        ↓
SQL Analytics
        ↓
Power BI Dashboard
```

---

## Tech Stack

* Python
* Pandas
* PySpark
* PostgreSQL
* SQL
* Power BI
* Apache Airflow
* Docker
* DAX
* Git & GitHub

---

## Dataset

Source:

NYC Taxi & Limousine Commission (TLC)

Dataset Used:

* Yellow Taxi Trip Records (January 2025)

Records Processed:

* 3.4M+ taxi trips

---

## Features

### Data Cleaning

* Removed invalid trip records
* Filtered negative fare and distance values
* Handled missing data

### Feature Engineering

Created:

* Trip Duration
* Pickup Hour
* Pickup Day
* Pickup Month

### Analytics

Calculated:

* Total Trips by Hour
* Average Fare by Hour
* Average Distance by Hour
* Total Revenue by Hour

### Workflow Orchestration

Automated ETL pipeline using Apache Airflow:

```
transform_data
      ↓
aggregate_data
      ↓
load_postgres
```

### Database Integration

* Stored analytics-ready data in PostgreSQL
* Executed SQL-based business analysis
* Connected Power BI directly to PostgreSQL

### Dashboarding

Created interactive Power BI dashboards for:

* Demand Analysis
* Revenue Trends
* Fare Analysis
* KPI Monitoring

---

## Key Business Insights

### Peak Demand Hour

* 6 PM (18:00)
* 236,588 trips

### Highest Average Fare Hour

* 5 AM
* Average Fare: $25.48

### Total Revenue

* $88.13M+

---

## Dashboard Preview

![Dashboard](reports/dashboard_overview.png)

---

## Project Structure

```text
nyc-taxi/
│
├── airflow/
│   ├── dags/
│   ├── logs/
│   ├── plugins/
│   └── docker-compose.yaml
├── dashboard/
├── data/
├── database/
├── etl/
├── notebooks/
├── reports/
├── spark_jobs/
├── README.md
└── requirements.txt
```

## How to Run

### Clone Repository

```bash
git clone https://github.com/RushilManidhanJangala/nyc-taxi.git
cd nyc-taxi
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Airflow

```bash
cd airflow
docker compose up -d
```

### Run Pipeline

Trigger DAG:

```
nyc_taxi_pipeline
```

Airflow automates:

```
transform_data
      ↓
aggregate_data
      ↓
load_postgres
```

---

## Future Enhancements

* AWS Cloud Deployment
* Data Warehouse Integration
* Real-Time Streaming Analytics
* Kafka-Based Ingestion
* DBT Transformations

---

## Author

Rushil Manidhan Jangala

Arizona State University (May 2026)
