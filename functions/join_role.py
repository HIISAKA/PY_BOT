import discord      
from discord.ext import commands

class Join_Role(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        guild = member.guild
        role = guild.get_role(1064569655278182400)

        try:  
            print(f"{member.name} a rejoins le serveur")
            await member.add_roles(role)

        except Exception as e:
            print(e)

async def setup(bot: commands.Bot):
    await bot.add_cog(Join_Role(bot))