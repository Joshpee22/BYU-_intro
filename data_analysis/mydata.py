def find_overall_min_max(lines):
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')

    for line in lines[1:]:
        parts = line.strip().split(',')
        try:
            life_expectancy = float(parts[3])  # Adjust column index based on the structure of your dataset
            min_life_expectancy = min(min_life_expectancy, life_expectancy)
            max_life_expectancy = max(max_life_expectancy, life_expectancy)
        except (ValueError, IndexError):
            continue

    if min_life_expectancy == float('inf') or max_life_expectancy == float('-inf'):
        print("No valid life expectancy values found in the dataset.")
        return

    print(f"The overall min life expectancy is: {min_life_expectancy:.2f}")
    print(f"The overall max life expectancy is: {max_life_expectancy:.2f}")


def find_year_statistics(lines, user_input_year):
    average_life_expectancy = 0
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    min_country = ""
    max_country = ""
    count = 0

    for line in lines[1:]:
        parts = line.strip().split(',')
        year = int(parts[2])  # Adjust column index based on the structure of your dataset
        
        try:
            life_expectancy = float(parts[3])  # Adjust column index based on the structure of your dataset
        except (ValueError, IndexError):
            continue

        if year == user_input_year:
            average_life_expectancy += life_expectancy
            count += 1
            min_life_expectancy = min(min_life_expectancy, life_expectancy)
            max_life_expectancy = max(max_life_expectancy, life_expectancy)
            if min_life_expectancy == life_expectancy:
                min_country = parts[1]
            if max_life_expectancy == life_expectancy:
                max_country = parts[1]

    if count == 0:
        print(f"No valid life expectancy values found for the year {user_input_year}.")
        return

    average_life_expectancy /= count

    print(f"For the year {user_input_year}:")
    print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
    print(f"The min life expectancy was {min_life_expectancy:.3f} from {min_country}")
    print(f"The max life expectancy was {max_life_expectancy:.3f} from {max_country}")


filename = 'life-expectancy (1).csv'

with open(filename, 'r') as file:
    lines = file.readlines()


find_overall_min_max(lines)

user_input_year = int(input("Enter the year of interest: "))

find_year_statistics(lines, user_input_year)

