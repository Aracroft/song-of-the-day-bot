import tweepy
import requests
import random
import os
from dotenv import load_dotenv


load_dotenv()

# Twitter/X API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Fun facts about music
FUN_FACTS = [
    "Beethoven was deaf when he composed his most famous symphony.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
    "Octopuses have three hearts and blue blood.",
    "The original name for Spotify was 'Spotify' — they never changed it!",
    "A group of flamingos is called a 'flamboyance'.",
    "The first song ever sung in space was 'Happy Birthday' in 1969.",
    "Honey never spoils. Archaeologists found 3000-year-old honey in Egyptian tombs that’s still edible!"
]
# Initialize Twitter API v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def get_song_of_the_day():
    try:
        # Your API call logic here (commented out since it's incomplete)
        # await = data[ await ]  # This line is invalid - remove it
        # data = ... (your API response data)
        title = "Song Title"  # Replace with actual title from API
        artist = "Artist Name"  # Replace with actual artist from API
        default_url = f"https://www.youtube.com/results?search_query={title}+{artist}"
        youtube_url = data.get("youtube_url", default_url)
        return f"Song of the Day: {title} by {artist} {youtube_url}"

    except requests.RequestException as e:
        print(f"API Request Failed: {e}")
        return "Song of the Day: Diamonds by LeoStayTrill & AyoMaff (http://bit.ly/4B0Sx8R)"

def tweet_song():
    song_text = get_song_of_the_day()
    fact = random.choice(FUN_FACTS)
    tweet = f"{song_text}\n\nFun-fact: {fact}\n\n#songOfTheDay #MusicBot"
    
    try:
        response = client.create_tweet(text=tweet)  # Fixed: text-tweet -> text=tweet
        print("Tweeted successfully!")
        print(response.data['id'])  # shows tweet ID
    except Exception as e:
        print("ERROR - Could not tweet.")
        print(e)  # THIS WILL SHOW THE REAL PROBLEM
        print(e.response.text if hasattr(e, 'response') else "No response")





