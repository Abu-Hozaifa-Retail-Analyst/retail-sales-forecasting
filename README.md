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

> **Forecast monthly retail sales for the next 3–6 months.**

The source dataset field `sales` will be used as the forecasting target.

The project will refer to this target as **Sales** rather than **Net Sales** because the source data profile does not establish that the `sales` field represents net sales.

### Forecasting Grain

The initial forecasting grain is:

**Month × Total Retail Business**

Daily Store × Product Family sales will be aggregated to monthly total sales before forecasting.

The final forecast horizon and methodology will be confirmed after data preparation, exploratory analysis, and time-series validation.

This initial monthly total-business forecast is intended to support:

- Sales planning
- Commercial planning
- Inventory planning
- Purchasing and replenishment
- Budgeting
- Management reporting
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

## Forecasting Target and Grain

The initial forecasting target is the source dataset's `sales` field.

The target is intentionally referred to as **Sales**, not **Net Sales**, because
the available source data definition does not establish that `sales` represents
net sales.

### Initial Forecasting Grain

**Month × Total Retail Business**

The source data is stored at:

**Date × Store × Product Family**

and will be aggregated to monthly total-business sales before the initial
forecasting model is developed.

### Preparation Principle

Raw source files will remain unchanged.

Cleaning, transformation, feature engineering, aggregation, and forecasting
datasets will be created separately from the raw source data.

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

### Controlled Working Data Layer

The project follows a raw-versus-processed data governance approach.

- `data/raw/` contains the original source datasets and is treated as read-only.
- `data/processed/` contains controlled working copies used for cleaning and transformation.
- Raw source files are never modified directly.
- Dataset preparation is performed through reproducible Python scripts.
- The initial working-copy creation is verified using file integrity checks.

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

**Status: Complete**

### Phase 2 Data Quality Summary

The overall data-quality assessment contains **16 validation checks**:

- **11 PASS**
- **5 REVIEW**
- **0 FAIL**

The identified REVIEW items are documented and will be handled during
data preparation and transformation.

The structured assessment is stored in:

`data/validation/data_quality_results.csv`

The validation artifact was exported and re-read successfully, confirming
16 records, the expected four columns, no missing values, and the expected
11 PASS / 5 REVIEW status distribution.

### Phase 2 Readiness Decision

**Status: Ready for Data Preparation**

The source data can proceed to structured preparation because no tested
validation rule resulted in FAIL. Known REVIEW items will remain documented
and will be explicitly addressed before they are used in downstream
analysis or forecasting.


### Phase 3 — Data Quality & Preparation

**Phase 3: In Progress**
**Phase 3.1: Forecasting target and grain defined**
**Phase 3.2: Controlled working datasets created without modifying raw source files**
**Phase 3.3: Data standardization completed and validated**

### Phase 3.3 — Data Standardization

**Status: Complete**

The controlled working datasets were standardized using reusable Python
functions in `src/retail_forecasting/preparation/cleaning.py`.

Standardization covered:

- Date conversion to datetime
- Numeric identifier types
- Numeric measure types
- Transaction and promotion counts
- Categorical text fields
- Holiday transfer indicators

The following standardized datasets were created:

- `data/processed/train_standardized.csv`
- `data/processed/transactions_standardized.csv`
- `data/processed/stores_standardized.csv`
- `data/processed/holidays_events_standardized.csv`
- `data/processed/oil_standardized.csv`

### Standardization Validation

The standardization process was validated before the datasets were saved.

**In-memory validation**

- 19 checks
- 19 PASS
- 0 FAIL

**Saved-file structural validation**

- 5 datasets checked
- 5 PASS
- 0 FAIL

Validation confirmed preservation of:

- Row counts
- Missing-value patterns
- Business values
- Expected columns
- Dataset structure

The 43 missing oil-price observations remain unchanged and will be
evaluated during later business-rule preparation.

### Data Governance

The project maintains separate data layers:

`Raw Source → Working Copy → Standardized Data → Clean Analytical Data`

