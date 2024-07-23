#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS, AUTO_LINK_CREATION
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    if not AUTO_LINK_CREATION:
        return  # Skip link creation if the feature is disabled
    
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>Here is your link</b>\n\n <blockquote>{link}</blockquote>", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    if not AUTO_LINK_CREATION:
        return  # Skip link creation if the feature is disabled
    
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>Here is your link</b>\n\n <blockquote>{link}</blockquote>", quote=True, reply_markup=reply_markup)

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch_plus'))
async def batch_plus(client: Client, message: Message):
    if not AUTO_LINK_CREATION:
        return  # Skip link creation if the feature is disabled

    while True:
        try:
            first_message = await client.ask(text="Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote=True)
            continue

    while True:
        try:
            num_files_message = await client.ask(text="Enter the number of files you want to batch process:", chat_id=message.from_user.id, filters=filters.text, timeout=60)
        except:
            return
        if num_files_message.text.isdigit():
            num_files = int(num_files_message.text)
            break
        else:
            await num_files_message.reply("❌ Error\n\nPlease enter a valid number.", quote=True)
            continue

    l_msg_id = f_msg_id + num_files - 1

    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{l_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await num_files_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch_pro'))
async def batch_pro(client: Client, message: Message):
    if not AUTO_LINK_CREATION:
        return  # Skip link creation if the feature is disabled

    # Step 1: Get the first message
    while True:
        try:
            first_message = await client.ask(text="Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote=True)
            continue

    # Step 2: Get the total number of files
    while True:
        try:
            total_files_message = await client.ask(text="Enter the total number of files to process:", chat_id=message.from_user.id, filters=filters.text, timeout=60)
        except:
            return
        if total_files_message.text.isdigit():
            total_files = int(total_files_message.text)
            break
        else:
            await total_files_message.reply("❌ Error\n\nPlease enter a valid number.", quote=True)
            continue

    # Step 3: Get the last message
    while True:
        try:
            last_message = await client.ask(text="Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        l_msg_id = await get_message_id(client, last_message)
        if l_msg_id:
            break
        else:
            await last_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote=True)
            continue

    # Step 4: Get the number of files per batch
    while True:
        try:
            batch_size_message = await client.ask(text="Enter the number of files per batch:", chat_id=message.from_user.id, filters=filters.text, timeout=60)
        except:
            return
        if batch_size_message.text.isdigit():
            batch_size = int(batch_size_message.text)
            break
        else:
            await batch_size_message.reply("❌ Error\n\nPlease enter a valid number.", quote=True)
            continue

    # Step 5: Notify user that batching is in progress
    batching_msg = await message.reply_text("📦 Batching in progress, please wait...")

    # Calculate the number of batches needed
    num_batches = (total_files + batch_size - 1) // batch_size
    batch_links = []

    for i in range(num_batches):
        start_id = f_msg_id + i * batch_size
        end_id = min(f_msg_id + (i + 1) * batch_size - 1, l_msg_id)
        batch_string = f"get-{start_id * abs(client.db_channel.id)}-{end_id * abs(client.db_channel.id)}"
        base64_string = await encode(batch_string)
        link = f"https://telegram.me/{client.username}?start={base64_string}"
        batch_links.append(link)

    # Step 6: Prepare the final message with all batch links
    batch_messages = [
        f"Batch Link {i + 1}\n{link}"
        for i, link in enumerate(batch_links)
    ]
    final_message_text = "<b>Here are your batch_pro links:</b>\n\n" + "\n".join(batch_messages)

    # Create InlineKeyboardMarkup with the batch links
    buttons = [InlineKeyboardButton(f"Batch {i+1}", url=link) for i, link in enumerate(batch_links)]
    reply_markup = InlineKeyboardMarkup([buttons[i:i + 3] for i in range(0, len(buttons), 3)])  # 3 links per row

    # Update the user with the batch links
    await batching_msg.edit_text(final_message_text, reply_markup=reply_markup)
