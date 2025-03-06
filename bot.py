import discord 
import os
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client=discord.Client(intents=intents)

commandtree = app_commands.CommandTree(client=client)



@client.event
async def on_ready():
    print(f"Pomyślnie uruchomiono bota '{client.user}'")
    try:
        await commandtree.sync()
    except Exception as e:
        print(e)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!piwo'):
        await message.channel.send("https://tenor.com/view/piwo-gif-9134806494356314119")

@commandtree.command(name='bet', description='bet on a team')
async def bet(interaction: discord.Interaction, team1: str, team2: str, home_goals: str, away_goals: str):
    await interaction.response.send_message(f' @{interaction.user.name} Obstawiłeś wynik {team1} {home_goals} : {away_goals} {team2}')


@bet.autocomplete('team1')
async def team_autocomplete(interaction: discord.Interaction, current: str):
    teams  = ['Napoli','Barcelona','Chelsea','Marsylia']
    return [app_commands.Choice(name=team, value=team) for team in teams if current.lower() in team.lower()]

@bet.autocomplete('team2')
async def team_autocomplete(interaction: discord.Interaction, current: str):
    teams  = ['Napoli','Barcelona','Chelsea','Marsylia']
    return [app_commands.Choice(name=team, value=team) for team in teams if current.lower() in team.lower()]

client.run(token)