Raw source files remain unchanged. No business-rule cleaning or imputation
was performed during Phase 3.3.

### Phase 3.4.1 — Missing Oil-Price Investigation

**Status: Complete — Investigation and treatment decision documented**

The 43 missing oil-price observations were investigated before any
imputation or deletion.

Findings:

* 43 missing observations
* 43/43 occurred on weekdays
* 23 occurred on Mondays
* 9 occurred on Fridays
* 7 occurred on Thursdays
* 2 occurred on Tuesdays
* 2 occurred on Wednesdays
* 17 of the 43 dates appeared in the retail holiday/event calendar
* 26 did not appear in the retail holiday/event calendar
* The missing observations showed a structured calendar pattern rather
  than an obviously random pattern
* Only one consecutive missing-date sequence was identified:
  2017-07-03 and 2017-07-04

For missing dates with observed oil prices on both sides:

* 9 had a 2-calendar-day gap between observed prices
* 31 had a 4-calendar-day gap
* 2 had a 5-calendar-day gap

### Treatment Decision

The 43 missing oil-price observations will remain missing in the
standardized dataset.

No automatic:

* Zero replacement
* Row deletion
* Forward-fill
* Linear interpolation

was applied at the standardized-data layer.

The reason is that oil price is an external economic variable and the
missing observations show a systematic calendar/trading pattern.
Creating synthetic daily oil prices before establishing their analytical
purpose would introduce unnecessary assumptions.

Any treatment required for an oil-derived forecasting feature will be
handled separately during feature engineering and model preparation.

The project will also evaluate whether oil price provides useful
incremental forecasting information before making it a required model
feature.

### Phase 3.4.2 — Christmas Calendar Gap Investigation

**Status: Complete — Expected calendar closure confirmed**

The four missing sales dates identified during initial profiling were
investigated:

* 2013-12-25
* 2014-12-25
* 2015-12-25
* 2016-12-25

The investigation confirmed that these are complete business-wide gaps,
not partial data-loss events.

For all four dates:

* Sales records = 0
* Store coverage = 0
* Product-family coverage = 0
* Transaction records = 0
* Holiday calendar classification = National Holiday
* Holiday description = Navidad

The surrounding dates contained the expected 54 stores and 33 product
families, with 1,782 store-family observations per operating day.

### Treatment Decision

The Christmas gaps are classified as:

**Expected Calendar Closure — Not a Data Quality Error**

The standardized sales dataset will remain unchanged.

No artificial sales records will be inserted and no sales values will be
imputed for Christmas.

Because the initial forecasting target is monthly total business sales,
monthly aggregation will use the actual observed sales for operating days.

If a complete daily analytical calendar is required later, Christmas can
be represented explicitly as a business-closure/calendar event in a
derived analytical dataset without modifying the standardized source data.

This preserves source-data integrity while allowing the forecasting
workflow to distinguish legitimate business closures from missing
operational data.


### Phase 3.4.3 — Transaction-Date Coverage Investigation

**Status: Complete — Transaction coverage limitation documented**

The transaction dataset was compared with the sales calendar.

Two sales dates had no transaction records:

* 2016-01-01
* 2016-01-03

The sales dataset contained complete coverage on both dates:

* 54 stores
* 33 product families
* 1,782 sales rows per date

### 2016-01-01

The date is documented in the holiday/event dataset as:

**National Holiday — Primer dia del ano**

Sales records remain valid and were not removed.

The absence of transaction records is treated as a supporting transaction
data gap with holiday context.

### 2016-01-03

The sales dataset contains complete coverage and total sales of
1,226,735.72.

No transaction records exist for the date, and no holiday/event record
was identified.

Transaction coverage around this period is also incomplete:

* 2015-12-31: 53 stores
* 2016-01-02: 36 stores
* 2016-01-04: 14 stores
* 2016-01-05: 53 stores

This indicates a broader limitation in the transaction dataset around
this period.

### Treatment Decision

Missing transaction records will not be replaced with zero and the
corresponding sales records will not be removed.

The project distinguishes between:

* No transaction record
* Observed zero transactions
* Observed positive transactions

