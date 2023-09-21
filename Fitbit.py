import sys
import re

# Function to parse a time string in the format HH.MM[AM/PM] and return hours and minutes.
def parse_time(time_str):
    match = re.match(r'(\d{1,2})\.(\d{2})([APap][Mm])', time_str)
    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        period = match.group(3).upper()
        
        # Convert the time to 24-hour format.
        if period == 'PM' and hours != 12:
            hours += 12
        elif period == 'AM' and hours == 12:
            hours = 0
        
        return hours, minutes
    
    return None

# Function to check if a time range is valid
def is_valid_time(start_time, end_time):
    start_hours, start_minutes = parse_time(start_time)
    end_hours, end_minutes = parse_time(end_time)
    
    if start_hours > end_hours or (start_hours == end_hours and start_minutes >= end_minutes):
        return False
    
    return True

# Function to calculate the hourly step rate given steps, start time, and end time.
def calculate_hourly_rate(steps, start_time, end_time):
    start_hours, start_minutes = parse_time(start_time)
    end_hours, end_minutes = parse_time(end_time)
    
    total_minutes = (end_hours - start_hours) * 60 + (end_minutes - start_minutes)
    
    if total_minutes == 0:
        return 0
    
    return (steps / total_minutes) * 60

# Main function for processing Fitbit data.
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 Fitbit.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    total_steps = 0
    total_minutes = 0

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            parts = line.split(':')
            if len(parts) != 3:
                print(f"INVALID data: {line}")
                continue
            
            start_time, end_time, steps_str = parts
            steps = int(steps_str)
            
            if not is_valid_time(start_time, end_time):
                print(f"INVALID data: {line}")
                continue
            
            total_steps += steps
            start_hours, start_minutes = parse_time(start_time)
            end_hours, end_minutes = parse_time(end_time)
            total_minutes += (end_hours - start_hours) * 60 + (end_minutes - start_minutes)

    if total_minutes == 0:
        print("Total steps:", total_steps)
        print("Hourly steps rate: 0")
    else:
        hourly_rate = (total_steps / total_minutes) * 60
        print()
        print("Total steps:", total_steps)
        print("Hourly steps rate:", int(hourly_rate))

if __name__ == "__main__":
    main()
