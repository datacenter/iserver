import json
import time
import traceback
import requests

from lib import output_helper
from lib import log_helper
from lib import info_helper
from lib import ssh

from lib.nexus.cache import Cache
from lib.nexus.ws import WebSocket

from lib.nexus.cdp.main import Cdp
from lib.nexus.config.main import Config
from lib.nexus.feature.main import Feature
from lib.nexus.hardware.main import Hardware
from lib.nexus.interface.main import Interface
from lib.nexus.lacp.main import Lacp
from lib.nexus.lldp.main import Lldp
from lib.nexus.mac.main import Mac
from lib.nexus.mon.main import Mon
from lib.nexus.pc.main import Pc
from lib.nexus.server.main import Server
from lib.nexus.version.main import Version
from lib.nexus.vlan.main import Vlan
from lib.nexus.vpc.main import Vpc
from lib.nexus.vrf.main import Vrf


class NxApi(
        Cache,
        Cdp,
        Config,
        Feature,
        Hardware,
        Interface,
        Lacp,
        Lldp,
        Mac,
        Mon,
        Pc,
        Server,
        Version,
        Vlan,
        Vpc,
        Vrf,
        WebSocket
        ):
    def __init__(self, ip_address, username, password, nxapi, name=None, verbose=False, debug=False, log_id=None, cache_enabled=False, paranoid=False):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)
        self.log_id = log_id
        self.info_handler = info_helper.InfoHelper(log_id=log_id)

        self.nexus_name = name
        if self.nexus_name is None:
            self.nexus_name = ip_address
        self.nexus_ip = ip_address
        self.username = username
        self.password = password
        self.paranoid = paranoid
        self.nxapi = nxapi
        self.session_handler = None
        self.session_connected = False
        self.token = None
        self.debug = debug

        self.ssh_handler = None
        self.ssh_session = None

        Cache.__init__(self, cache_enabled)
        WebSocket.__init__(self, ip_address, debug=debug)

        Cdp.__init__(self)
        Config.__init__(self)
        Feature.__init__(self)
        Hardware.__init__(self)
        Interface.__init__(self)
        Lacp.__init__(self)
        Lldp.__init__(self)
        Mac.__init__(self)
        Mon.__init__(self)
        Pc.__init__(self)
        Server.__init__(self)
        Version.__init__(self)
        Vlan.__init__(self)
        Vpc.__init__(self)
        Vrf.__init__(self)

    def __del__(self):
        self.disconnect_nxapi()
        self.disconnect_ssh()

    def get_token(self):
        return self.token

    def connect(self):
        if not self.nxapi:
            return True

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
        if not self.nxapi:
            return True

        if not self.session_connected and autoconnect:
            return self.connect()

        return self.session_connected

    def disconnect_ssh(self):
        if self.ssh_handler is None:
            return True

        if self.ssh_session is None:
            return True

        start_time = int(time.time() * 1000)
        success = True
        try:
            self.ssh_session.close()
        except BaseException:
            self.log.error(
                'nxapi.disconnect_ssh',
                traceback.format_exc()
            )
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.nexus(
            'disconnect-ssh %s' % (self.nexus_ip),
            success,
            duration_ms
        )

        self.ssh_handler = None
        self.ssh_session = None

        return success

    def disconnect_nxapi(self):
        if not self.nxapi:
            return True

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

    def run_show_command(self, command, cast_json=True, autoconnect=False, attempts=3):
        if not self.nxapi or not cast_json:
            if self.ssh_handler is None:
                self.ssh_handler = ssh.Ssh(
                    self.nexus_ip,
                    self.username,
                    password = self.password,
                    log_id=self.log_id
                )
                self.ssh_session, exception_name, error = self.ssh_handler.create_session()

            attempt = 1
            while True:
                if cast_json:
                    success, output, error = self.ssh_handler.run_cmd(
                        '%s | json' % (command),
                        pre='terminal length 0',
                        timeout=60,
                        debug=self.debug,
                        paranoid=self.paranoid,
                        session=self.ssh_session
                    )
                else:
                    success, output, error = self.ssh_handler.run_cmd(
                        command,
                        pre='terminal length 0',
                        timeout=60,
                        debug=self.debug,
                        paranoid=self.paranoid,
                        session=self.ssh_session
                    )

                if not success:
                    self.log.error(
                        'run_show_command',
                        'Failed attempt %s: %s' % (self.nexus_ip, command)
                    )
                    self.log.error(
                        'run_show_command',
                        str(output)
                    )
                    self.log.error(
                        'run_show_command',
                        str(error)
                    )
                    if attempt > attempts:
                        self.log.error(
                            'run_show_command',
                            'Failed to run on %s: %s' % (self.nexus_ip, command)
                        )
                        return None

                    attempt += 1
                    continue

                if cast_json:
                    if len(output) == 0:
                        return {}

                    try:
                        return json.loads(output)
                    except BaseException:
                        if attempt > attempts:
                            self.log.error(
                                'run_show_command',
                                'Failed to cast output to json on %s: %s' % (self.nexus_ip, command)
                            )
                            self.log.error(
                                'run_show_command',
                                output
                            )
                            return None

                    attempt += 1
                    continue

                return output

        if not self.is_connected(autoconnect=autoconnect):
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
