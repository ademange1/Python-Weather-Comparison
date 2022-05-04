import tkinter as tk
from tkinter import ttk
from tkinter import Frame
from City import City

"""
Changes and fixes since demo
-can now input invalid city names: defaults to london
-multiple cities with the same name now display properly in the sort screen
-city compare screen options now use a combobox
-compare screen now properly displays cities with the same data field
-added preset options
"""
# defining basic window properties
root = tk.Tk()
root.title("Python Weather Comparison")
window_width = 800
window_height = 600
frmMain = Frame(root)
root.resizable(False, False)

c1 = City()
c2 = City()
c3 = City()
c4 = City()
c5 = City()
c6 = City()
c7 = City()
c8 = City()
city_list = [c1, c2, c3, c4, c5, c6, c7, c8]
data_list = [False, False, False, False, False, False, False, False]

# getting screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# centering window in the middle of the screen
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# title
message = tk.Label(root, text="Python Weather Comparison", font=("Arial", 26))
message.grid(column=0, row=0, sticky=tk.N)


def update_cities():
    for i in city_list:
        if (i.city_name != ""):
            i.query_api(i.city_name)


# test function for input
def get_city(city_num):
    def show_display(name, num):
        name = city_name.get()
        num = city_num
        display.destroy()
        display_city(name, num)

    if data_list[city_num - 1] != False:
        display_city(city_list[city_num - 1].city_name, city_num)
    else:
        display = tk.Tk()
        window_width = 224
        window_height = 60
        display.title("Add a city")
        display.geometry(f'{window_width}x{window_height}')
        city_name_label = tk.Label(display, text="Enter the city name here: ")
        city_name_label.grid(column=1, row=0, sticky=tk.W, padx=2, pady=2)
        city_name = ttk.Entry(display)
        city_name.grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
        confirm = tk.Button(display, text="Confirm", command=lambda: show_display(city_name.get(), city_num))
        confirm.grid(column=2, row=1)
        display.mainloop


def preset1():
    city = City()
    city_list[0] = city.query_api("Chicago")
    data_list[0] = True
    cityButton1.config(text=city_list[0].city_name)
    city_list[1] = city.query_api("Denver")
    data_list[1] = True
    cityButton2.config(text=city_list[1].city_name)
    city_list[2] = city.query_api("Quebec")
    data_list[2] = True
    cityButton3.config(text=city_list[2].city_name)
    city_list[3] = city.query_api("Vancouver")
    data_list[3] = True
    cityButton4.config(text=city_list[3].city_name)
    city_list[4] = city.query_api("Houston")
    data_list[4] = True
    cityButton5.config(text=city_list[4].city_name)
    city_list[5] = city.query_api("Miami")
    data_list[5] = True
    cityButton6.config(text=city_list[5].city_name)
    city_list[6] = city.query_api("Los Angeles")
    data_list[6] = True
    cityButton7.config(text=city_list[6].city_name)
    city_list[7] = city.query_api("New York")
    data_list[7] = True
    cityButton8.config(text=city_list[7].city_name)

def preset2():
    city = City()
    city_list[0] = city.query_api("London")
    data_list[0] = True
    cityButton1.config(text=city_list[0].city_name)
    city_list[1] = city.query_api("Paris")
    data_list[1] = True
    cityButton2.config(text=city_list[1].city_name)
    city_list[2] = city.query_api("Beijing")
    data_list[2] = True
    cityButton3.config(text=city_list[2].city_name)
    city_list[3] = city.query_api("Berlin")
    data_list[3] = True
    cityButton4.config(text=city_list[3].city_name)
    city_list[4] = city.query_api("Moscow")
    data_list[4] = True
    cityButton5.config(text=city_list[4].city_name)
    city_list[5] = city.query_api("Frankfurt")
    data_list[5] = True
    cityButton6.config(text=city_list[5].city_name)
    city_list[6] = city.query_api("Giza")
    data_list[6] = True
    cityButton7.config(text=city_list[6].city_name)
    city_list[7] = city.query_api("Tokyo")
    data_list[7] = True
    cityButton8.config(text=city_list[7].city_name)


