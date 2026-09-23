from pyrogram import Client
from api.imports import *

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
api_id = 123456
api_hash = "api_hash"

decr8 = -1001280481543
decr8_v2 = -1001969042072
decr8loader = 1575933473
me = 487795386
p = re.compile("[a-z]+", re.IGNORECASE)
dcr8_url = "https://t.me/crateofnotsodasbutmusic/"
dcr8_v2_url = "https://t.me/thecrate/"
app = Client("decr8_g-host", api_id=api_id, api_hash=api_hash)
DB_PATH = "/home/decr8/decr8/decr8.db"
application = Application.builder().token(
    "token"
).build()
