import os

# https://www.alphavantage.co
API_KEY_ALPHAVANTAGE = os.getenv("GT_API_KEY_ALPHAVANTAGE") or "MAW9Y5Q85Y6NHWPN"

# https://financialmodelingprep.com/developer
API_KEY_FINANCIALMODELINGPREP = (
    os.getenv("GT_API_KEY_FINANCIALMODELINGPREP") or "31e099043007ea73856006fdaabd6389"
)

# https://www.quandl.com/tools/api
API_KEY_QUANDL = os.getenv("GT_API_KEY_QUANDL") or "HePLR_cMxaQw1b8dKQKF"

# https://www.reddit.com/prefs/apps
API_REDDIT_CLIENT_ID = os.getenv("GT_API_REDDIT_CLIENT_ID") or "XPogAhHJ5c2XFwd"
API_REDDIT_CLIENT_SECRET = os.getenv("GT_API_REDDIT_CLIENT_SECRET") or "8ButsJjsnFEL7x1u5-n62b72MCnzsQ"
API_REDDIT_USERNAME = os.getenv("GT_API_REDDIT_USERNAME") or "Decent_Astronaut151 "
API_REDDIT_USER_AGENT = os.getenv("GT_API_REDDIT_USER_AGENT") or "gamestonks-discord"
API_REDDIT_PASSWORD = os.getenv("GT_API_REDDIT_PASSWORD") or "REPLACE_ME"

# https://polygon.io
API_POLYGON_KEY = os.getenv("GT_API_POLYGON_KEY") or "bfotyoQevNUSpJT3fm3T4BcEPbx_XeZ4"

# https://developer.twitter.com
API_TWITTER_KEY = os.getenv("GT_API_TWITTER_KEY") or "REPLACE_ME"
API_TWITTER_SECRET_KEY = os.getenv("GT_API_TWITTER_SECRET_KEY") or "REPLACE_ME"
API_TWITTER_BEARER_TOKEN = os.getenv("GT_API_TWITTER_BEARER_TOKEN") or "REPLACE_ME"

# https://fred.stlouisfed.org/docs/api/api_key.html
API_FRED_KEY = os.getenv("GT_FRED_API_KEY") or "923a529b2aa5ce2d660eaffb6e48fc5a"

# https://discord.com/developers/applications/
DISCORD_TOKEN = os.getenv("GT_DISCORD_TOKEN") or "ODIyMzczNjAwNDU1NDI2MDY5.YFRVGQ.4CO-LVAMWnOfhwqvgzZI91DujoQ"
DISCORD_GUILD = os.getenv("GT_DISCORD_GUILD") or "822373600455426069"