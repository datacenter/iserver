from lib.ucsm import settings as ucsm_settings
from lib.xd.ucsm.blade import UcsmBlade
from lib.xd.ucsm.chassis import UcsmChassis
from lib.xd.ucsm.fabric import UcsmFabric
from lib.xd.ucsm.fi import UcsmFi
from lib.xd.ucsm.rack import UcsmRack


class Ucsm(UcsmBlade, UcsmChassis, UcsmFabric, UcsmFi, UcsmRack):
    def __init__(self):
        self.ucsm = {}
        UcsmBlade.__init__(self)
        UcsmChassis.__init__(self)
        UcsmFabric.__init__(self)
        UcsmFi.__init__(self)
        UcsmRack.__init__(self)

    def load_pre_ucsm(self):
        if not self.load_pre_ucsm_blade():
            return False

        if not self.load_pre_ucsm_chassis():
            return False

        if not self.load_pre_ucsm_fabric():
            return False

        if not self.load_pre_ucsm_fi():
            return False

        if not self.load_pre_ucsm_rack():
            return False

        return True

    def get_server_ucsm_name(self, serial):
        ucsm_name = self.get_blade_ucsm_name(serial)
        if ucsm_name is not None:
            return ucsm_name

        ucsm_name = self.get_rack_ucsm_name(serial)
        if ucsm_name is not None:
            return ucsm_name

        return None

    def prepare_ucsm_instances(self):
        ucsm_settings_handler = ucsm_settings.UcsmSettings(log_id=self.log_id)

        ucsm_instances = ucsm_settings_handler.get_ucsm_domain_managers(self.domain_name)
        if ucsm_instances is None:
            return False

        for ucsm_instance in ucsm_instances:
            self.ucsm[ucsm_instance['name']] = ucsm_instance

        return True

    def get_ucsm_handlers(self):
        ucsm_settings_handler = ucsm_settings.UcsmSettings(log_id=self.log_id)
        ucsm_instances = ucsm_settings_handler.get_ucsm_domain_managers(self.domain_name)
        return ucsm_instances

    def prepare_ucsm(self, allow_partial=False):
        success = True

        self.my_output.debug('Get ucsm access...')
        if not self.prepare_ucsm_instances():
            self.my_output.error('Get ucsm instances failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get ucsm blades with net info...')
        if not self.prepare_ucsm_blade():
            self.my_output.error('Get ucsm blades failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get ucsm chassis with net info...')
        if not self.prepare_ucsm_chassis():
            self.my_output.error('Get ucsm chassis failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get ucsm racks with net info...')
        if not self.prepare_ucsm_rack():
            self.my_output.error('Get ucsm racks failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get ucsm fi with net info...')
        if not self.prepare_ucsm_fi():
            self.my_output.error('Get ucsm fi failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get ucsm fabric...')
        if not self.prepare_ucsm_fabric():
            self.my_output.error('Get ucsm fabric failed')
            success = False
            if not allow_partial:
                return False

        return success

    def run_ucsm(self):
        self.my_output.debug('\t- fabric')
        if not self.run_ucsm_fabric():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- blade')
        if not self.run_ucsm_blade():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- rack')
        if not self.run_ucsm_rack():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- chassis')
        if not self.run_ucsm_chassis():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- fi')
        if not self.run_ucsm_fi():
            self.my_output.error('Failed')
            return False

        return True

    def run_ucsm_serial(self):
        if not self.run_ucsm_chassis_serial():
            return False

        return True

    def run_ucsm_mac(self):
        return True

    def load_post_ucsm(self):
        if not self.load_post_ucsm_blade():
            return False

        if not self.load_post_ucsm_chassis():
            return False

        if not self.load_post_ucsm_fabric():
            return False

        if not self.load_post_ucsm_fi():
            return False

        if not self.load_post_ucsm_rack():
            return False

        return True
