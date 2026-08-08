import os
import numpy as np
import pandas as pd
import fastf1

# SETTINGS

YEARS = [2024, 2025]

CACHE_DIR = "cache"
OUTPUT_DIR = "data"

fastf1.Cache.enable_cache(CACHE_DIR)

os.makedirs(OUTPUT_DIR, exist_ok=True)

master_rows = []

# DOWNLOAD DATA

for year in YEARS:

    print(f"\nLoading {year} Schedule...")

    schedule = fastf1.get_event_schedule(year)

    for _, event in schedule.iterrows():

        event_name = event["EventName"]

        # Skip Pre-Season Testing
        if "Pre-Season Testing" in str(event_name):
            print(f"Skipping {year} - {event_name}")
            continue

        print(f"Processing {year} - {event_name}")

        try:

            session = fastf1.get_session(year, event_name, "R")
            session.load()

            weather = session.weather_data

            track_temp = weather["TrackTemp"].mean()
            air_temp = weather["AirTemp"].mean()

            laps = session.laps.pick_accurate()

            for _, lap in laps.iterrows():

                # Skip bad laps
                if pd.isna(lap["LapTime"]):
                    continue

                if pd.isna(lap["TyreLife"]):
                    continue

                # Remove Safety Car / VSC / Red Flag laps
                if str(lap["TrackStatus"]) != "1":
                    continue

                fuel_estimate = max(
                    110 - (lap["LapNumber"] - 1) * 1.8,
                    0
                )

                master_rows.append({

                    "Year": year,

                    "Event": event_name,

                    "Driver": lap["Driver"],

                    "Team": lap["Team"],

                    "LapNumber": lap["LapNumber"],

                    "Stint": lap["Stint"],

                    "TyreLife": lap["TyreLife"],

                    "Compound": lap["Compound"],

                    "LapTime": lap["LapTime"].total_seconds(),

                    "Position": lap["Position"],

                    "TrackTemp": round(track_temp, 1),

                    "AirTemp": round(air_temp, 1),

                    "FuelEstimate": round(fuel_estimate, 1)

                })

        except Exception as e:

            print(f"Skipped {event_name}: {e}")

# SAVE CSV

master = pd.DataFrame(master_rows)

master.to_csv(
    os.path.join(OUTPUT_DIR, "master_dataset.csv"),
    index=False
)

print("\nDone!")
print(f"Rows: {len(master)}")
print(master.head())