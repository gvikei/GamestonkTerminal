import discord
import random

from io import StringIO
import sys


import terminal
import gamestonk_terminal.config_terminal as cfg

# Load env vars
TOKEN = cfg.DISCORD_TOKEN
GUILD = cfg.DISCORD_GUILD

# Running mode
DEBUGGING = True

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        self._stdin = sys.stdin
        sys.stdout = self._stringio_out = StringIO()
        sys.stdin = self._stringio_in = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio_out.getvalue().splitlines())
        self.extend(self._stringio_in.getvalue().splitlines())
        del self._stringio_out    # free up some memory
        del self._stringio_in
        sys.stdout = self._stdout
        sys.stdin = self._stdin


s_ticker = ""
s_start = ""
s_interval = "1440min"

def process(message):
    return f'Got {message} from user!'
    # get_stdout(terminal.main)

def get_stdout(func, *args, **kwargs):
    with Capturing() as output:
        func(*args, **kwargs)
    response = ('\n'.join(output))
    return response

if not DEBUGGING:
    print('LIVE!')
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user.name} has connected to Discord!')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content  == 'start!':
            response = get_stdout(terminal.print_help, s_ticker, s_start, s_interval, terminal.b_is_stock_market_open())

        else:
            response = process(message.content)
        await message.channel.send(response)


    client.run(TOKEN)

else:
    def main(args):
        user_cmd = args[0]
        print(process(user_cmd))

    if __name__ == "__main__":
       main(sys.argv[1:])