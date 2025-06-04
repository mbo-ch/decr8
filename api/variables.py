from pyrogram import Client
from api.imports import *

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
api_id = 314504
api_hash = "8c64c308e6f0186d495ae1e92a1c228d"

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
    "6019764680:AAHHW7sDL6I441HW3ineaJ3PM73tXwUlfLU"
).build()
