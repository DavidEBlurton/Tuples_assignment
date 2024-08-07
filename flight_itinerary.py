# Objective: The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, and string formatting. By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.

# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:

# "Itinerary 1: Alice - From New York to London"
# "Itinerary 2: Bob - From Tokyo to San Francisco"


flight_itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def format_itineraries(itineraries):

    for index, (traveler_name, origin, destination) in enumerate(flight_itineraries, start=1):
        formatted_string = f"Itinerary {index}: {traveler_name} - From {origin} to {destination}"
        print(formatted_string)

format_itineraries(flight_itineraries)
