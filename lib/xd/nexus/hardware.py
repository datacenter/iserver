import copy
from lib.nexus import nxapi


class NexusHardware():
    def __init__(self):
        self.nexus_hardware = None
        self.nexus_hw = None

    def load_pre_nexus_hardware(self):
        self.nexus_hardware = self.get_pre_cache('nexus', 'hardware')
        if self.nexus_hardware is None:
            return False
        self.analyze_nexus_hardware()
        return True

    def set_post_nexus_hardware(self):
        return self.set_post_cache('nexus-hardware', self.nexus_hardware)

    def load_post_nexus_hardware(self):
        self.nexus_hardware = self.get_post_cache('nexus-hardware')
        if self.nexus_feature is None:
            return False
        self.analyze_nexus_hardware()
        return True

    def analyze_nexus_hardware(self):
        self.nexus_hw = {}

        for nexus_device_name in self.nexus_hardware:
            self.nexus_hw[nexus_device_name] = None

            hardware = self.nexus_hardware[nexus_device_name]
            if 'chassis' in hardware and hardware['chassis'] is not None:
                if 'model_num' in hardware['chassis']:
                    self.nexus_hw[nexus_device_name] = hardware['chassis']['model_num']

            if 'modules' in hardware and len(hardware['modules']) == 1:
                if 'model_num' in hardware['modules'][0]:
                    self.nexus_hw[nexus_device_name] = hardware['modules'][0]['model_num']

    def get_nexus_hardware(self):
        info = copy.deepcopy(self.nexus_hardware)
        return info

    def prepare_nexus_hardware(self, cache_enabled=True, nexus_devices=None):
        if nexus_devices is None:
            nexus_devices = self.get_nexus_devices()
            if nexus_devices is None or len(nexus_devices) == 0:
                return False

        self.nexus_hardware = {}

        success = True
        for nexus_device in nexus_devices:
            self.my_output.debug('Nexus hardware: %s' % (nexus_device['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if nexus_device['name'] in self.nexus_hardware:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('nexus-%s-hardware' % (nexus_device['name']))
                if cache is not None:
                    self.nexus_hardware[nexus_device['name']] = cache
                    self.my_output.debug('L3 Cache hit')
                    continue

            self.my_output.debug('Cache miss')

            if 'handler' in nexus_device:
                nexus_handler = nexus_device['handler']
            else:
                nexus_handler = nxapi.NxApi(
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

            hardware = nexus_handler.get_hardware()
            if hardware is None:
                self.my_output.error('Hardware failed: %s' % (nexus_device['name']))
                success = False
                continue

            self.nexus_hardware[nexus_device['name']] = hardware

            self.my_output.debug('Data collected')

            self.set_cache(
                'nexus-%s-hardware' % (nexus_device['name']),
                self.nexus_hardware[nexus_device['name']]
            )

            self.my_output.debug('Cache set')

        self.analyze_nexus_hardware()
        return success

    def run_nexus_hardware(self):
        if not self.set_post_nexus_hardware():
            return False

        return True

    def run_nexus_hardware_serial(self):
        for device_name in self.nexus_hardware:
            parent_sn = None

            if 'serial_num' in self.nexus_hardware[device_name]['chassis']:
                item = {}
                item['serial'] = self.nexus_hardware[device_name]['chassis']['serial_num']
                item['domain'] = self.domain_name
                item['scope'] = 'nexus'
                item['type'] = 'Nexus'
                item['description'] = self.nexus_hardware[device_name]['chassis']['model_num']
                item['parent'] = None

                self.serial.append(
                    item
                )

                parent_sn = self.nexus_hardware[device_name]['chassis']['serial_num']

            if parent_sn is None and len(self.nexus_hardware[device_name]['modules']) > 0:
                item = {}
                item['serial'] = self.nexus_hardware[device_name]['modules'][0]['serial_num']
                item['domain'] = self.domain_name
                item['scope'] = 'nexus'
                item['type'] = 'Nexus'
                item['description'] = self.nexus_hardware[device_name]['chassis_id']
                item['parent'] = None

                self.serial.append(
                    item
                )

                parent_sn = self.nexus_hardware[device_name]['modules'][0]['serial_num']

            for module in self.nexus_hardware[device_name]['modules']:
                if module['serial_num'] is None:
                    continue

                if module['serial_num'] == '':
                    continue

                if module['serial_num'].lower() == 'n/a':
                    continue

                if module['serial_num'] == parent_sn:
                    continue

                item = {}
                item['serial'] = module['serial_num']
                item['domain'] = self.domain_name
                item['scope'] = 'nexus'
                item['type'] = 'Module'
                item['description'] = '%s [%s]' % (
                    module['type'],
                    module['model_num']
                )
                item['parent'] = parent_sn

                self.serial.append(
                    item
                )

            for ps in self.nexus_hardware[device_name]['ps']:
                if 'serial_num' not in ps:
                    continue

                if ps['serial_num'] is None:
                    continue

                if ps['serial_num'] == '':
                    continue

                if ps['serial_num'].lower() == 'n/a':
                    continue

                item = {}
                item['serial'] = ps['serial_num']
                item['domain'] = self.domain_name
                item['scope'] = 'nexus'
                item['type'] = 'Power Supply'
                item['description'] = '%s [%s]' % (
                    ps['type'],
                    ps['model_num']
                )
                item['parent'] = parent_sn

                self.serial.append(
                    item
                )

        return True
