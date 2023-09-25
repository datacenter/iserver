import json
import time
import traceback
import requests

from lib import output_helper
from lib import log_helper

from lib.nexus.lldp import Lldp
from lib.nexus.cache import Cache
from lib.nexus.ws import WebSocket


class NxApi(Cache, Lldp, WebSocket):
    def __init__(self, ip_address, username, password, verbose=False, debug=False, log_id=None, cache_enabled=False):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)

        self.nexus_ip = ip_address
        self.username = username
        self.password = password

        self.session_handler = None
        self.session_connected = False
        self.token = None

        Lldp.__init__(self)
        Cache.__init__(self, cache_enabled)
        WebSocket.__init__(self, ip_address, debug=debug)

    def __del__(self):
        self.disconnect()

    def get_token(self):
        return self.token

    def connect(self):
        if self.session_handler is not None:
            return True

        self.session_handler = requests.session()
        self.session_handler.auth = (
            self.username,
            self.password
        )
        self.session_handler.verify = False
        self.session_handler.headers.update(
            {'Content-Type': 'application/json'}
        )

        data = {
            'ins_api': {
                'chunk': '0',
                'version': '1.0',
                'sid': '1',
                'input': 'show version',
                'type': 'cli_show',
                'output_format': 'json'
            }
        }

        start_time = int(time.time() * 1000)
        try:
            uri = 'https://%s/ins/' % (self.nexus_ip)
            response = self.session_handler.request(
                'post',
                uri,
                data=json.dumps(data)
            )
            if response.status_code == 200:
                self.session_connected = True
                self.token = self.session_handler.cookies.get_dict()['nxapi_auth']

        except BaseException:
            self.log.error(
                'nxapi.connect',
                traceback.format_exc()
            )
            self.session_connected = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.nexus(
            'connect %s' % (self.nexus_ip),
            self.session_connected,
            duration_ms
        )

        return self.session_connected

    def is_connected(self, autoconnect=False):
        if not self.session_connected and autoconnect:
            return self.connect()

        return self.session_connected

    def disconnect(self):
        if not self.session_connected:
            return True

        start_time = int(time.time() * 1000)
        success = True
        try:
            self.session_handler.close()
        except BaseException:
            self.log.error(
                'nxapi.disconnect',
                traceback.format_exc()
            )
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.nexus(
            'disconnect %s' % (self.nexus_ip),
            success,
            duration_ms
        )

        self.session_connected = False
        self.session_handler = None

        return success

    def run_show_command(self, command):
        if not self.is_connected():
            return None

        data = {
            'ins_api': {
                'chunk': '0',
                'version': '1.0',
                'sid': '1',
                'input': command,
                'type': 'cli_show',
                'output_format': 'json'
            }
        }

        start_time = int(time.time() * 1000)
        output = None
        success = False
        try:
            uri = 'https://%s/ins/' % (self.nexus_ip)
            response = self.session_handler.request(
                'post',
                uri,
                data=json.dumps(data)
            )
            if response.status_code == 200:
                output = response.json()['ins_api']['outputs']['output']['body']
                success = True
                self.log.nexus_cli(
                    self.nexus_ip,
                    command.replace(' ', '_'),
                    output
                )

        except BaseException:
            self.log.error(
                'nxapi.run_show_commnd',
                'Command failed: %s' % (command)
            )

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.nexus(
            '%s %s' % (self.nexus_ip, command),
            success,
            duration_ms
        )

        return output
