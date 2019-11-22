# bot.py
import os
from logger import logger
from httpclient import http_get


from discord import Embed, Colour
from discord.ext import commands
from dotenv import load_dotenv

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
    if not json_response:
        await ctx.send("Error fetching info from Ticketmaster")
        return

    # create the embed
    em = Embed(
        title='Ticketmaster Inventory Count',
        colour=Colour.red()
    )
    if not json_response["sections"] or len(json_response["sections"]) == 0:
        em.add_field(name=f'Error', value=f'No seats available', inline=False)
    for section in json_response["sections"]:
        display_min_price = f'${section["min_price"]}'
        display_max_price = f'${section["max_price"]}'
        display_price = f'{display_min_price} - {display_max_price}'
        em.add_field(name=f'Section {section["section"]}', value=f'{display_price} Count: {section["count"]}',
                     inline=False)
    em.set_footer(text="Stock Checker made by ieatgoosefeces#2163")
    await ctx.send(embed=em)


@client.command(aliases=['tmintl'])
async def _tickemaster_intl_count(ctx, *, event_id):
    url = f'https://yrmfkazv8g.execute-api.ca-central-1.amazonaws.com/dev_ca_central_1/' \
          f'tmstockchecker/intl?access_code={api_access_code}&event_id={event_id}'
    json_response = await http_get(url)
    if not json_response:
        await ctx.send("Error fetching info from Ticketmaster")
        return

    # create the embed
    em = Embed(
        title='Ticketmaster Inventory Count',
        colour=Colour.red()
    )
    if not json_response["sections"] or len(json_response["sections"]) == 0:
        em.add_field(name=f'Error', value=f'No seats available', inline=False)
    for section in json_response["sections"]:
        display_min_price = f'${section["min_price"]}'
        display_max_price = f'${section["max_price"]}'
        display_price = f'{display_min_price} - {display_max_price}'
        em.add_field(name=f'Section {section["section"]}', value=f'{display_price} Count: {section["count"]}',
                     inline=False)
    em.set_footer(text="Stock Checker made by ieatgoosefeces#2163")
    await ctx.send(embed=em)


@client.command(aliases=['axs'])
async def _axs_count(ctx, *, event_id):
    url = f'https://yrmfkazv8g.execute-api.ca-central-1.amazonaws.com/dev_ca_central_1/' \
          f'axsstockchecker/intl?access_code={api_access_code}&event_id={event_id}'
    json_response = await http_get(url)
    if not json_response:
        await ctx.send("Error fetching info from Ticketmaster")
        return

    # create the embed
    em = Embed(
        title='AXS Inventory Count',
        colour=Colour.red()
    )
    if not json_response["sections"] or len(json_response["sections"]) == 0:
        em.add_field(name=f'Error', value=f'No seats available', inline=False)
    for section in json_response["sections"]:
        display_min_price = f'${section["min_price"]}'
        display_max_price = f'${section["max_price"]}'
        display_price = f'{display_min_price} - {display_max_price}'
        em.add_field(name=f'Section {section["section"]}', value=f'{display_price} Count: {section["count"]}',
                     inline=False)
    em.set_footer(text="Stock Checker made by ieatgoosefeces#2163")
    await ctx.send(embed=em)


if __name__ == "__main__":
    client.run(token)
