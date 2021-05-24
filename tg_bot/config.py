class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1869317947:AAHK7mAMdNFPueEMD8tMYNxQ8juppFZfRkE"
    OWNER_ID = "778307700"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "bughunter0"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None
