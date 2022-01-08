# Disnake Bot Template

This is my own template for making disnake bots. This is not, in any way, the best way to make bots but is the way I am comfortable with.

---

## Installation

Start with installing the required modules by using the following commands.

```bash
pip install disnake
pip install python-dotenv
```

---

## Guide

1. Start with putting the guild id of your test guild in the [test_guilds](https://github.com/NovaProtocol/DisnakeBotTemplate/blob/f6a9e0f8393e78e25edf6cf86cb643d4717f6965/src/main.py#L16) variable in the file [main.py](https://github.com/NovaProtocol/DisnakeBotTemplate/blob/master/src/main.py)
Multiple guild id should work as well.
    ```python
    test_guilds = [12345678901234, 13771298372174]
    ```
2. By default, it uses all intents as shown in the [code](https://github.com/NovaProtocol/DisnakeBotTemplate/blob/f6a9e0f8393e78e25edf6cf86cb643d4717f6965/src/main.py#L15). Change this or give the bot the necessary intents.
    ```python
    intents = disnake.Intents.all()  # all
    intents = disnake.Intents.default()  # all intents that don't require verification
    ```
   
3. Change the default bot settings. The default is a command bot meaning it acts as an interaction bot and a message bot.
    ```python
    # Default Interaction bot and Message bot
    bot = commands.Bot(
        command_prefix=commands.when_mentioned,
        intents=intents,
        test_guilds=test_guilds,
        help_command=commands.DefaultHelpCommand(),
    )
    
    # Interaction bot only
    bot = commands.InteractionBot(
        intents=intents,
        test_guilds=test_guilds,
        help_command=commands.DefaultHelpCommand(),
    )
    ```
   
4. Create a file in the same directory as [main.py](https://github.com/NovaProtocol/DisnakeBotTemplate/blob/master/src/main.py) and name it `token.env`. It should contain the token of the bot you are using in that format without spaces or quotation marks.
   ```env
   DISCORD_TOKEN=1234TOKENHERE1234
   ```

   #### After this, the bot should run without any errors after executing main.py from the same directory it is in.

---

## Guide on Cogs
Check out the [guide](https://github.com/NovaProtocol/DisnakeBotTemplate/blob/master/src/cogs/README.md) in the [cogs folder](https://github.com/NovaProtocol/DisnakeBotTemplate/tree/master/src/cogs) for a more in depth overview of how to use cogs.
