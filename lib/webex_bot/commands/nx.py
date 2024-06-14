import os
import uuid
import time
import json
import traceback
import logging

from lib import log_helper
from lib import file_helper
from lib.webex_bot.models.command import Command
from lib.nexus import settings as nexus_settings
from lib.nexus import bot_output
from lib.nexus import nxapi

logger = logging.getLogger(__name__)


class GetNexusCommand(Command):
    def __init__(self, my_webex_api_handler, url):
        super().__init__(
            command_keyword="get nx",
            help_message="get nx",
            card=None,
        )
        self.run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(self.run_id)
        self.log_handler.initialize()
        self.link = 'https://wwwin-github.cisco.com/emear-telcocloud/iserver/blob/master/doc/bot/GetNexus.md'
        self.url = url
        logger.info('Command initialized: get nexus [%s]', self.run_id[4:])

        self.my_webex_api_handler = my_webex_api_handler

    def help(self):
        output = 'Command syntax: get nx &lt;option&gt; &lt;device&gt;<br><br>'
        output = '%s- option: dev, cache, lacp, lldp, mac, version<br>' % (output)
        output = '%s- define multiple options or opt:all<br>' % (output)
        output = '%s- define multiple device names or dev:all<br>' % (output)
        output = '%s<br>Find more examples and documentation <a href="%s">here</a>' % (output, self.link)
        return output

    def doc(self, activity):
        files = []
        files.append(
            os.path.join(
                os.path.join(
                    os.path.join(
                        file_helper.get_main_dir(),
                        'doc'
                    ),
                    'bot'
                ),
                'GetNexus.md'
            )
        )
        self.my_webex_api_handler.create_message(
            room_id=activity['target']['globalId'],
            parent_id=activity['id'],
            files=files
        )

    def parse_command(self, message, command_run_id):
        nexus_settings_handler = nexus_settings.NexusSettings(log_id=command_run_id)

        options = {}
        options['success'] = True
        options['error'] = ''
        options['view'] = []
        options['device'] = []
        options['cache'] = None

        words = message.split(' ')
        if len(words) == 0:
            options['success'] = False
            options['error'] = 'Cannot parse the command'
            return options

        # View

        for view_name in words:
            if view_name in ['dev', 'cache', 'lacp', 'lldp', 'mac', 'version', 'opt:all']:
                if view_name == 'opt:all':
                    for item in ['cache', 'lacp', 'lldp', 'mac', 'version']:
                        if item not in options['view']:
                            options['view'].append(item)

                if view_name != 'opt:all':
                    if view_name not in options['view']:
                        options['view'].append(view_name)

        if len(options['view']) == 1 and 'dev' in options['view']:
            options['device'] = nexus_settings_handler.get_nexus_devices()
            return options

        # Device

        device_names = []
        for device_name in words:
            if device_name not in ['dev', 'cache', 'lacp', 'lldp', 'mac', 'version', 'cache:on', 'cache:off', 'opt:all']:
                if device_name in device_names:
                    continue

                if device_name == 'dev:all':
                    device_names = nexus_settings_handler.get_nexus_device_names()
                    options['device'] = nexus_settings_handler.get_nexus_devices()

                if device_name != 'dev:all':
                    device_names.append(device_name)
                    device_settings = nexus_settings_handler.get_nexus_device(device_name)
                    if device_settings is None:
                        options['success'] = False
                        options['error'] = 'Unknown device: %s' % (device_name)
                        return options

                    options['device'].append(
                        device_settings
                    )

        if len(device_names) == 0:
            options['success'] = False
            options['error'] = 'Select at least one device'
            return options

        # Cache

        for flag in words:
            if flag == 'cache:on':
                options['cache'] = True
            if flag == 'cache:off':
                options['cache'] = False

        return options

    def execute(self, message, attachment_actions, activity):
        command_run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(command_run_id)
        self.log_handler.initialize()

        logger.info('Command execution: get nx [%s]', command_run_id[4:])

        try:
            message = message.strip().lower()
            if len(message) == 0 or message in ['help', '?', '--help']:
                if activity['verb'] == 'cardAction':
                    return self.help()

                self.my_webex_api_handler.create_message(
                    room_id=activity['target']['globalId'],
                    markdown=self.help(),
                    parent_id=activity['id']
                )
                self.doc(activity)
                return

            options = self.parse_command(message, command_run_id)
            logger.info(options)
            if not options['success']:
                logger.info(options['error'])
                self.my_webex_api_handler.create_message(
                    room_id=activity['target']['globalId'],
                    markdown=options['error'],
                    parent_id=activity['id']
                )
                self.doc(activity)
                return

            self.my_webex_api_handler.create_message(
                room_id=activity['target']['globalId'],
                text='Processing request...',
                parent_id=activity['id']
            )

        except BaseException:
            output = '<b>Command execution failed [%s]</b>\n\n%s' % (command_run_id, traceback.format_exc())
            return output

        logger.info(json.dumps(options, indent=4))

        try:
            start_time = int(time.time() * 1000)

            nexus_settings_handler = nexus_settings.NexusSettings(log_id=command_run_id)
            bot_output_handler = bot_output.NexusBotOutput(log_id=command_run_id)

            cache_enabled = nexus_settings_handler.is_nexus_cache_enabled()
            if options['cache'] is not None:
                cache_enabled = options['cache']

            device_handlers = []
            for device in options['device']:
                device_handler = nxapi.NxApi(
                    device['ip'],
                    device['username'],
                    device['password'],
                    name=device['name'],
                    log_id=command_run_id,
                    debug=False,
                    cache_enabled=cache_enabled
                )

                device_handlers.append(
                    device_handler
                )

                device_cache = device_handler.get_cache_commands_timestamp()
                device['cache_command'] = device_cache['command']
                device['cache_valid'] = device_cache['valid']

            output = ''
            output_html = ''
            output_view_html = {}

            view_output, view_output_html = bot_output_handler.print_devices(options['device'], title=True)
            if 'dev' in options['view']:
                output = output + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

            if view_output_html is not None:
                output_view_html['dev'] = view_output_html

            if options['cache'] is None or options['cache']:
                view_output, view_output_html = bot_output_handler.print_devices_cache(options['device'], title=True)
                if 'cache' in options['view']:
                    output = output + view_output
                    if view_output_html is not None:
                        output_html = output_html + view_output_html

                if view_output_html is not None:
                    output_view_html['cache'] = view_output_html

            if 'version' in options['view']:
                neighbors = []
                for device_handler in device_handlers:
                    device_neighbors = device_handler.get_versions()
                    if device_neighbors is not None:
                        neighbors = neighbors + device_neighbors

                view_output, view_output_html = bot_output_handler.print_versions(neighbors, title=True)
                output = output + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                if view_output_html is not None:
                    output_view_html['version'] = view_output_html

            if 'lldp' in options['view']:
                neighbors = []
                for device_handler in device_handlers:
                    device_neighbors = device_handler.get_lldps()
                    if device_neighbors is not None:
                        neighbors = neighbors + device_neighbors

                view_output, view_output_html = bot_output_handler.print_lldps(neighbors, title=True)
                output = output + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                if view_output_html is not None:
                    output_view_html['lldp'] = view_output_html

            if 'lacp' in options['view']:
                neighbors = []
                for device_handler in device_handlers:
                    device_neighbors = device_handler.get_lacps()
                    if device_neighbors is not None:
                        neighbors = neighbors + device_neighbors

                view_output, view_output_html = bot_output_handler.print_lacps(neighbors, title=True)
                output = output + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                if view_output_html is not None:
                    output_view_html['lacp'] = view_output_html

            if 'mac' in options['view']:
                neighbors = []
                for device_handler in device_handlers:
                    device_neighbors = device_handler.get_macs()
                    if device_neighbors is not None:
                        neighbors = neighbors + device_neighbors

                view_output, view_output_html = bot_output_handler.print_macs(neighbors, title=True)
                output = output + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                if view_output_html is not None:
                    output_view_html['mac'] = view_output_html

            logger.info('Commands executed')

            execution_time = int(time.time() * 1000) - start_time

            files = None
            filename = self.log_handler.bot_output(output, log_id=command_run_id)
            if filename is not None:
                files = [filename]

            output = bot_output_handler.my_output.sanitize_bot_output(
                output,
                output_html,
                self.url,
                execution_time=execution_time
            )

            if len(output_html) > 0:
                if len(options['view']) == 1:
                    self.log_handler.output_html(
                        bot_output_handler.my_output.wrap_bot_html_output(
                            output_view_html[options['view'][0]],
                            command='get nx %s' % (message),
                            view=output_view_html,
                            exclude_view=[options['view'][0]]
                        )
                    )

                if len(options['view']) > 1:
                    self.log_handler.output_html(
                        bot_output_handler.my_output.wrap_bot_html_output(
                            output_view_html['dev'],
                            command='get nx %s' % (message),
                            view=output_view_html,
                            exclude_view=['dev']
                        )
                    )

                for key in output_view_html:
                    self.log_handler.output_html(
                        bot_output_handler.my_output.wrap_bot_html_output(
                            output_view_html[key],
                            command='get nx %s' % (message),
                            view=output_view_html,
                            exclude_view=[key]
                        ),
                        filename='%s.html' % (key)
                    )

            logger.info('Output prepared')

        except BaseException:
            files = None
            output = '<b>Command execution failed [%s]</b>\n\n%s' % (command_run_id, traceback.format_exc())

        self.my_webex_api_handler.create_message(
            room_id=activity['target']['globalId'],
            markdown=output,
            parent_id=activity['id']
        )

        self.my_webex_api_handler.create_message(
            room_id=activity['target']['globalId'],
            parent_id=activity['id'],
            files=files
        )

        return
