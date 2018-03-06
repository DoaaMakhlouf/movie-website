import fresh_tomatoes
import media

"""This file produces a web page containing a list of six movies,

represented by the movie title and poster image.

On clicking on the poster image, the youtube trailer will be played.
"""

# Creating movies
the_book_thief = media.Movie("The Book Thief",
                             "https://goo.gl/dpRx5M",
                             "https://www.youtube.com/watch?v=YCOwipZviSc")

black_swan = media.Movie("Black Swan",
                         "https://goo.gl/963RoS",
                         "https://www.youtube.com/watch?v=5jaI1XOB-bs")

big_hero_6 = media.Movie("Big Hero 6",
                         "https://goo.gl/x7QsSS",
                         "https://www.youtube.com/watch?v=z3biFxZIJOQ")

wall_e = media.Movie("WALL-E",
                     "https://goo.gl/XYQ7K3",
                     "https://www.youtube.com/watch?v=9pyBKj5-jVk")

v_for_vendetta = media.Movie("V for Vendetta",
                             "https://goo.gl/9K32xs",
                             "https://www.youtube.com/watch?v=k_13fFIrhPk")

about_time = media.Movie("About Time",
                         "https://goo.gl/98MyRm",
                         "https://www.youtube.com/watch?v=7OIFdWk83no")

# Creating the list of movies
movies = [the_book_thief, black_swan,
          big_hero_6, wall_e, v_for_vendetta, about_time]

# Creating the web page that contains the list of movies
fresh_tomatoes.open_movies_page(movies)
