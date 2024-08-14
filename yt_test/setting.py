import os
from dotenv import load_dotenv

load_dotenv()
api = os.getenv('API')

DOWNLOAD = 'download'
VIDEO = os.path.join(DOWNLOAD,'video')
CAPTION = os.path.join(DOWNLOAD,'caption')