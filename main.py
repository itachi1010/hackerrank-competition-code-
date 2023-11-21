def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

time_str1 = ("00:00:01").strip()
total_seconds1 = time_to_seconds(time_str1)
time_str2 = ("01:01:00").strip()
total_seconds2 = time_to_seconds(time_str2)
print(total_seconds1)
print(total_seconds2)
