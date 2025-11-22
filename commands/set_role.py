import discord
from discord.ext import commands
from discord import app_commands, Interaction
import json
import os
from datetime import datetime

class SetRoleCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="setrole")
    @app_commands.default_permissions(administrator=True)
    @app_commands.checks.has_permissions(administrator=True)
    async def set_role(self, interaction: Interaction, role: discord.Role):
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("❌ Impossible d'utiliser cette commande en DM.", ephemeral=True)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Can't use that commands in DM")
            return
        
        if role:
            save_role_id(guild.id, role.id)
            self.bot.default_role_id = role.id
            await interaction.response.send_message(f"✅ Rôle par défaut défini sur : {role.name}", ephemeral=True)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Default role defined as {role.name}")

        else:
            await interaction.response.send_message("❌ Rôle introuvable.", ephemeral=True)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Can't find any matching role")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..", "modules", "default_role.json")

def save_role_id(guild_id, role_id):
    data = {}
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
    data[str(guild_id)] = role_id
    with open(FILE_PATH, "w") as f:
        json.dump(data, f)

def load_role_id(guild_id):
    if not os.path.exists(FILE_PATH):
        return None
    with open(FILE_PATH, "r") as f:
        data = json.load(f)
    return data.get(str(guild_id))


async def setup(bot: commands.Bot):
    await bot.add_cog(SetRoleCommand(bot))