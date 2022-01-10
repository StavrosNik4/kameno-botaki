import discord
import os
import requests
import json
import random
from discord.ext import commands

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('#inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('#d4'):
        ran = random.randint(1, 4)
        await message.channel.send(ran)

    if message.content.startswith('#d6'):
        ran = random.randint(1, 6)
        await message.channel.send(ran)

    if message.content.startswith('#d8'):
        ran = random.randint(1, 8)
        await message.channel.send(ran)

    if message.content.startswith('#d20'):
        ran = random.randint(1, 20)
        await message.channel.send(ran)

    if message.content.startswith('#img'):
        num = random.randint(0, 999)
        await message.channel.send('https://picsum.photos/1280/720?random=' + str(num))

    if message.content.startswith('#qr'):
        await message.channel.send('https://drive.google.com/file/d/12tETNN6uePXtfwxcrQVw-jmwIuCJ8RWb/view?usp=sharing')

    if message.content.startswith('#coinflip'):
        num = random.randint(1, 2)
        if num == 1:
            await message.channel.send('**Heads**')

        if num == 2:
            await message.channel.send('**Tails**')

    if message.content.startswith('#rps'):
        ar = ["rock", "paper", "scissors"]
        bot_val = random.choice(ar)
        print(bot_val)
        p_val = ""
        if message.content.startswith('#rps rock'):
            p_val = "rock"
        elif message.content.startswith('#rps paper'):
            p_val = "paper"
        elif message.content.startswith('#rps scissors'):
            p_val = "scissors"

        if p_val != "":
            await message.channel.send(bot_val)
        else:
          await message.channel.send("Wrong Command!")

        if p_val == bot_val:
            await message.channel.send('**Draw!**')
        elif (p_val == "rock" and bot_val == "scissors") or (p_val == "paper" and bot_val == "rock") or (p_val == "scissors" and bot_val == "paper"):
            await message.channel.send('**You Win!**')
        else:
            await message.channel.send('**You Lose!**')


client.run("")
