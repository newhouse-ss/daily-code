import datetime

def log_file_analysis(log_entries):
    if not log_entries:
        return None#Handling empty entry
    
    time_differences = []
    for i in range(1, len(log_entries)):
        timestamp1 = datetime.datetime.strptime(log_entries[i-1][:19], "%Y-%m-%d %H:%M:%S")
        timestamp2 = datetime.datetime.strptime(log_entries[i][:19], "%Y-%m-%d %H:%M:%S")
        time_differences.append((timestamp2-timestamp1).total_seconds())
    print(time_differences)

    if not time_differences:
        return None#Handling single_line entry
    
    avg_difference = sum(time_differences)/len(time_differences)
    return avg_difference

log_entries = [
    "2024-10-26 10:00:00 - User logged in",
    "2024-10-26 10:00:30 - User accessed profile",
    "2024-10-26 10:01:15 - User made a post",
    "2024-10-26 10:02:00 - User logged out"
]
avg_difference = log_file_analysis(log_entries)
print(avg_difference)