# bot.py
import os
from logger import logger
from httpclient import http_get

from discord import Colour
from discord.ext import commands
from dotenv import load_dotenv

from bot_response import BotResponse

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
api_access_code = os.getenv('API_ACCESS_CODE')


client = commands.Bot(command_prefix='!stock ')


@client.event
async def on_ready():
    logger.info("bot is ready")


@client.command()
async def ping(ctx):
    logger.info("received ping command")
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['tm', 'ticketmaster'])
async def _tickemaster_count(ctx, *, event_id):
    url = f'https://yrmfkazv8g.execute-api.ca-central-1.amazonaws.com/dev_ca_central_1/' \
          f'tmstockchecker?access_code={api_access_code}&event_id={event_id}'
    json_response = await http_get(url)
    if not json_response or "sections" not in json_response:
        await ctx.send("Error fetching info from Ticketmaster")
        return

    # create the embed
    bot_msg = BotResponse("Ticketmaster Inventory Count", Colour.red())
    if len(json_response["sections"]) == 0:
        bot_msg.set_empty()
    else:
        for section in json_response["sections"]:
            bot_msg.add_section(section["section"], section["min_price"], section["max_price"], section["count"])
    await ctx.send(embed=bot_msg)


@client.command(aliases=['tmintl'])
async def _tickemaster_intl_count(ctx, *, event_id):
    url = f'https://yrmfkazv8g.execute-api.ca-central-1.amazonaws.com/dev_ca_central_1/' \
          f'tmstockchecker/intl?access_code={api_access_code}&event_id={event_id}'
    json_response = await http_get(url)
    if not json_response:
        await ctx.send("Error fetching info from Ticketmaster")
        return

    # create the embed
    bot_msg = BotResponse("Ticketmaster International Inventory Count", Colour.blue())
    if not json_response["sections"] or len(json_response["sections"]) == 0:
        bot_msg.set_empty()
    for section in json_response["sections"]:
        bot_msg.add_section(section["section"], section["min_price"], section["max_price"], section["count"])
    await ctx.send(embed=bot_msg)


@client.command(aliases=['axs'])
async def _axs_count(ctx, *, event_id):
    url = f'https://yrmfkazv8g.execute-api.ca-central-1.amazonaws.com/dev_ca_central_1/' \
          f'axsstockchecker/intl?access_code={api_access_code}&event_id={event_id}'
    json_response = await http_get(url)
    if not json_response:
        await ctx.send("Error fetching info from Ticketmaster")
        return

    # create the embed
    bot_msg = BotResponse("AXS Inventory Count", Colour.dark_blue())
    if not json_response["sections"] or len(json_response["sections"]) == 0:
        bot_msg.set_empty()
    for section in json_response["sections"]:
        bot_msg.add_section(section["section"], section["min_price"], section["max_price"], section["count"])
    await ctx.send(embed=bot_msg)


if __name__ == "__main__":
    client.run(token)
