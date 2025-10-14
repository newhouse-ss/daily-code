import datetime
def validate_time_interval(datetime_str1, datetime_str2, max_difference_seconds):
    """Validates if the time difference between two datetimes is within a maximum limit."""
    dt1 = datetime.datetime.strptime(datetime_str1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.datetime.strptime(datetime_str2, "%Y-%m-%d %H:%M:%S")
    print(type(dt1-dt2))
    time_difference = abs((dt2 - dt1).total_seconds())
    return time_difference <= max_difference_seconds
# Example usage:
datetime_str1 = "2024-10-26 10:00:00"
datetime_str2 = "2024-10-26 10:05:00"
max_diff = 360  # 6 minutes in seconds
is_valid = validate_time_interval(datetime_str1, datetime_str2, max_diff)
print(f"Time interval is valid: {is_valid}")