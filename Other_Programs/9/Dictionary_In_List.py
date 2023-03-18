# A variable that has list of items
# Nesting: List >>> Dictionaries >>> List
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Create a function that adds items into the travel_log variable by just calling the function an passing the parameters
def add_new_country (country_name, number_of_visits, cities_visited):
    
    # Create a new dictionary to hold all the values
    new_dictionary = {}
    
    # Insert all items into the dictionary
    new_dictionary["country"] = country_name
    # print(new_dictionary)
    new_dictionary["visits"] = number_of_visits
    new_dictionary["cities"] = cities_visited
    
    # Append the new_dictionary to the end of the list travel_log
    travel_log.append(new_dictionary)
    
# Call the function and pass the parameters
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# Print travel_log to see if the new_dictionary is added to the list travel_log
print(travel_log)
