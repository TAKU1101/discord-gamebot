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


center = (4, 4)


def gen_array():
    array = np.random.rand(10, 10)

    level = 0.85

    array[array > level] = 1
    array[array < level] = 0

    for i in range(center[0] - 1, center[0] + 2):
        for j in range(center[1] - 1, center[1] + 2):
            array[i, j] = 0
    return array

def mine_count(array, x, y):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            try:
                if array[i, j] == 1:
                    count += 1
            except IndexError:
                pass
    return count


def all_mine_count(array):
    x, y = array.shape
    count = np.zeros((x, y))
    for i in range(x):
        for j in range(y):
            count[i, j] = mine_count(array, i, j)
    return count


def replace_char(count, array):
    char_dict = [":zero:", ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]
    rtv = ""
    for i, line in enumerate(count):
        for j, elem in enumerate(line):
            if array[i, j] == 1:
                rtv = rtv + "||" + ":bomb:" + "||"
            elif center[0] - 1 <= i < center[0] + 2 and center[1] - 1 <= j < center[1] + 2:
                rtv = rtv + char_dict[int(elem)]
            else:
                rtv = rtv + "||" + char_dict[int(elem)] + "||"
        rtv = rtv + "\n"
    bomb_count = sum(sum(array))
    rtv = rtv + "\n\n" + ":bomb: 爆弾の数: " + str(int(bomb_count)) + "\n"
    return rtv


@bot.command()
async def minesweeper(ctx):
    array = gen_array()
    count = all_mine_count(array)
    msg = replace_char(count, array)
    await ctx.send(msg)

bot.run(token)
