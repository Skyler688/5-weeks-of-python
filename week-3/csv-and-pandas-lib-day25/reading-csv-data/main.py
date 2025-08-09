# python3 week-3/csv-and-pandas-lib-day25/reading-csv-data/main.py

import csv

# if running from the project dir "reading_csv_data"
# with open("weather_data.csv") as file:
    # data = csv.reader(file)

# if running from the home dir
# with open("week-3/csv-and-pandas-lib-day25/reading-csv-data/weather_data.csv") as file:
#     data = csv.reader(file)

#     temperatures = []
#     for index, row in enumerate(data):
#         print(row)
#         if (index > 0):
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas

data = pandas.read_csv("week-3/csv-and-pandas-lib-day25/reading-csv-data/weather_data.csv")
print(type(data)) # data frame
print(type(data["temp"])) # series

data_dict = data.to_dict() # converts the data fram to a dict
print(data_dict)

temp_list = data["temp"].to_list() # converts a series into a list (array)
print(temp_list)

# Challange -> calculate the average temp

sum = 0
for temp in temp_list:
    sum += temp

average = sum / len(temp_list)

# alternatively can use -> average = sum(temp_list) / len(temp_list)

print(average)    

# pandas spicific function ".mean()", dose the same as the challange above.

print(data["temp"].mean())


# Challange find the largest temp using a pandas data series spicific methods
print(data["temp"].nlargest(1))
# or
print(data["temp"].max())


# getting data in columns
print(data["condition"])
#or
print(data.condition)


#getting data in rows
print(data[data.day == "Monday"])


#  Challange -> pull the row where the temp is the maximum™¡
print(data[data.temp == data.temp.max()])


# Challange -> grab mondays temp and convert to fahrenheit
monday_temp_c = data.loc[data.day == "Monday", "temp"].item()
print((monday_temp_c * 9/5) + 32)


# create a data fram from scratch
data_dict = {
    "players": ["jeff", "billy", "mike"],
    "scores": [47, 86, 12]
}

game_data = pandas.DataFrame(data_dict)
print(game_data)

#can also create a csv file from a DataFrame
game_data.to_csv("week-3/csv-and-pandas-lib-day25/reading-csv-data/game_data.csv")