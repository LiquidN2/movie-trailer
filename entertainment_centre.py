import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Using rock to learn music",
                             "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                          "A rat learns to become a chef",
                          "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=1yKqLNnxGZw")

avengers_infinity_war = media.Movie("Avengers: Infinity War",
                       "A group of super heroes protect the Earth from aliens",
                       "https://en.wikipedia.org/wiki/Avengers:_Infinity_War#/media/File:Avengers_Infinity_War_poster.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

alien_covenant = media.Movie("Alien: Covenant",
                             "A group of space explorer discover alien civilization and and its terrible creation",
                             "https://en.wikipedia.org/wiki/Alien:_Covenant#/media/File:Alien_Covenant_Teaser_Poster.jpg",
                             "https://www.youtube.com/watch?v=svnAD0TApb8")

movies = [toy_story, avatar, school_of_rock, ratatouille, avengers_infinity_war, alien_covenant]
fresh_tomatoes.open_movies_page(movies)