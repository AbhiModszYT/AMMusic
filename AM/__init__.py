from AM.core.bot import AnonXBot
from AM.core.dir import dirr
from AM.core.git import git
from AM.core.userbot import Userbot
from AM.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = AnonXBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
