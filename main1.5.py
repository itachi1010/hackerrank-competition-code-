def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


# Read the number of test cases
T_input = input().strip()

# Set a default value of 2 if the input is blank
T = int(T_input) if T_input else 2

# Process each test case
for _ in range(T):
    # Read the time string
    time_str = input().strip()

    # Convert the time to seconds using the defined function
    total_seconds = time_to_seconds(time_str)

    # Print the result
    print(total_seconds)
