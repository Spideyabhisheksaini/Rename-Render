# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27064328")

API_HASH = os.environ.get("API_HASH", "7be1392c2fe5ebf4fc3228706fbfb504")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6570108244:AAFogHLTqoj2FOWwNYxe70ka8t_lDLo6eyI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "@MovieTimes_TV") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Missminutes")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Tonystarkbotz:Tonystarkbotz@missminutes.lbzdtkj.mongodb.net/?retryWrites=true&w=majority&appName=Missminutes")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/8df4d54ad838879691cf6.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5019668523').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
