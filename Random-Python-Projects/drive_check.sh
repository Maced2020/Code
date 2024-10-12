#!/bin/bash

# Define the threshold in gigabytes (1 GB in this case)
THRESHOLD=2

# Define the file to be deleted when space is below 1 GB
FILE_TO_DELETE="/home/ubuntu/output_data.txt"

# Run an infinite loop to check disk space every 10 seconds
while true; do
  # Get the available disk space in gigabytes
  AVAILABLE_SPACE=$(df --output=avail / | tail -n 1 | awk '{print $1}')
  AVAILABLE_SPACE_GB=$((AVAILABLE_SPACE / 1024 / 1024))

  # Check if the available space is less than the threshold
  if [ "$AVAILABLE_SPACE_GB" -lt "$THRESHOLD" ]; then
    # Low disk space warning and delete the file
    echo "Holy shit no space, scrubbing hard drive"
    
    # Check if the file exists before trying to delete
    if [ -f "$FILE_TO_DELETE" ]; then
      echo "Deleting $FILE_TO_DELETE"
      rm "$FILE_TO_DELETE"
      echo "File deleted: $FILE_TO_DELETE" >> disk_space_1gb.log
    else
      echo "File $FILE_TO_DELETE does not exist." >> disk_space_1gb.log
    fi
  else
    # Enough space
    echo "There is enough space. Available space: ${AVAILABLE_SPACE_GB}GB"
  fi

  # Sleep for 10 seconds before checking again
  sleep 3
done
