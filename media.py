import webbrowser


class Movie():

    """This class stores movie information and helps to show the trailer.
    Args:
        title (str): stores the movie's title
        poster_image_url (str): stores the movie's poster image URL
        trailer_youtube_url (str): stores the movie's trailer youtube URL
    Attributes:
        title (str): stores the movie's title
        poster_image_url (str): stores the movie's poster image URL
        trailer_youtube_url (str): stores the movie's trailer youtube URL
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # The following function is used to show the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
