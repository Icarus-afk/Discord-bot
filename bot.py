import discord
import wikipediaapi
import random
import asyncio
import requests

# Initialize the Discord client
client = discord.Client(intents=discord.Intents.default())

# Initialize the Wikipedia API client
wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)

def get_random_word():
    # Get a random article from the Wikipedia API
    response = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")
    data = response.json()
    title = data["title"]
    return title

# Function to get the summary of a random Wikipedia article
def get_summary():
    word = get_random_word()
    page = wiki.page(word)
    summary = page.summary
    word_list = word.split(" ")
    link = "https://en.wikipedia.org/wiki/"
    for word in word_list:
        link += word + "_"
    return (summary,link)

# Event that fires when the bot is ready to start
@client.event
async def on_ready():
    while not client.is_closed():
        for guild in client.guilds:
            for channel in guild.text_channels:
                if channel.name == "spam" and channel.permissions_for(guild.me).send_messages:   
                    summary, link = get_summary()
                    await channel.send(summary+"\nread full article: "+link)
                    await asyncio.sleep(300)
    
    

client.run('token')
