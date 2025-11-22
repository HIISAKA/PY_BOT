from discord.ext import commands
from datetime import datetime

class AdminBase(commands.Cog):
    async def cog_check(self, ctx):
        if not ctx.author.guild_permissions.administrator:
            raise commands.CheckFailure(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Need admin perms")
        return True
    
async def setup(bot):
    await bot.add_cog(AdminBase(bot))