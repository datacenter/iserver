import time
import traceback

from lib.webex_bot.commands.aci import GetAciCommand
from lib.webex_bot.commands.nx import GetNexusCommand
from lib.webex_bot.commands.server import GetServerCommand
from lib.webex_bot.commands.info import InfoCommand
from lib.webex_bot.commands.whoami import WhoamiCommand
from lib.webex_bot.commands.settings import SettingsCommand

from lib.webex_bot.webex_bot import MyWebexBot
from lib.webex_bot import api

def run(bot_settings, bot_modules):
    approved_users = []
    for user in bot_settings['users']:
        approved_users.append(
            user['username']
        )

    backend_url = None
    if 'backend' in bot_settings:
        backend_url = bot_settings['backend']

    bot = MyWebexBot(
        bot_settings['token'],
        bot_settings['email'],
        approved_users=approved_users,
        bot_name=bot_settings['name'],
        url=backend_url,
        include_demo_commands=False
    )

    my_webex_api_handler = api.MyWebexApi(
        bot_settings['token'],
        proxies=bot_settings['proxies']
    )

    # Add new commands for the bot to listen out for.
    bot.add_command(InfoCommand())
    bot.add_command(WhoamiCommand(bot_settings['users']))
    bot.add_command(SettingsCommand(backend_url))

    if 'aci' in bot_modules.split(','):
        bot.add_command(GetAciCommand(my_webex_api_handler, backend_url))
    if 'nexus' in bot_modules.split(','):
        bot.add_command(GetNexusCommand(my_webex_api_handler, backend_url))
    if 'intersight' in bot_modules.split(','):
        bot.add_command(GetServerCommand(my_webex_api_handler, backend_url))

    # Call `run` for the bot to wait for incoming messages.
    while True:
        try:
            bot.run()
        except BaseException:
            print(traceback.format_exc())

        time.sleep(3)
