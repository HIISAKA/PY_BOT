from discord.ext import commands
from commands.set_role import load_role_id
from datetime import datetime

class Join_Role(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:  
            role_id = load_role_id(member.guild.id)
            
            
            role = member.guild.get_role(role_id)
            await member.add_roles(role)            
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {member.name} joined {member.guild} and got the {role}")

            if role is None:
                return
        
        except Exception as e:
            print(e)

async def setup(bot: commands.Bot):
    await bot.add_cog(Join_Role(bot))