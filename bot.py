# bot.py
import os
from logger import logger
from httpclient import http_get

from discord import Colour
from discord.ext import commands
from dotenv import load_dotenv

from bot_response import BotResponse

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
API_ACCESS_CODE = os.getenv('API_ACCESS_CODE')
API_BASE_URL = os.getenv('API_BASE_URL')


client = commands.Bot(command_prefix='!stock ')
client.remove_command("help")


@client.event
async def on_ready():
    logger.info("bot is ready")


@client.command(aliases=['help'])
async def _show_help(ctx):
    bot_msg = BotResponse("Tickets Stock Checker", Colour.green(), True)
    bot_msg.build_display(True)
    await ctx.send(embed=bot_msg)


@client.command(aliases=['tm', 'ticketmaster'])
async def _tickemaster_count(ctx, *, event_id):
    # get count
    logger.info("fetching event ticket count")
    url = f'{API_BASE_URL}/tmstockchecker?access_code={API_ACCESS_CODE}&event_id={event_id}'
    count_response = await http_get(url)
    if not count_response or "sections" not in count_response:
        await ctx.send("Error fetching info from Ticketmaster")
        return

    # get info
    logger.info("fetching event info")
    url = f'{API_BASE_URL}/tmstockchecker/info?access_code={API_ACCESS_CODE}&event_id={event_id}'
    info_response = await http_get(url)
    event_name = info_response["event_name"] if info_response["event_name"] else event_id
    event_link = info_response["event_link"] if info_response["event_link"] \
        else f"https://www1.ticketmaster.com/events/{event_id}"
    event_city = info_response["event_city"]
    event_venue = info_response["event_venue"]
    event_datetime = info_response["event_date"]

    # create the embed
    bot_msg = BotResponse("Ticketmaster Inventory Count", event_id, Colour.red())
    bot_msg.set_name(event_name)
    bot_msg.set_name(event_name)
    bot_msg.set_url(event_link)
    bot_msg.set_city(event_city)
    bot_msg.set_venue(event_venue)
    bot_msg.set_datetime(event_datetime)
    for section in count_response["sections"]:
        bot_msg.add_section(section["section"], section["count"])
    bot_msg.build_display()
    await ctx.send(embed=bot_msg)


@client.command(aliases=['tmintl'])
async def _tickemaster_intl_count(ctx, *, event_id):
    url = f'{API_BASE_URL}/tmstockchecker/intl?access_code={API_ACCESS_CODE}&event_id={event_id}'
    json_response = await http_get(url)
    if not json_response or "sections" not in json_response:
        await ctx.send("Error fetching info from Ticketmaster")
        return

    # create the embed
    bot_msg = BotResponse("Ticketmaster International Inventory Count", event_id, Colour.blue())
    for section in json_response["sections"]:
        bot_msg.add_section(section["section"], section["count"])
    bot_msg.build_display()
    await ctx.send(embed=bot_msg)


@client.command(aliases=['axs'])
async def _axs_count(ctx, *, event_id):
    url = f'{API_BASE_URL}/axsstockchecker?access_code={API_ACCESS_CODE}&event_id={event_id}'
    json_response = await http_get(url)
    if not json_response or "sections" not in json_response:
        await ctx.send("Error fetching info from AXS")
        return

    # create the embed
    bot_msg = BotResponse("AXS Inventory Count", event_id, Colour.dark_blue())
    for section in json_response["sections"]:
        bot_msg.add_section(section["section"], section["count"])
    bot_msg.build_display()
    await ctx.send(embed=bot_msg)


if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
