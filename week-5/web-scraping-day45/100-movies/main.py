# Challange create a txt file containing the top 100 movies in order using web scraping of the websight.

from bs4 import BeautifulSoup as bs
import requests

# grab the html file with a get request
responce = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
responce.raise_for_status() # catch any errors

if responce.status_code == 200:
    html_file = responce.text

    soup = bs(html_file, "html.parser") # parse the html into a soup object
    
    titles = soup.find_all(name="h3", class_="title") # grabing the tags containing each title into a list
    movies = [None] * 100 # allocating space in the array so i can add movies in order using the movie rank (starts at 99)
    for title in titles:
        # used to grab the rank number of the list
        split = title.getText().split(")")
        # if the split failed try the ":"
        if len(split) == 1:
            split = title.getText().split(":") # NOTE had to add this because one of the movie titles has a typo, uses ":" intead of ")"

        rank = int(split[0]) - 1 
        movie = split[1]
        movies[rank] = movie # creating a orderd list with the movie rank "starts from 99"

    # create the ordered txt file with the orderd movie list
    with open("movies.txt", "w") as file:
        for rank, movie in enumerate(movies):
            file.write(f"{rank + 1}: {movie}\n")    

else:
    print(f"Failed to get html file.")    
