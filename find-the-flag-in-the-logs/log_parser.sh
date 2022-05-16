#!/bin/bash

# Flag to search
flag="FLAG{s3c8r3_l0g}"

# Print the flag we are going to search
echo "Finding $flag...";

# Encode the flag in Base64 and delete any new lines from flag
base64_encoded_flag=$(echo $flag | tr -d '\n' | base64)

# Encode Flag in Base64
echo "Base64 Encoded Flag: $base64_encoded_flag"

# Remove 2 equals from the end and replace with URL encoded format
base64_url_encoded_flag=$(echo $base64_encoded_flag | sed 's/==/%3D%3D/')

# Print the flag to search in the logs
echo "Base64 URL Encoded Flag: $base64_url_encoded_flag"

# Use grep to search for the exact line with the flag (-n to include the line number)
grep -n $base64_url_encoded_flag http_server.log
