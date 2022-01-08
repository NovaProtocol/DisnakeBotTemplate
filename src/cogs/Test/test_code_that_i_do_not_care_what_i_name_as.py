import disnake
from disnake.ext import commands

from . import ImportedFile

"""
Consider renaming sub cog to the format
    EXTENSIONGROUPSubCogName
like
    ECONOMYItemSellFunction
    
This is because disnake or any other forks hates non-unique cog name.
"""


class TESTTestCodeThatIDoNotCareWhatINameAs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """
    All command name needs to be unique for obvious reasons.
    """

    @commands.slash_command(name="test")
    async def test(self, inter: disnake.ApplicationCommandInteraction):
        """
        Command description.
        """
        message = ImportedFile.some_function()
        await inter.response.send_message(message)


def main_setup(bot: commands.Bot):
    # This just returns the main class of this sub cog.
    return TESTTestCodeThatIDoNotCareWhatINameAs(bot)
