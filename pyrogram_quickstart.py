from pyrogram import Client

api_id = 123456
api_hash = "api_hash"

app = Client("decr8_g-host", api_id=api_id, api_hash=api_hash)

@app.on_message()
async def hello(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}")

app.run()
