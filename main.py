import json
import os
import subprocess
from datetime import datetime, time
from time import sleep

# Define the path to the config file
config_file_path = "config.json"

def create_config_file(value):
    # Create a dictionary with the specified value
    config_data = {"ora": value}

    # Write the dictionary to the config file
    with open(config_file_path, "w") as config_file:
        json.dump(config_data, config_file)

def read_config_file():
    # Read the config file if it exists
    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as config_file:
            config_data = json.load(config_file)
            return config_data.get("ora")
    else:
        return None

def shutdown_pc():
    # Execute the Windows command to shut down the PC
    subprocess.run(["shutdown", "/s", "/t", "0"])

def main():
    while True:
        # Read the value from the config file
        a = read_config_file()
        if a is None:
            # If config file does not exist, prompt user for input
            a = input("Enter a value: ")
            create_config_file(a)
        else:
            #If config file exists, schedule shutdown at specified time
            try:
                shutdown_time = a
                current_time = datetime.now().time()
                if current_time == shutdown_time:
                    shutdown_pc()
            except ValueError:
                print("Invalid time format in config.json. Please provide time in HH:MM format.")
    
    


main()
KeyboardInterrupt()