The forecasting target remains **Sales**, so transaction data is not
required to construct the target.

Transactions may be evaluated later as an optional explanatory feature,
but their coverage and usefulness must be validated before they are used
for forecasting.

This preserves the distinction between the authoritative sales target
and supporting transaction data.

## Step 3.4.4M — Holiday/Event Representation Decision

### Investigation Result

The holiday/event dataset contains 350 records across 312 unique dates.

31 dates contain multiple holiday/event records:

- 25 dates contain 2 records
- 5 dates contain 3 records
- 1 date contains 4 records

No exact duplicate holiday/event rows were found.

The multiplicity is legitimate and reflects combinations of:

- Local holidays
- Regional holidays
- National holidays
- Events
- Additional holidays
- Bridge days
- Transfer days
- Work days

### Join-Risk Validation

A hypothetical date-only join between the sales dataset and the
multi-event holiday records demonstrated significant row multiplication.

Sales observations on multi-event dates:

42,768 rows

Holiday records on those dates:

69 records

Rows after a date-only join:

96,228 rows

Sales before hypothetical join:

19,442,379.03

Sales after hypothetical join:

42,372,171.03

Difference:

22,929,792.00

Therefore, the holiday/event table must not be directly joined to sales
using only the `date` field when calculating aggregated sales measures.

### Final Representation Decision

The standardized holiday/event detail dataset will remain at its original
event-level grain:

**Date × Holiday/Event Record**

A separate derived analytical calendar will be created later at:

**Date**

The analytical calendar will contain aggregated date-level holiday/event
features such as:

- holiday/event presence indicators
- national/local/regional indicators
- counts by event type
- holiday/event counts
- controlled descriptive fields where useful

This design preserves the original source detail while providing a safe
one-row-per-date representation for analytical joins and forecasting
features.

### Governance Rule

The raw and standardized holiday/event detail datasets will not be
deduplicated or collapsed merely because multiple records share the same
date.

Any derived calendar representation must preserve the business meaning
of the underlying records and must be validated for one-row-per-date
uniqueness before being joined to sales.

### Status

**Phase 3.4.4 — Complete**


### Data Governance

The standardized dataset continues to preserve the source missingness.

The project maintains a separation between:

1. Source observations
2. Standardized data
3. Analytical features
4. Model-specific transformations

No source-derived values were overwritten during this investigation.



### Phase 3.4.5 — Final Cross-Dataset Preparation Review

**Status: Complete — 8 PASS / 0 FAIL**

The cross-dataset review consolidated the four preparation findings identified during Phase 3.4:

| Area | Finding | Treatment |
|---|---|---|
| Oil prices | 43 missing observations | Preserve missing values; evaluate treatment during feature engineering |
| Sales calendar | 4 missing dates, all Christmas national holidays | Preserve source gaps; do not impute sales |
| Transactions | 2 sales dates without transaction records: 2016-01-01 and 2016-01-03 | Preserve missing transaction coverage; do not assume zero |
| Holiday/events | 31 dates contain multiple legitimate records | Preserve event-level detail; create a separate one-row-per-date analytical calendar later |

The review reconfirmed that raw source data remains unchanged and that missing values are not automatically converted to zero or imputed.

The holiday/event detail remains at **Date × Holiday/Event Record** grain because a date-only join can multiply sales rows and inflate aggregated sales. A controlled one-row-per-date analytical calendar will therefore be created later for safe date-level joins.

Oil prices and transactions remain optional supporting features until their coverage and forecasting usefulness are validated.

The project is now ready to move from cross-dataset review into controlled analytical preparation.

### Phase 3.5.5 — Holiday/Event Merge QA — ✅ COMPLETE

The analytical calendar was successfully validated after merging the aggregated holiday/event features.

**Calendar validation:**

* Calendar rows: 1,688
* Unique dates: 1,688
* Duplicate dates: 0
* Date range: 2013-01-01 to 2017-08-15

**Holiday/event validation:**

