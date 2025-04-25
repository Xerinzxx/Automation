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

# Write output to a text file
with open("role_user_mapping.txt", "w") as file:
    for role, users in role_to_users.items():
        file.write(f"{role}:\n")
        for user in users:
            file.write(f"  {user}\n")
        file.write("\n")  # Blank line after each role

print("Role-to-user mapping written to 'role_user_mapping.txt'")