# Retail Sales Forecasting & Business Planning Analytics

## Project Overview

This project develops an end-to-end **retail sales forecasting and business planning analytics solution** using historical retail sales data.

The project combines:

* SQL Server
* Excel
* Power Query
* Python
* Jupyter Notebooks
* Power BI
* Data Quality & Governance
* Time-Series Forecasting
* Forecast Evaluation
* Retail Business Analysis
* Git & GitHub

The goal is not only to forecast future sales, but to build a reliable analytical workflow that connects:

**Historical Sales → Data Quality → Retail Analysis → Forecasting → Forecast Evaluation → Business Planning**

---

## Business Problem

Retail businesses need reliable estimates of future sales to support decisions involving:

* Inventory planning
* Purchasing
* Replenishment
* Sales targets
* Commercial planning
* Promotion planning
* Budgeting
* Store planning
* Category planning
* Supply-chain coordination

Historical sales data can contain missing values, duplicates, inconsistent definitions, incorrect values, and other quality problems.

Therefore, forecasting should be performed only after the underlying data has been profiled, validated, cleaned, and documented.

This project addresses that problem by building a structured and reproducible retail forecasting workflow.

---

## Primary Forecasting Objective

The initial forecasting objective is:

> **Forecast monthly Net Sales for the next 3–6 months.**

The final forecast grain and horizon will be confirmed after inspecting the available dataset and validating its time coverage, completeness, and business suitability.

---

## Business Questions

The project will investigate questions such as:

### Historical Performance

* How have sales changed over time?
* What are the major sales trends?
* Are there seasonal patterns?
* Which stores contribute most to sales?
* Which products and categories contribute most to sales?
* How are transactions and units changing?
* How are ATV and UPT changing?

### Retail Drivers

* What factors are associated with changes in sales?
* How do pricing and discounts relate to sales?
* How do promotions affect sales performance?
* Which stores or categories show different sales patterns?
* Where are margin pressures appearing?

### Forecasting

* What should expected future sales look like?
* How does a simple baseline compare with more advanced forecasting methods?
* How accurate are the forecasts?
* Where are forecast errors concentrated?
* Are errors systematic or random?

### Business Planning

* What does the forecast imply for inventory planning?
* What does it imply for purchasing and replenishment?
* Where might management need closer monitoring?
* How can forecast uncertainty be incorporated into planning?

---

## Key KPIs

The project will evaluate retail performance using metrics such as:

### Sales

* Gross Sales
* Discounts
* Net Sales
* Sales Growth %

### Customer / Basket

* Transactions
* Units
* Average Transaction Value (ATV)
* Units per Transaction (UPT)

### Profitability

* Gross Profit
* Gross Margin %

### Forecasting

* Forecast Sales
* MAE
* RMSE
* WAPE
* Forecast Bias

The final KPI definitions will be documented in the project data dictionary.

---

## Tools & Technologies

| Area                 | Tools                                   |
| -------------------- | --------------------------------------- |
| Database             | SQL Server / SSMS                       |
| Data Preparation     | SQL, Power Query, Python                |
| Analysis             | SQL, Excel, Python, Pandas              |
| Forecasting          | Python, Statistical Time-Series Methods |
| Visualization        | Power BI, Python                        |
| Reporting            | Power BI, Excel                         |
| Notebook Environment | Jupyter                                 |
| Version Control      | Git / GitHub                            |
| Documentation        | Markdown                                |

---

## Forecasting Methodology

The forecasting workflow will follow a structured progression.

### 1. Baselines

Initial models will include simple approaches such as:

* Naive Forecast
* Seasonal Naive Forecast
* Moving Average
* Exponential Smoothing

### 2. Advanced Methods

Depending on the characteristics of the actual dataset, appropriate forecasting methods may include:

* ETS
* ARIMA
* SARIMA
* Prophet
* Regression-based forecasting
* Other appropriate time-series methods

Advanced models will only be introduced when they provide analytical value.

The project will avoid using complex models simply to make the project appear more advanced.

---

## Forecast Validation

Forecast validation will respect the chronological nature of time-series data.

Random train/test splitting will not be used for the primary forecasting evaluation.

The project will use approaches such as:

* Time-based train/test splits
* Rolling or expanding validation where appropriate
* Historical backtesting

Forecast performance will be evaluated using:

* MAE
* RMSE
* WAPE
* Bias

MAPE will be treated carefully because percentage-based error can become misleading when actual sales are zero or very small.

---

## Dataset Profile

The project currently uses the public Corporación Favorita Store Sales
Time Series Forecasting dataset.

### Main Sales Dataset

| Attribute | Result |
|---|---:|
| Sales records | 3,000,888 |
| Date range | 2013-01-01 to 2017-08-15 |
| Unique sales dates | 1,684 |
| Stores | 54 |
| Product families | 33 |
| Duplicate Date × Store × Family records | 0 |
| Duplicate IDs | 0 |
| Missing values in train | 0 |
| Negative sales records | 0 |
| Zero-sales records | 939,130 |

### Supporting Datasets

| Dataset | Records | Key Grain |
|---|---:|---|
| Transactions | 83,488 | Date × Store |
| Stores | 54 | Store |
| Holidays & Events | 350 | Event record |
| Oil Prices | 1,218 | Date |
| Test | 28,512 | Forecast submission record |

### Confirmed Sales Grain

The confirmed business grain of the main sales dataset is:

**Date × Store × Product Family**

Each combination has one sales record.

### Initial Data Quality Findings

The initial profiling identified:

