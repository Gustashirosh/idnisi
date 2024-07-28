import time

# Define the file path
file_path = 'example.txt'

# Continuous loop for writing and overwriting the file
while True:
    with open(file_path, 'w') as file:
        file.write('This content will be continuously overwritten.')
    
    # Introduce a delay before the next write operation
    time.sleep(1)
