#Import data loading functions
from poster_image_url_loader import poster_image_url_loader
from title_loader import title_loader
from trailer_youtube_url_loader import trailer_youtube_url_loader
from movie_list_maker import movie_list_maker
from fresh_tomatoes import open_movies_page

#Import Movie class
from Movie import Movie

#Load data
poster_image_url_s = poster_image_url_loader();
title_s = title_loader();
trailer_youtube_url_s = trailer_youtube_url_loader();

#Instantiate linked list of Movies with data
movies =  movie_list_maker(poster_image_url_s, title_s, trailer_youtube_url_s);
    
#Call function
open_movies_page(movies)
    
    