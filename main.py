import configparser
from telethon.sync import TelegramClient, events
from time import sleep

config = configparser.ConfigParser()
config.read("config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

reply_text = config['WunderWaffe']['reply_text']
delay = config['WunderWaffe']['delay']

channel_id = 1988659280
discussion_id = 1969573951

with (TelegramClient('WunderWaffe', api_id, api_hash) as client):
   @client.on(events.NewMessage(chats=[channel_id,]))
   async def handler(event):
      print("ATTENTION!!!")
      sleep(delay)
      last_message = (await client.get_messages(discussion_id, 1))[0]
      await client.send_message(entity=discussion_id, reply_to=last_message.id, message=reply_text)

   client.run_until_disconnected()