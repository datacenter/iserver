from lib import ip_helper
from lib import filter_helper


class ComputeFilter():
    """Class for server filtering
    """
    def __init__(self):
        pass

    def ip_filter_match(self, server, ip_filter):
        if len(ip_filter) == 0:
            return True

        if 'KvmIpAddresses' in server:
            for kvm_ip in server['KvmIpAddresses']:
                if kvm_ip['ClassId'] == 'compute.IpAddress':
                    for item in ip_filter:
                        if item['type'] == 'address':
                            if kvm_ip['Address'] == item['value']:
                                return True

                        if item['type'] == 'subnet':
                            if ip_helper.is_ipv4_in_cidr(kvm_ip['Address'], item['value']):
                                return True

        if 'ManagementIp' in server:
            for item in ip_filter:
                if item['type'] == 'address':
                    if server['ManagementIp'] == item['value']:
                        return True

                if item['type'] == 'subnet':
                    if ip_helper.is_ipv4_in_cidr(server['ManagementIp'], item['value']):
                        return True

        return False

    def name_filter_match(self, server, name_filter):
        if name_filter == '':
            return True

        for item in name_filter.split(','):
            if item.lower() in server['Name'].lower():
                return True

        return False

    def model_filter_match(self, server, model_filter):
        if model_filter == '':
            return True

        for item in model_filter.split(','):
            if item.lower() in server['Model'].lower():
                return True

        return False

    def locator_filter_match(self, server, locator_filter):
        if locator_filter == 'any':
            return True

        if locator_filter == 'on' and server['LocatorLedOn']:
            return True

        if locator_filter == 'off' and not server['LocatorLedOn']:
            return True

        return False

    def power_filter_match(self, server, power_filter):
        if power_filter == 'any':
            return True

        if power_filter == 'on' and server['OperPowerState'] == 'on':
            return True

        if power_filter == 'off' and server['OperPowerState'] != 'on':
            return True

        return False

    def alarms_filter_match(self, server, alarm_severity):
        # ['any', 'info', 'warn', 'crit']
        if alarm_severity == 'any':
            return True

        if alarm_severity == 'info':
            if server['AlarmSummary']['Critical'] > 0 or server['AlarmSummary']['Warning'] > 0 or server['AlarmSummary']['Info'] > 0:
                return True

        if alarm_severity == 'warn':
            if server['AlarmSummary']['Critical'] > 0 or server['AlarmSummary']['Warning'] > 0:
                return True

        if alarm_severity == 'crit':
            if server['AlarmSummary']['Critical'] > 0:
                return True

        return False

    def ucsm_filter_match(self, server, ucsm):
        if not ucsm:
            return True

        if server['ManagementMode'] == 'UCSM':
            return True

        return False

    def disconnected_filter_match(self, server, disconnected):
        if not disconnected:
            return True

        if not server['Connected']:
            return True

        return False

    def standalone_filter_match(self, server, standalone):
        if not standalone:
            return True

        if server['ManagementMode'] != 'UCSM':
            return True

        return False

    def serial_filter_match(self, server, serials):
        if len(serials) == 0:
            return True

        if server['Serial'] in serials:
            return True

        return False

    def ancestor_filter_match(self, server, ancestors):
        if len(ancestors) == 0:
            return True

        if 'Ancestors' not in server:
            return False

        if len(server['Ancestors']) == 0:
            return False

        for ancestor in server['Ancestors']:
            if ancestor['ObjectType'] == 'equipment.Chassis':
                for ancestor_moid in ancestors:
                    if ancestor_moid == ancestor['Moid']:
                        return True

        return False

    def fan_filter_match(self, server, fan):
        if not fan:
            return True

        if 'FanHealthy' not in server:
            return False

        if not server['FanHealthy']:
            return True

        return False

    def psu_filter_match(self, server_info, psu_filters):
        if len(psu_filters) == 0:
            return True

        if 'PsuInfo' not in server_info:
            return False

        for psu_filter in psu_filters:
            if len(psu_filter.split(':')) != 2:
                self.log_handler.error(
                    'psu_filter_match',
                    'Unsupported psu filter: %s' % (psu_filter)
                )
                return False

            (key, value) = psu_filter.split(':')

            if key not in ['state', 'model', 'serial']:
                self.log_handler.error(
                    'psu_filter_match',
                    'Unsupported psu filter key: %s' % (key)
                )
                return False

        any_psu_match = False
        for psu_info in server_info['PsuInfo']:
            psu_match = True

            for psu_filter in psu_filters:
                (key, value) = psu_filter.split(':')

                if key == 'state':
                    if value not in ['on', 'off']:
                        self.log_handler.error(
                            'psu_filter_match',
                            'Unsupported psu state filter value: %s' % (value)
                        )
                        return False

                    if value == 'on' and not psu_info['On']:
                        psu_match = False

                    if value == 'off' and psu_info['On']:
                        psu_match = False

                if key == 'model':
                    if not filter_helper.match_string(value, psu_info['Model']):
                        psu_match = False

                if key == 'serial':
                    if not filter_helper.match_string(value, psu_info['Serial']):
                        psu_match = False

            any_psu_match = any_psu_match or psu_match

        return any_psu_match

    def pci_filter_match(self, server, pci_filter):
        if pci_filter == '':
            return True

        for item in pci_filter.split(','):
            for model in server['PciSearch']:
                if item.lower() in model.lower():
                    return True

        return False

    def pci_match(self, server, pci_filter):
        if pci_filter == '':
            return server

        devices_info = []
        for device_info in server['PciDevicesInfo']:
            if device_info['Model'] is not None and len(device_info['Model']) > 0:
                if filter_helper.match_string(filter_helper.format_subtring_match(pci_filter), device_info['Model']):
                    devices_info.append(device_info)
                    continue

            if device_info['Pid'] is not None and len(device_info['Pid']) > 0:
                if device_info['Pid'].lower() not in ['unknown', 'n/a']:
                    if filter_helper.match_string(filter_helper.format_subtring_match(pci_filter), device_info['Pid']):
                        devices_info.append(device_info)
                        continue

        server['PciDevicesInfo'] = devices_info
        return server

    def mac_filter_match(self, server, mac_filter):
        if mac_filter == '':
            return True

        for item in mac_filter.split(','):
            item = item.replace(':', '').replace('.', '').lower()
            for mac_info in server['MacAddressInfo']:
                mac_address = mac_info['MacAddress'].replace(':', '').replace('.', '').lower()
                if item in mac_address:
                    return True

        return False

    def cpu_filter_match(self, server, cpu_filter):
        if cpu_filter == '':
            return True

        if cpu_filter.startswith('>='):
            if server['NumCpuCores'] >= int(cpu_filter.lstrip('>=')):
                return True
            return False

        if cpu_filter.startswith('ge'):
            if server['NumCpuCores'] >= int(cpu_filter.lstrip('ge')):
                return True
            return False

        if cpu_filter.startswith('<='):
            if server['NumCpuCores'] <= int(cpu_filter.lstrip('<=')):
                return True
            return False

        if cpu_filter.startswith('le'):
            if server['NumCpuCores'] <= int(cpu_filter.lstrip('le')):
                return True
            return False

        if cpu_filter.startswith('>'):
            if server['NumCpuCores'] > int(cpu_filter.lstrip('>')):
                return True
            return False

        if cpu_filter.startswith('gt'):
            if server['NumCpuCores'] > int(cpu_filter.lstrip('gt')):
                return True
            return False

        if cpu_filter.startswith('<'):
            if server['NumCpuCores'] < int(cpu_filter.lstrip('<')):
                return True
            return False

        if cpu_filter.startswith('lt'):
            if server['NumCpuCores'] < int(cpu_filter.lstrip('lt')):
                return True
            return False

        if cpu_filter.startswith('!='):
            if server['NumCpuCores'] != int(cpu_filter.lstrip('!=')):
                return True
            return False

        if cpu_filter.startswith('ne'):
            if server['NumCpuCores'] != int(cpu_filter.lstrip('ne')):
                return True
            return False

        if server['NumCpuCores'] == int(cpu_filter):
            return True

        return False

    def memory_filter_match(self, server, memory_filter):
        if memory_filter == '':
            return True

        if memory_filter.startswith('>='):
            if server['TotalMemoryGB'] >= int(memory_filter.lstrip('>=')):
                return True
            return False

        if memory_filter.startswith('ge'):
            if server['TotalMemoryGB'] >= int(memory_filter.lstrip('ge')):
                return True
            return False

        if memory_filter.startswith('<='):
            if server['TotalMemoryGB'] <= int(memory_filter.lstrip('<=')):
                return True
            return False

        if memory_filter.startswith('le'):
            if server['TotalMemoryGB'] <= int(memory_filter.lstrip('le')):
                return True
            return False

        if memory_filter.startswith('>'):
            if server['TotalMemoryGB'] > int(memory_filter.lstrip('>')):
                return True
            return False

        if memory_filter.startswith('gt'):
            if server['TotalMemoryGB'] > int(memory_filter.lstrip('gt')):
                return True
            return False

        if memory_filter.startswith('<'):
            if server['TotalMemoryGB'] < int(memory_filter.lstrip('<')):
                return True
            return False

        if memory_filter.startswith('lt'):
            if server['TotalMemoryGB'] < int(memory_filter.lstrip('lt')):
                return True
            return False

        if memory_filter.startswith('!='):
            if server['TotalMemoryGB'] != int(memory_filter.lstrip('!=')):
                return True
            return False

        if memory_filter.startswith('ne'):
            if server['TotalMemoryGB'] != int(memory_filter.lstrip('ne')):
                return True
            return False

        if server['TotalMemoryGB'] == int(memory_filter):
            return True

        return False

    def match_server(self, server, rules, base_match=False, debug_logs=True):
        if rules is None:
            return server

        if 'ancestor' in rules:
            if not self.ancestor_filter_match(server, rules['ancestor']):
                if debug_logs:
                    self.log_handler.debug(
                        'compute_filter.match_server',
                        'Server %s match fails on ancestor %s' % (
                            server['Moid'],
                            rules['ancestor']
                        )
                    )
                return None

        # If match is based on the base server attributes, exit early
        if base_match:
            return server

        if not self.locator_filter_match(server, rules['locator']):
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on locator %s' % (
                        server['Moid'],
                        rules['locator']
                    )
                )
            return None

        if not self.power_filter_match(server, rules['power']):
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on power off %s' % (
                        server['Moid'],
                        rules['power']
                    )
                )
            return None

        if not self.alarms_filter_match(server, rules['alarms']):
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on alarms %s' % (
                        server['Moid'],
                        rules['alarms']
                    )
                )
            return None

        if not self.ucsm_filter_match(server, rules['ucsm']):
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on ucsm %s' % (
                        server['Moid'],
                        rules['ucsm']
                    )
                )
            return None

        if not self.disconnected_filter_match(server, rules['disconnected']):
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on disconnected %s' % (
                        server['Moid'],
                        rules['disconnected']
                    )
                )
            return None

        if not self.standalone_filter_match(server, rules['standalone']):
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on standalone %s' % (
                        server['Moid'],
                        rules['standalone']
                    )
                )
            return None

        if not self.fan_filter_match(server, rules['fan']):
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on fan %s' % (
                        server['Moid'],
                        rules['fan']
                    )
                )
            return None

        if not self.psu_filter_match(server, rules['psu']):
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on psu %s' % (
                        server['Moid'],
                        rules['psu']
                    )
                )
            return None

        pci_match = self.pci_filter_match(server, rules['pci'])
        if not pci_match:
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on pci %s' % (
                        server['Moid'],
                        rules['pci']
                    )
                )
            return None

        server = self.pci_match(server, rules['pci'])

        if not self.mac_filter_match(server, rules['mac']):
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on mac %s' % (
                        server['Moid'],
                        rules['mac']
                    )
                )
            return None

        if not self.cpu_filter_match(server, rules['cpu']):
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on cpu %s' % (
                        server['Moid'],
                        rules['cpu']
                    )
                )
            return None

        if not self.memory_filter_match(server, rules['memory']):
            if debug_logs:
                self.log_handler.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on memory %s' % (
                        server['Moid'],
                        rules['memory']
                    )
                )
            return None

        return server

    def ip_filter_match_mo(self, server_mo, ip_filter):
        if server_mo['ManagementIp'] is None:
            return False

        for item in ip_filter:
            if item['type'] == 'address':
                if server_mo['ManagementIp'] == item['value']:
                    return True

            if item['type'] == 'subnet':
                if ip_helper.is_ipv4_in_cidr(server_mo['ManagementIp'], item['value']):
                    return True

        return False

    def name_filter_match_mo(self, server_mo, name_filter):
        for item in name_filter:
            if '*' in item:
                if filter_helper.match_string(item, server_mo['Name']):
                    return True
            if '*' not in item:
                if item.lower() in server_mo['Name'].lower():
                    return True
        return False

    def model_filter_match_mo(self, server_mo, model_filter):
        for item in model_filter:
            if '*' in item:
                if filter_helper.match_string(item, server_mo['Model']):
                    return True
            if '*' not in model_filter:
                if item.lower() in server_mo['Model'].lower():
                    return True
        return False

    def serial_filter_match_mo(self, server_mo, serials):
        for item in serials:
            if '*' in item:
                if filter_helper.match_string(item, server_mo['Serial']):
                    return True
            if '*' not in item:
                if server_mo['Serial'] == item:
                    return True
        return False

    def match_server_mo(self, server_mo, match_rules):
        if match_rules is None:
            return True

        if 'ip' in match_rules and len(match_rules['ip']) > 0:
            if not self.ip_filter_match_mo(server_mo, match_rules['ip']):
                return False

        if 'name' in match_rules and len(match_rules['name']) > 0:
            if not self.name_filter_match_mo(server_mo, match_rules['name']):
                return False

        if 'model' in match_rules and len(match_rules['model']) > 0:
            if not self.model_filter_match_mo(server_mo, match_rules['model']):
                return False

        if 'serial' in match_rules and len(match_rules['serial']) > 0:
            if not self.serial_filter_match_mo(server_mo, match_rules['serial']):
                return False

        return True

    def get_mo_match_rules(self, ip_filter=None, name_filter=None, serial_filter=None, model_filter=None):
        match_rules = {}
        match_rules['ip'] = []
        match_rules['name'] = []
        match_rules['serial'] = []
        match_rules['model'] = []

        if ip_filter is not None and len(ip_filter) > 0:
            for ip_filter_entry in ip_filter:
                if ip_helper.is_valid_ipv4_address(ip_filter_entry):
                    match_rules['ip'].append(
                        dict(
                            type='address',
                            value=ip_filter_entry
                        )
                    )
                    continue

                if ip_helper.is_valid_ipv4_cidr(ip_filter_entry):
                    match_rules['ip'].append(
                        dict(
                            type='subnet',
                            value=ip_filter_entry
                        )
                    )
                    continue

                ip_address = ip_helper.get_ip(ip_filter_entry)
                if ip_address is not None:
                    match_rules['ip'].append(
                        dict(
                            type='address',
                            value=ip_address
                        )
                    )
                    continue

                self.log_handler.error(
                    'get_mo_match_rules',
                    'Invalid ip entry: %s' % (ip_filter_entry)
                )

        if name_filter is not None and len(name_filter) > 0:
            for item in name_filter:
                match_rules['name'].append(item)

        if serial_filter is not None and len(serial_filter) > 0:
            for item in serial_filter:
                match_rules['serial'].append(item)

        if model_filter is not None and len(model_filter) > 0:
            for item in model_filter:
                match_rules['model'].append(item)

        return match_rules
