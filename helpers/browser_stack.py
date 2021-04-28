from json import loads
from requests import post
from os.path import abspath


def upload_app(app_path: str, app_name: str) -> dict:
    with open(abspath(app_path), 'rb') as file:
        files = {
            'file': file
        }

        return loads(
            post(
                'https://api-cloud.browserstack.com/app-automate/upload',
                files=files,
                auth=('augustoteixeira_XcHa4y', 'wLD4zP4qHh79MpRrYh54')
            ).text
        )
