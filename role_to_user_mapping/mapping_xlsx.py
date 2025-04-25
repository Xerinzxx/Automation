import pandas as pd
from collections import defaultdict

# Load the Excel file
df = pd.read_excel("your_file.xlsx")

# Create a dictionary where each role maps to a set of users
role_to_users = defaultdict(set)

# Build the mapping
for user in df.columns:
    for role in df[user].dropna():
        role_to_users[role.strip()].add(user)

# Prepare data for writing to Excel
data = {
    "Role": [],
    "Users": []
}

for role, users in role_to_users.items():
    data["Role"].append(role)
    data["Users"].append(", ".join(sorted(users)))

# Convert to DataFrame
output_df = pd.DataFrame(data)

# Write to a new Excel file
output_df.to_excel("role_user_mapping.xlsx", index=False)

print("Role-to-user mapping written to 'role_user_mapping.xlsx'")