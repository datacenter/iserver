import json
import os
import traceback

from lib.settings_helper import Settings

SSH_TIMEOUT = 3


class MyServer(Settings):
    def __init__(self):
        Settings.__init__(self)
        self.my_server_filename = os.path.join(
            self.settings_dir,
            'my_server'
        )

    def clear_my_server(self):
        return self.set_my_server([])

    def is_my_server(self):
        '''
        Returns True if $HOME/.itool/my_server file exists
        Returns False otherwise
        '''
        return os.path.isfile(self.my_server_filename)

    def initialize(self):
        '''
        If $HOME/.iwectl/my_server does not exist, then save it with [] content
        Return True/False
        '''
        if not self.is_my_server():
            return self.set_my_server([])
        return True

    def get_my_server_names(self, iaccount):
        '''
            [
                "milan-kali",
                "milan-kali-bgp"
            ]
        '''
        try:
            clusters = self.get_my_server()
            if clusters is not None:
                names = []
                for cluster in clusters:
                    if cluster['iaccount'] == iaccount:
                        names.append(cluster['cluster_name'])
                return names

        except BaseException:
            self.log.error('my_server_helper.get_my_server_names', traceback.format_exc())

        return None

    def get_my_server(self):
        '''
            [
                {
                    "iaccount": "isctl",
                    "cluster_name": "milan-kali"
                },
                {
                    "iaccount": "isctl",
                    "cluster_name": "milan-kali-bgp"
                }
            ]
        '''
        if self.is_my_server():
            try:
                with open(self.my_server_filename, 'r', encoding='utf-8') as file_handler:
                    values = json.loads(file_handler.read())

                if len(values) > 0:
                    values = sorted(values, key=lambda i: (i['iaccount'], i['cluster_name']))

                return values

            except BaseException:
                self.log.error('my_server_helper.get_my_server', traceback.format_exc())

        return None

    def set_my_server(self, my_server):
        '''
        Returns True/False
        '''
        try:
            with open(self.my_server_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(my_server, indent=4))
        except BaseException:
            self.log.error('my_server_helper.set_my_server', traceback.format_exc())
            return False
        return True

    def is_my_cluster(self, iaccount, cluster_name):
        '''
        True/False
        Checks (iaccount, cluster_name) entry in my_server json
        '''
        my_server = self.get_my_server()
        for my_cluster in my_server:
            if my_cluster['iaccount'] == iaccount and my_cluster['cluster_name'] == cluster_name:
                return True
        return False

    def add(self, iaccount, cluster_name):
        if self.is_my_cluster(iaccount, cluster_name):
            return True, None

        my_server = self.get_my_server()
        my_server.append(
            dict(
                iaccount=iaccount,
                cluster_name=cluster_name
            )
        )
        success = self.set_my_server(my_server)
        response = None
        if not success:
            response = 'Failed to write my_server file'
        return success, response

    def delete(self, iaccount, cluster_name):
        my_server = self.get_my_server()
        new_my_server = []
        for my_cluster in my_server:
            if my_cluster['iaccount'] == iaccount and my_cluster['cluster_name'] == cluster_name:
                continue
            new_my_server.append(my_cluster)
        success = self.set_my_server(new_my_server)
        response = None
        if not success:
            response = 'Failed to write my_server file'
        return success, response
