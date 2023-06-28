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
import openai
from PIL import Image
from io import BytesIO
import os

# comments to let it go
# comments to let module works

openai.api_key = os.getenv("OPENAI_API_KEY")
print(f"Openai KEY : {openai.api_key}")

require_chat = on_command('c3')

context_3 = {}

@require_chat.handle()
async def _(bot: Bot, event: Event, state: T_State):
    group_id = event.get_session_id()
    if str(group_id).startswith('group_725194874'):
        if group_id not in context_3:
            context_3[group_id] = []
        print(str(event.get_message())[2:])
        input = (str(event.get_message())[2:]).strip()
        # print(f'Input {input}')
        while(len(context_3[group_id]) > 10):
            context_3[group_id].pop(0)
        context_3[group_id].append({"role":"user", "content":input})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613", 
            messages=context_3[group_id]
        )
        answer = str(completion['choices'][0]['message']['content']).strip()
        context_3[group_id].append({"role":"assistant", "content":answer})
        answer = re.sub(r"(.{30})", "\\1\n", answer)
        await require_chat.finish(Message([
            MessageSegment("image", {
                    "file": f"base64://{str(image_to_base64(text_to_image(answer)), encoding='utf-8')}"
            }),
        ]))
        
        
require_chat = on_command('c4')

context_4 = {}

@require_chat.handle()
async def _(bot: Bot, event: Event, state: T_State):
    group_id = event.get_session_id()
    if str(group_id).startswith('group_725194874'):
        if group_id not in context_4:
            context_4[group_id] = []
        print(str(event.get_message())[2:])
        input = (str(event.get_message())[2:]).strip()
        # print(f'Input {input}')
        while(len(context_4[group_id]) > 10):
            context_4[group_id].pop(0)
        context_4[group_id].append({"role":"user", "content":input})
        completion = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=context_4[group_id]
        )
        answer = str(completion['choices'][0]['message']['content']).strip()
        context_4[group_id].append({"role":"assistant", "content":answer})
        answer = re.sub(r"(.{30})", "\\1\n", answer)
        await require_chat.finish(Message([
            MessageSegment("image", {
                    "file": f"base64://{str(image_to_base64(text_to_image(answer)), encoding='utf-8')}"
            }),
        ]))
        