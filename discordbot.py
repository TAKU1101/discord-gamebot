from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong!!!')


@bot.command()
async def minesweeper(ctx):
    await ctx.send('''||:zero:||||:zero:||||:zero:||||:one:||||:one:||||:two:||||:two:||||:two:||||:one:||||:zero:||
||:zero:||||:one:||||:two:||||:three:||||:bomb:||||:two:||||:bomb:||||:bomb:||||:one:||||:zero:||
||:one:||||:two:||||:bomb:||||:bomb:||:three::two::two:||:two:||||:one:||||:zero:||
||:one:||||:bomb:||||:four:||||:bomb:||:two::zero::zero:||:zero:||||:zero:||||:zero:||
||:one:||||:one:||||:three:||||:two:||:two::zero::zero:||:zero:||||:zero:||||:zero:||
||:one:||||:one:||||:one:||||:bomb:||||:one:||||:zero:||||:zero:||||:zero:||||:zero:||||:zero:||
||:bomb:||||:one:||||:one:||||:two:||||:two:||||:one:||||:zero:||||:zero:||||:zero:||||:zero:||
||:one:||||:one:||||:zero:||||:one:||||:bomb:||||:one:||||:zero:||||:zero:||||:zero:||||:zero:||
||:zero:||||:zero:||||:zero:||||:one:||||:one:||||:one:||||:zero:||||:zero:||||:zero:||||:zero:||
||:zero:||||:zero:||||:zero:||||:zero:||||:zero:||||:zero:||||:zero:||||:zero:||||:zero:||||:zero:||''')


bot.run(token)
