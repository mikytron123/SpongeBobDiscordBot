# bot.py
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from discord.ext import commands
from dotenv import load_dotenv
from io import BytesIO
load_dotenv()
import discord
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

@bot.command()
async def spongebob(ctx,arg):
    addstr = str(arg)
    img = Image.open("spongebob.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 48)
    draw.text((590, 32),addstr,(255,255,255),font=font)
    with BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)
