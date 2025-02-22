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

# deep-linking parameters.
DECR8 = 'decr8'
USING_ENTITIES = 'using-entities-here'
SO_COOL = 'so-cool'

DEVELOPER_CHAT_ID = 'me'

STAGE1, STAGE2, STAGE3, STAGE4 = range(4)

app = Client("decr8_g-host", api_id=api_id, api_hash=api_hash)

application = Application.builder().token(
    "6019764680:AAHHW7sDL6I441HW3ineaJ3PM73tXwUlfLU"
).build()

def process_data(file_path, logger):
    with open(file_path, "r+", encoding="utf-8") as f:
        logger.info("Unpacking data to dict.")
        d = json.load(f)
        sorted(d)
    return d

# Call the function and assign the result to a variable
data = process_data("/home/decr8/decr8/res/decr8_data.json", logger)
data_v2 = process_data("/home/decr8/decr8/res/decr8_data_v2.json", logger)
