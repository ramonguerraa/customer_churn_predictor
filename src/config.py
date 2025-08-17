import os

# Root directory (carpeta raíz del proyecto)
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# Data folders
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
EXTERNAL_DIR = os.path.join(DATA_DIR, "external")

# File paths
DATA_RAW = os.path.join(RAW_DIR, "churn.csv")
DATA_PROCESSED = os.path.join(PROCESSED_DIR, "churn_clean.csv")

if __name__ == "__main__":
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("DATA_RAW:", DATA_RAW)
    print("DATA_PROCESSED:", DATA_PROCESSED)

