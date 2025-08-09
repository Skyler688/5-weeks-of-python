# python3 week-3/csv-and-pandas-lib-day25/squirrel-census/main.py

import pandas

# Chalange create new csv with the total number of each primary color ("Grey", "Cinnamon", "Black")

data = pandas.read_csv("week-3/csv-and-pandas-lib-day25/squirrel-census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_list = data["Primary Fur Color"].to_list() # create a list from the prymary color series

# loop through the list counting each color
gray = 0
cinnamon = 0
black = 0
null = 0
for color in color_list:
    if (color == 'Gray'):
        gray += 1
    elif (color == 'Cinnamon'):
        cinnamon += 1
    elif (color == 'Black'):
        black += 1
    else:
        print(f"Error, invalid color type: {color}") 
        null += 1

# print(gray)
# print(cinnamon)
# print(black) 
# print(null)     

# create a dict with the color data
total_colors = {
    "colors": ["Gray", "Cinnamon", "Black", "Null"],
    "number": [gray, cinnamon, black, null]
}

# convert the dict to a data fram
total_colors_frame = pandas.DataFrame(total_colors)

# create a csv with the data frame
total_colors_frame.to_csv("week-3/csv-and-pandas-lib-day25/squirrel-census/total_colors.csv")