import requests

API_Key = "489176b587c21459245061f5c733de8c"


def get_data(place, days=None):
    url = (
        f"https://api.openweathermap.org/data/2.5/forecast?"
        f"q={place}&appid={API_Key}&units=metric"
    )
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    nr_values = 8 * days
    filter_data = filter_data[:nr_values]
    return filter_data


if __name__ == "__main__":
    print(get_data(place="lagos, days = 3"))
