# F1 Tyre Degradation Model

A machine-learning project investigating **Formula 1 tyre degradation** using real race data from the **2024 and 2025 F1 seasons**.

The project uses **2024 data for training** and **2025 data for testing**. The goal is to investigate how tyre age, compound, fuel load, weather, and circuit characteristics affect F1 lap-time performance.

---
# Requirements

### Python

* Python 3.x
* FastF1
* NumPy
* Pandas

### MATLAB

* MATLAB
* Statistics and Machine Learning Toolbox

---

# 1. Data Collection — Python + FastF1

The project begins with Python and the **FastF1** library.

The data collection script retrieves race data from the **2024 and 2025 Formula 1 seasons** and creates the initial dataset.

The dataset contains information including:

* Driver
* Team
* Event
* Lap Number
* Stint
* Tyre Life
* Compound
* Lap Time
* Position
* Track Temperature
* Air Temperature
* Fuel Estimate

### Run the Python script

From the project directory:

```bash
python your_data_collection_script.py
```

The script creates:

```text
data/master_dataset.csv
```

This CSV is then used by MATLAB.

---

# 2. Data Exploration — MATLAB

Open the MATLAB project:

```text
F1TyreModel.prj
```

Run:

```text
scripts/Data_Exploration.mlx
```

This stage examines and cleans the raw dataset.

The analysis focuses on the three dry-weather compounds:

```text
SOFT
MEDIUM
HARD
```

The cleaned data is then passed to the feature-engineering stage.

---

# 3. Feature Engineering — MATLAB

Run:

```text
scripts/Feature_Engineering.mlx
```

This stage prepares the cleaned data for machine learning.

Raw race data is transformed into features that can be used to investigate relationships between tyre conditions and lap-time performance.

The resulting dataset is:

```text
data/engineered_dataset.csv
```

This dataset is used for the track analysis and machine-learning stages.

---

# 4. Track Analysis — MATLAB

Run:

```text
scripts/Track_Analysis.mlx
```

This script analyzes tyre performance at individual circuits and automatically generates track-specific figures.

The primary relationship investigated is:

[
\text{Lap in Stint} \rightarrow \text{Performance Loss}
]

Figures are automatically organized into folders within:

```text
figures/
```

The analysis allows comparison of the degradation behavior of:

* Soft
* Medium
* Hard

tyres across different circuits.

---

# 5. Random Forest Model — MATLAB

Run:

```text
scripts/RandomForest_Model.mlx
```

The Random Forest model is trained using **2024 data** and evaluated using **2025 data**.

### Current model inputs

The model currently uses:

| Feature        | Description                                   |
| -------------- | --------------------------------------------- |
| `LapInStint`   | Number of laps completed on the current stint |
| `Compound`     | Soft, Medium, or Hard                         |
| `FuelEstimate` | Estimated fuel load                           |
| `TrackTemp`    | Track temperature                             |
| `AirTemp`      | Air temperature                               |
| `Event`        | F1 circuit/event                              |

### Target

```text
LapTime
```

The trained model, predictions, evaluation metrics, and figures are automatically saved to:

```text
results/
```

---

# Model Results

The current Random Forest model produced the following results on the **2025 test data**:

| Metric   |       Result |
| -------- | -----------: |
| **RMSE** | **5.4323 s** |
| **MAE**  | **4.4687 s** |
| **R²**   |  **0.73941** |

### RMSE — 5.4323 s

An RMSE of **5.43 seconds** indicates that the model still has substantial error when predicting absolute F1 lap time.

### MAE — 4.4687 s

The model's predictions differ from actual lap times by approximately **4.47 seconds per lap on average**.

### R² — 0.73941

The **R² value** indicates that the model explains approximately **73.9% of the variation in lap times** within the test dataset.

---

# Model Limitations

The current model provides a baseline, but several factors that influence F1 lap time and tyre degradation are not currently represented.

### Tyre State

* `TyreLife`
* `FreshTyre`
* Previous tyre usage
* Stint history

`LapInStint` alone does not completely describe the physical age of a tyre.

### Race Conditions

The model does not fully account for:

* Safety Car / VSC periods
* Yellow flags
* Pit-in and pit-out laps
* Traffic
* Dirty air
* Track evolution

These can significantly alter lap time without representing actual tyre degradation.

### Fuel Load

The current `FuelEstimate` is an approximation. A more accurate fuel-load model could better separate the performance effect of decreasing fuel mass from actual tyre degradation.

### Driver and Car Performance

Driver and team/car performance are not directly included as model predictors.

This prevents the model from simply learning that certain drivers or cars are faster instead of learning tyre behavior.

A future approach could normalize lap time around a driver/car baseline to isolate tyre-related performance loss.

### Weather

The model currently uses track and air temperature but does not fully capture changing conditions throughout a race.

Future versions could incorporate:

* Lap-by-lap track temperature
* Humidity
* Wind speed
* Wind direction
* Air pressure

### Track Characteristics

Currently, `Event` identifies the circuit, but the model does not explicitly understand the physical characteristics that make one circuit different from another.

Future features could include:

* Track length
* Average speed
* Corner count
* High-speed corner count
* Low-speed corner count
* Braking zones
* Track abrasiveness
* Lateral tyre loading
* Longitudinal tyre loading

---

# Future Improvements

The current model should be treated as a **baseline** for future development.

A major improvement would be changing the target from absolute:

```text
LapTime
```

to a normalized:

```text
Performance Loss
```

This would allow the model to focus more directly on tyre degradation rather than overall driver and car pace.

The improved model could incorporate:

```text
TyreLife
Compound
Fuel Load
Track Temperature
Air Temperature
Track Evolution
Track Characteristics
Driver/Car Normalized Pace
Traffic
Race Conditions
```
---

# Future Model Development

Future versions can compare multiple machine-learning approaches using the same training and testing methodology:

* Random Forest
* Gradient Boosting
* Gaussian Process Regression

All models can be trained on **2024 data** and evaluated on **2025 data** to determine which approach best predicts tyre performance.


The current results establish a baseline against which future feature-engineering and modeling improvements can be measured.

```
```
