import nextcord
from nextcord.ext import commands
import os

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True  # Needed for member join events
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.slash_command(name="dmall", description="Send a DM to all server members")
async def dmall(interaction: nextcord.Interaction, message: str):
    if interaction.user.id == 1263949136424865894:
        await interaction.response.send_message("Sending DMs to all members...", ephemeral=True)
        for member in interaction.guild.members:
            if not member.bot:
                try:
                    await member.send(message)
                except nextcord.Forbidden:
                    pass
        await interaction.followup.send("Message sent to all members.", ephemeral=True)
    else:
        await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
