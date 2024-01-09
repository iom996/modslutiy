from hikkatl.types import Message
from .. import loader
import random


@loader.tds
class ruletkaModule(loader.Module):
    """русская рулетка"""

    strings = {"name": "ruletka", "loose": f"<b>you loose!<b>", "win": f"<b>you won!<b>"}
    strings_ru = {"loose": f"<b>вы проиграли!<b>", "win": f"<b>вы победили!<b>"}

    @loader.command(
        )
    async def rulcmd(self, message: Message):
        """any number 1-6"""
        numo = random(random.randint(1-6))
        num = utils.get_args_raw(message)
        if num == numo :
            await utils.answer(message, self.strings("loose"))
        else:
            await utils.answer(message, self.strings("win"))
