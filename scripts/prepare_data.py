from pathlib import Path
import shutil


# ------------------------------------------------------------
# Project paths
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


# ------------------------------------------------------------
# Create processed directory if it does not exist
# ------------------------------------------------------------

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Raw → Working dataset mapping
# ------------------------------------------------------------

DATASETS = {
    "train.csv": "train_working.csv",
    "transactions.csv": "transactions_working.csv",
    "stores.csv": "stores_working.csv",
    "holidays_events.csv": "holidays_events_working.csv",
    "oil.csv": "oil_working.csv",
}


# ------------------------------------------------------------
# Create controlled working copies
# ------------------------------------------------------------

for raw_name, working_name in DATASETS.items():
    raw_path = RAW_DIR / raw_name
    working_path = PROCESSED_DIR / working_name

    if not raw_path.exists():
        raise FileNotFoundError(f"Raw dataset not found: {raw_path}")

    shutil.copy2(raw_path, working_path)

    print(f"Created: {working_path.name}")


# ------------------------------------------------------------
# Completion message
# ------------------------------------------------------------

print("\nControlled working dataset creation completed.")
print(f"Raw directory: {RAW_DIR}")
print(f"Processed directory: {PROCESSED_DIR}")
