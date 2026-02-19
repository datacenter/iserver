from lib.nexus import settings as nexus_settings
from lib.nexus import nxapi

from lib.xd.nexus.cdp import NexusCdp
from lib.xd.nexus.configuration import NexusConfiguration
from lib.xd.nexus.feature import NexusFeature
from lib.xd.nexus.hardware import NexusHardware
from lib.xd.nexus.interface import NexusInterface
from lib.xd.nexus.lldp import NexusLldp
from lib.xd.nexus.mac import NexusMac
from lib.xd.nexus.pc import NexusPc
from lib.xd.nexus.server import NexusServer
from lib.xd.nexus.version import NexusVersion
from lib.xd.nexus.vlan import NexusVlan
from lib.xd.nexus.vpc import NexusVpc
from lib.xd.nexus.vrf import NexusVrf


class Nexus(
        NexusCdp,
        NexusConfiguration,
        NexusFeature,
        NexusHardware,
        NexusInterface,
        NexusLldp,
        NexusMac,
        NexusPc,
        NexusServer,
        NexusVersion,
        NexusVlan,
        NexusVpc,
        NexusVrf
    ):
    def __init__(self):
        NexusCdp.__init__(self)
        NexusConfiguration.__init__(self)
        NexusFeature.__init__(self)
        NexusHardware.__init__(self)
        NexusInterface.__init__(self)
        NexusLldp.__init__(self)
        NexusMac.__init__(self)
        NexusPc.__init__(self)
        NexusServer.__init__(self)
        NexusVersion.__init__(self)
        NexusVlan.__init__(self)
        NexusVpc.__init__(self)
        NexusVrf.__init__(self)

        self.paranoid = True

    def load_pre_nexus(self):
        if not self.load_pre_nexus_cdp():
            return False

        if not self.load_pre_nexus_configuration():
            return False

        if not self.load_pre_nexus_feature():
            return False

        if not self.load_pre_nexus_hardware():
            return False

        if not self.load_pre_nexus_transceiver():
            return False

        if not self.load_pre_nexus_interface_brief():
            return False

        if not self.load_pre_nexus_interface_state():
            return False

        if not self.load_pre_nexus_lldp():
            return False

        if not self.load_pre_nexus_mac():
            return False

        if not self.load_pre_nexus_pc_database():
            return False

        if not self.load_pre_nexus_pc_lb():
            return False

        if not self.load_pre_nexus_pc_state():
            return False

        if not self.load_pre_nexus_pc_traffic():
            return False

        if not self.load_pre_nexus_version():
            return False

        if not self.load_pre_nexus_vlan():
            return False

        if not self.load_pre_nexus_vpc_keepalive():
            return False

        if not self.load_pre_nexus_vpc_role():
            return False

        if not self.load_pre_nexus_vpc_state():
            return False

        if not self.load_pre_nexus_vrf():
            return False

        return True

    def get_nexus_devices(self):
        nexus_settings_handler = nexus_settings.NexusSettings(log_id=self.log_id)
        nexus_devices = nexus_settings_handler.get_nexus_domain_devices(self.domain_name)
        return nexus_devices

    def is_switch(self, device_name, port_id):
        for item in self.nexus_lldp:
            if item == device_name:
                for lldp in self.nexus_lldp[item]:
                    if lldp['l_port_id'] == port_id:
                        if 'Cisco Nexus Operating System (NX-OS)' in lldp['sys_desc']:
                            return True

                        if lldp['enabled_capability'] == 'B, R':
                            return True

        for item in self.nexus_cdp:
            if item == device_name:
                for cdp in self.nexus_cdp[item]:
                    if cdp['intf_id'] == port_id:
                        if 'router' in cdp['capability'] and 'switch' in cdp['capability']:
                            return True

                    if len(port_id.split('Eth')) == 2 and len(cdp['intf_id'].split('Ethernet')) == 2:
                        if cdp['intf_id'].split('Ethernet')[1] == port_id.split('Eth')[1]:
                            if 'router' in cdp['capability'] and 'switch' in cdp['capability']:
                                return True

        return False

    def prepare_nexus(self, cache_enabled=True, allow_partial=False, prepare_modules=None):
        success = True

        nexus_devices = self.get_nexus_devices()
        if nexus_devices is None or len(nexus_devices) == 0:
            return False

        for nexus_device in nexus_devices:
            nexus_device['handler'] = nxapi.NxApi(
                nexus_device['ip'],
                nexus_device['username'],
                nexus_device['password'],
                nexus_device['nxapi'],
                name=nexus_device['name'],
                log_id=self.log_id,
                cache_enabled=False,
                debug=True,
                paranoid=self.paranoid
            )

            self.my_output.debug('Get device outputs: %s' % (nexus_device['name']))

            if prepare_modules is None or 'config' in prepare_modules:
                if not self.prepare_nexus_configuration(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus configuration failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'version' in prepare_modules:
                if not self.prepare_nexus_version(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus version failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'hardware' in prepare_modules:
                if not self.prepare_nexus_hardware(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus hardware failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'interface' in prepare_modules:
                if not self.prepare_nexus_interface_state(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus interface state failed')
                    if not allow_partial:
                        return False

                if not self.prepare_nexus_interface_brief(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus interface brief failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'lldp' in prepare_modules:
                if not self.prepare_nexus_lldp(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus lldp failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'cdp' in prepare_modules:
                if not self.prepare_nexus_cdp(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus cdp failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'mac' in prepare_modules:
                if not self.prepare_nexus_mac_table(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus mac failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'optics' in prepare_modules:
                if not self.prepare_nexus_transceiver(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus optics failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'feature' in prepare_modules:
                if not self.prepare_nexus_feature(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus feature failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'pc' in prepare_modules:
                if not self.prepare_nexus_pc_database(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus port-channel database failed')
                    if not allow_partial:
                        return False

                if not self.prepare_nexus_pc_lb(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus port-channel lb failed')
                    if not allow_partial:
                        return False

                if not self.prepare_nexus_pc_state(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus port-channel state failed')
                    if not allow_partial:
                        return False

                if not self.prepare_nexus_pc_traffic(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus port-channel traffic failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'vlan' in prepare_modules:
                if not self.prepare_nexus_vlan(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus vlan failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'vpc' in prepare_modules:
                if not self.prepare_nexus_vpc_keepalive(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus vpc keepalive failed')
                    if not allow_partial:
                        return False

                if not self.prepare_nexus_vpc_role(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus vpc role failed')
                    if not allow_partial:
                        return False

                if not self.prepare_nexus_vpc_state(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus vpc state failed')
                    if not allow_partial:
                        return False

            if prepare_modules is None or 'vrf' in prepare_modules:
                if not self.prepare_nexus_vrf(cache_enabled=cache_enabled, nexus_devices=[nexus_device]):
                    success = False
                    self.my_output.error('Get nexus vrf failed')
                    if not allow_partial:
                        return False

            del nexus_device['handler']

        return success

    def run_nexus(self):
        self.my_output.debug('\t- config')
        if not self.run_nexus_configuration():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- feature')
        if not self.run_nexus_feature():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- hw')
        if not self.run_nexus_hardware():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- mac')
        if not self.run_nexus_mac_table():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- version')
        if not self.run_nexus_version():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- vlan')
        if not self.run_nexus_vlan():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- vrf')
        if not self.run_nexus_vrf():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- interface (independent)')
        if not self.run_nexus_interface_independent():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- cdp')
        if not self.run_nexus_cdp():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- lldp')
        if not self.run_nexus_lldp():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- server')
        if not self.run_nexus_server():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- pc')
        if not self.run_nexus_pc():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- vpc')
        if not self.run_nexus_vpc():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- interface (xd)')
        if not self.run_nexus_interface_xd():
            self.my_output.error('Failed')
            return False


        # 2nd run for augmented data
        self.my_output.debug('\t- pc (2nd run)')
        if not self.run_nexus_pc():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- vpc (2nd run)')
        if not self.run_nexus_vpc():
            self.my_output.error('Failed')
            return False

        return True

    def run_nexus_serial(self):
        if not self.run_nexus_hardware_serial():
            return False

        return True

    def run_nexus_mac(self):
        return True

    def load_post_nexus(self):
        if not self.load_post_nexus_cdp():
            return False

        if not self.load_post_nexus_configuration():
            return False

        if not self.load_post_nexus_feature():
            return False

        if not self.load_post_nexus_hardware():
            return False

        if not self.load_post_nexus_transceiver():
            return False

        if not self.load_post_nexus_interface_brief():
            return False

        if not self.load_post_nexus_interface_state():
            return False

        if not self.load_post_nexus_interface():
            return False

        if not self.load_post_nexus_lldp():
            return False

        if not self.load_post_nexus_mac():
            return False

        if not self.load_post_nexus_pc_database():
            return False

        if not self.load_post_nexus_pc_lb():
            return False

        if not self.load_post_nexus_pc_state():
            return False

        if not self.load_post_nexus_pc_traffic():
            return False

        if not self.load_post_nexus_version():
            return False

        if not self.load_post_nexus_vlan():
            return False

        if not self.load_post_nexus_vpc_keepalive():
            return False

        if not self.load_post_nexus_vpc_role():
            return False

        if not self.load_post_nexus_vpc_state():
            return False

        if not self.load_post_nexus_vrf():
            return False

        if not self.load_post_nexus_server():
            return False

        return True
