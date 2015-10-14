#collect info on favourite movies then display them as an html page with links to trailers

import webbrowser
import fresh_tomatoes

class Movie:
	title = ""
	poster_image_url = ""
	trailer_youtube_url = ""
	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

interstellar = Movie()
interstellar.title = "Interstellar"
interstellar.poster_image_url = "http://fangirlnation.com/wp-content/uploads/2014/10/interstellar-poster.jpg" 
interstellar.trailer_youtube_url = "https://www.youtube.com/watch?v=zSWdZVtXT7E"

eot = Movie()
eot.title = "Edge of Tomorrow"
eot.poster_image_url = "http://www.graffitiwithpunctuation.net/wp-content/uploads/2014/06/Edge_of_Tomorrow_live-die-repeat.jpg"
eot.trailer_youtube_url = "https://www.youtube.com/watch?v=yUmSVcttXnI"

movies = [interstellar, eot]
fresh_tomatoes.open_movies_page(movies)
