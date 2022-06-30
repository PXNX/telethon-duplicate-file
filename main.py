import asyncio
from collections import defaultdict

from telethon import TelegramClient
from telethon.tl.types import MessageMediaDocument

import config


def is_audio(message) -> bool:
    return message.media is not None and type(
        message.media) is MessageMediaDocument and message.media.document is not None and message.media.document.mime_type.startswith(
        "audio")


async def get_duplicates(client):
    audios = defaultdict(list)

    async for message in client.iter_messages(config.GROUP):

        if is_audio(message):
            print(message)
            audios[message.media.document.size].append(message.id)

    print(audios)

    for file_size, message_ids in audios.items():

        if len(message_ids) == 1:
            continue

        text = f"There's multiple entries for {file_size}:"

        for message_id in message_ids:
            text += f"\n\n>> https://t.me/{config.GROUP}/{message_id}"

        await client.send_message("me", text)
        await asyncio.sleep(0.3)


if __name__ == "__main__":
    with TelegramClient("remove_inactive", config.api_id, config.api_hash) as tgclient:
        asyncio.get_event_loop().run_until_complete(get_duplicates(tgclient))
