import json

from lib import ip_helper


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
        if not locator_filter:
            return True

        if server['LocatorLedOn']:
            return True

        return False

    def power_off_filter_match(self, server, power_off):
        if not power_off:
            return True

        if server['OperPowerState'] != 'on':
            return True

        return False

    def alarms_filter_match(self, server, alarms):
        if not alarms:
            return True

        if server['AlarmSummary']['Warning'] == 0 and server['AlarmSummary']['Critical'] == 0:
            return False

        return True

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

    def fan_filter_match(self, server, fan):
        if not fan:
            return True

        if not server['FanHealthy']:
            return True

        return False

    def psu_filter_match(self, server, psu):
        if not psu:
            return True

        if not server['PsuHealthy']:
            return True

        return False

    def pci_filter_match(self, server, pci_filter):
        if pci_filter == '':
            return True

        for item in pci_filter.split(','):
            for model in server['PciModels']:
                if item.lower() in model.lower():
                    return True

        return False

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

    def match_server(self, server, rules, base_match=False, debug_logs=False):
        if rules is None:
            return True

        if not self.ip_filter_match(server, rules['ip']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on IP %s' % (
                        server['Moid'],
                        rules['ip']
                    )
                )
            return False

        if not self.name_filter_match(server, rules['name']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on name %s' % (
                        server['Moid'],
                        rules['name']
                    )
                )
            return False

        if not self.model_filter_match(server, rules['model']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on model %s' % (
                        server['Moid'],
                        rules['model']
                    )
                )
            return False

        if not self.serial_filter_match(server, rules['serials']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on serial %s' % (
                        server['Moid'],
                        rules['serials']
                    )
                )
            return False

        # If match is based on the base server attributes, exit early
        if base_match:
            return True

        if not self.locator_filter_match(server, rules['locator']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on locator %s' % (
                        server['Moid'],
                        rules['locator']
                    )
                )
            return False

        if not self.power_off_filter_match(server, rules['power_off']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on power off %s' % (
                        server['Moid'],
                        rules['power_off']
                    )
                )
            return False

        if not self.alarms_filter_match(server, rules['alarms']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on alarms %s' % (
                        server['Moid'],
                        rules['alarms']
                    )
                )
            return False

        if not self.ucsm_filter_match(server, rules['ucsm']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on ucsm %s' % (
                        server['Moid'],
                        rules['ucsm']
                    )
                )
            return False

        if not self.disconnected_filter_match(server, rules['disconnected']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on disconnected %s' % (
                        server['Moid'],
                        rules['disconnected']
                    )
                )
            return False

        if not self.standalone_filter_match(server, rules['standalone']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on standalone %s' % (
                        server['Moid'],
                        rules['standalone']
                    )
                )
            return False

        if not self.fan_filter_match(server, rules['fan']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on fan %s' % (
                        server['Moid'],
                        rules['fan']
                    )
                )
            return False

        if not self.psu_filter_match(server, rules['psu']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on psu %s' % (
                        server['Moid'],
                        rules['psu']
                    )
                )
            return False

        if not self.pci_filter_match(server, rules['pci']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on pci %s' % (
                        server['Moid'],
                        rules['pci']
                    )
                )
            return False

        if not self.mac_filter_match(server, rules['mac']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on mac %s' % (
                        server['Moid'],
                        rules['mac']
                    )
                )
            return False

        if not self.cpu_filter_match(server, rules['cpu']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on cpu %s' % (
                        server['Moid'],
                        rules['cpu']
                    )
                )
            return False

        if not self.memory_filter_match(server, rules['memory']):
            if debug_logs:
                self.log.debug(
                    'compute_filter.match_server',
                    'Server %s match fails on memory %s' % (
                        server['Moid'],
                        rules['memory']
                    )
                )
            return False

        return True
