import sys

from lib import output_helper
from lib import settings_helper
from lib import my_servers_helper
from lib import my_server_helper
from menu import main as menu_main


def initialize():
    my_output = output_helper.OutputHelper()

    settings_handler = settings_helper.Settings()
    if not settings_handler.initialize_settings():
        my_output.error('Local settings initialization failure...')
        return False

    my_servers = my_servers_helper.MyServers()
    if not my_servers.initialize():
        my_output.error('My servers settings initialization failure...')
        return False

    my_server = my_server_helper.MyServer()
    if not my_server.initialize():
        my_output.error('My server settings initialization failure...')
        return False

    return True


if __name__ == "__main__":
    if not initialize():
        sys.exit(1)

    parameters = []
    for item in sys.argv:
        if len(item.split(' ')) == 1:
            parameters.append(item)
        else:
            parameters.append('"%s"' % (item))

    USER_INPUT = ' '.join(parameters)
    menu_main.run(USER_INPUT)
