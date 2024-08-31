import os
import time
import getpass

def write_username_to_file():
    # Get the current user's name
    username = getpass.getuser()
    
    while True:
        # Get the current epoch time
        epoch_time = int(time.time())
        
        # Create a filename with the epoch time
        filename = f"{epoch_time}.txt"
        
        # Write the username to the file
        with open(filename, 'w') as file:
            file.write(username)
        
        print(f"Created file {filename} with username {username}.")
        
        # Wait for 10 seconds
        time.sleep(10)

if __name__ == "__main__":
    write_username_to_file()
