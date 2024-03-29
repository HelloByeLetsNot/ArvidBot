# bot.py
from keep_alive import keep_alive
import os
import random
import discord
import json
import requests
import mechanicalsoup
from discord.ext import commands
from dotenv import load_dotenv

keep_alive()
TOKEN = os.environ['arvid']

bot = commands.Bot(command_prefix='$')
####
#Endless-Online Change Update ###
#Json - Post Info? Testing
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.command(name='sausage', help='posts current bots exp and lvl')
@commands.cooldown(1, 50, commands.BucketType.user)
async def exp(ctx):
    r = requests.get('https://game.eoserv.net/api/get_character?name=sausage')
    json_data = json.loads(r.text)
    status_bot = json_data['level']
    status_exp = json_data['exp']
    await ctx.send('Bot Level is: **{}**'.format(status_bot) +
                   '       Current EXP is: **{}**'.format(status_exp) +
                   '       http://bbis.us/~blo/eosig/?user=sausage&type=4')


# CHAR LOOK UP
@bot.command(
    name='player',
    help=
    '$player posts player stats.'
)
@commands.cooldown(1, 50, commands.BucketType.user)
async def exp(ctx, charName):
    r = requests.get('https://game.eoserv.net/api/get_character?name=' +
                     charName)
    json_data = json.loads(r.text)
    status_bot = json_data['level']
    status_exp = json_data['exp']
    await ctx.send('Player Level is: **{}**'.format(status_bot) +
                   '       Current EXP is: **{}**'.format(status_exp) +
                   '     Player status is: http://bbis.us/~blo/eosig/?user=' +
                   charName + '&type=4')
####
##item look up
# CHAR LOOK UP
@bot.command(
    name='sitem',
    help=
    'Look up and Item via eoserv.net using the Items ID number.'
)
@commands.cooldown(1, 50, commands.BucketType.user)
async def exp(ctx, itemID):
    r = requests.get('https://game.eoserv.net/item?item=' +
                     itemID)

    await ctx.send('https://game.eoserv.net/item?item=' +
                     itemID) 


###DOWNLOAD EO
@bot.command(name="servers", help='Endless Online Downloads')
@commands.cooldown(1, 50, commands.BucketType.user)
async def displayembed(ctx):
    embed = discord.Embed(title="**EO Clone**",
                          description="https://game.eoserv.net/")
    embed.add_field(name="**Fallen Evolution**",
                    value="https://fallen-evolution.com/",
                    inline=False)
    embed.add_field(name="**Bones Underground**",
                    value="http://game.bones-underground.org",
                    inline=False)
    embed.add_field(name="**EO2**",
                    value="http://www.endlessonline2.com/",
                    inline=False)
    embed.add_field(name="**EO Plus**",
                    value="http://eo-plus.com/",
                    inline=False)
    embed.add_field(name="**Server List**",
                    value="http://www.apollo-games.com/SLN/sln.php",
                    inline=False)

    embed.set_footer(
        text='\u200b',
        icon_url="https://cdn-icons-png.flaticon.com/512/183/183580.png")
    await ctx.send(embed=embed)


#Embed Commands


@bot.command(name="arvid", help='Arvid lists his commands.')
@commands.cooldown(1, 50, commands.BucketType.user)
async def displayembed(ctx):
    embed = discord.Embed(title="Hi, I'm Arvid.",
                          description="I'm a bot, I like to wall people.")
    embed.add_field(name="**$player <name>**",
                    value="This will post the players level and exp.",
                    inline=False)
    embed.add_field(name="**$eosig <name>**",
                    value="This will post a random eosig of the player.",
                    inline=False)
    embed.add_field(name="**$eo**",
                    value="This will post a random Endless Online Fact.",
                    inline=False)
    embed.add_field(name="**$servers**",
                    value="This will post the best known EO Servers.",
                    inline=False)

    embed.set_footer(
        text='\u200b',
        icon_url="https://cdn-icons-png.flaticon.com/512/183/183580.png")
    await ctx.send(embed=embed)


#EOSERV LOGIN and LOC
import mechanicalsoup


@bot.command(name="coords", help='bot cords')
@commands.cooldown(1, 50, commands.BucketType.user)
async def displayembed(ctx):

    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://game.eoserv.net/character?name=CHAR NAME HERE")
    browser.select_form()
    browser["username"] = ""
    browser["password"] = ""
    browser.submit_selected()

    page = browser.page

    startIndex = page.text.find("nMap") + 1
    endIndex = page.text.find("Stats")
    newStringArray = page.text[startIndex:endIndex].split(
    )  # ['Map143', 'X3', 'Y28']

    mapOutput = newStringArray[0]  # 'Map143'
    coordsOutput = newStringArray[1] + "\n" + newStringArray[
        2]  # 'X3 <newline> Y28'

    embed = discord.Embed(
        title="Location",
        description=
        "Current character location information, if character is on map 76 bot has been jailed. "
    )
    embed.add_field(name="Map", value=mapOutput, inline=False)
    embed.add_field(name="Coords", value=coordsOutput, inline=False)

    await ctx.send(embed=embed)


#######


#Endless Online Facts
@bot.command(name='eo', help='Posts a random *fact* about Endless Online.')
@commands.cooldown(1,50, commands.BucketType.user)
async def eo_history(ctx):
    eo_history = [
        'The server was destroyed.',
        'Is this eo discord or hello kitty online?',
        ('2022 - New Client: http://endless-online.com/downloads.html'),
        ('26th November 2009 - Servers are back online'),
      ('Sordie had us all with the kelogs!'),
        ('Eoserv.net - lets make a private server!'),
        ('2022 - VULT CAME HOME,'
         ' but will he be qwiddled again?'),
        ('21st March 2011 - Character reset'),
        ('July 2015 - BUYVM.NET aka frantech gave away the server'
         ' ..they got qwiddled'),
        ('Auguest 2015 - To the community'
         ' Its still unbelievable for me knowing that this critical access was just handed over by BUYVM.NET to people with bad intentions. EO will be down for now.'
         ),
        ('v16 released Jan 15th,'
         ' but on the 18th the server went down due to a heartless datacentre.'
         ),
        ('21st September 2005  Update Now that we have a magic/skill system working the next step should be a new NPC type to train learn new spells.'
         ),
        ('9th Febuary 2004 - OMG! we are back -Yep, we are back and meanwhile we have been working quite hard on the mmrpg project. (see version history) Things can only get better from this point since there is a dedicated server available.'
         ),
    ]

    response = random.choice(eo_history)
    await ctx.send(response)


#RANDOM IMAGE EOSIG LOOK UP
@bot.command(name='eosig', help='Look Up Char Info Via EoSig')
@commands.cooldown(1, 50, commands.BucketType.user)
async def eosig(ctx, charName):
    eosig = [
        'http://bbis.us/~blo/eosig/?user=' + charName + '&type=2',
        'http://bbis.us/~blo/eosig/?user=' + charName + '&type=3',
        ('http://bbis.us/~blo/eosig/?user=' + charName + '&type=1 '),
    ]

    response = random.choice(eosig)
    await ctx.send(response)


#dice roll
@bot.command(name='roll', help='Simulates rolling dice.')
@commands.cooldown(1, 50, commands.BucketType.user)
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))



bot.run(TOKEN)
