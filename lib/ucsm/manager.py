import time
import json

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.ucscoreutils import get_meta_info

from lib import output_helper
from lib import log_helper

from lib.ucsm.blade import Blade
from lib.ucsm.chassis import Chassis
from lib.ucsm.fi import Fi
from lib.ucsm.power import Power
from lib.ucsm.rack import Rack
from lib.ucsm.thermal import Thermal
from lib.ucsm.networking.main import Networking


class UcsManager(
        Blade,
        Chassis,
        Fi,
        Networking,
        Power,
        Rack,
        Thermal
    ):
    def __init__(self, ucsm_ip, username, password, verbose=False, debug=False, log_id=None):
        Blade.__init__(self)
        Chassis.__init__(self)
        Fi.__init__(self)
        Networking.__init__(self)
        Power.__init__(self)
        Rack.__init__(self)
        Thermal.__init__(self)

        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)

        self.ucsm_ip = ucsm_ip
        self.ucsm_username = username
        self.ucsm_password = password

        self.session_handler = None
        self.session_connected = False
        self.connect()

    def __del__(self):
        self.disconnect()

    def debug_object(self, managed_object):
        self.log.debug('debug_object', str(managed_object))
        self.log.debug('debug_object', json.dumps(dir(managed_object), indent=4))
        meta = get_meta_info(managed_object.get_class_id())
        if meta is not None:
            self.log.debug('debug_object', meta)

    def is_connected(self):
        return self.session_connected

    def connect(self):
        if self.session_handler is not None:
            return True

        start_time = int(time.time() * 1000)
        self.session_handler = UcsHandle(
            self.ucsm_ip,
            self.ucsm_username,
            self.ucsm_password
        )

        try:
            self.session_connected = self.session_handler.login()
        except BaseException:
            self.session_connected = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.ucsm(
            'connect %s' % (self.ucsm_ip),
            self.session_connected,
            duration_ms
        )

        return self.session_connected

    def disconnect(self):
        if self.session_handler is None:
            return True

        if not self.session_connected:
            return True

        start_time = int(time.time() * 1000)
        try:
            if self.session_handler.logout():
                self.session_connected = False
                success = True
        except BaseException:
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.ucsm(
            'disconnect %s' % (self.ucsm_ip),
            success,
            duration_ms
        )

        return False

    def query_classid(self, class_id):
        if not self.is_connected():
            return None

        start_time = int(time.time() * 1000)
        managed_objects = self.session_handler.query_classid(
            class_id
        )

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.ucsm(
            '%s:%s' % (self.ucsm_ip, class_id),
            True,
            duration_ms
        )

        return managed_objects

    def get_fabric(self):
        fabric = {}
        fabric['vlan'] = self.get_fabric_vlan()
        fabric['pooledVlan'] = self.get_fabric_pooled_vlan()
        fabric['netGroup'] = self.get_fabric_net_group()
        fabric['ethLanPc'] = self.get_fabric_eth_lan_pc()
        fabric['ethLanPcEp'] = self.get_fabric_eth_lan_pc_ep()
        fabric['ethVlanPc'] = self.get_fabric_eth_vlan_pc()
        return fabric

    def get_inventory(self):
        inventory = {}
        inventory['Chassis'] = self.get_chassiz()
        inventory['Blades'] = self.get_blades()
        return inventory

    def print_inventory(self, inventory):
        self.print_chassiz(inventory['Chassis'])
        self.print_blades(inventory['Blades'])
