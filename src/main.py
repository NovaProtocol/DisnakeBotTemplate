import datetime
import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv("token.env")
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    print("Token not detected")
    exit()

intents = disnake.Intents.all()
test_guilds = [835447361115258910]  # place your guild ids here

bot = commands.Bot(
    command_prefix=commands.when_mentioned,
    intents=intents,
    test_guilds=test_guilds,
    help_command=commands.DefaultHelpCommand(),
)

"""
    # use this if you want an "interaction" bot and not a "command and interaction" bot

    bot = commands.InteractionBot(
        intents=intents,
        test_guilds=test_guilds,
        help_command=commands.DefaultHelpCommand(),
    )
"""

for filename in os.listdir("cogs"):
    if filename.startswith("_"):
        continue
    elif "cog.py" in os.listdir(f"cogs/{filename}"):
        bot.load_extension(f"cogs.{filename}.cog")
        print(f"Loaded {filename} cog")
    else:
        print(f"Failed loading {filename}. Reason: No cog.py file found")


@bot.listen()
async def on_ready():
    message = f"Bot named {bot.user} was launched at {datetime.datetime.now().strftime('%B %d, %Y at %I:%M:%S %p')}"

    print(
        f"\n{'-' * (len(message) + 2)}\n"
        f" {message} \n"
        f"{'-' * (len(message) + 2)}\n"
    )

    print("Loaded extensions:")
    for cog in bot.extensions.keys():
        print(cog.split(".")[1])

if __name__ == "__main__":
    bot.run(TOKEN)