* Source holiday/event records within the sales period: 286
* Aggregated holiday/event records preserved: 286
* Dates with one event record: 232
* Dates with two event records: 19
* Dates with three event records: 4
* Dates with four event records: 1

**Christmas closure validation:**

* 2013-12-25: present in analytical calendar
* 2014-12-25: present in analytical calendar
* 2015-12-25: present in analytical calendar
* 2016-12-25: present in analytical calendar
* All four dates correctly identified as national holidays

**QA result:** All holiday merge checks passed.

The analytical calendar remains at one row per date, preventing holiday-event multiplicity from causing accidental row multiplication when calendar features are later joined to sales data.


### Phase 3.5 — Analytical Calendar — ✅ COMPLETE

The project now includes a validated analytical calendar covering the complete sales analysis period from **2013-01-01 to 2017-08-15**.

The analytical calendar provides a controlled **one-row-per-date** structure for combining calendar attributes, holiday/event information, sales coverage, transaction coverage, and documented sales closures without introducing duplicate dates or holiday-event join multiplication.

#### Calendar scope

* Calendar start date: 2013-01-01
* Calendar end date: 2017-08-15
* Calendar rows: 1,688
* Calendar columns: 31
* Unique dates: 1,688
* Duplicate dates: 0
* Missing dates: 0
* Missing cells: 0

#### Calendar features

The analytical calendar contains:

* Date attributes including year, quarter, month, week, day, day of week, and day name
* Weekend indicator
* Sequential time index (`days_from_start`)
* Sales-record coverage indicator
* Transaction-record coverage indicator
* Holiday/event presence indicator
* Holiday/event record count
* National, regional, and local holiday indicators
* Holiday, event, additional, bridge, transfer, and work-day indicators
* Category-level holiday/event counts
* Explicit sales-closure indicator

#### Sales and transaction coverage

The calendar was reconciled against the source sales and transaction datasets.

* Dates with sales records: 1,684
* Dates without sales records: 4
* Dates with transaction records: 1,682
* Dates without transaction records: 6

The four missing sales dates were identified as the documented Christmas closure dates:

* 2013-12-25
* 2014-12-25
* 2015-12-25
* 2016-12-25

These dates are represented explicitly using the `is_sales_closure` indicator rather than imputing sales values.

The two additional transaction coverage gaps, **2016-01-01** and **2016-01-03**, remain represented as missing transaction coverage. No transaction values were imputed.

#### Holiday and event aggregation

Holiday/event records were aggregated from the detailed source data into a one-row-per-date structure before being merged into the analytical calendar.

* Source holiday/event records within the sales period: 286
* Aggregated records reconciled: 286
* Dates with one event record: 232
* Dates with two event records: 19
* Dates with three event records: 4
* Dates with four event records: 1

The source holiday/event detail was not deduplicated. Instead, event counts and category indicators were created so that multiple events on the same date do not cause accidental row multiplication when calendar features are joined to sales data.

#### Analytical calendar QA

The exported analytical calendar passed all final validation checks:

| QA Check                         | Result |
| -------------------------------- | ------ |
| Rows correct                     | PASS   |
| Columns correct                  | PASS   |
| Dates unique                     | PASS   |
| No duplicate dates               | PASS   |
| Date range correct               | PASS   |
| No missing values                | PASS   |
| Sales coverage correct           | PASS   |
| Transaction coverage correct     | PASS   |
| Sales closures correct           | PASS   |
| Holiday/event records reconciled | PASS   |

**Overall QA result: PASS**

The validated analytical calendar is now ready to support downstream sales aggregation, feature engineering, exploratory analysis, forecasting, and Power BI modeling.

### Phase 3.6 — Sales Data Grain & Coverage Validation — ✅ COMPLETE

The source sales dataset was validated before aggregation to confirm that the Date × Store × Product Family grain was complete and suitable for downstream sales aggregation.

#### Daily sales grain

* Sales dates with records: 1,684
* Stores: 54
* Product families: 33
* Expected rows per complete sales date: 1,782
* Incomplete sales dates: 0

Every date containing sales records has complete Store × Product Family coverage:

