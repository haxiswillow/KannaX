""" convert text """

# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

from kannax import Message, kannax


@kannax.on_cmd(
    "small",
    about={"header": "Make caps smaller", "usage": "{tr}small [text | reply to msg]"},
)
async def small_(message: Message):
    """text to small"""
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("input not found")
        return
    await message.edit(
        text.translate(
            str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘqʀꜱᴛᴜᴠᴡxʏᴢ")
        )
    )


@kannax.on_cmd(
    "lower",
    about={
        "header": "Convert text to lowwer",
        "usage": "{tr}lower [text | reply to msg]",
    },
)
async def lower_(message: Message):
    """text to lower"""
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("input not found")
        return
    await message.edit(text.lower())


@kannax.on_cmd(
    "upper",
    about={
        "header": "Convert text to upper",
        "usage": "{tr}upper [text | reply to msg]",
    },
)
async def upper_(message: Message):
    """text to upper"""
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("input not found")
        return
    await message.edit(text.upper())