def display_city(name, city_num):
    def update():
        city_list[city_num - 1].convert_units()
        city_temp_label.config(text=city_list[city_num - 1].current_temp)
        city_low_label.config(text=city_list[city_num - 1].low_temp)
        city_high_temp.config(text=city_list[city_num - 1].high_temp)
        if (city_list[city_num - 1].temp_unit == True):
            units.config(text="Temperatures listed in farenheight")
        else:
            units.config(text="Temperatures listed in celcius")

    def change_city(city_num):
        data_list[city_num - 1] = False
        get_city(city_num)
        city_screen.destroy()

    data_list[city_num - 1] = True
    city_screen = tk.Tk()
    city_screen.title("Weather")
    city_screen.resizable(False, False)
    window_width = 350
    window_height = 250
    city_screen.geometry(f'{window_width}x{window_height}')
    temp = City()
    city_list[city_num - 1] = temp.query_api(name)
    city_name_label = tk.Label(city_screen, text="Weather for " + city_list[city_num - 1].city_name, font=("Arial", 14))
    city_name_label.grid(column=0, row=0, sticky=tk.W)
    units = tk.Label(city_screen, text="Temperatures listed in farenhieght")
    units.grid(column=0, row=1, sticky=tk.W)
    temp_label = tk.Label(city_screen, text="current temperature: ")
    temp_label.grid(column=0, row=2, sticky=tk.W)
    city_temp_label = tk.Label(city_screen, text=city_list[city_num - 1].current_temp)
    city_temp_label.grid(column=1, row=2, sticky=tk.W)

    low_label = tk.Label(city_screen, text="lowest temperature: ")
    low_label.grid(column=0, row=3, sticky=tk.W)
    city_low_label = tk.Label(city_screen, text=city_list[city_num - 1].low_temp)
    city_low_label.grid(column=1, row=3, sticky=tk.W)

    high_label = tk.Label(city_screen, text="highest temperature: ")
    high_label.grid(column=0, row=4, sticky=tk.W)
    city_high_temp = tk.Label(city_screen, text=city_list[city_num - 1].high_temp)
    city_high_temp.grid(column=1, row=4, sticky=tk.W)

    hum_label = tk.Label(city_screen, text="humidity: ")
    hum_label.grid(column=0, row=6, sticky=tk.W)
    city_hum = tk.Label(city_screen, text=city_list[city_num - 1].humidity)
    city_hum.grid(column=1, row=6, sticky=tk.W)

    description_label = tk.Label(city_screen, text="description: ")
    description_label.grid(column=0, row=8, sticky=tk.W)
    city_description = tk.Label(city_screen, text=city_list[city_num - 1].description)
    city_description.grid(column=1, row=8, sticky=tk.W)

    feel_label = tk.Label(city_screen, text="feels like: ")
    feel_label.grid(column=0, row=5, sticky=tk.W)
    city_feels_like = tk.Label(city_screen, text=city_list[city_num - 1].feels_like)
    city_feels_like.grid(column=1, row=5, sticky=tk.W)

    pressure_label = tk.Label(city_screen, text="pressure: ")
    pressure_label.grid(column=0, row=7, sticky=tk.W)
    city_pressure = tk.Label(city_screen, text=city_list[city_num - 1].pressure)
    city_pressure.grid(column=1, row=7, sticky=tk.W)

    change_button = ttk.Button(city_screen, text="Change city", command=lambda: change_city(city_num))
    change_button.grid(column=0, row=9, sticky=tk.W)

    refresh = ttk.Button(city_screen, text="Refresh data",
                         command=lambda: city_list[city_num - 1].query_api(city_list[city_num - 1].city_name))
    refresh.grid(column=1, row=9, sticky=tk.SW, pady=23)
    if (city_num == 1):
        cityButton1.config(text=city_list[0].city_name)
    elif (city_num == 2):
        cityButton2.config(text=city_list[1].city_name)
    elif (city_num == 3):
        cityButton3.config(text=city_list[2].city_name)
    elif (city_num == 4):
        cityButton4.config(text=city_list[3].city_name)
    elif (city_num == 5):
        cityButton5.config(text=city_list[4].city_name)
    elif (city_num == 6):
        cityButton6.config(text=city_list[5].city_name)
    elif (city_num == 7):
        cityButton7.config(text=city_list[6].city_name)
    elif (city_num == 8):
        cityButton8.config(text=city_list[7].city_name)

    city_screen.mainloop()


