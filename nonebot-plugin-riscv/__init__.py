import nonebot
from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent

import json

# Opening JSON file
f = open('/root/nonebot/my-bot/my_bot/plugins/riscv/data.json')

# returns JSON object as
# a dictionary
datas = json.load(f)

riscv = on_command("risvc", aliases={"rv"}, priority=3, block=True)


@riscv.handle()
async def _(event: MessageEvent):
    try:
        msg = event.get_plaintext()
        command = msg.split()[-1]
        msg = "指令未找到"
        for data in datas:
            if data.get('name') == command:
                msg = data.get('content')
                msg = msg + '\n相关推荐：' + ' '.join(data.get('relevant'))
                break
        await riscv.finish(msg)
    except:
        pass
