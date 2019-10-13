import media
import fresh_tomatoes


toy_story4 = media.Movie("Toy Story 4",
                        "Toy come to life",
                        "http://2.bp.blogspot.com/-Lf3Xcyd48P8/USPLlqv1t8I/AAAAAAAAKhc/wPtgEjmc1eo/s1600/Toy+Story+4+Poster.png",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")
#print(toy_story.title)

school_of_rock = media.Movie("Toy Story",
                        "Toy come to life",
                        "http://2.bp.blogspot.com/-Lf3Xcyd48P8/USPLlqv1t8I/AAAAAAAAKhc/wPtgEjmc1eo/s1600/Toy+Story+4+Poster.png",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

ratatouile = media.Movie("Toy Story",
                        "Toy come to life",
                        "http://2.bp.blogspot.com/-Lf3Xcyd48P8/USPLlqv1t8I/AAAAAAAAKhc/wPtgEjmc1eo/s1600/Toy+Story+4+Poster.png",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

midnight_in_paris = media.Movie("Toy Story",
                        "Toy come to life",
                        "http://2.bp.blogspot.com/-Lf3Xcyd48P8/USPLlqv1t8I/AAAAAAAAKhc/wPtgEjmc1eo/s1600/Toy+Story+4+Poster.png",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

hunger_game = media.Movie("Toy Story",
                        "Toy come to life",
                        "http://2.bp.blogspot.com/-Lf3Xcyd48P8/USPLlqv1t8I/AAAAAAAAKhc/wPtgEjmc1eo/s1600/Toy+Story+4+Poster.png",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

avatar = media.Movie("Toy Story",
                        "Toy come to life",
                        "http://2.bp.blogspot.com/-Lf3Xcyd48P8/USPLlqv1t8I/AAAAAAAAKhc/wPtgEjmc1eo/s1600/Toy+Story+4+Poster.png",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")




movies = [toy_story4, school_of_rock, ratatouile, midnight_in_paris, hunger_game, avatar]

fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)