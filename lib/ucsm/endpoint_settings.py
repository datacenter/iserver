from lib import log_helper
from lib import output_helper

from lib.endpoint_helper import EndpointSettings
from lib.ucsm import manager
from lib.ucsm.power_modules import server as power_server
from lib.ucsm.power_modules import chassis as power_chassis
from lib.ucsm.thermal_modules import server as thermal_server
from lib.ucsm.thermal_modules import chassis as thermal_chassis


class UcsmEndpointSettings(EndpointSettings):
    def __init__(self, log_id=None):
        EndpointSettings.__init__(self, log_id=log_id)

        self.log = log_helper.Log(log_id=log_id)
        self.log_id = log_id
        self.my_output = None

    def get_ucsm_endpoint_id(self, ucsm_mo):
        return ucsm_mo['serial']

    def is_ucsm_endpoint(self, endpoint_id):
        if self.get_ucsm_endpoint_settings(endpoint_id) is None:
            return False
        return True

    def get_ucsm_endpoint_settings(self, endpoint_id):
        endpoint_settings = self.get_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return None

        if 'ucsm' in endpoint_settings:
            return endpoint_settings['ucsm']

        return None

    def set_ucsm_endpoint_settings(self, ucsm_mo, ucsm_manager):
        endpoint_id = self.get_ucsm_endpoint_id(
            ucsm_mo
        )

        endpoint_settings = self.get_endpoint_settings(
            endpoint_id
        )
        if endpoint_settings is None:
            endpoint_settings = {}
            endpoint_settings['endpoint_id'] = endpoint_id

        endpoint_settings['ucsm'] = {}
        endpoint_settings['ucsm']['mo_type'] = ucsm_mo['mo_type']
        endpoint_settings['ucsm']['ip'] = ucsm_manager['ip']
        endpoint_settings['ucsm']['username'] = ucsm_manager['username']
        endpoint_settings['ucsm']['password'] = ucsm_manager['password']

        return self.set_endpoint_settings(endpoint_id, endpoint_settings)

    def get_ucsm_endpoint_power_template(self, endpoint_id):
        endpoint_settings = self.get_ucsm_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return None

        ucsm_handler = manager.UcsManager(
            endpoint_settings['ip'],
            endpoint_settings['username'],
            endpoint_settings['password'],
            log_id=self.log_id
        )

        if not ucsm_handler.is_connected():
            self.log.error('get_ucsm_endpoint_power_template', 'Failed to connect to UCSM')
            return None

        chassis_id = ucsm_handler.get_chassis_id(
            chassis_serial=endpoint_id
        )
        if chassis_id is not None:
            chassis_info = ucsm_handler.get_chassis(
                chassis_id=chassis_id,
                power=True
            )
            return chassis_info['power_stats']

        blade_info = ucsm_handler.get_blade(
            blade_serial=endpoint_id,
            power=True
        )
        if blade_info is not None:
            return blade_info['power']

        return None

    def get_ucsm_endpoint_thermal_template(self, endpoint_id):
        endpoint_settings = self.get_ucsm_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return None

        ucsm_handler = manager.UcsManager(
            endpoint_settings['ip'],
            endpoint_settings['username'],
            endpoint_settings['password'],
            log_id=self.log_id
        )

        if not ucsm_handler.is_connected():
            self.log.error('get_ucsm_endpoint_power_template', 'Failed to connect to UCSM')
            return None

        chassis_id = ucsm_handler.get_chassis_id(
            chassis_serial=endpoint_id
        )
        if chassis_id is not None:
            chassis_info = ucsm_handler.get_chassis(
                chassis_id=chassis_id,
                thermal=True
            )
            return chassis_info['thermal_stats']

        blade_info = ucsm_handler.get_blade(
            blade_serial=endpoint_id,
            thermal=True
        )
        if blade_info is not None:
            return blade_info['thermal']

        return None

    def get_ucsm_endpoint_template(self, endpoint_id, template_name):
        if template_name == 'power':
            return self.get_ucsm_endpoint_power_template(endpoint_id)

        if template_name == 'thermal':
            return self.get_ucsm_endpoint_thermal_template(endpoint_id)

        return None

    def print_ucsm_endpoint_power_template(self, endpoint_id, data):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(
                log_id=self.log_id,
                verbose=False,
                debug=False
            )

        endpoint_settings = self.get_ucsm_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return

        if endpoint_settings['mo_type'] == 'blade':
            power_server_handler = power_server.ServerPower(
                log_id=self.log_id
            )
            power_server_handler.print_blade_power(
                data
            )

        if endpoint_settings['mo_type'] == 'chassis':
            power_server_handler = power_chassis.ChassisPower(
                log_id=self.log_id
            )
            power_server_handler.print_chassis_power(
                data
            )
            power_server_handler.print_chassis_psu(
                data
            )

    def print_ucsm_endpoint_thermal_template(self, endpoint_id, data):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(
                log_id=self.log_id,
                verbose=False,
                debug=False
            )

        endpoint_settings = self.get_ucsm_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return

        if endpoint_settings['mo_type'] == 'blade':
            power_server_handler = thermal_server.ServerThermal(
                log_id=self.log_id
            )
            power_server_handler.print_blade_thermal(
                data
            )

        if endpoint_settings['mo_type'] == 'chassis':
            power_server_handler = thermal_chassis.ChassisThermal(
                log_id=self.log_id
            )
            power_server_handler.print_chassis_thermal(
                data
            )

    def print_ucsm_endpoint_template(self, endpoint_id, template_name, data):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(
                log_id=self.log_id,
                verbose=False,
                debug=False
            )

        if template_name == 'power':
            self.print_ucsm_endpoint_power_template(endpoint_id, data)

        if template_name == 'thermal':
            self.print_ucsm_endpoint_thermal_template(endpoint_id, data)
