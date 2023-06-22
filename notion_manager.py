# https://github.com/ramnes/notion-sdk-py
import os
from notion_client import Client
from dotenv import load_dotenv
from pprint import pprint
from dataclasses import dataclass, field

@dataclass
class Properties:
    배포일: dict
    빌드번호: dict
    이름: dict
    
    @property
    def title(self):
        return self.이름['title'][0]['plain_text']


load_dotenv()

notion_secret = os.getenv('NOTION_TOKEN')
db_id = os.getenv('DATABASE_ID')
notion = Client(auth=notion_secret)

if db_id:
    dbd = notion.databases.query(database_id=db_id)
    pprint(dbd)
    if isinstance(dbd, dict):
        print(dbd['results'][0]['properties']) 
        d = Properties(**dbd['results'][0]['properties'])
        print(d.title)
    