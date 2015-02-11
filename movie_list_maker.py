from Movie import Movie

def movie_list_maker(poster_image_url_s, title_s, trailer_youtube_url_s):
    movies = [];
    for i in range(0, 3):
        movies.append(Movie(poster_image_url_s[i], title_s[i], trailer_youtube_url_s[i]));
        
    return movies;