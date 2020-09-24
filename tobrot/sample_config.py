import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1177066431:AAHyN0PxJ9B_Vw5GPwbRspFHcy9u3rxUM8M")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 1474808))
    API_HASH = os.environ.get("API_HASH", 10c9e59fb3bfaee28bb6e76f7d5a6855)
    OWNER_ID = int(os.environ.get("OWNER_ID", 1283735480))
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "-477648128").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 15))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "type = drive
scope = drive
token = {"access_token":"ya29.a0AfH6SMDct2uWnbN_LJDR-wTSUu3N5AKTDHehBWNjGGpRsHkKihW4F1PGaeYmRHsYf1-B8DBdHjhw5ybX0_oMs7ge1q_bCT0NDtkf7Pln_vr8flKzW11dU531wh_5N_EsKJh6I5sx3yk_taMXcaP9N8rVXrVeUtaTxxQ","token_type":"Bearer","refresh_token":"1//0gPZ3HWJ6W7YcCgYIARAAGBASNwF-L9IrNL8CeXTDU221kgJ5aspuIDlk4hM7WHcXf1LotnnIhEq7Bieuzw4zH2kUUxetBquIhFM","expiry":"2020-06-23T18:32:03.76910669Z"}
root_folder_id = 18iWw_jEh2G4CNXMKuxwUm9h6HPfPCxzp")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "Gleech")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech")
    INDEX_LINK = os.environ.get("INDEX_LINK", "")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail")
    UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "true")
    PYTDL_COMMAND_G = os.environ.get("PYTDL_COMMAND_G", "pytdl")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "log")
    CLONE_COMMAND_G = os.environ.get("CLONE_COMMAND_G", "gclone")
