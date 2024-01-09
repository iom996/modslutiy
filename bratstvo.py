from collections import UserList, UserString
import logging
import time

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)

# meta developer: @imloveonegirl


@loader.tds
class BratstvoMod(loader.Module):
    """удаляет братство"""
    strings = {"name": "bratstvo"}

    async def udalitcmd(self, message: Message) -> None:
        """начинает удаление"""
        br = 0
        while br <= 99 :
            await message.edit("удаление братства: " + str(br) + "%")
            br += 1
        await message.edit("ашибка братства не удалить")       