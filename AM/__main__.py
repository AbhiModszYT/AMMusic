import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AM import LOGGER, app, userbot
from AM.core.call import Anon
from AM.plugins import ALL_MODULES
from AM.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("AM").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("AM").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AM.plugins." + all_module)
    LOGGER("AM.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Anon.start()
    try:
        await Anon.stream_call(
            "https://telegra.ph/file/e542f112509f7b1ee6b11.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("AM").error(
            "[ERROR] - \n\nHey Dear, firstly open telegram and turn on voice chat in Logger Group else. If you ever ended voice chat in log group i will stop working."
        )
        sys.exit()
    except:
        pass
    await Anon.decorators()
    LOGGER("AM").info("\x53\x6F\x70\x68\x69\x61\x20\x4D\x75\x73\x69\x63\x20\x42\x6F\x74\x20\x73\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6C\x6C\x79\x2E\x2E\x2E\x5C\x6E\x5C\x6E\x20\x4E\x6F\x77\x20\x4A\x6F\x69\x6E\x20\x40\x41\x62\x68\x69\x4D\x6F\x64\x73\x7A\x59\x54\x5F\x52\x65\x74\x75\x72\x6E")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AM").info("Stopping Music Bot...")
