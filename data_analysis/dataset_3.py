# Function to find overall min and max life expectancies
def find_overall_min_max(lines):
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')

    for line in lines[1:]:  # Skip the header line
        parts = line.strip().split(',')
        life_expectancy = float(parts[2])  # Assuming life expectancy is in the third column
        min_life_expectancy = min(min_life_expectancy, life_expectancy)
        max_life_expectancy = max(max_life_expectancy, life_expectancy)

    print(f"The overall min life expectancy is: {min_life_expectancy:.2f}")
    print(f"The overall max life expectancy is: {max_life_expectancy:.2f}")


# Function to find year-specific average, min, and max life expectancies
def find_year_statistics(lines, user_input_year):
    average_life_expectancy = 0
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    min_country = ""
    max_country = ""
    count = 0

    for line in lines[1:]:
        parts = line.strip().split(',')
        year = int(parts[0])
        if year == user_input_year:
            life_expectancy = float(parts[2])
            average_life_expectancy += life_expectancy
            count += 1
            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                min_country = parts[1]
            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                max_country = parts[1]

    average_life_expectancy /= count

    print(f"For the year {user_input_year}:")
    print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
    print(f"The min life expectancy was {min_life_expectancy:.3f} from {min_country}")
    print(f"The max life expectancy was {max_life_expectancy:.3f} from {max_country}")


# Main program
filename = 'life-expectancy.csv'

with open('life-expectancy (1).csv', 'r') as file:
    lines = file.readlines()

# Find overall min and max life expectancies
find_overall_min_max(lines)

# Allow user input for a specific year
user_input_year = int(input("Enter the year of interest: "))

# Find year-specific statistics
find_year_statistics(lines, user_input_year)