# compare function for comparing stats
def compare():
    def display_ranks(event):
        names = []
        sort = []
        text = weather_option.get()
        for i in city_list:
            if (i.city_name != ""):
                names.append(i)
        if (text == "Current temperature"):
            for i in city_list:
                if i.current_temp != 0:
                    sort.append(i.current_temp)
            mergesort(sort)
            label2.config(text="Current temperature")
            names = pair_names("current", names, sort)
            update_labels(sort, names)
        elif (text == "Low temperature"):
            for i in city_list:
                if i.low_temp != 0:
                    sort.append(i.low_temp)
            mergesort(sort)
            label2.config(text="Lowest temperature")
            reverse_order(sort)
            names = pair_names("lowest", names, sort)
            update_labels(sort, names)
        elif (text == "High temperature"):
            for i in city_list:
                if i.high_temp != 0:
                    sort.append(i.high_temp)
            mergesort(sort)
            label2.config(text="Highest temperature")
            names = pair_names("highest", names, sort)
            update_labels(sort, names)
        elif (text == "Feels like"):
            for i in city_list:
                if i.high_temp != 0:
                    sort.append(i.feels_like)
            mergesort(sort)
            label2.config(text="Currently feels like")
            names = pair_names("feels", names, sort)
            update_labels(sort, names)
        elif (text == "Humidity"):
            for i in city_list:
                if i.humidity != 0:
                    sort.append(i.humidity)
            mergesort(sort)
            label2.config(text="Current humidity")
            names = pair_names("humidity", names, sort)
            update_labels(sort, names)
        elif (text == "Pressure"):
            for i in city_list:
                if i.pressure != 0:
                    sort.append(i.pressure)
            mergesort(sort)
            label2.config(text="Current pressure")
            names = pair_names("pressure", names, sort)
            update_labels(sort, names)
        else:
            pass

    def mergesort(list):
        if len(list) > 1:
            mid = len(list) // 2
            left = list[:mid]
            right = list[mid:]
            mergesort(left)
            mergesort(right)
            ctr = 0
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    list[ctr] = left[i]
                    i += 1
                else:
                    list[ctr] = right[j]
                    j += 1
                ctr += 1
            while i < len(left):
                list[ctr] = left[i]
                i += 1
                ctr += 1
            while j < len(right):
                list[ctr] = right[j]
                j += 1
                ctr += 1

    def reverse_order(list):
        templist = []
        ctr = len(list) - 1
        while ctr >= 0:
            templist.append(list[ctr] - 1)
            ctr -= 1

    def update_labels(data, names):
        if data_list[0] == True:
            sort_label1_desc.config(text=data[0])
            sort_label1.config(text=names[0])
        if data_list[1] == True:
            sort_label2_desc.config(text=data[1])
            sort_label2.config(text=names[1])
        if data_list[2] == True:
            sort_label3_desc.config(text=data[2])
            sort_label3.config(text=names[2])
        if data_list[3] == True:
            sort_label4_desc.config(text=data[3])
            sort_label4.config(text=names[3])
        if data_list[4] == True:
            sort_label5_desc.config(text=data[4])
            sort_label5.config(text=names[4])
        if data_list[5] == True:
            sort_label6_desc.config(text=data[5])
            sort_label6.config(text=names[5])
        if data_list[6] == True:
            sort_label7_desc.config(text=data[6])
            sort_label7.config(text=names[6])
        if data_list[7] == True:
            sort_label8_desc.config(text=data[7])
            sort_label8.config(text=names[7])

    def pair_names(identifier, names, data):
        newnames = []
        temp_list = city_list.copy()
        if identifier == "current":
            for i in data:
                found = False
                for j in temp_list:
                    if i == j.current_temp and found == False:
                        newnames.append(j.city_name)
                        temp_list.remove(j)
                        found = True
        elif identifier == "lowest":
            for i in data:
                found = False
                for j in temp_list:
                    if i == j.low_temp and found == False:
                        newnames.append(j.city_name)
                        temp_list.remove(j)
                        found = True
        elif identifier == "highest":
            for i in data:
                found = False
                for j in temp_list:
                    if i == j.high_temp and found == False:
                        newnames.append(j.city_name)
                        temp_list.remove(j)
                        found = True
        elif identifier == "humidity":
            for i in data:
                found = False
                for j in temp_list:
                    if i == j.humidity and found == False:
                        newnames.append(j.city_name)
                        temp_list.remove(j)
                        found = True
        elif identifier == "pressure":
            for i in data:
                found = False
                for j in temp_list:
                    if i == j.pressure and found == False:
                        newnames.append(j.city_name)
                        temp_list.remove(j)
                        found = True
        elif identifier == "feels":
            for i in data:
                found = False
                for j in temp_list:
                    if i == j.feels_like and found == False:
                        newnames.append(j.city_name)
                        temp_list.remove(j)
                        found = True
        return newnames

    comparescreen = tk.Tk()
    compare_window_width = 800
    compare_window_height = 600
    center_x = int(screen_width / 2 - compare_window_width / 2)
    center_y = int(screen_height / 2 - compare_window_height / 2)
    comparescreen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    comparescreen.title("Compare")

    choices = ["Current temperature", "Low temperature", "High temperature", "Feels like", "Humidity", "Pressure"]
    option = tk.StringVar()
    weather_option = ttk.Combobox(comparescreen, textvariable=option)
    weather_option['values'] = choices
    weather_option['state'] = 'readonly'
    weather_option.bind('<<ComboboxSelected>>', display_ranks)
    weather_option.grid(column=0, row=2, padx = 12, sticky=tk.W)
    weather_option.selection_clear()

    compare_label = tk.Label(comparescreen, text="Compare the weather of cities", font=("Arial", 14))
    compare_label.grid(column=0, row=0, sticky=tk.NSEW)

    refresh_button = tk.Button(comparescreen, text="Refresh data", command=lambda: update_cities())
    refresh_button.grid(column=0, row=3, padx = 12, sticky=tk.SW)

    label1 = tk.Label(comparescreen, text="City: ", font=("Arial", 15))
    label1.grid(column=1, row=1)
    label2 = tk.Label(comparescreen, text="Current temperature: ", font=("Arial", 15))
    label2.grid(column=2, row=1, ipadx=20, sticky=tk.W)

    if (data_list[0] == True):
        sort_label1 = tk.Label(comparescreen, text=city_list[0].city_name, font=("Arial", 15))
        sort_label1.grid(column=1, row=2, sticky=tk.W)
        sort_label1_desc = tk.Label(comparescreen, text=city_list[0].current_temp, font=("Arial", 15))
        sort_label1_desc.grid(column=2, row=2, sticky=tk.EW)

    if (data_list[1] == True):
        sort_label2 = tk.Label(comparescreen, text=city_list[1].city_name, font=("Arial", 15))
        sort_label2.grid(column=1, row=3, sticky=tk.W)
        sort_label2_desc = tk.Label(comparescreen, text=city_list[1].current_temp, font=("Arial", 15))
        sort_label2_desc.grid(column=2, row=3, sticky=tk.EW)

    if (data_list[2] == True):
        sort_label3 = tk.Label(comparescreen, text=city_list[2].city_name, font=("Arial", 15))
        sort_label3.grid(column=1, row=4, sticky=tk.W)
        sort_label3_desc = tk.Label(comparescreen, text=city_list[2].current_temp, font=("Arial", 15))
        sort_label3_desc.grid(column=2, row=4, sticky=tk.EW)

    if (data_list[3] == True):
        sort_label4 = tk.Label(comparescreen, text=city_list[3].city_name, font=("Arial", 15))
        sort_label4.grid(column=1, row=5, sticky=tk.W)
        sort_label4_desc = tk.Label(comparescreen, text=city_list[3].current_temp, font=("Arial", 15))
        sort_label4_desc.grid(column=2, row=5, sticky=tk.EW)

    if (data_list[4] == True):
        sort_label5 = tk.Label(comparescreen, text=city_list[4].city_name, font=("Arial", 15))
        sort_label5.grid(column=1, row=6, sticky=tk.W)
        sort_label5_desc = tk.Label(comparescreen, text=city_list[4].current_temp, font=("Arial", 15))
        sort_label5_desc.grid(column=2, row=6, sticky=tk.EW)

    if (data_list[5] == True):
        sort_label6 = tk.Label(comparescreen, text=city_list[5].city_name, font=("Arial", 15))
        sort_label6.grid(column=1, row=7, sticky=tk.W)
        sort_label6_desc = tk.Label(comparescreen, text=city_list[5].current_temp, font=("Arial", 15))
        sort_label6_desc.grid(column=2, row=7, sticky=tk.EW)

    if (data_list[6] == True):
        sort_label7 = tk.Label(comparescreen, text=city_list[6].city_name, font=("Arial", 15))
        sort_label7.grid(column=1, row=8, sticky=tk.W)
        sort_label7_desc = tk.Label(comparescreen, text=city_list[6].current_temp, font=("Arial", 15))
        sort_label7_desc.grid(column=2, row=8, sticky=tk.EW)

    if (data_list[7] == True):
        sort_label8 = tk.Label(comparescreen, text=city_list[7].city_name, font=("Arial", 15))
        sort_label8.grid(column=1, row=9, sticky=tk.W)
        sort_label8_desc = tk.Label(comparescreen, text=city_list[7].current_temp, font=("Arial", 15))
        sort_label8_desc.grid(column=2, row=9, sticky=tk.EW)

    comparescreen.mainloop()


