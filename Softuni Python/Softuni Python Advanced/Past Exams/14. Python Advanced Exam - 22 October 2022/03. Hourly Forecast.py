def forecast(*args) -> str:
    def comparator(a, b):
        if a == "Sunny":
            return True

        elif a == "Rainy":
            return b != "Sunny"

        else:
            return False
    city_data = {
        "Sunny":[],
        "Cloudy": [],
        "Rainy":[]
    }

    for forecast_data in args:
        city_data[forecast_data[1]] += [forecast_data[0]]

    result = []

    for forecast in city_data:
        if city_data[forecast] == []:
            continue
        for city in sorted(city_data[forecast]):
            result.append(f"{city} - {forecast}")

    return "\n".join(result)

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print("------")
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print("------")
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