**54 stores × 33 product families = 1,782 rows per sales date**

#### Grain uniqueness

The source sales grain was validated at:

**Date × Store × Product Family**

* Duplicate Date × Store × Family rows: 0
* Expected total rows: 3,000,888
* Actual total rows: 3,000,888
* Row-count reconciliation: PASS

The four previously identified Christmas closure dates remain absent from the sales dataset and are represented separately through the analytical calendar rather than being treated as incomplete operating days.

#### Sales value integrity

* Missing Sales values: 0
* Negative Sales values: 0
* Zero Sales values: 939,130
* Total Sales before aggregation: 1,073,644,952.2030684

Zero-sales observations were retained because zero sales can represent valid Store × Product Family observations.

#### Extreme-value review

Several high Sales observations were investigated in Store × Product Family context.

The highest observations occur within complete Store × Product Family histories. No duplicate-grain or missing-coverage issue was identified.

Extreme Sales values are therefore classified as **REVIEW**, not as confirmed data-quality errors.

No outlier removal, winsorization, or Sales imputation was performed.

#### Final Sales QA Gate

| QA Check | Result |
|---|---|
| Daily coverage | PASS |
| Grain uniqueness | PASS |
| Row reconciliation | PASS |
| Missing Sales values | PASS |
| Negative Sales values | PASS |
| Extreme values | REVIEW |

**Overall Sales QA result: PASS**

The validated sales dataset is now ready for the next stage: controlled sales aggregation and forecasting-dataset preparation.

### Phase 3.7 — Controlled Sales Aggregation — ✅ COMPLETE

The validated daily Sales dataset was aggregated from Date × Store × Product Family to Month × Total Retail Business.

#### Aggregation design

| Attribute                    | Decision                      |
| ---------------------------- | ----------------------------- |
| Source grain                 | Date × Store × Product Family |
| Target grain                 | Month × Total Retail Business |
| Measure                      | Sales                         |
| Aggregation                  | SUM                           |
| Sales imputation             | Not performed                 |
| Christmas closure imputation | Not performed                 |
| Zero-sales observations      | Retained                      |

#### Monthly dataset results

| Metric                         |                   Result |
| ------------------------------ | -----------------------: |
| Total monthly periods          |                       56 |
| Complete months                |                       55 |
| Partial months                 |                        1 |
| Complete-month date range      |   January 2013–July 2017 |
| Partial period                 |        August 1–15, 2017 |
| Source Sales total             |    1,073,644,952.2030684 |
| Aggregated monthly Sales total |    1,073,644,952.2030685 |
| Reconciliation difference      | Approximately 0.00000012 |
| Sales reconciliation           |                     PASS |

The small reconciliation difference is attributable to floating-point precision and is within the defined 0.01 tolerance.

#### Monthly coverage treatment

The four documented Christmas closure dates were retained as closures rather than imputed Sales observations.

August 2017 was retained in the complete monthly reporting dataset but excluded from the initial full-month forecasting dataset because the source data ends on August 15, 2017.

#### Output datasets

* `data/processed/monthly_sales.csv` — all 56 monthly periods, including partial August 2017.
* `data/processed/monthly_sales_complete.csv` — 55 complete monthly periods for initial forecasting.

#### Quality assurance

All seven monthly dataset QA checks passed:

* Monthly period count
* Month uniqueness
* Continuous monthly sequence
* Sales value integrity
* Partial-month classification
* Complete-month coverage
* Sales control-total reconciliation

Exported files were reloaded and validated successfully.

**Phase 3.7 status: COMPLETE**

The controlled monthly Sales datasets are ready for exploratory time-series analysis and forecasting preparation.

### Phase 3.8 — Monthly Sales Time-Series Exploration

**Status: Completed**

#### Analysis scope

Exploratory analysis was conducted using 55 complete monthly Sales observations from January 2013 through July 2017.

August 2017 was excluded from the primary time-series analysis because it contains only 15 observed days.

#### Annual Sales trend

