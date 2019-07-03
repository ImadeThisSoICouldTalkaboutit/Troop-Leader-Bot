import discord

client = discord.Client()
id = client.get_guild(595772661393784842)
@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hiwo")
@client.event
async def on_message(message):
    id = client.get_guild(595772661393784842)

    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")
    elif message.content == "!users":
        await message.channel.send(f"""# of Members: {id.member_count}""")
@client.event
async def on_message(message):
    id = client.get_guild(ID)
    channels = ["commands"]
    valid_users = ["jareetbaree457#5329"] # Only users in this list can use commands

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")
@client.event
async def on_message(message):
    ...
    bad_words = ["REEE", "Sausake", "Fleek"]

    for word in bad_words:
        if message.content.count(word) > 0:
            print("YOU SAID A FURRY SLUR! BAD BOY/GIRL/APACHE ATTACK HELICOPTER")
            await message.channel.purge(limit=1)

client.run(NTg5NjQzMDA4ODAzMDc4MTU0.XRv5jQ.Gc0L6e104_x3qamJMynSBI6HPd8)
