import qrcode
import requests


class QRCodeAPI:
    def create_qrcode(self, url, save_file_name, callback):
        img = qrcode.make(url)
        img.save(save_file_name)
        callback()


class BitlyAPI:
    def __init__(self, token: str):
        self.BASE_URL = "https://api-ssl.bitly.com"
        self.token = token
        self.group_guid = self.get_group_guid()

    def get_group_guid(self):
        end_point = "/v4/groups"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(self.BASE_URL + end_point, headers=headers)
        try:
            result = response.json()["groups"][0]["guid"]
        except:
            result = ""

        return result

    def shorten_url(self, url) -> str:
        """단축 URL 반환"""
        end_point = "/v4/shorten"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        data = {
            "long_url": f"{url}",
            "domain": "bit.ly",
            "group_guid": f"{self.group_guid}",
        }
        response = requests.post(self.BASE_URL + end_point, headers=headers, json=data)
        try:
            result = response.json()["link"]
        except:
            result = ""

        return result
