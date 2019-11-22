import aiohttp
from logger import logger


async def http_get(url):
    session = aiohttp.ClientSession()
    logger.debug(f'Calling URL {url}')
    logger.info("Sending request to API")
    response = ''
    try:
        response = await session.get(url)
        json_response = await response.json()
        logger.info(json_response)
        return json_response
    except aiohttp.ClientError:
        logger.info(response)
        return None
    finally:
        await session.close()
