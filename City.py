import requests


class City:
    city_name = ""
    description = ""
    current_temp = 0
    low_temp = 0
    high_temp = 0
    humidity = 0
    pressure = 0
    feels_like = 0
    temp_unit = True

    def __int__(self):
        self.city_name = "null"

    def __repr__(self):
        return self.city_name

    def __str__(self):
        return self.city_name

    def display_info(self):
        print("City: " + self.city_name)
        print("Current Temp: %d" % self.current_temp)
        print("Low temp: %d" % self.low_temp)
        print("High temp: %d" % self.high_temp)

    def query_api(self, cityname):
        c = City()
        web_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = "88b20825c3148ac2316289b987785623"
        complete_url = web_url + "appid=" + api_key + "&q=" + cityname
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] != "404":
            y = data["main"]
            current_temperature = y["temp"]
            current_temperature = self.convert_faren_from_k(current_temperature)
            current_humidity = y["humidity"]
            z = data["weather"]
            low_temp = y["temp_min"]
            low_temp = self.convert_faren_from_k(low_temp)
            high_temp = y["temp_max"]
            high_temp = self.convert_faren_from_k(high_temp)
            pressure = y["pressure"]
            feelslike = y["feels_like"]
            feelslike = self.convert_faren_from_k(feelslike)
            description = z[0]["description"]
            c.set(cityname, description, current_temperature, low_temp, high_temp, current_humidity, pressure, feelslike)
            return c
        else:
            c = c.query_api("London")
            return c

    def set(self, name, desc, temp, low, high, hum, pres, feel):
        self.city_name = name
        self.description = desc
        self.current_temp = temp
        self.low_temp = low
        self.high_temp = high
        self.humidity = hum
        self.pressure = pres
        self.feels_like = feel

    def convert_units(self):
        if self.temp_unit == True:
            # F to C
            self.temp_unit = False
            self.current_temp = (self.current_temp - 32) * 5 / 9
            self.low_temp = (self.low_temp - 32) * 5 / 9
            self.high_temp = (self.high_temp - 32) * 5 / 9
        else:
            self.temp_unit = True
            # C to F
            self.current_temp = (self.current_temp * 9 / 5) + 32
            self.low_temp = (self.low_temp * 9 / 5) + 32
            self.high_temp = (self.high_temp * 9 / 5) + 32

    def convert_faren_from_k(self, kelvin):
        return (int)(kelvin - 273.25) * 9 / 5 + 32

    def compare(self, other):
        print(other)
        return (self.city_name == other.city_name and self.current_temp == other.current_temp and self.humidity == other.humidity
                and self.low_temp == other.low_temp and self.high_temp == other.high_temp)

    def print(self):
        print("City: " + self.city_name + "Current temp: ", self.current_temp, "Low temp: ", self.low_temp,
              "High temp: ", self.high_temp)
