import random
import re

from typing import Optional, Dict, List
from collections import defaultdict
from PIL import Image
from nonebot import on_command, on_message, on_notice, require, get_driver, on_regex
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Event, Bot
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.exception import IgnoredException
from nonebot.message import event_preprocessor
from src.libraries.image import *
from random import randint
import time
from PIL import Image
import requests
from PIL import Image
from io import BytesIO
import aiohttp
from nonebot.adapters.cqhttp import MessageSegment

import requests as req
from PIL import Image
from io import BytesIO

# comments to let it go
# comments to let module works


async def setu_generate():
    try:
        buffer = BytesIO()
        # print('wuwuwu')
        c = pycurl.Curl()
        c.setopt(c.URL, 'https://danbooru.donmai.us/posts/random.xml')
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.CAINFO, certifi.where())
        # print(c)
        c.perform()
        # print(c)
        c.close()
        body = buffer.getvalue().decode('iso-8859-1')
        # print(body)
        xdict = xmltodict.parse(body)
        pic_url = xdict['post']['file-url']
        # print(pic_url)
        resp = requests.get(pic_url)
        image = Image.open(BytesIO(resp.content))
        Image_copy = Image.Image.copy(image)
        image.close()
        Image_copy = Image_copy.convert("RGBA")
        return Image
    except:
        return None


require_setu = on_regex(r"求求你了来张色图")

@require_setu.handle()
async def _(bot: Bot, event: Event, state: T_State):
    img = await setu_generate()
    if img == None:
        await require_setu.finish(Message([
            MessageSegment.reply(event.message_id), 
            MessageSegment("text", {
            "text": "没有色图了喵" })
            ]))
    else:
        await require_setu.finish(Message([
            MessageSegment("image", {
                    "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
            })
        ]))