| Year | Months Available | Annual Sales |     YoY Growth |
| ---- | ---------------: | -----------: | -------------: |
| 2013 |               12 |      140.42M |              — |
| 2014 |               12 |      209.47M |        +49.18% |
| 2015 |               12 |      240.88M |        +14.99% |
| 2016 |               12 |      288.65M |        +19.83% |
| 2017 |                7 |      181.78M | Not comparable |

Annual growth was evaluated only for complete calendar years. The partial 2017 total was not interpreted as a full-year decline.

#### Seasonal analysis

Monthly Sales were examined using:

* Average and median Sales by calendar month
* Monthly seasonal index
* Within-year normalized Sales index
* Year-by-year seasonal consistency
* Visual comparison of normalized monthly patterns

#### Key exploratory findings

* February was below its annual average in all five observed years.
* December was above its annual average in all four observed years.
* November was above its annual average in all four observed years.
* September and October were generally elevated, with some variation.
* January through August displayed more mixed seasonal behavior.

The average normalized seasonal index was approximately:

| Month     | Normalized Index |
| --------- | ---------------: |
| February  |            0.801 |
| July      |            1.039 |
| September |            1.061 |
| October   |            1.091 |
| November  |            1.098 |
| December  |            1.334 |

These are exploratory descriptive patterns, not confirmed causal effects or guaranteed future demand changes.

#### Analytical limitations

* Only four or five annual observations are available for each calendar month.
* Seasonal effects may interact with the underlying growth trend.
* Promotional activity, holidays, transactions, and other business drivers have not yet been fully investigated.
* No forecasting model has been selected or evaluated at this stage.

#### Outputs

* Monthly Sales trend visualization
* Annual Sales summary
* Monthly seasonality summary
* Normalized seasonal profile
* Year-by-year seasonality comparison
* Seasonal consistency table

#### Readiness

The exploratory analysis provides an initial understanding of trend and seasonal behavior for subsequent forecasting preparation and chronological model validation.

### Phase 3.9 — Forecasting Readiness & Validation Design

**Status: Initial validation design completed**

#### Forecasting specification

| Component                  | Design                        |
| -------------------------- | ----------------------------- |
| Forecast target            | Total Monthly Sales           |
| Forecast grain             | Month × Total Retail Business |
| Available complete history | January 2013 – July 2017      |
| Complete observations      | 55                            |
| Initial forecast horizon   | 3 months                      |
| Validation method          | Chronological holdout         |
| Initial baselines          | Naive and Seasonal Naive      |
| Evaluation metrics         | MAE, RMSE, WAPE, Bias         |

#### Initial training and validation split

| Dataset    | Period                    | Observations |
| ---------- | ------------------------- | -----------: |
| Training   | January 2013 – April 2017 |           52 |
| Validation | May 2017 – July 2017      |            3 |

The final three complete months were reserved for initial out-of-sample evaluation.

The training period ends before the validation period begins. No random shuffling was applied.

#### Validation controls

The following checks passed:

* Training period is earlier than validation period.
* Training observation count is correct.
* Validation observation count is correct.
* Forecast horizon is three months.
* Training and validation periods do not overlap.
* Both datasets are chronologically ordered.

**Result: 6/6 validation-design checks passed.**

#### Baseline methodology

**Naive baseline:** Uses the last observed training Sales value as the forecast for each validation month.

**Seasonal Naive baseline:** Uses the Sales value from the corresponding month 12 months earlier.

Both baselines will be evaluated against the same validation observations.

#### Forecast evaluation

The planned evaluation metrics are:

* MAE — Mean Absolute Error
* RMSE — Root Mean Squared Error
* WAPE — Weighted Absolute Percentage Error
* Bias — Direction and magnitude of forecast error

No forecast accuracy results have been established yet.

#### Limitations and next steps

The initial three-month holdout provides a first evaluation, but it does not establish performance across all possible forecast origins or business conditions.

Subsequent evaluation may include rolling-origin validation, forecast error analysis, and comparison with additional forecasting approaches.

The validation design was established before model fitting to reduce the risk of future-information leakage.



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
