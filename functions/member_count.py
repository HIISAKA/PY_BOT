import discord
from discord.ext import commands, tasks
from datetime import datetime

class Member_Count(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.update_member_count.start()

    def cog_unload(self):
        self.update_member_count.cancel()

    

    @tasks.loop(minutes=10)
    async def update_member_count(self):
        try: 
            GUILD_ID = 727479004327575673
            guild = self.bot.get_guild(GUILD_ID)

            if not guild:
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Guild not found")
                return 

            if guild:
                member_count = guild.member_count
                member_count_channel = self.bot.get_channel(768600443260764170)

            if member_count_channel and isinstance(member_count_channel, discord.VoiceChannel):
                await member_count_channel.edit(name=f"⚡┃Membres : {member_count}")
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Updated member count")

            else :
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Member count is the same, no rename")

        except Exception as e:
            print(e)

async def setup(bot: commands.Bot):
    await bot.add_cog(Member_Count(bot))