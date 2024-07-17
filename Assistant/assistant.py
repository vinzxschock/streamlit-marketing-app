"""
Liste mit Custom GPTs
"""

import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


# Insert your assistant id
OPENAI_ASSISTANT = 'asst_jy1FXRxyLQ5IdzrRW9WWSPvk'


gpts = {
    "CustomGPT": OPENAI_ASSISTANT,
}