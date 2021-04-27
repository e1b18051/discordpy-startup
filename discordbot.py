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

# @client.event
# async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
#     if message.author.bot:
#         return
    # 「入室」と発言したら「入室しました」とリプライされる処理
#     if message.content == '入室':
#         reply = f'{message.author.mention} が入室しました' # 返信メッセージの作成
#         await message.channel.send(reply) # 返信メッセージを送信
    # 「退室」と発言したら「退室しました」とリプライされる処理
#     if message.content == '退室':
#         reply = f'{message.author.mention} が退室しました' # 返信メッセージの作成
#         await message.channel.send(reply) # 返信メッセージを送信


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def enter(ctx):
    reply = f'{ctx.author.mention}が入室しました。'
    await ctx.send('reply')

@bot.command()
async def leave(ctx):
    reply = f'{ctx.author.mention}が退室しました。'
    await ctx.send('reply')

bot.run(token)
