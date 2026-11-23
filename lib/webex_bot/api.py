import time
from webexteamssdk import WebexTeamsAPI


class MyWebexApi():
    def __init__(self, bot_token, proxies=None):
        self.webex_api_handler = None
        self.bot_token = bot_token
        self.proxies = proxies

    def create_message(self, room_id=None, text=None, markdown=None, parent_id=None, files=None, max_attempts=3):
        try:
            if len(self.proxies) == 0:
                self.webex_api_handler = WebexTeamsAPI(
                    access_token=self.bot_token
                )
            else:
                self.webex_api_handler = WebexTeamsAPI(
                    access_token=self.bot_token,
                    proxies=self.proxies
                )

        except BaseException:
            return False

        attempt = 1
        while True:
            try:
                success = True
                self.webex_api_handler.messages.create(
                    roomId=room_id,
                    markdown=markdown,
                    text=text,
                    parentId=parent_id,
                    files=files
                )
            except BaseException:
                success = False

            if success:
                break

            attempt = attempt + 1
            time.sleep(.5)
            if attempt > max_attempts:
                return False

        return True
