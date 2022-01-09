# Guide on How to Use Cogs in This Template

---

## Guide

1. Start by either copying the folder [Test](https://github.com/NovaProtocol/DisnakeBotTemplate/tree/master/src/cogs/Test) or by making a folder of your own. Copying is a stress-free way to setup a new cog but if you want to learn how to create your own, feel free to continue this.


2. If you created your own folder, start by making a cog.py file in that folder. This will contain the loader of all the files you would use in that cog.
   
   Let's assume that you named your cog files as `file1`, `file2`, and `file3`, and the cog group as `CogGroupSample`.

   It should contain the following:

   ```python
   import discord
   
   from . import file1, file2, file3
   
   def setup(bot):
       bot.add_cog(file1.main_setup(bot))
       bot.add_cog(file2.main_setup(bot))
       bot.add_cog(file3.main_setup(bot))
   ```
   

3. Now let's create the individual cog files.
   
   If you have any experience with working with cogs before this, you would know that they're basically just a class.
   ```python
   import disnake
   from disnake.ext import commands
   
   class COGGROUPSAMPLEFile1Function(commands.Cog):
       def __init__(self, bot: commands.Bot):
           self.bot = bot
   
       @commands.slash_command(name="hello")
       async def hello(self, inter: disnake.ApplicationCommandInteraction):
           await inter.response.send_message('Hello World!')
   
   def main_setup(bot: commands.Bot):
       return COGGROUPSAMPLEFile1Function(bot)
   ```
   Now, I know what you are thinking. What's with the awful naming? Well, the problem with how discord.py as well as its forks work. Each cog class needs to have a unique name. This is why I named it `COGGROUPSAMPLEHelloWorld` which uses the format `COGGROUP`+`SubCog` to make sure it uses a unique name. Feel free to modify this part as some may not be comfortable with this.
   

4. Create a blank `__init__.py` at the same directory. This allows relative imports which makes our lives easier.

   That should be all for the cog.

---

## Questionable Design Choices Answer

1. Why didn't you just make a cog folder and put all the cogs in there, like it was meant to be?
   
   > Because some cogs are very large and would take up too many lines if you tried to fit it in one file and multiple files of one cog getting mixed in with the other cogs if you used one folder is very confusing.


2. Why didn't you just use one cog per group instead?

   > To be honest, I was considering this too but the it's kinda annoying that you can't use some of the decorator like @commands.listener() since it's not meant to work like that. If you found a way, feel free to post on the issues tab, so I can have a look at it.
