from info import animes_series_name, animes_shorts_name, type, choice_series, choise_shorts, anime_series, anime_shorts
from random import choice

if type == 'series':
    print(" ")  # <--- this is to make it clearer
    print("I recommend the anime:", choice_series)
    if choice_series == 'horimiya':
        print("The duration of one episode is:", anime_series[0][1])
        print("link:", anime_series[0][2])
        print(" ")  # <--- this is to make it clearer
    elif choice_series == 'the great cleric':
        print("The duration of one episode is:", anime_series[1][1])
        print("link:", anime_series[1][2])
        print(" ")  # <--- this is to make it clearer
    elif choice_series == 'my tiny sempai':
        print("The duration of one episode is:", anime_series[2][1])
        print("link:", anime_series[2][2])
        print(" ")  # <--- this is to make it clearer
    elif choice_series == 'log horizan':
        print("The duration of one episode is:", anime_series[3][1])
        print("link:", anime_series[3][2])
        print(" ")  # <--- this is to make it clearer
elif type == 'shorts':
    print(" ")  # <--- this is to make it clearer
    print("I recommend the anime short:", choise_shorts)
    if choise_shorts == 'Danchigai':
        print("The duration of one episode is:", anime_shorts[0][1])
        print("link", anime_shorts[0][2])
        print(" ")  # <--- this is to make it clearer
    elif choise_shorts == 'My Wife is the Student Council President':
        print("The duration of one episode is:", anime_shorts[1][1])
        print("link", anime_shorts[1][2])
        print(" ")  # <--- this is to make it clearer
    elif choise_shorts == 'Love is Like a Cocktail':
        print("The duration of one episode is:", anime_shorts[2][1])
        print("link", anime_shorts[2][2])
        print(" ")  # <--- this is to make it clearer
else:
    print("error I don't understand")
    print("please chose between series or shorts")
