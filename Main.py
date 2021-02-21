import os
from discord.ext import commands
from pathlib import Path
import discord


def main():
    # https://github.com/cheran-senthil/TLE/blob/bae59c2de6a2313be4a6ba4a5a5cbba81352e229/tle/__main__.py
    BOT_TOKEN = "ODExNzUwNzU2ODY0MjI5NDA2.YC2vzg.KJjXb4x2362tVbVMXb97uBPLh1A"
    # API_TOKEN = os.environ["JOMD_TOKEN"]

    if not BOT_TOKEN:
        print('Missing bot token')
        return

    intents = discord.Intents.default()  # All but the two privileged ones
    intents.members = True  # Subscribe to the Members intent

    pref = '+'
    bot = commands.Bot(command_prefix=commands.when_mentioned_or(pref),
                       intents=intents)

    cogs = [file.stem for file in Path('cogs').glob('*.py')]
    for extension in cogs:
        bot.load_extension(f'cogs.{extension}')
    print(f'Cogs loaded: {", ".join(bot.cogs)}')

    def no_dm_check(ctx):
        if ctx.guild is None:
            raise commands.NoPrivateMessage('Private messages not permitted.')
        return True

    # Restrict bot usage to inside guild channels only.
    bot.add_check(no_dm_check)

    bot.run(BOT_TOKEN)


if __name__ == '__main__':
    main()
