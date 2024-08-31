def convert_seconds(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return minutes, seconds

# Example usage
total_seconds = 125
minutes, seconds = convert_seconds(total_seconds)
print(f"{total_seconds} seconds is {minutes} minutes and {seconds} seconds")
