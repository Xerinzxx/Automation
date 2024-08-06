'''
Module/Script Name: Vastool_Details_Finder.py
Author: Srinivas Yedida

Script: Vastool User Details Extraction

Description:
This script extracts details based on the information provided in an input file. It executes a series of commands for each user listed in the input file, retrieves the output, and saves it in an output file.

Dependencies:
- Python interpreter
- Operating System (OS) commands

Usage:
Ensure that the necessary dependencies are installed and available in the environment where the script will run. Update the file paths `input_file` and `output_file` as needed to point to the correct locations of the input and output files containing user details.

Input:
- `users.txt`: A text file containing a list of user names or identifiers, each on a separate line.

Output:
- `output.txt`: A text file containing the extracted user details for each user listed in the input file. Each user's details are separated by a line of equal signs (========).

Execution:
The script reads each user name from the `users.txt` file, executes a command to extract user details, and writes the results to the `output.txt` file. The command executed for each user involves retrieving user attributes using `vastool`, filtering the output using `grep`, and manipulating the output using `sed`.

Example:
Suppose `users.txt` contains the following user names:
'''

import os

input_file = "users.txt"
output_file = "output.txt"

# Open input file and read user details
with open(input_file, "r") as f:
    users = [line.strip() for line in f]

# Open output file
with open(output_file, "w") as f:
    # Loop through each user
    for user in users:
        # Define the command to be executed
        #command = f"vastool attrs {user} | grep IDM | sed -E 's/.*CN=([^,]*).*/\\1/'"
        #command = f"vastool attrs {user} | grep RADIO  | sed -E 's/.*CN=([^,]*).*/\\1/'"
        #command = f"ypcat -k auto.home | grep {user}"
        command = f"vastool attrs {user} | grep mail:"
        #command = f"vastool attrs {user} | grep unixHomeDirectory:"
        #command = f"id -a {user} | tr ',' '\012' | grep uid"
        #command = f"id -a {user} | tr ',' '\012' | cat -n | grep yedida"
        #command = f"id -a {user} | tr ',' '\012' | cat -n | wc -l"  #To find number of groups user has
        # Execute the command and store its output
        output = os.popen(command).read()
        f.write("=====================================================\n")
        # Write user, command, output, and separator to the output file
        f.write(f"User: {user}\n")
        #f.write(f"Command: {command}\n")
        f.write("=====================================================\n")
        f.write(output)
        f.write("\n")
