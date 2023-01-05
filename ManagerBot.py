import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'INSERT TOKEN HERE'
GUILD = os.getenv('White Van')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
emoji = '✅'


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})'
    )
    channel = client.get_channel(791133687579410472)
    await channel.send('Click the ✅ to verify.')
    print('sent message')

@client.event
async def on_message(message):
    if message.author==client.user:
        await message.add_reaction(emoji)
        print("Added a reaction to the message")

@client.event
async def on_member_join(member):
    print("Recognized that a member called " + member.name + " joined")


@client.event
async def on_member_remove(member):
    print("Recognized that a member called " + member.name + " left")



@client.event
async def on_reaction_add(reaction, user):
    if user.name != 'WhiteVan' and reaction.emoji == '✅':
        await user.add_roles(discord.utils.get(user.guild.roles, name="Member"))
        print("Added role to " + user.name)
        await reaction.remove(user)
        print('Deleted reaction')
        channel = client.get_channel(771496849269719070)
        title = "Member Count: " + str(len(client.users))
        await channel.edit(name=title)
        print("Updated member count")


client.run(TOKEN)
