cityButton1 = ttk.Button(frmMain, text='Add a city', command=lambda: get_city(1))
cityButton1.grid(column=1, row=2, padx=3, pady=6, ipadx=8, ipady=8)

cityButton2 = ttk.Button(frmMain, text='Add a city', command=lambda: get_city(2))
cityButton2.grid(column=2, row=2, padx=3, pady=6, ipadx=8, ipady=8)

cityButton3 = ttk.Button(frmMain, text="Add a city", command=lambda: get_city(3))
cityButton3.grid(column=3, row=2, padx=3, pady=6, ipadx=8, ipady=8)

cityButton4 = ttk.Button(frmMain, text="Add a city", command=lambda: get_city(4))
cityButton4.grid(column=4, row=2, padx=3, pady=6, ipadx=8, ipady=8)

cityButton5 = ttk.Button(frmMain, text="Add a city", command=lambda: get_city(5))
cityButton5.grid(column=1, row=3, ipadx=8, ipady=8)

cityButton6 = ttk.Button(frmMain, text="Add a city", command=lambda: get_city(6))
cityButton6.grid(column=2, row=3, ipadx=8, ipady=8)

cityButton7 = ttk.Button(frmMain, text="Add a city", command=lambda: get_city(7))
cityButton7.grid(column=3, row=3, ipadx=8, ipady=8)

cityButton8 = ttk.Button(frmMain, text="Add a city", command=lambda: get_city(8))
cityButton8.grid(column=4, row=3, ipadx=8, ipady=8)

compareButton = ttk.Button(frmMain, text="Compare", command=lambda: compare())
compareButton.grid(column=2, row=4, sticky=tk.NSEW, pady=9, ipadx=8, ipady=8, columnspan=2)

presetButton1 = ttk.Button(frmMain, text="Preset 1", command=lambda: preset1())
presetButton1.grid(column=2, row=5, pady=3, ipadx=8, ipady=8)

presetButton2 = ttk.Button(frmMain, text="Preset 2",command=lambda: preset2())
presetButton2.grid(column=3, row=5, ipadx=8, ipady=8)

help_label = tk.Label(root, text="Press one of the \"Add a city\" buttons to get started")
help_label.grid(column=0, row=1)

frmMain.grid(row=0, column=0)
frmMain.grid_rowconfigure(0, weight=1)
frmMain.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
