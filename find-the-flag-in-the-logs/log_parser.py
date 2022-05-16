#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Galoget Latorre
# Organization: Hackem Cybersecurity Research Group
# Created in:
# - Python 3.9.12
# - pip 22.0.4
#
# Validated with:
# - pylint 2.12.2
# - astroid 2.9.3
# - Python 3.9.12 (main, Mar 24 2022, 13:02:21)
# - [GCC 11.2.0]
#
# Tested in:
# - Kali GNU/Linux Rolling 2022.1
# - 5.16.0-kali6-amd64 #1 SMP PREEMPT
# - Debian 5.16.14-1kali2 (2022-03-23) x86_64 GNU/Linux

"""
Python script that searches for a base64 encoded flag inside a log file
"""

# import os
import base64
import urllib.parse

# Function to read the file and return it as a list of lines
def read_file():
    """
    Function that reads the log file and returns its content as a list of lines
    """
    with open("http_server.log", "r", encoding="utf-8") as log_file:
        return log_file.readlines()

# Main function
if __name__ == "__main__":
    # Load the log file
    log_lines = read_file()

    # Explore all the lines in the log file
    for line in log_lines:
        # If the line matches the conditions, that may be the line we are looking for.
        # Type of request: POST
        # Event: /login
        # Status code: 200
        if ("POST" in line) and ("/login" in line) and ("HTTP/1.1\" 200" in line):
            # Index where the token starts
            index_start_token = line.find("/login?token=") + 13
            # Index where the token ends
            index_end_token = line[index_start_token:].find("%3D%3D") + index_start_token + 6
            # Select the token string, URL encode it and transform it to bytes
            token_bytes = urllib.parse.unquote(line[index_start_token:index_end_token]).encode()
            # Decode the token in Base64
            token = base64.b64decode(token_bytes).decode()
            # If the token starts with the string "FLAG", that's our line
            if token.startswith("FLAG"):
                print(f"Token: {token} - Line: {line.strip()}")
                # os.system("echo " + token + " | base64 -d | grep s3c8r3_l0g")
