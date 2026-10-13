import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": [
        " ali", "SARA ", "bilal", " Ayesha",
        "HAMZA", "zain ", "Noor", " usman "
    ],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"]
}

df = pd.DataFrame(data)

df["Name"] = df["Name"].str.strip().str.title()

df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

print("Cleaned Student Marks:")
print(df.to_string(index=False))

plt.figure(figsize=(9, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("marks_bar.png")
plt.show()

print("\nSaved marks_bar.png")
