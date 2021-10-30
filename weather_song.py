
from bs4 import BeautifulSoup
import requests
import re
import random
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# adapted from https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

def weather(city):
    """
    Scrape location, time, sky info, and temperature from google
    :param city: the city to get weather for
    :return: 
    """
    city = city.replace(" ", "+")
    res = requests.get(f'https://www.google.com/search?q={city}+weather&oq={city}+weather&aqs=chrome..69i57j69i64.3873j0j1&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather+"°F")
    

def sky(city):
    """
    Scrape and return sky info from google
    :param city: the city to get weather for
    :return: the sky info (Sunny, Cloudy, Rainy, etc)
    """
    city = city.replace(" ", "+")
    res = requests.get(f'https://www.google.com/search?q={city}+weather&oq={city}+weather&aqs=chrome..69i57j69i64.3873j0j1&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    sky = soup.select('#wob_dc')[0].getText().strip()
    return sky

def temperature(city):
    """
    Scrape and return temperature from google
    :param city: the city to get weather for
    :return: the temperature in degrees F
    """
    city = city.replace(" ", "+")
    res = requests.get(f'https://www.google.com/search?q={city}+weather&oq={city}+weather&aqs=chrome..69i57j69i64.3873j0j1&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    temp = int(soup.select('#wob_tm')[0].getText().strip())
    return temp

###
# Lists of songs to choose from based on the weather
###
sunny_list = [ \
    "Sound of Sunshine", \
    "Sunshine & Whiskey", \
    "Sunshine - NEEDTOBREATHE", \
    "Till Dawn (Here Comes The Sun)", \
    "Sunflower - Spiderman", \
    "Beers and Sunshine", \
    "Sun Daze", \
    "Brighter Than The Sun", \
    "Here Comes The Sun", \
    "Walking On Sunshine", \
    "Good Day Sunshine - The Beatles", \
    "Good Day sunshine - Haley Reinhart", \
    "Mr. Blue Sky", \
    "Blue Skies - Frank Sinatra", \
    "Blue Skies - Ella Fitzgerald", \
    "Blue Skies - Jamiroquai", \
    "Island In The Sun" \
]

cloudy_list = [ \
    "Aint No Sunshine", \
    "Cloudy Day - Tones and I", \
    "Cloudy This Morning - George winston", \
    "Cloudy Sky - Tundra Beats", \
    "Cloudy - Simon and Garfunkel", \
    "Partly Cloudy Kids Aviva", \
    "Overcast - Denham", \
    "Clouds - Zach Sobiech", \
    "Never Seen The Rain" \
]

stormy_list = [ \
    "Riders On The Storm", \
    "Stormy Weather - Etta James", \
    "Like A Hurricane", \
    "Stormy Weather - Kings of Leon", \
    "Thunderstruck", \
    "Stormy Weather - frank Sinatra", \
    "Stormy Weather - Tony Bennet", \
    "Praise You In This Storm", \
    "Lightning - eric church", \
    "Lightning and Thunder feat John Legend", \
    "Rock You Like a Hurricane", \
    "Like a Hurricane - Neil Young", \
    "Hurricane - Luke Combs", \
    "Crying Lightning", \
    "Storm Warning", \
    "Hurricane - Kanye West", \
    "Hurricane - Thirty Seconds To Mars", \
    "Thunder - Imagine Dragons", \
    "Tornado - Little Big Town", \
    "Shelter From The Storm", \
    "Thunder Road" \
]

rainy_list = [ \
    "It Will Rain", \
    "RAIN", \
    "Paris in the Rain", \
    "Set Fire to the Rain", \
    "Dancing In The Rain", \
    "Have You Ever Seen the Rain ", \
    "Candy Rain", \
    "Purple Rain", \
    "When it rains it pours", \
    "God Love the Rain", \
    "Rain is a Good Thing", \
    "Umbrella", \
    "Raindrops keep fallin on my head", \
    "November Rain", \
    "The Rain Song", \
    "Wholl Stop the Rain", \
    "Have you ever seen the Rain", \
    "Raining on Sunday", \
    "Blue Eyes Crying in the Rain", \
    "I Wish It Would Rain Down", \
    "Rain On Me" \
]

snowy_list = [ \
    "Snow (hey oh)", \
    "Snow - Zach Bryan", \
    "Snow in my Shoe - Jazzinuf", \
    "Snowman - Sia", \
    "Sleet - Cloudchord", \
    "Snowstorm", \
    "While I Shovel the Snow" \
]

freezing_list = [ \
    "Cold feat Future", \
    "Colder Weather", \
    "Cold as You", \
    "Cold - Post Malone", \
    "Cold Water ", \
    "Cold as Ice", \
    "Cold as You - Taylor Swift", \
    "Cold as Stone - Lady A", \
    "Winter Winds", \
    "Valley Winter Song", \
    "The Fox in the Snow", \
    "Winter Sound - Bonus Track", \
    "Winter - Khalid", \
    "Coldest Winter", \
    "Wintertime - Cordae", \
    "Winter Wonderland", \
    "A Hazy Shade of Winter", \
    "Cold Stares" \
]

cool_list = [ \
    "Sweater Weather", \
    "Jacket Over Hoodie Over Shirt", \
    "Denim Jacket", \
    "Sweatpants", \
    "Flannel - Justin Timberlake", \
    "Hoodie Weather", \
    "BOOTS", \
    "Flannel Is The Color Of My Energy" \
]

warm_list = [ \
    "(Love is like a) Heat Wave", \
    "Heath Waves", \
    "Hot In Herre", \
    "Hot Stuff - Kygo", \
    "Heat of the Moment - Drake", \
    "Heat of the Night", \
    "Heat of the Summer", \
    "Summer Night City", \
    "Summer Wind - Frank Sinatra", \
    "Hot Fun in the Summertime", \
    "A Summer Song - Chad & Jeremy", \
    "Summer in the City", \
    "Boys of Summer", \
    "Under the Boardwalk", \
    "Summertime Sadness", \
    "Summertime - Kenny Chesney", \
    "Summertime - DJ Jazzy Jeff & the fresh prince", \
    "In the Summertime", \
    "Cruel Summer", \
    "Summertime Blues", \
    "(Sittin' On) the Dock of the Bay", \
    "Too Hot - Kool & The Gang", \
    "Too Hot - Jason Derulo" \
]

def get_sky_song(city):
    """
    Return a song based on the sky info for the city
    :param city: the city to get weather for
    :return: the song name
    """
    current_sky = sky(city)
    print(f"SKY:{current_sky}")
    if (re.search("[sS]torm", current_sky) or re.search("[tT]hunder", current_sky) or re.search("[lL]ightning", current_sky)):
        return random.choice(stormy_list)
    elif (re.search("[cC]loudy", current_sky) or re.search("[oO]vercast", current_sky)):
        return random.choice(cloudy_list)
    elif (re.search("[sS]un", current_sky) or re.search("[cC]lear", current_sky)):
        return random.choice(sunny_list)
    elif (re.search(f"{current_sky} [sS]now", current_sky) or re.search("[sS]leet", current_sky)):
        return random.choice(snowy_list)
    elif (re.search("[rR]ain", current_sky)):
        return random.choice(rainy_list)

def get_temperature_song(city):
    """
    Return a song based on the temperature for the city
    :param city: the city to get weather for
    :return: the song name
    """
    current_temp = int(temperature(city))
    print(f"TEMP:{current_temp}")
    if (current_temp > 60):
        return random.choice(warm_list)
    elif (current_temp > 32):
        return random.choice(cool_list)
    else:
        return random.choice(freezing_list)


###
# Local function tests
###
if __name__ == "__main__":
    print(get_sky_song("New York NY"))
    print(get_sky_song("Oklahoma City, OK"))
    print(get_sky_song("Texas"))
    print(get_sky_song("Miami, FL"))
    print(get_sky_song("Presena"))
    print(get_temperature_song("New York NY"))
