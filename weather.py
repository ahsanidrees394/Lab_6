
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": [
        "2026-06-01", "2026-06-02", "2026-06-03",
        "2026-06-04", "2026-06-05", "2026-06-06",
        "2026-06-07", "2026-06-08", "2026-06-09",
        "2026-06-10", "2026-06-11", "2026-06-12",
        "2026-06-13", "2026-06-14", "2026-06-15",
        "2026-06-03"
    ],
    "City": [
        " lahore", "LAHORE ", "Islamabad", " karachi",
        "LAHORE", "islamabad ", "Karachi", " lahore ",
        "ISLAMABAD", "karachi ", "Lahore", " Islamabad",
        "KARACHI", "lahore", "Islamabad", "Islamabad"
    ],
    "Temperature": [
        "32C", "34C", "30C", "35C", "33C",
        "29C", "36C", "31C", "28C", "37C",
        "34C", "30C", "38C", "32C", "29C", "30C"
    ],
    "Humidity": [
        55, 60, None, 50, 58, 65, None, 57,
        62, 45, None, 59, 42, 56, 63, None
    ],
    "Condition": [
        "sunny", " Sunny ", "CLOUDY", " Rainy",
        "SUNNY", "cloudy ", "rainy", " Sunny",
        "CLOUDY ", "rainy", "sunny", "cloudy",
        "RAINY ", "sunny ", "CLOUDY", "cloudy"
    ]
}

df = pd.DataFrame(data)

for column in ["City", "Condition"]:
    df[column] = df[column].str.strip().str.title()

df["Temperature"] = (
    df["Temperature"]
    .str.replace("C", "", regex=False)
    .astype(float)
)

df["Date"] = pd.to_datetime(df["Date"])

df = df.drop_duplicates().copy()

print("Rows after dropping duplicates:", len(df))

humidity_median = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(humidity_median)

print("Missing Humidity filled with median:", humidity_median)


df_encoded = pd.get_dummies(
    df, columns=["Condition"], dtype=int
)

condition_columns = [
    column for column in df_encoded.columns
    if column.startswith("Condition_")
]

print("\nEncoded Condition Columns:")
print(df_encoded[condition_columns].to_string(index=False))

correlation = df["Temperature"].corr(df["Humidity"])
print(
    "\nCorrelation (Temperature, Humidity):",
    round(correlation, 3)
)

condition_counts = df["Condition"].value_counts()

print("\nCondition counts:")
print(condition_counts)

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

axes[0, 0].plot(
    df["Date"], df["Temperature"], marker="o"
)
axes[0, 0].set_title("Temperature Over Date")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=35)

axes[0, 1].scatter(
    df["Temperature"], df["Humidity"]
)
axes[0, 1].set_title("Temperature vs Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity (%)")

axes[1, 0].pie(
    condition_counts.values,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 0].set_title("Weather Condition Share")

axes[1, 1].hist(
    df["Temperature"], bins=5, edgecolor="black"
)
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

fig.suptitle("Weather Overview", fontsize=16)
fig.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()

print("\nSaved weather_dashboard.png")
