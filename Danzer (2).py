from telethon import TelegramClient
import asyncio

# Set your API credentials
API_ID = 'your_api_id'  # Replace with your API ID
API_HASH = 'your_api_hash'  # Replace with your API hash

# Define the source group and destination channel
SOURCE_GROUP_ID = -1001234567890  # Replace with the source group ID
DESTINATION_CHANNEL_ID = -1009876543210  # Replace with the destination channel ID

# Initialize the client with a user session
client = TelegramClient('user_session', API_ID, API_HASH)

async def clone_messages():
    """Fetches and forwards all past messages from the source group to the destination channel."""
    async for message in client.iter_messages(SOURCE_GROUP_ID, reverse=True):
        try:
            await client.send_message(DESTINATION_CHANNEL_ID, message)
            print(f"Cloned message {message.id}")
        except Exception as e:
            print(f"Error cloning message {message.id}: {e}")

async def main():
    await client.start()
    await clone_messages()
    print("Cloning completed.")

print("User session running...")
client.loop.run_until_complete(main())
