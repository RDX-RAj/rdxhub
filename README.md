``` python

import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from rdxhub import rdxhub as papardx
from RDXMUSIC import app

@app.on_message(filters.command("rdxhub"))
async def rdxhub(_, message):
    text = message.text[len("/rdxhub") :]
    papardx(f"{text}").save(f"rdxhub_{message.from_user.id}.png")
    await message.reply_photo(f"rdxhub_{message.from_user.id}.png")
    os.remove(f"rdxhub_{message.from_user.id}.png")

```
``` python
 pip install rdxhub

```




# rdxhub 


![Project Image](https://github.com/RDX-RAj/rdxhub/blob/main/RDX.png)

