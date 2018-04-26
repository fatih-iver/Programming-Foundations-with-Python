import media, fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch2v=vwy3H85NOG4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://upload.wikimedia.org/wikipediand/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceRgWV8io") 

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch2v=atLg2wQ12mvu")

hunger_games = media.Movie("Honger Games",
                           "Storyline",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch2v=PbA63a7H0bo") 

ratatouille = media.Movie("Ratatouille",
                          "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch2v=c3sBBRxDAgk")  

school_of_rock = media.Movie("School of Rock",
                             "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch2v=3PsUJFEBC74") 

movies = [toy_story, avatar, midnight_in_paris, hunger_games, ratatouille, school_of_rock]

print(media.Movie.VALID_RATINGS)

#fresh_tomatoes.open_movies_page(movies)
