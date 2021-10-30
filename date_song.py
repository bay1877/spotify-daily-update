import datetime
import calendar
import random

def day_of_week():
    """
    Get the day of the week (Monday, Tuesday, Wednesday, etc)
    :return: the day of the week
    """
    return calendar.day_name[datetime.date.today().weekday()]

def day_of_month():
    """
    Get the day of the month (1, 2, 3, 4, 5, etc)
    :return: the day of the month
    """
    return datetime.date.today().day

def get_weekday_song():
    """
    Return a song based on the day of the week
    :return: the song name
    """
    current_day = day_of_week()
    print(f"WEEKDAY:{current_day}")
    if (current_day == "Monday"):
        return random.choice([ \
                            "Monday - Imagine Dragons", \
                            "Monday Morning - Quinn XCII", \
                            "Monday Mornin' Missin' You - Blake Shelton", \
                            "Monday Morning - Fleetwood Mac", \
                            "Monday, Monday", \
                            "Every Day is a Monday"])
    elif (current_day == "Tuesday"):
        return random.choice([ \
                            "Tuesdays", \
                            "Tuesday (feat Drake)", \
                            "Tuesday's Gone", \
                            "Tuesday I'll Be Gone", \
                            "Taco Tuesday - Migos", \
                            "Taco Tuesday - Lil Jon", \
                            "Tuesday Afternoon"])
    elif (current_day == "Wednesday"):
        return random.choice([ \
                            "Wednesday Morning - Macklemore", \
                            "Wednesday Night Interlude - Drake", \
                            "Wednesday Morning, 3AM"])
    elif (current_day == "Thursday"):
        return random.choice([ \
                            "Thursday - The Weeknd", \
                            "Thursday - Jess Glyne", \
                            "(Thursday) Here's Why I Did Not Go to Work Today", \
                            "Like a Summer Thursday", \
                            "Sweet Thursday"])
    elif (current_day == "Friday"):
        return random.choice([ \
                            "Friday Night - Eric Paslay ", \
                            "Last Friday Night", \
                            "Finally Friday - George Jones", \
                            "Friday Rascall Flatts", \
                            "I Gotta Feeling", \
                            "Friday Night in Dixie", \
                            "Fridays Child", \
                            "Hymn for the Weekend", \
                            "Friday Night Fish Fry", \
                            "Friday Night - Lady A", \
                            "Hello Friday - Flo Rida"])
    elif (current_day == "Saturday"):
        return random.choice([ \
                            "Louisiana Saturday Night", \
                            "American Saturday Night", \
                            "Small Town Saturday Night", \
                            "Satuday Night's Alright", \
                            "Saturday in the Park", \
                            "Saturday - Twenty One Pilots", \
                            "Saturday Nights - Khalid", \
                            "Saturday Sun - Vance Joy"])
    elif (current_day == "Sunday"):
        return random.choice([ \
                            "Sunday Candy", \
                            "Sunday Morning - Parmalee", \
                            "Sunday Morning - Maroon 5", \
                            "Sunday Best", \
                            "Sunday", \
                            "Closed on Sunday", \
                            "Raining on Sunday", \
                            "A Month of Sundays", \
                            "That's What I Love About Sunday", \
                            "Sunday Drive", \
                            "Another Sunday in the South - Miranda Lambert", \
                            "Sunday - Sia", \
                            "Sunday Morning - Maroon 5", \
                            "A Month of Sundays - Don Henly", \
                            "Lazing on a Sunday Afternoon - Queen", \
                            "Sunday Morning Coming Down", \
                            "Blue Sunday - The Doors", \
                            "A Sunday Kind of Love - Etta James"])

def get_monthday_song():
    """
    Return a song based on the day of the month
    :return: the song name
    """
    current_day = day_of_month()
    print(f"MONTHDAY:{current_day}")
    if (current_day == 1):
        return random.choice([ \
                            "One of Us", \
                            "One - Harry Nilsson", \
                            "One More Night ", \
                            "One - Metallica", \
                            "The One - Backstreet Boys", \
                            "1 Step Forward, 3 Steps Back"])
    elif (current_day == 2):
        return random.choice(["It Takes Two", "Two Black Cadillacs"])
    elif (current_day == 3):
        return random.choice(["Three Little Birds"])
    elif (current_day == 4):
        return random.choice(["Four Mintues", "Four Five Seconds"])
    elif (current_day == 5):
        return random.choice(["Mambo Number 5", "I Got 5 on It", "Five More Minutes"])
    elif (current_day == 6):
        return random.choice(["Six Feet Under"])
    elif (current_day == 7):
        return random.choice([ \
                            "7 Years", \
                            "Seven Bridges Road", \
                            "Seven Seas of Rhye", \
                            "Seven Nation Army", \
                            "7 things"])
    elif (current_day == 8):
        return random.choice(["Eight Days a Week", "Eight Miles High", "8 out of 10"])
    elif (current_day == 9):
        return random.choice(["Love Potion Number 9"])
    elif (current_day == 13):
        return random.choice([
                            "13 - LANY", \
                            "Floor 13 - Machine Gun Kelly", \
                            "13 - DDG", \
                            "Thirteen - Johnny Cash"])
    elif (current_day == 14):
        return random.choice(["14,400 Minutes", "March 15th", "14 Miles From Home"])
    elif (current_day == 15):
        return random.choice(["Fifteen - Taylor Swift"])
    elif (current_day == 16):
        return random.choice(["Summer Sixteen", "Sixteen Tons", "Sixteen"])
    elif (current_day == 17):
        return random.choice(["Edge of Seventeen"])
    elif (current_day == 21):
        return random.choice(["Twenty One - Khalid"])
    elif (current_day == 22):
        return random.choice(["22 - Taylor Swift", "Twenty Two and Some Change", "Twentytwo - Thea"])
    elif (current_day == 23):
        return random.choice(["23 Sam Hunt", "23 Mike Will", "23 Chayce Beckham"])
    elif (current_day == 24):
        return random.choice(["24 - Kanye"])
    else:
        return ""



###
# Local function tests
###
if __name__ == "__main__":
    print(get_weekday_song())
    print(get_monthday_song())