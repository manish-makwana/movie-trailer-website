#/usr/bin/python
"""
Collect info on favourite movies then display them as an html page with
links to trailers.
"""


import webbrowser
import fresh_tomatoes


class Movie(object):
    """
    Return an object with movie metadata.
    
    Attributes:
        movie_title: Title of the movie.
        poster_image: URL to an image of the movie's poster.
        trailer_youtube: URL to a youtube video of the official trailer.
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open the film trailer in the system default web browser."""
        webbrowser.open(self.trailer_youtube_url)


def main():
    # Create a list of favourite movies, with relevant metadata loaded.
    INTERSTELLAR = Movie(
        movie_title = "Interstellar",
        poster_image = ("http://fangirlnation.com/wp-content/"
                        "uploads/2014/10/interstellar-poster.jpg"),
        trailer_youtube = "https://www.youtube.com/watch?v=zSWdZVtXT7E")
    EOT = Movie(
        movie_title = "Edge of Tomorrow",
        poster_image = ("http://www.graffitiwithpunctuation.net/wp-content/"
                        "uploads/2014/06/Edge_of_Tomorrow_live-die-repeat.jpg"),
        trailer_youtube = "https://www.youtube.com/watch?v=yUmSVcttXnI")
    MOVIES = [INTERSTELLAR, EOT]

    # Generate an HTML file and load in the movie information.
    fresh_tomatoes.open_movies_page(MOVIES)

if __name__ == '__main__':
        main()
