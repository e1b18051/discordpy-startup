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
    await ctx.send('pong')

@bot.command()
async def enter(ctx):
    reply = f'{ctx.author.mention}が入室しました。'
    await ctx.send(reply)

@bot.command()
async def leave(ctx):
    reply = f'{ctx.author.mention}が退室しました。'
    await ctx.send(reply)
    
@bot.command()
async def /help(ctx):
    reply = f'入室コマンド：/enter\n退室コマンド：/leave'
    await ctx.send(reply)

bot.run(token)
