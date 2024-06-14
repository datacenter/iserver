import copy
import json
import os
import traceback

from lib.settings_helper import Settings
from lib import output_helper

SSH_TIMEOUT = 3


class MyServers(Settings):
    def __init__(self):
        Settings.__init__(self)
        self.my_servers_filename = os.path.join(
            self.settings_dir,
            'my_servers'
        )
        self.my_output = None

    def clear_my_servers(self):
        return self.set_my_servers({})

    def is_my_servers(self):
        '''
        Returns True if $HOME/.itool/my_servers file exists
        Returns False otherwise
        '''
        return os.path.isfile(self.my_servers_filename)

    def initialize(self):
        '''
        If $HOME/.itool/my_servers does not exist, then save it with [] content
        Return True/False
        '''
        if not self.is_my_servers():
            return self.set_my_servers({})
        return True

    def get_serials(self):
        serials = {}
        my_servers = self.get_my_servers()
        if my_servers is None:
            return serials

        for group_name in my_servers:
            for server in my_servers[group_name]:
                if server['Serial'] not in serials:
                    serials[server['Serial']] = []
                serials[server['Serial']].append(group_name)

        return serials

    def get_my_servers(self):
        if self.is_my_servers():
            try:
                with open(self.my_servers_filename, 'r', encoding='utf-8') as file_handler:
                    values = json.loads(file_handler.read())

            except BaseException:
                self.log.error('my_servers_helper.get_my_servers', traceback.format_exc())
                return None

        return values

    def set_my_servers(self, my_servers):
        '''
        Returns True/False
        '''
        try:
            with open(self.my_servers_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(my_servers, indent=4))
        except BaseException:
            self.log.error('my_servers_helper.set_my_servers', traceback.format_exc())
            return False
        return True

    def is_group(self, group_name):
        '''
        True/False
        Checks group_name dict entry in my_servers
        '''
        my_servers = self.get_my_servers()
        if group_name in my_servers:
            return True
        return False

    def get_group(self, group_name):
        """Get group members

        Args:
            group_name (string): group name

        Returns:
            list: list of servers or None if group not found
        """
        my_servers = self.get_my_servers()
        if group_name in my_servers:
            return my_servers[group_name]
        return None

    def get_group_serials(self, group_name):
        """Get group members' serial list

        Args:
            group_name (string): group name

        Returns:
            list: list of serials
        """
        servers = self.get_group(group_name)
        if servers is None:
            return None

        serials = []
        for server in servers:
            serials.append(server['Serial'])

        return serials

    def add_group(self, group_name):
        """Add empty group

        Args:
            group_name (string): group name

        Return True if group already exists

        Returns:
            bool: success or failure
        """
        if self.is_group(group_name):
            return True

        my_servers = self.get_my_servers()
        if my_servers is None:
            return False

        my_servers[group_name] = []
        return self.set_my_servers(my_servers)

    def del_group(self, group_name):
        """Delete group with all servers

        Args:
            group_name (string): group name

        Return True if group does not exist

        Returns:
            bool: success or failure
        """
        if not self.is_group(group_name):
            return True

        my_servers = self.get_my_servers()
        if my_servers is None:
            return False

        del my_servers[group_name]
        return self.set_my_servers(my_servers)

    def is_group_server(self, group_name, server_serial):
        """Check if server serial is member of group

        Args:
            group_name (string): group name
            server_serial (string): serial number
        """
        my_servers = self.get_my_servers()
        if my_servers is None:
            return False

        if group_name not in my_servers:
            return False

        for server in my_servers[group_name]:
            if server['Serial'] == server_serial:
                return True

        return False

    def get_server_definition(self, server):
        """Get subset of the server properties to be stored in my_servers structure

        Args:
            server (dict): Full server description
        """

        attributes = {}
        for key in ['Name', 'Serial', 'Model', 'ManagementIp']:
            if key in server:
                attributes[key] = server[key]
            else:
                attributes[key] = None

        return attributes

    def add_group_servers(self, group_name, servers):
        """Add server to group

        Args:
            group_name (string): group name
            servers (list): list of server definitions

        If group does not exist, create it

        Returns:
            bool: success or failure
        """
        my_servers = self.get_my_servers()
        if my_servers is None:
            return False

        if group_name not in my_servers:
            my_servers[group_name] = []

        for server in servers:
            if not self.is_group_server(group_name, server['Serial']):
                my_servers[group_name].append(
                    self.get_server_definition(server)
                )

        return self.set_my_servers(my_servers)

    def add_group_server(self, group_name, server):
        return self.add_group_servers(group_name, [server])

    def set_group_servers(self, group_name, servers):
        """Set group with servers

        Args:
            group_name (string): group name
            servers (list): list of server definitions

        If group does not exist, create it

        Returns:
            bool: success or failure
        """
        my_servers = self.get_my_servers()
        if my_servers is None:
            return False

        my_servers[group_name] = []

        for server in servers:
            my_servers[group_name].append(
                self.get_server_definition(server)
            )

        return self.set_my_servers(my_servers)

    def set_group_server(self, group_name, server):
        return self.set_group_servers(group_name, [server])

    def del_group_servers(self, group_name, servers):
        """Delete servers from group

        Args:
            group_name (string): group name
            servers (list): list of server definitions

        If group does not exist, return True

        Returns:
            bool: success or failure
        """
        my_servers = self.get_my_servers()
        if my_servers is None:
            return False

        if group_name not in my_servers:
            return True

        current_members = copy.deepcopy(my_servers[group_name])
        my_servers[group_name] = []

        for server in servers:
            for current_member in current_members:
                add_server = True
                for server in servers:
                    if server['Serial'] == current_member['Serial']:
                        add_server = False
                        break

                if add_server:
                    my_servers[group_name].append(current_member)

        return self.set_my_servers(my_servers)

    def del_group_server(self, group_name, server):
        return self.del_group_servers(group_name, [server])

    def print_group(self, group_name):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper()

        servers = self.get_group(group_name)
        if servers is None:
            self.my_output.error('Group not found: %s' % (group_name))
            return

        sorted_servers = sorted(servers, key=lambda i: i['Name'])

        order = [
            'Name',
            'Serial',
            'Model',
            'ManagementIP'
        ]

        headers = [
            'Name',
            'Serial',
            'Model',
            'IP'
        ]

        self.my_output.my_table(
            sorted_servers,
            order=order,
            headers=headers,
            table=True
        )
