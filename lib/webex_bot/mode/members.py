from webexteamssdk import WebexTeamsAPI


def run(bot_settings):
    # https://webexteamssdk.readthedocs.io/en/latest/user/api.html#memberships
    webex_api_handler = WebexTeamsAPI(
        access_token=bot_settings['token'],
        proxies=bot_settings['proxies']
    )

    memberships = webex_api_handler.memberships.list()
    for membership in memberships:
        print(membership)
