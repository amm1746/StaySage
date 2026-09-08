from pathlib import Path

# settings, files, file paths, city definitions, etc

# goes up two folder lvls to staysage/
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"
MODELS = PROJECT_ROOT / "models"
FIGURES = PROJECT_ROOT / "reports" / "figures"

# creates folders if they don't exist. exist_ok
# =True means it wont crash if its already there
RAW_DATA.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA.mkdir(parents=True, exist_ok=True)
MODELS.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

# the cities. each city is one entry in the dictionary. the key
# is just a nickname for file names. the values inside are
# longer. 

# ** COME BACK TO THIS FOR MORE CITIES
CITIES = {
    "austin": {
        "name": "Austin, TX",
        "lat": 30.2672,
        "lon": -97.7431,
        "listings_url": "https://data.insideairbnb.com/united-states/tx/austin/2026-06-22/data/listings.csv.gz",
        "calendar_url": "https://data.insideairbnb.com/united-states/tx/austin/2026-06-22/data/calendar.csv.gz",
    },
    "nashville": {
        "name": "Nashville, TN",
                "lat": 36.1627,
                "lon": -86.7816,
                "listings_url": "https://data.insideairbnb.com/united-states/tn/nashville/2026-06-26/data/listings.csv.gz",
                "calendar_url": "https://data.insideairbnb.com/united-states/tn/nashville/2026-06-26/data/calendar.csv.gz",

    },
    "boston": {
            "name": "Boston, MA",
                    "lat": 42.3601,
                    "lon": -71.0589,
                    "listings_url": "https://data.insideairbnb.com/united-states/ma/boston/2026-06-15/data/listings.csv.gz",
                    "calendar_url": "https://data.insideairbnb.com/united-states/ma/boston/2026-06-15/data/calendar.csv.gz",
    
        }
}

def listings_path(city_key):
    # where listings files are saved for cities
    return RAW_DATA / (city_key + "_listings.csv.gz")

def calendar_path(city_key):
    # where calender files are saved for cities
    return RAW_DATA / (city_key + "_calendar.csv.gv")

# processed file names
DATASET_FILE = PROCESSED_DATA / "dataset.parquet"
NEIGHBORHOOD_FILE = PROCESSED_DATA / "neighborhoods.csv"
MONTHLY_FILE = PROCESSED_DATA / "airbnb_monthly.csv"
HOTEL_FILE = PROCESSED_DATA / "hotel_rates.csv"
PRICE_MODEL_FILE = MODELS / "price_model.joblib"
SCARCITY_MODEL_FILE = MODELS / "scarcity_model.joblib"
META_FILE = MODELS / "meta.joblib"

# model/sampling settings

# how many amenities will become model columns
TOP_AMENITIES = 40

# map districts leanred per city
LOCATION_CLUSTERS = 20

# for steps that involve randomness
RANDOM_SEED = 1234

# keep every nth night - 17 so you get the seven weekdays 
NTH_NIGHT = 17

# listing cap
MAX_LISTINGS = 5000