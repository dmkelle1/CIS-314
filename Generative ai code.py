import re

def extract_unique_ips(log_file_path):
    # Open and read the log file
    with open(log_file_path, 'r') as file:
        log_data = file.readlines()
    
    # Regular expression pattern for matching IP addresses
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    unique_ips = set()  # Use a set to keep unique IPs

    # Parse each log entry
    for entry in log_data:
        found_ips = re.findall(ip_pattern, entry)
        unique_ips.update(found_ips)

    return unique_ips

# Example usage
if __name__ == "__main__":
    log_file = 'webserver.log'  # Change this to your log file's path
    unique_ips = extract_unique_ips(log_file)
    print("Unique IP Addresses:", unique_ips)