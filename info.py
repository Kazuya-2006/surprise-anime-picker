from random import choice
animes_series_name = ['horimiya', 'the great cleric', 'my tiny sempai', 'log horizan']
animes_shorts_name = ['Danchigai', 'My Wife is the Student Council President', 'Love is Like a Cocktail']

type = input("please input one of these options: series or shorts")

choice_series = choice(animes_series_name)
choise_shorts = choice(animes_shorts_name)

anime_series =[
    ['horimiya', '24 minutes', 'https://www.crunchyroll.com/series/G9VHN9P43/horimiya'],
    ['the great cleric', '24 minutes', 'https://www.crunchyroll.com/series/GG5H5XQ24/the-great-cleric'],
    ['my tiny sempai', '24 minutes', 'https://www.crunchyroll.com/series/G79H23Z45/my-tiny-senpai'],
    ['log horizan', '24 minutes', 'https://www.crunchyroll.com/series/GRVNMG93Y/log-horizon']
]

anime_shorts = [
    ['Danchigai', '3,5 minutes', 'https://www.crunchyroll.com/series/GY8VX3X7Y/danchigai'],
    ['My Wife is the Student Council President', '8 minutes', 'https://www.crunchyroll.com/series/GYP8XN95Y/my-wife-is-the-student-council-president'],
    ['Love is Like a Cocktail', '3 minutes', 'https://www.crunchyroll.com/series/G6P8QX856/love-is-like-a-cocktail']
]