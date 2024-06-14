import os
import uuid
import time
import json
import traceback
import logging

from lib.webex_bot.models.command import Command
from lib.aci import settings as aci_settings
from lib.aci import bot_output
from lib.aci import apic
from lib import log_helper
from lib import ip_helper
from lib import file_helper

logger = logging.getLogger(__name__)


class GetAciCommand(Command):
    def __init__(self, my_webex_api_handler, url):
        super().__init__(
            command_keyword="get aci",
            help_message="get aci",
            card=None,
        )
        self.run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(self.run_id)
        self.log_handler.initialize()
        self.link = 'https://wwwin-github.cisco.com/emear-telcocloud/iserver/blob/master/doc/bot/GetAci.md'
        self.url = url
        logger.info('Command initialized: get aci [%s]', self.run_id[4:])

        self.my_webex_api_handler = my_webex_api_handler

    def help(self):
        output = 'Supported commands followed by controller names, device names and filtering options<br><br>'
        output = '%s- get aci apic<br>' % (output)
        output = '%s- get aci ep<br>' % (output)
        output = '%s- get aci lacp<br>' % (output)
        output = '%s- get aci lldp<br>' % (output)
        output = '%s- get aci node<br>' % (output)
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
                'GetAci.md'
            )
        )

        self.my_webex_api_handler.create_message(
            room_id=activity['target']['globalId'],
            parent_id=activity['id'],
            files=files
        )

    def parse_command(self, message, command_run_id):
        options = {}
        options['success'] = True
        options['error'] = ''
        options['view'] = []
        options['apic'] = []
        options['filter'] = {}
        options['cache'] = None

        words = message.split(' ')
        if len(words) == 0:
            options['success'] = False
            options['error'] = 'Cannot parse the command. Check <a href="%s">documnetation</a>.' % (self.link)
            return options

        # View

        for view_name in words:
            if view_name in ['apic', 'ep', 'node', 'lacp', 'lldp', 'cache']:
                if view_name not in options['view']:
                    options['view'].append(view_name)

        # Controller

        aci_settings_handler = aci_settings.ApicSettings(log_id=command_run_id)
        controller_names = []
        for controller_name in words:
            if controller_name not in ['apic', 'ep', 'node', 'lacp', 'lldp', 'cache', 'cache:on', 'cache:off']:
                if controller_name in controller_names:
                    continue

                if controller_name == 'apic:all':
                    controller_names = aci_settings_handler.get_apic_controller_names()
                    options['apic'] = aci_settings_handler.get_apic_controllers()

                if controller_name != 'dev:all':
                    if len(controller_name.split(':')) > 1:
                        continue

                    controller_names.append(controller_name)
                    controller_settings = aci_settings_handler.get_apic_controller(controller_name)
                    if controller_settings is None:
                        options['success'] = False
                        options['error'] = 'Unknown controller: %s' % (controller_name)
                        return options

                    options['apic'].append(
                        controller_settings
                    )

        if len(controller_names) == 0:
            if len(options['view']) == 1 and 'apic' in options['view']:
                options['apic'] = aci_settings_handler.get_apic_controllers()
            else:
                controller_names = aci_settings_handler.get_apic_controller_names()
                options['success'] = False
                options['error'] = 'Select at least one controller: %s' % (','.join(controller_names))
                return options

        # Filter

        for item in words:
            if item in controller_names:
                continue

            if item in options['view']:
                continue

            if item in ['cache:on', 'cache:off', 'apic:all']:
                continue

            if len(item.split(':')) == 1:
                options['success'] = False
                options['error'] = 'Filtering options should follow key:value format: %s. Check <a href="%s">documnetation</a>.' % (item, self.link)
                return options

            key = item.split(':')[0]
            value = ':'.join(item.split(':')[1:])

            if len(value) == 0:
                options['success'] = False
                options['error'] = 'Filtering options should follow key:value format: %s. Check <a href="%s">documnetation</a>.' % (item, self.link)
                return options

            if ip_helper.is_valid_ipv4_address(value) or ip_helper.is_valid_ipv4_cidr(value):
                options['filter'][key] = value
            else:
                items = value.split('/')
                new_items = []
                for item in items:
                    if item == '*':
                        new_items.append(item)
                        continue

                    item = '*%s*' % (item.replace('*', ''))
                    new_items.append(item)

                options['filter'][key] = '/'.join(new_items)

        for key in options['filter']:
            if key not in ['ap', 'bd', 'epg', 'mac', 'ip', 'subnet', 'tenant', 'vrf']:
                options['success'] = False
                options['error'] = 'Unsupported filter key: %s. Check <a href="%s">documnetation</a>.' % (key, self.link)
                return options

            if key == 'ip':
                if not ip_helper.is_valid_ipv4_address(options['filter'][key]):
                    options['success'] = False
                    options['error'] = 'Invalid ip value: %s. Check <a href="%s">documnetation</a>.' % (options['filter'][key], self.link)
                    return options

            if key == 'subnet':
                if not ip_helper.is_valid_ipv4_cidr(options['filter'][key]):
                    options['success'] = False
                    options['error'] = 'Invalid subnet value: %s. Check <a href="%s">documnetation</a>.' % (options['filter'][key], self.link)
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

        logger.info('Command execution: get aci [%s]', command_run_id[4:])

        try:
            message = message.strip().lower()
            logger.info('Message: [%s]', message)
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

            bot_output_handler = bot_output.ApicBotOutput(log_id=command_run_id)

            # Bot should always have cache enabled but can be per-command disabled by user
            no_cache = False
            if options['cache'] is not None and not options['cache']:
                no_cache = True

            apic_handlers = []
            for controller in options['apic']:
                apic_handlers.append(
                    apic.Apic(
                        controller['ip'],
                        controller['port'],
                        controller['username'],
                        controller['password'],
                        apic_name=controller['name'],
                        log_id=command_run_id,
                        debug=False,
                        no_cache=no_cache
                    )
                )

            output = ''
            output_html = ''
            output_view_html = {}

            if 'apic' in options['view']:
                view_output, view_output_html = bot_output_handler.print_apic_controllers(options['apic'])
                output = output + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                if view_output_html is not None:
                    output_view_html['apic'] = view_output_html

            if 'ep' in options['view']:
                endpoints = []
                endpoint_filter = []
                for key in ['bd', 'epg', 'mac', 'ip', 'subnet', 'tenant', 'vrf']:
                    if key in options['filter']:
                        endpoint_filter.append(
                            '%s:%s' % (
                                key,
                                options['filter'][key]
                            )
                        )

                for apic_handler in apic_handlers:
                    apic_endpoints = apic_handler.get_endpoints(
                        endpoint_filter
                    )
                    if apic_endpoints is not None:
                        endpoints = endpoints + apic_endpoints

                view_output, view_output_html = bot_output_handler.print_endpoints(endpoints, title=True)
                output = output + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                if view_output_html is not None:
                    output_view_html['ep'] = view_output_html

            if 'node' in options['view']:
                nodes = []
                for apic_handler in apic_handlers:
                    apic_nodes = apic_handler.get_nodes()
                    if apic_nodes is not None:
                        nodes = nodes + apic_nodes

                view_output, view_output_html = bot_output_handler.print_nodes(nodes, title=True)
                output = output + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                if view_output_html is not None:
                    output_view_html['node'] = view_output_html

            if 'lacp' in options['view']:
                instance = []
                interface = []
                for apic_handler in apic_handlers:
                    apic_nodes = apic_handler.get_nodes()
                    if apic_nodes is None:
                        continue

                    for apic_node in apic_nodes:
                        if apic_node['role'] == 'controller':
                            continue

                        proto_info = apic_handler.get_protocol_lacp(
                            apic_node['podId'],
                            apic_node['id'],
                            instance_info=True,
                            interface_info=True,
                            interface_filter=[]
                        )
                        if proto_info is None:
                            continue

                        instance.append(proto_info['instance'])
                        if 'interfaces' in proto_info and proto_info['interfaces'] is not None:
                            interface = interface + proto_info['interfaces']

                view_output, view_output_html = bot_output_handler.print_proto_lacp_instances(instance, title=True)
                if view_output_html is not None:
                    output_view_html['lacp instance'] = view_output_html

                view_output, view_output_html = bot_output_handler.print_proto_lacp_interfaces(interface, title=True)
                output = output + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                if view_output_html is not None:
                    output_view_html['lacp'] = view_output_html

                view_output, view_output_html = bot_output_handler.print_proto_lacp_interfaces_stats(interface, title=True)
                if view_output_html is not None:
                    output_view_html['lacp stats'] = view_output_html

            if 'lldp' in options['view']:
                instance = []
                stats = []
                adjacency = []
                for apic_handler in apic_handlers:
                    apic_nodes = apic_handler.get_nodes()
                    if apic_nodes is None:
                        continue

                    for apic_node in apic_nodes:
                        if apic_node['role'] == 'controller':
                            continue

                        proto_info = apic_handler.get_protocol_lldp(
                            apic_node['podId'],
                            apic_node['id'],
                            adjacency_filter=[],
                            instance_info=True,
                            stats_info=True,
                            adjacency_info=True
                        )
                        if proto_info is None:
                            continue

                        if 'instance' in proto_info and proto_info['instance'] is not None:
                            instance.append(proto_info['instance'])

                        if 'stats' in proto_info and proto_info['stats'] is not None:
                            stats.append(
                                proto_info['stats']
                            )

                        if 'adjacency' in proto_info and proto_info['adjacency'] is not None:
                            adjacency = adjacency + proto_info['adjacency']

                view_output, view_output_html = bot_output_handler.print_proto_lldp_instances(instance, title=True)
                if view_output_html is not None:
                    output_view_html['lldp instance'] = view_output_html

                view_output, view_output_html = bot_output_handler.print_proto_lldp_adjacency(adjacency, title=True)
                output = output + view_output
                if view_output_html is not None:
                    output_html = output_html + view_output_html

                if view_output_html is not None:
                    output_view_html['lldp'] = view_output_html

                view_output, view_output_html = bot_output_handler.print_proto_lldp_interfaces_stats(stats, title=True)
                if view_output_html is not None:
                    output_view_html['lldp stats'] = view_output_html

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
                self.log_handler.output_html(
                    bot_output_handler.my_output.wrap_bot_html_output(
                        output_view_html[options['view'][0]],
                        command='get aci %s' % (message),
                        view=output_view_html,
                        exclude_view=[options['view'][0]]
                    )
                )

            for key in output_view_html:
                self.log_handler.output_html(
                    bot_output_handler.my_output.wrap_bot_html_output(
                        output_view_html[key],
                        command='get aci %s' % (message),
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
