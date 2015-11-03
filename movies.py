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

    Args:
        movie_title: Title of the movie.
        year: Year the movie was released.
        poster_image: URL to an image of the movie's poster.
        trailer_youtube: URL to a youtube video of the official trailer.
        rating: Rating (0-100%) according to the Rotten Tomatoes website.
        budget: The money spent making the film (in USD millions).
        revenue: The money earned worldwide from the movie (in USD millions).

    Attributes:
        movie_title: Title of the movie.
        year: Year the movie was released.
        poster_image: URL to an image of the movie's poster.
        trailer_youtube: URL to a youtube video of the official trailer.
        rating: "Fresh" or "Rotten" according to the Rotten Tomatoes website.
        profit_ratio: revenue / profit - how much of a financial success it was.
    """

    # Can't avoid lots of arguments. pylint: disable=too-many-arguments
    def __init__(self, movie_title, year, poster_image,
                 trailer_youtube, rating, budget, revenue):
        self.title = movie_title
        self.year = year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        if rating >= 60:
            self.rating = "Fresh"
        else:
            self.rating = "Rotten"
        self.profit_ratio = round(revenue / budget, 2)

    def show_trailer(self):
        """Open the film trailer in the system default web browser."""
        webbrowser.open(self.trailer_youtube_url)


def main():
    """Main function."""
    # Create a list of favourite movies, with relevant metadata loaded.
    interstellar = Movie(
        movie_title="Interstellar",
        year=2014,
        poster_image=("http://fangirlnation.com/wp-content/"
                      "uploads/2014/10/interstellar-poster.jpg"),
        trailer_youtube="https://www.youtube.com/watch?v=zSWdZVtXT7E",
        rating=71,
        budget=165,
        revenue=675)
    edge_of_tomorrow = Movie(
        movie_title="Edge of Tomorrow",
        year=2014,
        poster_image=("http://www.graffitiwithpunctuation.net/wp-content/"
                      "uploads/2014/06/Edge_of_Tomorrow_live-die-repeat.jpg"),
        trailer_youtube="https://www.youtube.com/watch?v=yUmSVcttXnI",
        rating=90,
        budget=178,
        revenue=369.2)
    bridge_of_spies = Movie(
        movie_title="Bridge of Spies",
        year=2015,
        poster_image=("http://www.kinemamillennium.com/wp-content/"
                      "uploads/2015/09/d2.jpg"),
        trailer_youtube="https://www.youtube.com/watch?v=mBBuzHrZBro",
        rating=92,
        budget=40,
        revenue=57.9)
    the_matrix = Movie(
        movie_title="The Matrix",
        year=1999,
        poster_image=("http://www.fatmovieguy.com/wp-content/uploads/"
                      "2014/12/The-Matrix-Movie-Poster.jpg"),
        trailer_youtube="https://www.youtube.com/watch?v=vKQi3bBA1y8",
        rating=87,
        budget=63,
        revenue=463.5)
    movies = [interstellar, edge_of_tomorrow, bridge_of_spies, the_matrix]
    # Sort movies from oldest to newest.
    movies.sort(key=lambda x: x.year)

    # Generate an HTML file and load in the movie information.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
