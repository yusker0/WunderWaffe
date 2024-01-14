
# WunderWaffe

This is a Python script that works with the telegram API using the telethon library to send a comment to the channel first.


## How To Use

You only need to fill the config file (config.ini) in the root of the project. 
These are the fields you need to fill:

- api_id (You need to get this from [My Telegram](https://my.telegram.org/apps))
- api_hash (You need to get this from [My Telegram](https://my.telegram.org/apps))
- channel_name (Optional. If you don't have a channel and discussion id, you'll need to fill this field)
- channel_id (If you don't have it, fill in the channel_name and run [idFinder.py](idFinder.py))
- discussion_id (If you don't have it, fill in the channel_name and run [idFinder.py](idFinder.py))
- reply_text (What you will write in the comments)
- delay (Delay between the post and your comment. Measured in seconds, minimum 2.6)

After you've filled out the config, you need to run [main.py](main.py) and follow the instructions on the screen.
## License

[WTFPL](http://www.wtfpl.net)
