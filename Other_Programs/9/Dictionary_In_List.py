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


# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country (country_name, number_of_visits, cities_visited):
    travel_log[0] = country_name
    travel_log[1] = number_of_visits
    travel_log[2] = cities_visited


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
