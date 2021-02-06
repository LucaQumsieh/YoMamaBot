import discord

bot = commands.Bot(command_prefix='/')

jokes = {"Yo mama so stupid, she put two quarters in her ears and thought she was listening to 50 Cent."
         "Yo mama so poor, she can’t afford to pay attention."
         "Yo mama so dark she went to night school and was marked absent!"}

@bot.command()
async def joke(ctx):
    global jokes
    joke_key = random.choice(list(jokes.keys()))
    await ctx.send(joke_key)
    await asyncio.sleep(5)
    await ctx.send(jokes[joke_key])
    
token = ""
bot.run(token)
