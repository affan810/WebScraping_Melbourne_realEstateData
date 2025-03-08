import pandas as pd

# List of suburb names
with open("suburb.txt", "r", encoding="utf-8") as file:
    suburbs = [line.strip() for line in file.readlines()]

# Create DataFrame
df = pd.DataFrame(suburbs, columns=["Suburb"])

# Save to CSV
df.to_csv("suburbs.csv", index=False)

print("CSV file created successfully: suburbs.csv")
