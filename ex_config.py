# FOR SELF HOST
# EDIT THIS FILE AND RENAME TO config.py TO MAKE THIS BOT WORKING
# FILL THESE VALUES ACCORDINGLY.

from HellConfig.config import Config


class Development(Config):
    # get these values from my.telegram.org.
    
    APP_ID = 4277083  # 666666 is a placeholder. Fill your 6 digit api id
    
    API_HASH = "bb0ddae0921fc020ce61faae2d1261d5"  # replace this with your api hash
    
    BOT_TOKEN = "5528571909:AAG5EacovJwxXoworfgj7IIum2F5tRke-GY"  # Create a bot from @BotFather and paste the token here
    
    BOT_LIBRARY = "telethon"  # fill 'pyrogram' if you want pyrogram version of hellbot else leave it as it is.

    DB_URI = "postgresql://xuajpuxl:k2vvRADJk0ggkxGf0AgTb9IJ2iwv5Mhu@mouse.db.elephantsql.com/xuajpuxl"  # A postgresql database url from elephantsql

    HELLBOT_SESSION = "1BVtsOI4Bux92SQlZLQ9MFguLb_TEvWthwwd08nJtVMw1UxD5D9Livo-g-zDyqWiF77RMP3gWAiPelosZ4UPKbOkt4Gf5RWbbljYVMD3G5DFt6FJEd_HyQamS4uOxvWPdGw_xM2Reww9JrKuzcFJLmiH7XgtWheMWl1zUscLvz9llfXVLyEl-geXneqA3_dBD-LX0_8zzeixpxNvmjRmMbjijoxKnV0Ryr25Ki8MUoIy9SChwipYqhJwLRs5eMdFwyM0YDnmLIJ6ZKlzWZ6CEOTC9-6iKUNDJ6bk_Y_NaRCeqVc7z2IvIn8DyWeWieNVzedwiIHsQKj4lAjBfrqj1NStca6WOhWw="  # telethon or pyrogram string according to BOT_LIBRARY

    HANDLER = "."  # Custom Command Handler

    SUDO_HANDLER = "!"  # Custom Command Handler for sudo users.


# end of required config
# hellbot
