# cogs/fun.py
import discord
from discord.ext import commands
from discord import app_commands, Interaction

class Bip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="system_call_bip", description="return boop, mainly a test command")
    async def system_call_bip(self, interaction: discord.Interaction):
        await interaction.response.send_message("Boop")

async def setup(bot):
    await bot.add_cog(Bip(bot))