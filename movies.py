#collect info on favourite movies then display them as an html page with links to trailers

import webbrowser
import fresh_tomatoes

class Movie:
	def __init__(self, movie_title, poster_image, trailer_youtube):
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

interstellar = Movie(movie_title="Interstellar",
	poster_image="http://fangirlnation.com/wp-content/uploads/2014/10/interstellar-poster.jpg",
	trailer_youtube="https://www.youtube.com/watch?v=zSWdZVtXT7E")

print(interstellar.__dict__)

eot = Movie(movie_title = "Edge of Tomorrow",
	poster_image = "http://www.graffitiwithpunctuation.net/wp-content/uploads/2014/06/Edge_of_Tomorrow_live-die-repeat.jpg",
	trailer_youtube = "https://www.youtube.com/watch?v=yUmSVcttXnI")
print(eot.__dict__)
movies = [interstellar, eot]
fresh_tomatoes.open_movies_page(movies)
