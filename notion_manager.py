# https://github.com/ramnes/notion-sdk-py
import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])