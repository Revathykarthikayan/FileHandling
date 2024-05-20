from datetime import datetime

def current_timestamp_file():
         # Get the current timestamp
    current_timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    file_name = "timestamp.txt"

    with open(file_name, 'w') as file:
        file.write(f"Current Timestamp: {current_timestamp}")


    print(f"Timestamp written to {file_name}")
current_timestamp_file()



