# Role-to-User Mapping Script

This project processes an Excel file where each column represents a user, and each cell under a column lists a role that user has filled. The script generates an inverted mapping: for each role, it lists all users who have that role.

---

## Input Format

An Excel file (`.xlsx`) structured as follows:

| Alice   | Bob     | Charlie |
|---------|---------|---------|
| Admin   | Admin   | Admin   |
| Dev     | Dev     | Dev     |
| Tester  | Tester  | Tester  |
|         | Analyst |         |

---

## Output Options

### 1. Text Output (`role_user_mapping.txt`)

Generates a human-readable text file where each role is followed by the list of users who have filled that role.

**Example:**

Dev:
Alice
Bob
Charlie

Analyst:
Bob

Tester:
Alice
Bob
Charlie


#### ==========

### 2. Excel Output (`role_user_mapping.xlsx`)

Generates a structured Excel file with two columns:

| Role   | Users                  |
|--------|------------------------|
| Dev    | Alice, Bob, Charlie    |
| Analyst| Bob                    |
| Tester | Alice, Bob, Charlie    |

---

## How to Run

1. Ensure your input Excel file is named `your_file.xlsx` or change the filename in the script accordingly.
2. Run the script using Python 3:
   ```bash
   python mapping_txt.py

### 3.	The output will be saved in the same directory as:
	•	role_user_mapping.txt (text format)
	•	role_user_mapping.xlsx (Excel format)