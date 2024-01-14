from telethon.sync import TelegramClient, events
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

channel_name = config['Target']['channel_name']
channel_found = False
discussion_found = False

with (TelegramClient('WunderWaffe', api_id, api_hash) as client):
    for dialog in client.get_dialogs():
        if dialog.name == channel_name:
            channel_found = True
            channel_id = dialog.entity.id
            discussion_id = dialog.message.replies.channel_id
            config['Target']['channel_id'] = str(channel_id)
            print("channel_id:", channel_id)
            if discussion_id is not None:
                discussion_found = True
                config['Target']['discussion_id'] = str(discussion_id)
                print("discussion_id:", discussion_id)
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            break
    if channel_found and not discussion_found:
        print("Target channel has no comments")
    elif not channel_found:
        print("Target channel was not found")
