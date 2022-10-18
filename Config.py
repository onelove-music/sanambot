import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "4508453"))
    API_HASH = os.environ.get("API_HASH", "9fc008a9ff9656f124fb1a7fd008d68d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1969642651:AAETxnchH3tG5qFTFI3fAVB897ZqEHj4qg")
    STRING_SESSION = os.environ.get("STRING_SEASSION", "BQALM2m_ZjifP4u0INn53Md_KtRh3V7HIUL8hAskMV_PESkIi8BVJhBtQeB_PvN4j5OeTZQOlWOr5O9wBQzpIoVHPopesFCuZwLnTqbizUhKOxHXi_D-mBHDXDhB2MQUBvCc19IlgITiMh3QL6H-cVGKU5yZXncVnz9yTmg4nNG5yx9upnDlj-7Zi8tmqJVAHXT7dBH34BLP2eWx5Zz0KKcyednNf59ttrfdX5sa2f2navseheCP-5FBVG_mwuzCRZFJwQZXlr7wayMLutO4U67_D6s8SEI5Ku320DKu5nt0jZRr0HcvKOrbos8cb8Kql1aNrIcJ5nLFq3af1rBnECioW9FwggA.")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME","NISHI_MUSIC_bot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/paradiseworld_1") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/Paradiseworld543") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID","1540452482")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
