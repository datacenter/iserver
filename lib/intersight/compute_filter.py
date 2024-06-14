from lib import ip_helper
from lib import filter_helper


class ComputeFilter():
    """Class for server filtering
    """
    def __init__(self):
        pass

    def int_filter_match(self, value, filter_rule):
        if filter_rule.startswith('>='):
            if value >= int(filter_rule.lstrip('>=')):
                return True
            return False

        if filter_rule.startswith('ge'):
            if value >= int(filter_rule.lstrip('ge')):
                return True
            return False

        if filter_rule.startswith('<='):
            if value <= int(filter_rule.lstrip('<=')):
                return True
            return False

        if filter_rule.startswith('le'):
            if value <= int(filter_rule.lstrip('le')):
                return True
            return False

        if filter_rule.startswith('>'):
            if value > int(filter_rule.lstrip('>')):
                return True
            return False

        if filter_rule.startswith('gt'):
            if value > int(filter_rule.lstrip('gt')):
                return True
            return False

        if filter_rule.startswith('<'):
            if value < int(filter_rule.lstrip('<')):
                return True
            return False

        if filter_rule.startswith('lt'):
            if value < int(filter_rule.lstrip('lt')):
                return True
            return False

        if filter_rule.startswith('!='):
            if value != int(filter_rule.lstrip('!=')):
                return True
            return False

        if filter_rule.startswith('ne'):
            if value != int(filter_rule.lstrip('ne')):
                return True
            return False

        if value == int(filter_rule):
            return True

        return False

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

        if server['Connected']:
            return False

        return True

    def imm_filter_match(self, server, imm):
        if not imm:
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

    def cpu_filter_match(self, server, cpu_filter):
        for key in cpu_filter:
            if key == 'core':
                if not self.int_filter_match(server['NumCpuCores'], cpu_filter[key]):
                    return False

            if key == 'socket':
                if not self.int_filter_match(server['NumCpus'], cpu_filter[key]):
                    return False

            if key == 'thread':
                if not self.int_filter_match(server['NumThreads'], cpu_filter[key]):
                    return False

            if key == 'vendor':
                found = False
                if 'CpuInfo' not in server:
                    return False

                for cpu_info in server['CpuInfo']:
                    if cpu_info['VendorName'] == cpu_filter[key]:
                        found = True

                if not found:
                    return False

            if key == 'arch':
                found = False
                if 'CpuInfo' not in server:
                    return False

                for cpu_info in server['CpuInfo']:
                    if cpu_info['Architecture'].lower() == cpu_filter[key].lower():
                        found = True

                if not found:
                    return False

            if key == 'model':
                found = False
                if 'CpuInfo' not in server:
                    return False

                for cpu_info in server['CpuInfo']:
                    if cpu_filter[key].lower() in cpu_info['Model'].lower():
                        found = True

                if not found:
                    return False

        return True

    def cpu_match(self, server, cpu_filter):
        if 'CpuInfo' in server:
            for cpu_info in server['CpuInfo']:
                cpu_info['__show'] = True
                if 'model' in cpu_filter:
                    if cpu_info['Model'] is None:
                        cpu_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(cpu_filter['model']), cpu_info['Model']):
                        cpu_info['__show'] = False
                        continue

                if 'serial' in cpu_filter:
                    if cpu_info['Serial'] is None:
                        cpu_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(cpu_filter['serial']), cpu_info['Serial']):
                        cpu_info['__show'] = False
                        continue

                if 'arch' in cpu_filter:
                    if cpu_info['Architecture'] is None:
                        cpu_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(cpu_filter['arch']), cpu_info['Architecture']):
                        cpu_info['__show'] = False
                        continue

        return server

    def gpu_filter_match(self, server, gpu_filter):
        for key in gpu_filter:
            if key == 'slot':
                if not self.int_filter_match(len(server['GpuInfo']), gpu_filter[key]):
                    return False

            if key == 'model':
                found = False
                if 'GpuInfo' not in server:
                    return False

                for gpu_info in server['GpuInfo']:
                    if gpu_filter[key].lower() in gpu_info['Model'].lower():
                        found = True

                if not found:
                    return False

        return True

    def gpu_match(self, server, gpu_filter):
        if 'GpuInfo' in server:
            for gpu_info in server['GpuInfo']:
                gpu_info['__show'] = True
                if 'model' in gpu_filter:
                    if gpu_info['Model'] is None:
                        gpu_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(gpu_filter['model']), gpu_info['Model']):
                        gpu_info['__show'] = False
                        continue

        return server

    def memory_filter_match(self, server, memory_filter):
        for key in memory_filter:
            if key == 'size':
                if not self.int_filter_match(server['TotalMemoryGB'], memory_filter[key]):
                    return False

            if key == 'dimm':
                if 'MemoryInfo' not in server:
                    return False

                count = 0
                for memory_info in server['MemoryInfo']:
                    if memory_info['Presence'] == 'equipped':
                        count = count + 1

                if not self.int_filter_match(count, memory_filter[key]):
                    return False

            if key == 'model':
                found = False
                if 'MemoryInfo' not in server:
                    return False

                for memory_info in server['MemoryInfo']:
                    if memory_info['Model'] is not None:
                        if memory_filter[key].lower() in memory_info['Model'].lower():
                            found = True

                if not found:
                    return False

            if key == 'serial':
                found = False
                if 'MemoryInfo' not in server:
                    return False

                for memory_info in server['MemoryInfo']:
                    if memory_info['Serial'] is not None:
                        if memory_filter[key].lower() in memory_info['Serial'].lower():
                            found = True

                if not found:
                    return False

        return True

    def mem_match(self, server, memory_filter):
        if 'MemoryInfo' in server:
            for memory_info in server['MemoryInfo']:
                memory_info['__show'] = True
                if 'model' in memory_filter:
                    if memory_info['Model'] is None:
                        memory_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(memory_filter['model']), memory_info['Model']):
                        memory_info['__show'] = False
                        continue

                if 'serial' in memory_filter:
                    if memory_info['Serial'] is None:
                        memory_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(memory_filter['serial']), memory_info['Serial']):
                        memory_info['__show'] = False
                        continue

        return server

    def pci_filter_match(self, server, pci_filter):
        for key in pci_filter:
            if key == 'slot':
                if 'PciDevicesInfo' not in server:
                    return False

                if not self.int_filter_match(len(server['PciDevicesInfo']), pci_filter[key]):
                    return False

            if key == 'model':
                found = False
                if 'PciDevicesInfo' not in server:
                    return False

                for pci_info in server['PciDevicesInfo']:
                    if pci_info['Model'] is not None:
                        if pci_filter[key].lower() in pci_info['Model'].lower():
                            found = True

                if not found:
                    return False

            if key == 'pid':
                found = False
                if 'PciDevicesInfo' not in server:
                    return False

                for pci_info in server['PciDevicesInfo']:
                    if pci_info['Pid'] is not None:
                        if pci_filter[key].lower() in pci_info['Pid'].lower():
                            found = True

                if not found:
                    return False

        return True

    def pci_match(self, server, pci_filter):
        for device_info in server['PciDevicesInfo']:
            device_info['__show'] = True
            if 'model' in pci_filter:
                if device_info['Model'] is None:
                    device_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['model']), device_info['Model']):
                    device_info['__show'] = False
                    continue

            if 'pid' in pci_filter:
                if device_info['Pid'] is None:
                    device_info['__show'] = False
                    continue

                if device_info['Pid'].lower() in ['unknown', 'n/a']:
                    device_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['pid']), device_info['Pid']):
                    device_info['__show'] = False
                    continue

        for device_info in server['PciNodesInfo']:
            device_info['__show'] = True
            if 'model' in pci_filter:
                if device_info['Model'] is None:
                    device_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['model']), device_info['Model']):
                    device_info['__show'] = False
                    continue

            if 'pid' in pci_filter:
                if device_info['Pid'] is None:
                    device_info['__show'] = False
                    continue

                if device_info['Pid'].lower() in ['unknown', 'n/a']:
                    device_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['pid']), device_info['Pid']):
                    device_info['__show'] = False
                    continue

        if 'CimcInfo' in server:
            for interface_info in server['CimcInfo']:
                interface_info['__show'] = False

        if 'ExtEthInfo' in server:
            for interface_info in server['ExtEthInfo']:
                interface_info['__show'] = True
                if 'model' in pci_filter:
                    if interface_info['AdapterModel'] is None:
                        interface_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['model']), interface_info['AdapterModel']):
                        interface_info['__show'] = False
                        continue

                if 'pid' in pci_filter:
                    if interface_info['Pid'] is None:
                        interface_info['__show'] = False
                        continue

                    if interface_info['Pid'].lower() in ['unknown', 'n/a']:
                        interface_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['pid']), interface_info['Pid']):
                        interface_info['__show'] = False
                        continue

        if 'HostEthInfo' in server:
            for interface_info in server['HostEthInfo']:
                interface_info['__show'] = True
                if 'model' in pci_filter:
                    if interface_info['AdapterModel'] is None:
                        interface_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['model']), interface_info['AdapterModel']):
                        interface_info['__show'] = False
                        continue

                if 'pid' in pci_filter:
                    if interface_info['Pid'] is None:
                        interface_info['__show'] = False
                        continue

                    if interface_info['Pid'].lower() in ['unknown', 'n/a']:
                        interface_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['pid']), interface_info['Pid']):
                        interface_info['__show'] = False
                        continue

        if 'HostFcInfo' in server:
            for interface_info in server['HostFcInfo']:
                interface_info['__show'] = True
                if 'model' in pci_filter:
                    if interface_info['AdapterModel'] is None:
                        interface_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['model']), interface_info['AdapterModel']):
                        interface_info['__show'] = False
                        continue

                if 'pid' in pci_filter:
                    if interface_info['Pid'] is None:
                        interface_info['__show'] = False
                        continue

                    if interface_info['Pid'].lower() in ['unknown', 'n/a']:
                        interface_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['pid']), interface_info['Pid']):
                        interface_info['__show'] = False
                        continue

        if 'AdaptersInfo' in server:
            for adapter_info in server['AdaptersInfo']:
                adapter_info['__show'] = True
                if 'model' in pci_filter:
                    if adapter_info['Model'] is None:
                        adapter_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['model']), adapter_info['Model']):
                        adapter_info['__show'] = False
                        continue

                if 'pid' in pci_filter:
                    if adapter_info['Pid'] is None:
                        adapter_info['__show'] = False
                        continue

                    if adapter_info['Pid'].lower() in ['unknown', 'n/a']:
                        adapter_info['__show'] = False
                        continue

                    if not filter_helper.match_string(filter_helper.format_subtring_match(pci_filter['pid']), adapter_info['Pid']):
                        adapter_info['__show'] = False
                        continue

        return server

    def mac_filter_match(self, server, mac_filter):
        if isinstance(mac_filter, str):
            mac_filter = [mac_filter]

        if len(mac_filter) == 0:
            return True

        for mac_item in mac_filter:
            for item in mac_item.split(','):
                for mac_info in server['MacAddressInfo']:
                    if filter_helper.match_mac(item, mac_info['MacAddress']):
                        return True

        return False

    def mac_match(self, server, mac_filter):
        if isinstance(mac_filter, str):
            mac_filter = [mac_filter]

        if len(mac_filter) == 0:
            return server

        if 'ExtEthInfo' in server:
            for interface_info in server['ExtEthInfo']:
                interface_info['__show'] = True

                found = False
                for mac_item in mac_filter:
                    for item in mac_item.split(','):
                        if filter_helper.match_mac(item, interface_info['MacAddress']):
                            found = True

                if not found:
                    interface_info['__show'] = False

        if 'HostEthInfo' in server:
            for interface_info in server['HostEthInfo']:
                interface_info['__show'] = True

                found = False
                for mac_item in mac_filter:
                    for item in mac_item.split(','):
                        if filter_helper.match_mac(item, interface_info['MacAddress']):
                            found = True

                if not found:
                    interface_info['__show'] = False

        if 'HostFcInfo' in server:
            for interface_info in server['HostFcInfo']:
                interface_info['__show'] = True

                found = False
                for mac_item in mac_filter:
                    for item in mac_item.split(','):
                        if filter_helper.match_wwn(item, interface_info['Wwnn']) and not filter_helper.match_wwn(item, interface_info['Wwpn']):
                            found = True

                if not found:
                    interface_info['__show'] = False

        return server

    def sc_filter_match(self, server, sc_filter):
        for key in sc_filter:
            if key == 'serial':
                found = False
                if 'StorageControllerInfo' not in server:
                    return False

                for sc_info in server['StorageControllerInfo']:
                    if sc_info['Serial'] is not None:
                        if sc_filter[key].lower() in sc_info['Serial'].lower():
                            found = True

                if not found:
                    return False

            if key == 'vendor':
                found = False
                if 'StorageControllerInfo' not in server:
                    return False

                for sc_info in server['StorageControllerInfo']:
                    if sc_info['Vendor'] is not None:
                        if sc_filter[key].lower() in sc_info['Vendor'].lower():
                            found = True

                if not found:
                    return False

        return True

    def sc_match(self, server, sc_filter):
        for sc_info in server['StorageControllerInfo']:
            sc_info['__show'] = True
            if 'serial' in sc_filter:
                if sc_info['Serial'] is None:
                    sc_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(sc_filter['serial']), sc_info['Serial']):
                    sc_info['__show'] = False
                    continue

            if 'vendor' in sc_filter:
                if sc_info['Vendor'] is None:
                    sc_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(sc_filter['vendor']), sc_info['Vendor']):
                    sc_info['__show'] = False
                    continue

        return server

    def pd_filter_match(self, server, pd_filter):
        for key in pd_filter:
            if key == 'count':
                if 'PhysicalDiskInfo' not in server:
                    return False

                if not self.int_filter_match(len(server['PhysicalDiskInfo']), pd_filter[key]):
                    return False

            if key == 'type':
                found = False
                if 'PhysicalDiskInfo' not in server:
                    return False

                for pd_info in server['PhysicalDiskInfo']:
                    if pd_info['Type'] is not None:
                        if pd_filter[key].lower() in pd_info['Type'].lower():
                            found = True

                if not found:
                    return False

            if key == 'proto':
                found = False
                if 'PhysicalDiskInfo' not in server:
                    return False

                for pd_info in server['PhysicalDiskInfo']:
                    if pd_info['Protocol'] is not None:
                        if pd_filter[key].lower() in pd_info['Protocol'].lower():
                            found = True

                if not found:
                    return False

            if key == 'pid':
                found = False
                if 'PhysicalDiskInfo' not in server:
                    return False

                for pd_info in server['PhysicalDiskInfo']:
                    if pd_info['Pid'] is not None:
                        if pd_filter[key].lower() in pd_info['Pid'].lower():
                            found = True

                if not found:
                    return False

            if key == 'model':
                found = False
                if 'PhysicalDiskInfo' not in server:
                    return False

                for pd_info in server['PhysicalDiskInfo']:
                    if pd_info['Model'] is not None:
                        if pd_filter[key].lower() in pd_info['Model'].lower():
                            found = True

                if not found:
                    return False

            if key == 'vendor':
                found = False
                if 'PhysicalDiskInfo' not in server:
                    return False

                for pd_info in server['PhysicalDiskInfo']:
                    if pd_info['Vendor'] is not None:
                        if pd_filter[key].lower() in pd_info['Vendor'].lower():
                            found = True

                if not found:
                    return False

            if key == 'serial':
                found = False
                if 'PhysicalDiskInfo' not in server:
                    return False

                for pd_info in server['PhysicalDiskInfo']:
                    if pd_info['Serial'] is not None:
                        if pd_filter[key].lower() in pd_info['Serial'].lower():
                            found = True

                if not found:
                    return False

        return True

    def pd_match(self, server, pd_filter):
        for pd_info in server['PhysicalDiskInfo']:
            pd_info['__show'] = True
            if 'type' in pd_filter:
                if pd_info['Type'] is None:
                    pd_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(pd_filter['type']), pd_info['Type']):
                    pd_info['__show'] = False
                    continue

            if 'proto' in pd_filter:
                if pd_info['Protocol'] is None:
                    pd_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(pd_filter['proto']), pd_info['Protocol']):
                    pd_info['__show'] = False
                    continue

            if 'pid' in pd_filter:
                if pd_info['Pid'] is None:
                    pd_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(pd_filter['pid']), pd_info['Pid']):
                    pd_info['__show'] = False
                    continue

            if 'model' in pd_filter:
                if pd_info['Model'] is None:
                    pd_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(pd_filter['model']), pd_info['Model']):
                    pd_info['__show'] = False
                    continue

            if 'vendor' in pd_filter:
                if pd_info['Vendor'] is None:
                    pd_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(pd_filter['vendor']), pd_info['Vendor']):
                    pd_info['__show'] = False
                    continue

            if 'serial' in pd_filter:
                if pd_info['Serial'] is None:
                    pd_info['__show'] = False
                    continue

                if not filter_helper.match_string(filter_helper.format_subtring_match(pd_filter['serial']), pd_info['Serial']):
                    pd_info['__show'] = False
                    continue

        return server

    def vd_filter_match(self, server, vd_filter):
        for key in vd_filter:
            if key == 'count':
                if 'VirtualDisks' not in server:
                    return False

                if not self.int_filter_match(len(server['VirtualDisks']), vd_filter[key]):
                    return False

        return True

    def fan_filter_match(self, server, fan_filter):
        for key in fan_filter:
            if key == 'mod':
                if 'FanModuleInfo' not in server:
                    return False

                count = 0
                for module_info in server['FanModuleInfo']:
                    if module_info['Presence'] == 'equipped':
                        count = count + 1

                if not self.int_filter_match(count, fan_filter[key]):
                    return False

            if key == 'unit':
                if 'FanInfo' not in server:
                    return False

                count = 0
                for fan_info in server['FanInfo']:
                    if fan_info['Presence'] == 'equipped':
                        count = count + 1

                if not self.int_filter_match(count, fan_filter[key]):
                    return False

            if key == 'state':
                if 'FanHealthy' not in server:
                    return False

                if fan_filter['state'] == 'ok' and not server['FanHealthy']:
                    return False

                if fan_filter['state'] == 'nok' and server['FanHealthy']:
                    return False

        return True

    def fan_match(self, server, fan_filter):
        for fan_info in server['FanInfo']:
            fan_info['__show'] = True
            if 'state' in fan_filter:
                if fan_filter['state'] == 'ok' and not fan_info['On']:
                    fan_info['__show'] = False
                    continue

                if fan_filter['state'] == 'nok' and fan_info['On']:
                    fan_info['__show'] = False
                    continue

        return server

    def psu_filter_match(self, server_info, psu_filter):
        for key in psu_filter:
            if key == 'state':
                if 'PsuHealthy' not in server_info:
                    return False

                if psu_filter['state'] == 'ok' and not server_info['PsuHealthy']:
                    return False

                if psu_filter['state'] == 'nok' and server_info['PsuHealthy']:
                    return False

            if key == 'model':
                found = False
                if 'PsuInfo' not in server_info:
                    return False

                for psu_info in server_info['PsuInfo']:
                    if psu_info['Model'] is not None:
                        if psu_filter[key].lower() in psu_info['Model'].lower():
                            found = True

                if not found:
                    return False

            if key == 'serial':
                found = False
                if 'PsuInfo' not in server_info:
                    return False

                for psu_info in server_info['PsuInfo']:
                    if psu_info['Serial'] is not None:
                        if psu_filter[key].lower() in psu_info['Serial'].lower():
                            found = True

                if not found:
                    return False

            if key == 'vendor':
                found = False
                if 'PsuInfo' not in server_info:
                    return False

                for psu_info in server_info['PsuInfo']:
                    if psu_info['Vendor'] is not None:
                        if psu_filter[key].lower() in psu_info['Vendor'].lower():
                            found = True

                if not found:
                    return False

        return True

    def psu_match(self, server, psu_filter):
        for psu_info in server['PsuInfo']:
            psu_info['__show'] = True
            if 'state' in psu_filter:
                if psu_filter['state'] == 'ok' and not psu_info['On']:
                    psu_info['__show'] = False
                    continue

                if psu_filter['state'] == 'nok' and psu_info['On']:
                    psu_info['__show'] = False
                    continue

            if 'model' in psu_filter:
                if psu_info['Model'] is None:
                    psu_info['__show'] = False
                    continue

                if psu_info['Model'] is not None and psu_filter['model'].lower() not in psu_info['Model'].lower():
                    psu_info['__show'] = False
                    continue

            if 'serial' in psu_filter:
                if psu_info['Serial'] is None:
                    psu_info['__show'] = False
                    continue

                if psu_info['Serial'] is not None and psu_filter['serial'].lower() not in psu_info['Serial'].lower():
                    psu_info['__show'] = False
                    continue

            if 'vendor' in psu_filter:
                if psu_info['Vendor'] is None:
                    psu_info['__show'] = False
                    continue

                if psu_info['Vendor'] is not None and psu_filter['vendor'].lower() not in psu_info['Vendor'].lower():
                    psu_info['__show'] = False
                    continue

        return server

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

        if 'locator' in rules:
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

        if 'power' in rules:
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

        if 'alarms' in rules:
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

        if 'ucsm' in rules:
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

        if 'disconnected' in rules:
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

        if 'imm' in rules:
            if not self.imm_filter_match(server, rules['imm']):
                if debug_logs:
                    self.log_handler.debug(
                        'compute_filter.match_server',
                        'Server %s match fails on imm %s' % (
                            server['Moid'],
                            rules['imm']
                        )
                    )
                return None

        if 'cpu' in rules and rules['cpu']['enabled']:
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

            server = self.cpu_match(server, rules['cpu'])

        if 'gpu' in rules and rules['gpu']['enabled']:
            if not self.gpu_filter_match(server, rules['gpu']):
                if debug_logs:
                    self.log_handler.debug(
                        'compute_filter.match_server',
                        'Server %s match fails on gpu %s' % (
                            server['Moid'],
                            rules['gpu']
                        )
                    )
                return None

            server = self.gpu_match(server, rules['gpu'])

        if 'memory' in rules and rules['memory']['enabled']:
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

            server = self.mem_match(server, rules['memory'])

        if 'pci' in rules and rules['pci']['enabled']:
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

        if 'mac' in rules:
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

            server = self.mac_match(server, rules['mac'])

        if 'sc' in rules and rules['sc']['enabled']:
            sc_match = self.sc_filter_match(server, rules['sc'])
            if not sc_match:
                if debug_logs:
                    self.log_handler.debug(
                        'compute_filter.match_server',
                        'Server %s match fails on storage controller %s' % (
                            server['Moid'],
                            rules['sc']
                        )
                    )
                return None

            server = self.sc_match(server, rules['sc'])

        if 'pd' in rules and rules['pd']['enabled']:
            pd_match = self.pd_filter_match(server, rules['pd'])
            if not pd_match:
                if debug_logs:
                    self.log_handler.debug(
                        'compute_filter.match_server',
                        'Server %s match fails on physical disk %s' % (
                            server['Moid'],
                            rules['pd']
                        )
                    )
                return None

            server = self.pd_match(server, rules['pd'])

        if 'vd' in rules and rules['vd']['enabled']:
            vd_match = self.vd_filter_match(server, rules['vd'])
            if not vd_match:
                if debug_logs:
                    self.log_handler.debug(
                        'compute_filter.match_server',
                        'Server %s match fails on virtual drive %s' % (
                            server['Moid'],
                            rules['vd']
                        )
                    )
                return None

        if 'fan' in rules and rules['fan']['enabled']:
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

            server = self.fan_match(server, rules['fan'])

        if 'psu' in rules and rules['psu']['enabled']:
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

            server = self.psu_match(server, rules['psu'])

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

    def name_filter_match_mo(self, server_mo, name_rules, logical):
        if logical == 'and':
            names_match = True

        if logical == 'or':
            names_match = False

        for name_rule in name_rules:
            name_match = False

            if isinstance(name_rule, dict):
                if not name_rule['negative']:
                    if filter_helper.match_string(name_rule['value'], server_mo['Name']):
                        name_match = True

                if name_rule['negative']:
                    name_found = False
                    if filter_helper.match_string(name_rule['value'], server_mo['Name']):
                        name_found = True

                    name_match = not name_found

            if isinstance(name_rule, str):
                if filter_helper.match_string(name_rule, server_mo['Name']):
                    name_match = True

            if logical == 'and':
                names_match = names_match and name_match

            if logical == 'or':
                names_match = names_match or name_match

        return names_match

    def model_filter_match_mo(self, server_mo, model_rules, logical):
        if logical == 'and':
            models_match = True

        if logical == 'or':
            models_match = False

        for model_rule in model_rules:
            model_match = False

            if isinstance(model_rule, dict):
                if not model_rule['negative']:
                    if filter_helper.match_string(model_rule['value'], server_mo['Model']):
                        model_match = True

                if model_rule['negative']:
                    model_found = False
                    if filter_helper.match_string(model_rule['value'], server_mo['Model']):
                        model_found = True

                    model_match = not model_found

            if isinstance(model_rule, str):
                if filter_helper.match_string(model_rule, server_mo['Model']):
                    model_match = True

            if logical == 'and':
                models_match = models_match and model_match

            if logical == 'or':
                models_match = models_match or model_match

        return models_match

    def serial_filter_match_mo(self, server_mo, serial_rules, logical):
        if logical == 'and':
            serials_match = True

        if logical == 'or':
            serials_match = False

        for serial_rule in serial_rules:
            serial_match = False

            if isinstance(serial_rule, dict):
                if not serial_rule['negative']:
                    if filter_helper.match_string(serial_rule['value'], server_mo['Serial']):
                        serial_match = True

                if serial_rule['negative']:
                    serial_found = False
                    if filter_helper.match_string(serial_rule['value'], server_mo['Serial']):
                        serial_found = True

                    serial_match = not serial_found

            if isinstance(serial_rule, str):
                if filter_helper.match_string(serial_rule, server_mo['Serial']):
                    serial_match = True

            if logical == 'and':
                serials_match = serials_match and serial_match

            if logical == 'or':
                serials_match = serials_match or serial_match

        return serials_match

    def tag_filter_match_mo(self, server_mo, tag_rules, logical):
        if logical == 'and':
            tags_match = True

        if logical == 'or':
            tags_match = False

        for tag_rule in tag_rules:
            tag_match = False

            if isinstance(tag_rule, dict):
                if not tag_rule['negative']:
                    if tag_rule['key'] == '_count_':
                        if len(server_mo['Tags']) - 1 == int(tag_rule['value']):
                            tag_match = True

                    if tag_rule['key'] != '_count_':
                        for tag_mo in server_mo['Tags']:
                            if tag_mo['Key'] == 'Intersight.LicenseTier':
                                continue

                            if filter_helper.match_string(tag_rule['key'], tag_mo['Key']):
                                if filter_helper.match_string(tag_rule['value'], tag_mo['Value']):
                                    tag_match = True
                                    break

                if tag_rule['negative']:
                    tag_found = False

                    for tag_mo in server_mo['Tags']:
                        if tag_mo['Key'] == 'Intersight.LicenseTier':
                            continue

                        if filter_helper.match_string(tag_rule['key'], tag_mo['Key']):
                            if filter_helper.match_string(tag_rule['value'], tag_mo['Value']):
                                tag_found = True
                                break

                    tag_match = not tag_found

            if isinstance(tag_rule, str):
                if tag_rule.split(':')[0] == '_count_':
                    if len(server_mo['Tags']) - 1 == int(tag_rule.split(':')[1]):
                        tag_match = True

                if tag_rule.split(':')[0] != '_count_':
                    if tag_rule.split(':')[0].startswith('!'):
                        tag_found = False
                        for tag_mo in server_mo['Tags']:
                            if tag_mo['Key'] == 'Intersight.LicenseTier':
                                continue

                            if filter_helper.match_string(tag_rule.split(':')[0][1:], tag_mo['Key']):
                                if filter_helper.match_string(tag_rule.split(':')[1], tag_mo['Value']):
                                    tag_found = True
                                    break

                        tag_match = not tag_found

                    if not tag_rule.split(':')[0].startswith('!'):
                        for tag_mo in server_mo['Tags']:
                            if tag_mo['Key'] == 'Intersight.LicenseTier':
                                continue

                            if filter_helper.match_string(tag_rule.split(':')[0], tag_mo['Key']):
                                if filter_helper.match_string(tag_rule.split(':')[1], tag_mo['Value']):
                                    tag_match = True
                                    break

            if logical == 'and':
                tags_match = tags_match and tag_match

            if logical == 'or':
                tags_match = tags_match or tag_match

        return tags_match

    def match_server_mo(self, server_mo, match_rules):
        if match_rules is None:
            return True

        if 'ip' in match_rules and len(match_rules['ip']) > 0:
            if not self.ip_filter_match_mo(server_mo, match_rules['ip']):
                return False

        if 'name' in match_rules and len(match_rules['name']) > 0:
            if not self.name_filter_match_mo(server_mo, match_rules['name'], match_rules['logical']['name']):
                return False

        if 'model' in match_rules and len(match_rules['model']) > 0:
            if not self.model_filter_match_mo(server_mo, match_rules['model'], match_rules['logical']['model']):
                return False

        if 'serial' in match_rules and len(match_rules['serial']) > 0:
            if not self.serial_filter_match_mo(server_mo, match_rules['serial'], match_rules['logical']['serial']):
                return False

        if 'tag' in match_rules and len(match_rules['tag']) > 0:
            if not self.tag_filter_match_mo(server_mo, match_rules['tag'], match_rules['logical']['tag']):
                return False

        return True

    def get_mo_match_rules(self, ip_filter=None, name_filter=None, serial_filter=None, model_filter=None, tag_filter=None):
        match_rules = {}
        match_rules['logical'] = {}

        for key in ['ip', 'name', 'serial', 'model', 'tag']:
            match_rules[key] = []
            match_rules['logical'][key] = 'or'

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

                if len(ip_filter_entry.split('-')) == 2:
                    (start_adress, end_address) = ip_filter_entry.split('-')
                    if len(end_address.split('.')) == 1:
                        end_address = '%s.%s' % (
                            '.'.join(start_adress.split('.')[:3]),
                            end_address
                        )

                    ip_addresses = ip_helper.get_ipv4_addresses_in_range(
                        start_adress,
                        end_address
                    )
                    for ip_address in ip_addresses:
                        match_rules['ip'].append(
                            dict(
                                type='address',
                                value=ip_address
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

        if name_filter is not None:
            if isinstance(name_filter, dict):
                match_rules['logical']['name'] = name_filter['logical']
                for item in name_filter['rule']:
                    match_rules['name'].append(item)

            if isinstance(name_filter, list):
                for item in name_filter:
                    match_rules['name'].append(item)

        if serial_filter is not None:
            if isinstance(serial_filter, dict):
                match_rules['logical']['serial'] = serial_filter['logical']
                for item in serial_filter['rule']:
                    match_rules['serial'].append(item)

            if isinstance(serial_filter, list):
                for item in serial_filter:
                    match_rules['serial'].append(item)

        if model_filter is not None:
            if isinstance(model_filter, dict):
                match_rules['logical']['model'] = model_filter['logical']
                for item in model_filter['rule']:
                    match_rules['model'].append(item)

            if isinstance(model_filter, list):
                for item in model_filter:
                    match_rules['model'].append(item)

        if tag_filter is not None:
            if isinstance(tag_filter, dict):
                match_rules['logical']['tag'] = tag_filter['logical']
                for item in tag_filter['rule']:
                    match_rules['tag'].append(item)

            if isinstance(tag_filter, list):
                for item in tag_filter:
                    match_rules['tag'].append(item)

        return match_rules
