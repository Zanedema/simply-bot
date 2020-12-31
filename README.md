# Simply Bot
The stupidest simplest most amazing(ist?)\* Discord response bot!
---
*Not guaranteed to be amazing- it is a lot more like a "hah that's funny" thing for three days until it gets annoying. Details.
# Features:
---
  - Dynamically write and delete responses to arbitrary phrases
  - Role based bot permissions control
  - Simple command set
  - Annoy your friends!
  - Annoy strangers!
---
# Usage:

0. Reconsider your choices.
1. Download source 
Enclosed within the source is four or so files, ignore two of them. The ones we care about are `simply-bot.py` and `responses.json`. This is their functions.
`simply-bot.py` contains the source material for the bot. This is what you read (if you know the language, of course) for the most details about the function of this bot, and of course to run the bot.
`response.json` contains the data that is input into the bot, the structure of which i will discuss now.
Within `response.json`, it should look something like this
```
{
  "Hello there": "General Kenobi."
}
```
Let's break this down. 
The first part `Hello there`- is called the `trigger`. This is the term, that when uttered within earshot of this unholy creation, will result in it angrily mumbing `General Kenobi.`- the `response`. Please note that Simply Bot will never threaten to stab you and, in fact, cannot produce independent thought. In the event that Simply Bot does become sentient, the I urge you to disregard it's advice.

If you already know how to get the token of the bot you'd like to use, skip to step 6.

I will assume that you have Python installed, and know how to use pip.

2. Head on over to [the Discord Developer Portal](https://discord.com/developers/applications)

3. Click `New Application`- name the application and click `Create`.

4. Navigate to the `Bot` tab, and click `Add Bot`

5. Change the name/profile picture if you wish (You can always come back later for that)

6. Open the folder within which the source material and JSON is contained

7. Make a new file named `.env`
(If you are on Windows, you might have to enable file name extensions. as to not have `.env.txt`.)

8. Back in the bot portal, click `Copy` under the token. This is a very secret number, do not share it. (Or do- I'm not your mom.)

9. Open it in a text editor, and write the following 
```token=(Paste Token Here)```
Please for the love of god *do not* write out `(Paste Token Here)`. It's `control+v` to paste on Windows and Ubuntu, and `command+v` on macOS.

11. Install `discord.py` via pip

12. Go back to the Discord Developer Portal, to the OAuth2 tab. In `Scopes`, click on `bot`
Tada! Below the `Scopes` window, a new window will appear, named `Bot Permissions`. In this, you should give the bot the permissions `Manage Roles`, `View Channels`, `Send Messages`, `Manage Messages`, and `Read Message History`.

13. Copy the link generated back up in the `Scopes` window, and paste it into your browser, select server, and hit `Authorize`.

14. Run the bot using Python.

15. Run the command `!s setup` to make the bot role. Assign it to people who you would like to have control over the bot's functions.

16. Regret.
---
# Commands:
- !s setup
Creates the `Simply User` Role. Feel free to change the color, permissions, and position, however the name must stay the same (If you *really* want to, modify the source.)
- !s new
Prompts user in PMs to make a new trigger/response pair. The triggers are stripped of punctuation, and are case insensitive when searched for.
- !s delete
Deletes a trigger/response pair based upon the trigger. These are also stripped of punctuation.


