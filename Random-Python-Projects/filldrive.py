import os
import time
from tqdm import tqdm

# Define the size of the target file in gigabytes
TARGET_SIZE_GB = 5
# Convert gigabytes to bytes
TARGET_SIZE_BYTES = TARGET_SIZE_GB * 1024 * 1024 * 1024

# Define the size of each chunk of data (in bytes) that we will write in each step
CHUNK_SIZE = 1024 * 1024  # 1 MB

# Define the file name
filename = "output_data.txt"

# Generate some random or repeated data to write
data_to_write = "This is some sample text data.\n" * (CHUNK_SIZE // len("This is some sample text data.\n"))

# Function to write to file with exception handling
def write_to_file():
    try:
        # Open the file in append mode, so it continues writing from the last point
        with open(filename, 'a') as file:
            # Get the current size of the file
            current_size = os.path.getsize(filename)

            # Calculate how many more bytes are needed to reach the target size
            remaining_bytes = TARGET_SIZE_BYTES - current_size
            remaining_iterations = remaining_bytes // CHUNK_SIZE

            # Use tqdm to display a progress bar for the remaining data
            for _ in tqdm(range(remaining_iterations), desc="Writing data to file", unit="MB"):
                file.write(data_to_write)
        
        # Return True if the writing completed successfully
        return True
    except OSError as e:
        if e.errno == 28:  # No space left on device
            print("OSError: No space left on device. Sleeping for 5 seconds before retrying...")
            time.sleep(5)
            return False  # Return False to indicate retry
        else:
            raise  # Raise any other OSError

# Main loop to retry writing to the file
while True:
    # Ensure the file exists or is created
    if not os.path.exists(filename):
        print(f"Creating the file: {filename}")
        open(filename, 'w').close()  # Create an empty file if it doesn't exist

    success = write_to_file()

    # If write_to_file() succeeds (returns True), exit the loop
    if success:
        final_size = os.path.getsize(filename)
        if final_size >= TARGET_SIZE_BYTES:
            print(f"File written successfully: {final_size / (1024 * 1024 * 1024):.2f} GB")
            break
        else:
            print(f"File incomplete, only {final_size / (1024 * 1024):.2f} MB written. Retrying in 5 seconds...")
            time.sleep(5)
