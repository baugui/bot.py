import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hola, soy un bot, aquí esta la lista de mis comandos:juegos, deporte, hora , ¿en que te puedo ayudar?!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('juegos'):
        await message.channel.send(f'juegos para pasar el rato: Uno, monopoly o dominó!')
    elif message.content.startswith('deporte'):
        await message.channel.send(f'el mojer deporte es el futbol!')
    
        
client.run('MTIxNzUyMTgyNzE4NzAwMzQyMw.G8xPwQ.jpLkNOfdikcBXL8fKIwOtoHmmZbwi2TFxBplNc')
