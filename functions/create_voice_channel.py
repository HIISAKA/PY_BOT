from discord.ext import commands
from datetime import datetime

class Custom_Voice_Channel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.auto_channels = {}

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
       try:
            CHANNEL_ID=727479004994469901
            if after.channel and after.channel.id == CHANNEL_ID:
                guild = member.guild
                category = after.channel.category
            
                new_channel = await guild.create_voice_channel(
                    name=f"Vocal de {member.global_name}",
                    category=category,
                    user_limit=99                        
                )
                
                await member.move_to(new_channel)
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] New voice channel created by {member.name}")

                self.auto_channels[new_channel.id] = member.id

            if before.channel and before.channel.id in self.auto_channels:
                voice_channel = before.channel
                members = voice_channel.members

                if not members:
                    await voice_channel.delete(reason="Empty auto-channel deleted")
                    del self.auto_channels[voice_channel.id]

       except Exception as e:
           print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Something went wrong while creating a voice channel")
           print(e)

async def setup(bot: commands.Bot):
    await bot.add_cog(Custom_Voice_Channel(bot))