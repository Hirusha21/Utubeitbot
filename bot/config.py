import os


class Config:

    BOT_TOKEN = os.environ.get("5662705097:AAERW7P1AJQvlJsW9vk8_0FM--LrB3iRKJs")

    SESSION_NAME = "YouTubeUploadhdRobot"

    API_ID = int(os.environ.get("2208116"))

    API_HASH = os.environ.get("e908365e42dcd3051c24d412102f356e")

    CLIENT_ID = os.environ.get("671533383876-dtppjmg1gtadi6cfev4ssh9bgonc570m.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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)

    BOT_OWNER = int(os.environ.get("1339693473"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 755681801] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
