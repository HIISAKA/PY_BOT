import discord      
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

class On_Ready(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Bot is ready")
        try:
            synced = await self.bot.tree.sync()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Synced {len(synced)} command(s)")

            activity = discord.CustomActivity("Cherche d'la moune")
            await self.bot.change_presence(status=discord.Status.online, activity=activity)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Bot presence defined")

        except Exception as e:
            print(e)

async def setup(bot: commands.Bot):
    await bot.add_cog(On_Ready(bot))
