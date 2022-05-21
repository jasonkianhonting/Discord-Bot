import os
from urllib import response
import discord
import requests
import json
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

# Defining function to extract the useful information


def get_quote():
    res = requests.get("https://zenquotes.io/api/random")
    data = json.loads(res.text)
    quote = data[0]['q'] + " -" + data[0]['a']
    return(quote)


def get_random_dog():
    res = requests.get("https://random.dog/woof.json")
    data = json.loads(res.text)
    dog_data = data['url']
    return dog_data


@client.event
async def on_ready():
    print('Python Bot is ready: {0.user}'.format(client))


# Linking the code with the client where the client verifies the user and detects any message with the special abbreviations
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$dog'):
        dog = get_random_dog()
        await message.channel.send(dog)

client.run(os.getenv('TOKEN'))
