#/usr/bin/python
"""
Collect info on favourite movies then display them as an html page with
links to trailers.
"""


import webbrowser
import fresh_tomatoes



# Don't need additional methods. pylint: disable=too-few-public-methods
class Movie(object):
    """
    Return an object with movie metadata.

    Attributes:
        movie_title: Title of the movie.
        poster_image: URL to an image of the movie's poster.
        trailer_youtube: URL to a youtube video of the official trailer.
        rating: Rating (0-100%) according to the Rotten Tomatoes website.
        budget: The money spent making the film (in USD millions).
        revenue: The money earned worldwide from the movie (in USD millions).
    """

    # Can't avoid lots of arguments. pylint: disable=too-many-arguments
    def __init__(self, movie_title, poster_image, trailer_youtube,
                 rating, budget, revenue):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        if rating >= 60:
            self.rating = "Fresh"
        else:
            self.rating = "Rotten"
        if revenue - budget >= 0:
            self.financial_success = True
        else:
            self.financial_success = False

    def show_trailer(self):
        """Open the film trailer in the system default web browser."""
        webbrowser.open(self.trailer_youtube_url)


def main():
    """Main function."""
    # Create a list of favourite movies, with relevant metadata loaded.
    interstellar = Movie(
        movie_title="Interstellar",
        poster_image=("http://fangirlnation.com/wp-content/"
                      "uploads/2014/10/interstellar-poster.jpg"),
        trailer_youtube="https://www.youtube.com/watch?v=zSWdZVtXT7E",
        rating=71,
        budget=165,
        revenue=675)
    edge_of_tomorrow = Movie(
        movie_title="Edge of Tomorrow",
        poster_image=("http://www.graffitiwithpunctuation.net/wp-content/"
                      "uploads/2014/06/Edge_of_Tomorrow_live-die-repeat.jpg"),
        trailer_youtube="https://www.youtube.com/watch?v=yUmSVcttXnI",
        rating=90,
        budget=178,
        revenue=369.2)
    movies = [interstellar, edge_of_tomorrow]

    # Generate an HTML file and load in the movie information.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
