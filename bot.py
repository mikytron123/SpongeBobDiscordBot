# bot.py
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from discord.ext import commands
from dotenv import load_dotenv
from io import BytesIO
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from discord_slash.model import SlashCommandOptionType

from fontTools.ttLib import TTFont
load_dotenv()
import discord
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
slash = SlashCommand(bot, sync_commands=True)

def has_glyph(font, glyph):
    for table in font['cmap'].tables:
        if ord(glyph) in table.cmap.keys():
            return True
    return False

@slash.slash(name="spongebob",
             description="Adds text to spongebob image",
              options=[
               create_option(
                 name="text",
                 description="Text to add to image",
                 option_type=SlashCommandOptionType.STRING,
                 required=True
               )
             ])
async def spongebob(ctx,text):
    await ctx.defer()
    addstr = str(text)
    img = Image.open("spongebob.jpg")
    draw = ImageDraw.Draw(img)
    startlen = 590
    maxlen = 480
    startsize = 55
    FONT_SIZE = await getfontsize(startsize,maxlen,addstr)
    for char in addstr:
        checkfont = TTFont('uni.ttf')
        checkfont2 = TTFont('color.ttf')
        if has_glyph(checkfont,char):
            font = ImageFont.truetype("uni.ttf",FONT_SIZE,encoding='unic')
        elif has_glyph(checkfont2,char):
            font = ImageFont.truetype("color.ttf",FONT_SIZE)
        else:
            font = ImageFont.truetype("uni.ttf",FONT_SIZE,encoding='unic')
        size = font.getsize(char)
        draw.text((startlen, 20),char,font=font,embedded_color=True)
        startlen += size[0]
    with BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))

async def getfontsize(startsize,maxlen,addstr):
    FONT_SIZE = startsize
    for font_size in range(startsize,5,-1):
        font = ImageFont.truetype("uni.ttf",font_size,encoding='unic')
        if font.getsize(addstr)[0] <maxlen:
            FONT_SIZE = font_size
            break
    return FONT_SIZE



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)