- No missing values in the main sales dataset.
- No duplicate sales records at the confirmed business grain.
- No duplicate sales IDs.
- No negative sales values.
- Store referential integrity passed between sales and store master.
- Store referential integrity passed between transactions and store master.
- Transaction Date × Store duplicate check passed.
- Holiday data contains multiple records on some dates and therefore requires
  controlled joining.
- Four sales calendar dates are absent from the sales dataset; all four are
  December 25 national Christmas holidays.
- Two sales dates have no transaction records: 2016-01-01 and 2016-01-03.
- The oil dataset contains 43 missing price observations.
- `onpromotion` behaves as a promotion count rather than a binary indicator.
- Raw date fields are currently loaded as strings and will be standardized
  during data preparation.

## Data Quality & Governance

Data quality will be evaluated before forecasting.

The project will investigate areas including:

* Missing values
* Duplicate records
* Invalid dates
* Invalid quantities
* Invalid prices
* Negative or impossible values
* Inconsistent categories
* Referential integrity
* Date continuity
* Duplicate transactions
* Data type consistency
* Business-rule violations

Data definitions and validation rules will be documented so that analytical results can be traced back to the underlying data.

---

## Project Workflow

The project follows this overall workflow:

```text
Raw Retail Data
       ↓
Data Profiling
       ↓
Data Quality Validation
       ↓
Data Cleaning & Preparation
       ↓
Retail Exploratory Analysis
       ↓
Retail Driver Analysis
       ↓
Forecasting
       ↓
Forecast Evaluation
       ↓
Forecast Error Analysis
       ↓
Business Insights
       ↓
Inventory / Business Planning
       ↓
Power BI Reporting
```

---

## Project Structure

```text
retail-sales-forecasting/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── validation/
│   └── forecast/
│
├── sql/
│   ├── 01_schema/
│   ├── 02_data_quality/
│   ├── 03_analysis/
│   └── 04_forecasting/
│
├── excel/
├── power_query/
│
├── notebooks/
│   ├── 01_data_quality/
│   ├── 02_data_preparation/
│   ├── 03_exploratory_analysis/
│   ├── 04_retail_driver_analysis/
│   ├── 05_forecasting/
│   ├── 06_forecast_evaluation/
│   └── 07_business_insights/
│
├── src/
│   └── retail_forecasting/
│       ├── data_quality/
│       ├── preparation/
│       ├── analysis/
│       ├── forecasting/
│       └── visualization/
│
├── scripts/
├── tests/
├── powerbi/
│
├── docs/
├── outputs/
│
├── README.md
├── .gitignore
├── requirements.txt
└── pyproject.toml
```

---

## Reproducibility

The project is designed to be reproducible through:

* Structured project directories
* Documented data preparation
* SQL scripts
* Power Query workflows
* Python notebooks
* Reusable Python modules
* Automated scripts
* Validation tests
* Forecast evaluation
* Git version control
* Project documentation

---

## Current Project Status

### Phase 0 — Project Planning

**Status: Complete**

Business objectives, scope, stakeholders, KPIs, forecasting objective, and success criteria have been defined.

### Phase 1 — Project & Python Setup
**Status: Complete**

Completed:

- Project directory structure
- Python 3.13 virtual environment
- JupyterLab / Jupyter Notebook
- Project-specific Jupyter kernel
- Core analytics packages
- `src/retail_forecasting` Python package
- `pyproject.toml` package configuration
- Environment validation notebook
- Git repository initialization
- Initial Git checkpoint
- GitHub repository
- `main` branch
- Remote repository synchronization


### Phase 2(A) — Data Acquisition & Initial Profiling

**Status: Complete**

### Phase 2(B) — Overall Data Quality Assessment

**Status: Next**


### Phase 3 — Data Quality & Preparation

**Status: Not Started**

### Phase 4 — Retail Exploratory Analysis

**Status: Not Started**

### Phase 5 — Retail Driver Analysis

**Status: Not Started**

### Phase 6 — Forecasting

**Status: Not Started**

### Phase 7 — Forecast Evaluation

**Status: Not Started**

### Phase 8 — Business Insights & Planning

**Status: Not Started**

### Phase 9 — Power BI Reporting

**Status: Not Started**

### Phase 10 — Final Portfolio & Interview Preparation

**Status: Not Started**

---

## Key Principles

This project follows several principles:

1. **Data quality before analysis**
2. **Retail business logic before model complexity**
3. **Chronological validation for forecasting**
4. **Baseline models before advanced models**
5. **Forecast accuracy must be measurable**
6. **Forecast errors must be investigated**
7. **Business usefulness matters more than model complexity**
8. **Results must be reproducible**
9. **Documentation must remain synchronized with the project**
10. **No analytical result will be reported without evidence from the project data**

---

## Findings

*To be populated after analysis is completed.*

---

## Business Recommendations

*To be populated after validated findings and forecast results are available.*

---

## Limitations

*To be documented after the dataset, forecasting methodology, and validation results are finalized.*

---

## Git Workflow

Git will be used throughout the project to track meaningful milestones.

Major checkpoints will include:

* Project setup
* Data acquisition
* Data-quality completion
* Data preparation
* Exploratory analysis
* Forecasting
* Forecast evaluation
* Business insights
* Power BI completion
* Final portfolio release

Each major checkpoint will include appropriate documentation updates.

---

## Disclaimer

This project is intended for portfolio, learning, and analytical demonstration purposes.

Forecasts are analytical estimates and should be interpreted together with business knowledge, operational constraints, promotions, inventory availability, market conditions, and other relevant information.
