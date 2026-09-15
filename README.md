# F1 Tyre Degradation Model

# Requirements

### Python

* Python 3.x
* FastF1
* Pandas
* NumPy

### MATLAB

* MATLAB R2024b or newer
* Statistics and Machine Learning Toolbox

# 1. Data Collection — Python + FastF1

The Python data collection script uses FastF1 to collect Formula 1 lap-by-lap data.

The current project focuses on **Oscar Piastri** and **McLaren**.

### Run the Python script

Run the data collection Python script to download the required race data.

The collected data is stored in the `data/` directory.

# 2. Data Exploration — MATLAB

The `Data_Exploration.mlx` script explores the collected lap data and prepares it for modeling.

The dataset is filtered to:

* Driver: Piastri (`PIA`)
* Team: McLaren
* Dry tyre compounds: Soft, Medium, Hard

Pit-in and pit-out laps are removed, along with short stints containing fewer than five laps.

Lap times are also normalized relative to the fastest lap at each event to reduce differences between circuits.

The cleaned dataset is saved as:

`data/clean_dataset.csv`

# 3. Feature Engineering — MATLAB

Feature engineering converts the cleaned dataset into variables that can be used by the machine learning model.

Current features include:

* `LapInStint` — Number of laps completed on the current tyre stint
* `Compound` — Soft, Medium, or Hard
* `FuelEstimate` — Estimated fuel load
* `TrackTemp` — Track temperature
* `AirTemp` — Air temperature
* `Event` — F1 race/event
* `TyreLife` — Total tyre age
* `AbrasivenessRating` — Estimated track abrasiveness

# 4. Track Analysis — MATLAB

Track characteristics are analyzed to account for differences between circuits.

Track-specific information is stored in:

`data/track_characteristics.csv`

This allows the model to distinguish between circuits rather than treating every track as having the same tyre behavior.

# 5. Track Abrasiveness — MATLAB

Track abrasiveness is estimated using a data-derived degradation proxy.

The `Compute_Abrasiveness_Proxy.mlx` script:

1. Loads the engineered dataset.
2. Uses 2024 data.
3. Groups laps by event.
4. Uses laps 2–15 of each stint.
5. Calculates the degradation slope between `LapInStint` and `DeltaBestLap`.
6. Requires at least five observations per event.
7. Converts the resulting degradation slopes into a 1–5 abrasiveness rating using quintiles.
8. Writes the resulting ratings into `data/track_characteristics.csv`.

A rating of **1** represents relatively low observed tyre degradation, while **5** represents relatively high observed tyre degradation.

This is a **data-derived proxy for track abrasiveness**, not a direct physical measurement of the track surface.

# 6. Random Forest Model — MATLAB

A Random Forest regression model is used to predict tyre performance.

### Current model inputs

* `LapInStint`
* `Compound`
* `FuelEstimate`
* `TrackTemp`
* `AirTemp`
* `Event`
* `TyreLife`
* `AbrasivenessRating`

### Target

The model evaluates two targets:

* `DeltaBestLap` — Lap time above the event's fastest lap
* `AbsoluteLapTime` — Raw lap time in seconds

# Model Results

### DeltaBestLap

* **RMSE:** 0.78436 s
* **MAE:** 0.58646 s
* **R²:** -0.22211

### AbsoluteLapTime

* **RMSE:** 0.78436 s
* **MAE:** 0.58646 s
* **R²:** 0.99480

# Model Limitations

### Tyre State

The model does not fully capture every factor affecting tyre degradation, including tyre preparation, graining, overheating, and individual tyre sets.

### Race Conditions

Safety cars, traffic, yellow flags, and changing race conditions can affect lap times.

### Fuel Load

Fuel load is estimated rather than directly measured.

### Driver and Car Performance

The model currently focuses on Oscar Piastri and McLaren, so the results may not generalize directly to other drivers or teams.

### Weather

Weather and track conditions can change throughout a session.

### Track Characteristics

The abrasiveness rating is a data-derived proxy based on observed degradation and should not be interpreted as a direct measurement of physical track surface properties.

# Future Improvements

* Add more drivers and teams
* Improve fuel-load estimation
* Include weather changes during sessions
* Add tyre compound-specific degradation models
* Incorporate traffic and race conditions
* Improve track characteristic measurements
* Test additional machine learning algorithms

# Future Model Development

Future versions of the model will aim to provide more detailed tyre degradation predictions by combining driver behavior, tyre characteristics, track conditions, and race strategy.
