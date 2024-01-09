from .. import loader, utils
from telethon.tl.types import Message
from telethon.tl.functions.contacts import BlockRequest

# meta developer: @imloveonegirl

@loader.tds
class BlMod(loader.Module):
    """блокирует"""

    strings = {"name": "Bl"}

    async def blcmd(self, message: Message) -> None:
        """<текст>"""
        c = utils.get_chat_id(message)
        reson = utils.get_args_raw(message)
        await self._client(BlockRequest(id=c))
        if not reson :
            await utils.answer(
                message, 
                               f"<b>ти лох ХАХХААХАХАХААХААХХАХ<b>")
        else :
            await utils.answer(
                message, 
                               f"<b>Вы были заблокировани моим юзер ботом потомучто {reson}<b>")