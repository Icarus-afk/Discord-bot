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
    article = requests.get("https://en.wikipedia.org/api/rest_v1/page/"+word+"/summary")
    print(article)
    data_article = article.json()
    final_response = data_article["extract"]
    link = "https://en.wikipedia.org/wiki/" + word
    return (final_response,link)


# Event that fires when the bot is ready to start
@client.event
async def on_ready():
    channel = client.get_channel(client.guilds[0].text_channels[0].id)
    while True:
        summary, link = get_summary()
        await channel.send(summary)
        await asyncio.sleep(15)

client.run('MTA0MDMzMTMwMjMyMDIxODEyMw.G14ZZ2.93dBjTmOxR8jgGEZ_jlGly-jc5WVmVgT4dpnGQ')
