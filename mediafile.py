import webbrowser

class Tollywoodmovies():
    def __init__(self,movie_title,movie_storyline,movie_postering_url,movie_youtubeurl):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=movie_postering_url
        self.trailer_youtube_url=movie_youtubeurl
    def show_movie_trailers(self):
        webbrowser.open(self.trailer_youtube_url)
