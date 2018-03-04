import fresh_tomatoes
import media

"""This file produces a web page containing a list of six movies,

represented by the movie title and poster image. On clicking on the poster image,

the youtube trailer will be played.
"""

# Creating movies
the_book_thief = media.Movie("The Book Thief",
                "https://upload.wikimedia.org/wikipedia/en/7/72/The-Book-Thief_poster.jpg",
                "https://www.youtube.com/watch?v=YCOwipZviSc")

black_swan = media.Movie("Black Swan",
            "https://upload.wikimedia.org/wikipedia/en/6/68/Black_Swan_poster.jpg",
            "https://www.youtube.com/watch?v=5jaI1XOB-bs")

big_hero_6 = media.Movie("Big Hero 6",
            "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
            "https://www.youtube.com/watch?v=z3biFxZIJOQ")

wall_e = media.Movie("WALL-E",
        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/WALL-Eposter.jpg/220px-WALL-Eposter.jpg",
        "https://www.youtube.com/watch?v=9pyBKj5-jVk")

v_for_vendetta = media.Movie("V for Vendetta",
                "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",
                "https://www.youtube.com/watch?v=k_13fFIrhPk")

about_time = media.Movie("About Time",
        "https://upload.wikimedia.org/wikipedia/en/thumb/8/88/About_Time_Poster.jpg/250px-About_Time_Poster.jpg",
        "https://www.youtube.com/watch?v=7OIFdWk83no")

# Creating the list of movies
movies = [the_book_thief, black_swan, big_hero_6, wall_e, v_for_vendetta, about_time]

# Creating the web page that contains the list of movies
fresh_tomatoes.open_movies_page(movies)
