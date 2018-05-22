# ---------------
# Module import
# ---------------
import os
import re
import time
import tqdm
import json
import requests
from bs4 import BeautifulSoup as BS

# ----------------
# Constant setting
# ----------------
SLEEPTIME = 1.5

# ----------------------------
# Class or Function definition
# ----------------------------
class ReviewInfor:
    """レストランのレビューページをスクレイピングするためのクラス."""

    def __init__(self, url):
        """コンストラクタ."""
        self.url = url


# ------------------
# Main processing
# ------------------
if __name__=="__main__":
    pass
