import discord
from discord.ext import commands
from discord.ext.commands import has_role
from discord.utils import get
import os
import string
import re
import json
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="~s ")


def writeJSON(trigger, response):
    newDict = ({trigger: response.content})
    with open('responses.json', encoding='utf8') as file:
        oldDict = json.load(file)

    final = dict(oldDict, **newDict)

    with open('responses.json', "w", encoding='utf8') as file:
        json.dump(final, file, indent=2)


def delJson(user, trigger):
    with open('responses.json', encoding='utf8') as file:
        dictionary = json.load(file)

    deletedEntry = dictionary.pop(trigger)
    delLog(user, deletedEntry)

    with open('responses.json', "w", encoding='utf8') as file:
        json.dump(dictionary, file, indent=2)


def writeLog(author, message, response):
    log = open("log.txt", "a", encoding='utf8')
    entry = ("User " + str(author) + " entered the trigger '" + message + "' with the response '" + response + "'\n")
    log.write(entry)
    print(entry)
    log.close()


def delLog(author, message):
    log = open("log.txt", "a", encoding='utf8')
    entry = ("User " + str(author) + " deleted the entry '" + message + "'\n")
    log.write(entry)
    print(entry)
    log.close()


def check(author):
    def check2(message):
        if message.author != author:
            return False
        return True

    return check2


@bot.command(brief="Makes the bot user role.",
             description="Makes the bot user role. You are free to change the color and permissions, "
                         "but do not change the name.")
async def setup(ctx):
    await ctx.message.delete()
    if get(ctx.guild.roles, name="Simply User"):
        await ctx.author.send("Role is already setup.")
    else:
        await ctx.guild.create_role(name="Simply User", colour=discord.Colour.from_rgb(105, 135, 209))
        await ctx.author.send("Role created! 🎉")


@bot.command(brief="Adds new triggers and responses.",
             description="Adds new triggers and responses. Note that it ignores punctuation only in the triggers.")
@has_role("Simply User")
async def new(ctx):
    await ctx.message.delete()
    await ctx.author.send("What would you like the trigger message to be? `cancel` to cancel.")
    unconditionedTrigger = await bot.wait_for('message', check=check(ctx.author))
    message = unconditionedTrigger.content

    if message == "cancel":
        await ctx.author.send("Cancelling.")
        return

    for punc in string.punctuation:
        message = message.replace(punc, "")

    await ctx.author.send("Duly noted. What would you like the response to be? ")
    response = await bot.wait_for('message', check=check(ctx.author))
    await ctx.author.send("All done. 😀")
    writeLog(unconditionedTrigger.author, message, response.content)
    writeJSON(message, response)


@new.error
async def new_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.author.send("You do not have permissions to add an entry!")
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.author.send("You cannot run this command in PMs!")


@bot.command(brief="Deletes a selected trigger/response pair.",
             description="Deletes a selected trigger/response pair. Note that it ignores punctuation in the target "
                         "trigger.")
async def delete(ctx):
    await ctx.message.delete()
    await ctx.author.send("What trigger would you like to delete? 🗑 (`cancel` to cancel.)")
    unconTargetTrig = await bot.wait_for('message', check=check(ctx.author))
    targetTrig = unconTargetTrig.content

    if targetTrig == "cancel":
        await ctx.author.send("Cancelling.")
        return

    for punc in string.punctuation:
        targetTrig = targetTrig.replace(punc, "")
    found = False
    with open('responses.json') as file:
        searchDict = json.load(file)
        for key in searchDict:
            if key.lower() == targetTrig.lower():
                await ctx.author.send("Sure thing.")
                found = True
                delJson(ctx.author, key)
    if not found:
        await ctx.author.send("I can't find the entry you're looking for 🤔. Try again, or ask the host for help.")


@delete.error
async def delete_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.author.send("You do not have permissions to delete an entry!")
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.author.send("You cannot run this command in PMs!")


@bot.event
async def on_message(message):
    if message.author != bot.user and not isinstance(message.channel, discord.channel.DMChannel) and not message.author.bot:
        with open('responses.json') as file:
            searchDict = json.load(file)
            for key in searchDict:
                if re.search(r"\b" + re.escape(key) + r"(\b|$)", message.content,
                             re.MULTILINE | re.IGNORECASE):
                    await message.channel.send(searchDict[key])
    await bot.process_commands(message)


@bot.event
async def on_ready():
    print("Bot Operational!")


load_dotenv()
token = os.getenv('token')
bot.run(token)

#             .,-:;//;:=,
#         . :H@@@MM@M#H/.,+%;,
#      ,/X+ +M@@M@MM%=,-%HMMM@X/,
#     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
#    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
#  ,%MM@@MH ,@%=            .---=-=:=,.
#  -@#@@@MX .,              -%HX$$%%%+;
# =-./@M@M$                  .;@MMMM@MM:
# X@/ -$MM/                    .+MM@@@M$
#,@M@H: :@:                    . -X#@@@@-
#,@@@MMX, .                    /H- ;@M@M=
#.H@@@@M@+,                    %MM+..%#$.
# /MMMM@MMH/.                  XM@MH; -;
#  /%+%$XHH@$=              , .H@@@@MX,
#   .=--------.           -%H.,@@@@@MX,
#   .%MM@@@HHHXX$$$%+- .:$MMX -M@@MM%.
#     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
#       =%@M@M#@$-.=$@MM@@@M; %M%=
#         ,:+$+-,/H#MMMMMMM@- -,
#               =++%%%%+/:-.
#