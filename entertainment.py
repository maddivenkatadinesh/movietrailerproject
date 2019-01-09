import mediafile
import fresh_tomatoes
bharathanenenu=mediafile.Tollywoodmovies("BHARATH ANE NENU",
                                           "The YOUNGEST C.M UNEXPECTEDLY",
                                           "https://upload.wikimedia.org/wikipedia/en/thumb/6/68/Bharat_Ane_Nenu_poster.jpg/220px-Bharat_Ane_Nenu_poster.jpg",
                                           "https://www.youtube.com/watch?v=orkPrGSAETs")
avengers=mediafile.Tollywoodmovies("AVENGERS INFINITY WAR",
                                   "A STORY OF SUPER HEROES",
                                   "https://cdn.newsapi.com.au/image/v1/e5adc2d6b5484c81a226d418494194aa?width=650",
                                   "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
blackpanther=mediafile.Tollywoodmovies("BLACK PANTHER",
                                       "A HERO WHICH HELP THE PEOPLE BY THE DEVILS",
                                       "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCW2mXEW_SKNsBPucrMTJl2yVCCCUwgKluVC3pM8K5-82UfPhf",
                                       "https://www.youtube.com/watch?v=xjDjIWPwcPU")
fastandfurious=mediafile.Tollywoodmovies("FAST AND FURIOUS",
                                         "IT IS AN ACTION THRIlING MOVIE",
                                         "https://upload.wikimedia.org/wikipedia/en/thumb/b/bb/Fast_Six_Soundtrack.jpg/220px-Fast_Six_Soundtrack.jpg",
                                         "https://www.youtube.com/watch?v=J_k1yGJtHgw")
battleship=mediafile.Tollywoodmovies("BATTLE SHIP",
                                     "IT IS FULL OF ALIENS",
                                     "https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Battleship_Poster.jpg/220px-Battleship_Poster.jpg",
                                     "https://www.youtube.com/watch?v=yWuZtDeeZmc")
thenun=mediafile.Tollywoodmovies("THE NUN",
                                 "HALLOWIN FILM",
                                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6tuXR-7MW1s2EN939XbmaoNANr_n88fXRrjrNSXgihPgbouX5",
                                 "https://www.youtube.com/watch?v=pzD9zGcUNrw")
movies=[bharathanenenu,avengers,blackpanther,fastandfurious,battleship,thenun]
fresh_tomatoes.open_movies_page(movies)
