# This example requires the 'message_content' intent.

import discord
import discord.ext

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot {client.user} démarée !')

@client.event
async def on_member_join(member):
    channel = client.get_channel(1034775509168558141)
    await channel.send('Bienvenue !')

client.run('MTAzNDc3OTQ3NDI5OTk5ODI2OA.GsT89r.cEQK1-ZfkLMsGAvp6A1246Tdnr2cY6WHirEIoI')