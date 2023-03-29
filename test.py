
import aiohttp
import asyncio
import requests
import json
import pycurl
from io import BytesIO
import re
import xmltodict
import pycurl
import certifi
from io import BytesIO

async def setu_generate():
    try:
        buffer = BytesIO()
        print('wuwuwu')
        c = pycurl.Curl()
        c.setopt(c.URL, 'https://testbooru.donmai.us/posts/random.xml')
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.CAINFO, certifi.where())
        print(c)
        c.perform()
        print(c)
        c.close()
        body = buffer.getvalue().decode('iso-8859-1')
        print(body)
        xdict = xmltodict.parse(body)
        pic_url = xdict['post']['file-url']
        
        print(pic_url)
        resp = requests.get(pic_url)
        image = Image.open(BytesIO(resp.content))
        Image_copy = Image.Image.copy(image)
        image.close()
        Image_copy = Image_copy.convert("RGBA")
        return Image
    except:
        return None

async def setu():
    fuck = await setu_generate()
    pass

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    forecast = loop.run_until_complete(setu_generate())
    loop.close()
    pass