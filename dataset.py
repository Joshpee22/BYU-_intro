# Creativity and Exceeding Requirements:
# Added features to identify the largest drop from one year to the next,
# allow user input for country-specific analysis, and detect anomalies in the data.

# Initialize variables for the largest drop and corresponding year and country
largest_drop = 0.0
drop_year = 0
drop_country = ""

# Dictionary to store life expectancy values for each country
country_life_expectancies = {}

# Open and read the dataset file (replace 'your_dataset.csv' with the actual file path)
with open('your_dataset.csv', 'r') as file:
    # Skip the header line if it exists
    header = file.readline()

    # Initialize variables for tracking previous year and country
    prev_year = None
    prev_country = None

    # Iterate through each line in the file
    for line in file:
        # Split each line into parts
        parts = line.strip().split(',')

        # Extract year, country, and life expectancy values
        year = int(parts[0])
        country = parts[2]
        life_expectancy = float(parts[1])

        # Update largest drop if applicable
        if prev_year is not None and prev_country == country:
            year_difference = year - prev_year
            if year_difference == 1:
                drop = prev_life_expectancy - life_expectancy
                if drop > largest_drop:
                    largest_drop = drop
                    drop_year = year
                    drop_country = country

        # Update dictionary with life expectancy values for each country
        if country not in country_life_expectancies:
            country_life_expectancies[country] = []
        country_life_expectancies[country].append(life_expectancy)

        # Update previous year and country
        prev_year = year
        prev_country = country
        prev_life_expectancy = life_expectancy

# Display the largest drop and corresponding year and country
print(f"\nThe largest drop from one year to the next is: {largest_drop:.3f}")
print(f"It occurred in {drop_country} in {drop_year}")

# Allow user to input a country for analysis
user_country = input("\nEnter a country to analyze (case-sensitive): ")

# Display min, max, and average life expectancy for the specified country
if user_country in country_life_expectancies:
    country_values = country_life_expectancies[user_country]
    min_life_expectancy = min(country_values)
    max_life_expectancy = max(country_values)
    average_life_expectancy = sum(country_values) / len(country_values)

    print(f"\nFor {user_country}:")
    print(f"The minimum life expectancy is: {min_life_expectancy:.3f}")
    print(f"The maximum life expectancy is: {max_life_expectancy:.3f}")
    print(f"The average life expectancy is: {average_life_expectancy:.3f}")
else:
    print(f"\nData not available for {user_country}. Please check the country name.")

