import requests
import datetime
import webbrowser
import pywhatkit
import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv(
    "OPENWEATHER_API_KEY", "bd5e378503939ddaee76f12ad7a97608"
)

# def map_task(intent, user_text):
#     # TIME
#     if intent == "time":
#         return datetime.datetime.now().strftime("The time is %H:%M")

#     # DATE
#     elif intent == "date":
#         return f"Today's date is {datetime.date.today()}"

#     # WEATHER (FIXED CITY)
#     elif intent == "weather":
#         city = "Nainital"
#         try:
#             url = (
#                 "https://api.openweathermap.org/data/2.5/weather"
#                 f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
#             )
#             res = requests.get(url).json()
#             if res.get("cod") != 200:
#                 return "Unable to fetch weather right now."
#             weather = res["weather"][0]["description"]
#             temp = res["main"]["temp"]
#             return f"The weather in {city} is {weather} with temperature {temp}°C"
#         except:
#             return "Weather service is unavailable."

#     # GOOGLE SEARCH
#     elif intent == "google_search":
#         try:
#             webbrowser.open(f"https://www.google.com/search?q={user_text}")
#             return f"Searching Google for {user_text}."
#         except:
#             return "Google search failed."

#     # MUSIC
#     elif intent == "music":
#         try:
#             pywhatkit.playonyt(user_text)
#             return f"Playing {user_text} on YouTube."
#         except:
#             return "Unable to play music."

#     # CLOSE TAB (SAFE MODE)
#     elif intent == "close tab":
#         return (
#             "I can't safely close browser tabs from the web interface. "
#             "Please close the tab manually."
#         )

#     # ALARM (DISABLED IN WEB MODE)
#     elif intent == "alarm":
#         return "Alarm feature is disabled in web mode."

#     return None
# import requests
# import datetime
# import webbrowser
# import pywhatkit
# import os
# from dotenv import load_dotenv

# load_dotenv()

# OPENWEATHER_API_KEY = os.getenv(
#     "OPENWEATHER_API_KEY", "bd5e378503939ddaee76f12ad7a97608"
# )

def map_task(intent, user_text):
    # TIME
    if intent == "time":
        return datetime.datetime.now().strftime("The time is %H:%M")

    # DATE
    elif intent == "date":
        return f"Today's date is {datetime.date.today()}"

    # WEATHER (FIXED CITY)
    elif intent == "weather":
        city = "Nainital"
        try:
            url = (
                "https://api.openweathermap.org/data/2.5/weather"
                f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
            )
            res = requests.get(url).json()
            if res.get("cod") != 200:
                return "Unable to fetch weather right now."
            weather = res["weather"][0]["description"]
            temp = res["main"]["temp"]
            return f"The weather in {city} is {weather} with temperature {temp}°C"
        except:
            return "Weather service is unavailable."

    # GOOGLE SEARCH
    elif intent == "google_search":
        try:
            webbrowser.open(f"https://www.google.com/search?q={user_text}")
            return f"Searching Google for {user_text}."
        except:
            return "Google search failed."

    # MUSIC
    elif intent == "music":
        try:
            pywhatkit.playonyt(user_text)
            return f"Playing {user_text} on YouTube."
        except:
            return "Unable to play music."

    # CLOSE TAB (SAFE MODE)
    elif intent == "close tab":
        return (
            "I can't safely close browser tabs from the web interface. "
            "Please close the tab manually."
        )

    # ALARM (DISABLED IN WEB MODE)
    elif intent == "alarm":
        return "Alarm feature is disabled in web mode."

    return None
