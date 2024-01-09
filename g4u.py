from .. import loader, utils
from telethon.tl.types import Message  # type: ignore

#meta developer:@imloveonegirl

@loader.tds
class googleMod(loader.Module):
    """загугли..."""

    strings = {"name": "google",
               "noag": "no args"}
    strings_ru = {"noag": "нету запроса",}

    async def goglcmd(self, message: Message) :
        """<args>"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no args"))
            return
        g = args.replace(" ", "+")
        gogl = f"https://googlegiksearch.github.io/?q={g}"
        await utils.answer(message, gogl)