from .. import loader, utils
from telethon.tl.types import Message

# meta developer: @imloveonegirl

@loader.tds
class PmMod(loader.Module):
    """пишат то что нужно лс"""

    strings = {"name": "pm",
                "ls": f"<b>please go to pm<b>",
                "ls_ru": f"<b>пожалуйста напиши мне в лс<b>",
                "ls_ukr": f"<b>будь ласка напишіть мені у пс<b>",
                }

    async def pmcmd(self, message: Message) -> None:
        """<ru or en>"""
        lang = utils.get_args_raw(message)
        if lang == "ru" :
            await utils.answer(message, self.strings("ls_ru"))
        if lang == "en" :
            await utils.answer(message, self.strings("ls"))
        if not lang:
            await utils.answer(message, self.strings("ls_ukr"))

