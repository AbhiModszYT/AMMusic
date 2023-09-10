import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","12227067"))
API_HASH = getenv("API_HASH","b463bedd791aa733ae2297e6520302fe")

BOT_TOKEN = getenv("BOT_TOKEN","6695096262:AAEY_iryJXb2WdiyVE7cN86_9BkNVMKF4ds")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ambot:ambot@ambot.onafiyb.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1001973171142"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝑴𝒊𝒔𝒔 𝒔𝒐𝒏𝒂")

OWNER_ID = list(map(int, getenv("OWNER_ID", "6634748952").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AbhiModszYT/AMMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AmBotYT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/AM_YTSUPPORT")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999999999999999"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "6400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQCrwet9Lr-abhuEpZdg4hgFd7kQTMkbRNe2LR0wJBlc6iImz6Eb_AoHyhBybAjqHF4024Vjh1UiCk0I8BGxBPjDo46gRMwZPrJsAhsAOne2H8cm1vbJ21ot-ucZVHf3CEPSEK8kysyRLwGmb3u7zYmM0fvkHzIAx5rfWO-QfFHMsgD6J83RkWWuglyEioZ1RvaaCbbIUMEO1aay3hhCAUFO2BeYUsasBI3eu7YRkm1uhmpHxrqdOThdmlbj9T5dLIKvRZhqJ1UxG-bPevG_WZqe1Ye_cRkJ26aMifE3YoomKDJrzR7UOLmLVo6rOLSjbGZqvLkXhwCrtNF7MWaefIa0AAAAAX7UZY0A")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/f5473b8c1556a2dbc71bb.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/f5473b8c1556a2dbc71bb.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/8d3944528638ff176d115.jpg","https://te.legra.ph/file/00294cbabc8bd4a9e75b0.mp4","https://graph.org/file/7ca0ae3fe2e327d3dcc86.jpg","https://te.legra.ph/file/e7629907cf40431ec6ccd.jpg","https://graph.org/file/a39f6f364c34e724ef367.jpg","https://graph.org/file/88fcdd5e044279c0d1747.jpg","https://graph.org/file/fcc2837e0f83cd4d08765.jpg","https://graph.org/file/1fcd0f7d5fdb7e700dca5.jpg","https://graph.org/file/39c27bf76bf8742a148c4.jpg","https://graph.org/file/2c5e6f38ca28687c8c3e8.jpg","https://graph.org/file/71682c8fb277c84031c0f.jpg","https://graph.org/file/c118207cef395ceb196ee.jpg","https://graph.org/file/1b765cd3d9fcc99614a32.jpg","https://graph.org/file/d935b6fbb2e3936b1850a.jpg","https://graph.org/file/e94c4566b9a7cf7d23a4b.jpg","https://graph.org/file/fd2196561ba6e8c4c46a9.jpg","https://graph.org/file/17cbf7cedbc44b85c7bda.jpg","https://graph.org/file/cd72a1c4c3b1d52070a90.jpg","https://graph.org/file/8663d4f19f5d9c30f8ff9.jpg","https://graph.org/file/255e5501d4f8b2e348d87.jpg","https://graph.org/file/cf28d171b08e0590749c7.jpg","https://graph.org/file/a1d7ccd85d58b076f8f88.jpg","https://graph.org/file/aa10da451e1e263105516.jpg","https://graph.org/file/cba9cd9f3fd1bcf841db2.jpg","https://graph.org/file/a06eaee8e9070840947bd.jpg","https://graph.org/file/83f5a1123580bd75f591e.jpg","https://graph.org/file/2f4f60ba8405368505ba2.jpg","https://graph.org/file/18da6db0b032a6c428471.jpg","https://graph.org/file/cd0f7fd0dc68ce8dbe2d4.jpg","https://graph.org/file/eabfa2836ec2e6fb41cd5.jpg","https://graph.org/file/59fb7cd9ea2d1331e75ef.jpg","https://graph.org/file/748e908aaa6cbb6c03402.jpg","https://graph.org/file/a26d09d472ddce5532ca2.jpg","https://graph.org/file/3fb4577387c3934eed027.jpg","https://graph.org/file/e19ab57b45fe4c9765869.jpg","https://graph.org/file/4b9b5d7b6e1a46c55dea1.jpg","https://graph.org/file/d7f9dd74e37f3e4985075.jpg","https://graph.org/file/8fd58648581a8f8d3f19b.jpg","https://te.legra.ph/file/7b10f2f5ffb1bc6075197.jpg","https://te.legra.ph/file/628180b161e5233889919.jpg","https://te.legra.ph/file/e8571aeadbd3204a28076.jpg","https://te.legra.ph/file/8d3944528638ff176d115.jpg","https://te.legra.ph/file/95c760593b889ac2cf283.jpg",

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/56d1760224589ee370186.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/e7a8c2b902d3e2fefd4ff.jpg"
