from lib import info_helper
from lib import output_helper


class ComputesSummary():
    """Class for server summary
    """
    def __init__(self, settings, log_id=None):
        self.info_handler = info_helper.InfoHelper(log_id=log_id)
        self.my_output = output_helper.OutputHelper(log_id=log_id)
        self.settings = settings

    def get_type_summary(self, summary, servers):
        type_dict = {}
        type_dict['Rack'] = 0
        type_dict['Blade'] = 0

        for server in servers:
            if server['Type'] == 'Rack':
                type_dict['Rack'] = type_dict['Rack'] + 1
            else:
                type_dict['Blade'] = type_dict['Blade'] + 1

        summary['type'] = type_dict

        return summary

    def print_type_summary(self, summary):
        if 'type' in summary:
            self.my_output.dictionary(
                summary['type'],
                title='Type',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['type'].keys(),
                start=''
            )

    def get_model_summary(self, summary, servers):
        models_dict = {}
        for server in servers:
            model_name = server['Model']
            if model_name not in models_dict:
                models_dict[model_name] = 1
                continue

            models_dict[model_name] = models_dict[model_name] + 1

        models_list = []
        for model_name in models_dict:
            models_list.append(
                dict(
                    key=model_name,
                    value=models_dict[model_name]
                )
            )

        summary['models_dict'] = dict(sorted(models_dict.items()))
        summary['models_list'] = models_list

        return summary

    def print_model_summary(self, summary):
        if 'models_dict' in summary:
            self.my_output.dictionary(
                summary['models_dict'],
                title='Models',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['models_dict'].keys(),
                start=''
            )

    def get_max_summary(self, summary, servers):
        max_dict = {}
        max_dict['CpuSockets'] = 0
        max_dict['CpuCores'] = 0
        max_dict['CpuThreads'] = 0
        max_dict['Memory'] = 0
        if self.settings['storage']:
            max_dict['Storage Controllers'] = 0
            max_dict['Total Disk Capacity'] = 0
            max_dict['HDD Count'] = 0
            max_dict['HDD Capacity'] = 0
            max_dict['SSD Count'] = 0
            max_dict['SSD Capacity'] = 0
        if self.settings['pci']:
            max_dict['PCI Devices'] = 0

        for server in servers:
            max_dict['CpuSockets'] = max(
                max_dict['CpuSockets'],
                server['NumCpus']
            )
            max_dict['CpuCores'] = max(
                max_dict['CpuCores'],
                server['NumCpuCores']
            )
            max_dict['CpuThreads'] = max(
                max_dict['CpuThreads'],
                server['NumThreads']
            )
            max_dict['Memory'] = max(
                max_dict['Memory'],
                server['TotalMemoryGB']
            )
            if self.settings['storage']:
                max_dict['Storage Controllers'] = max(
                    max_dict['Storage Controllers'],
                    server['StorageControllerCount']
                )
                max_dict['Total Disk Capacity'] = max(
                    max_dict['Total Disk Capacity'],
                    server['PhysicalDiskCapacity']
                )
                max_dict['HDD Count'] = max(
                    max_dict['HDD Count'],
                    server['HddDiskCount']
                )
                max_dict['HDD Capacity'] = max(
                    max_dict['HDD Capacity'],
                    server['HddDiskCapacity']
                )
                max_dict['SSD Count'] = max(
                    max_dict['SSD Count'],
                    server['SsdDiskCount']
                )
                max_dict['SSD Capacity'] = max(
                    max_dict['SSD Capacity'],
                    server['SsdDiskCapacity']
                )

            if self.settings['pci']:
                max_dict['PCI Devices'] = max(
                    max_dict['PCI Devices'],
                    len(server['PciModels'])
                )

        if self.settings['storage']:
            for key in ['Total Disk Capacity', 'HDD Capacity', 'SSD Capacity']:
                max_dict[key] = self.info_handler.convert_storage(max_dict[key])

        summary['max'] = max_dict

        return summary

    def print_max_summary(self, summary):
        if 'max' in summary:
            self.my_output.dictionary(
                summary['max'],
                title='Maximum',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['max'].keys(),
                start=''
            )

    def get_power_summary(self, summary, servers):
        power_dict = {}
        power_dict['On'] = 0
        power_dict['Off'] = 0

        for server in servers:
            if server['OperPowerState'] == 'on':
                power_dict['On'] = power_dict['On'] + 1
            else:
                power_dict['Off'] = power_dict['Off'] + 1

        summary['power'] = power_dict

        return summary

    def print_power_summary(self, summary):
        if 'power' in summary:
            self.my_output.dictionary(
                summary['power'],
                title='Power',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['power'].keys(),
                start=''
            )

    def get_health_summary(self, summary, servers):
        health_dict = {}
        health_dict['Healthy'] = 0
        health_dict['Warning'] = 0
        health_dict['Critical'] = 0

        for server in servers:
            if server['AlarmSummary']['Warning'] == 0 and server['AlarmSummary']['Critical'] == 0:
                health_dict['Healthy'] = health_dict['Healthy'] + 1
            if server['AlarmSummary']['Warning'] > 0 and server['AlarmSummary']['Critical'] == 0:
                health_dict['Warning'] = health_dict['Warning'] + 1
            if server['AlarmSummary']['Critical'] > 0:
                health_dict['Critical'] = health_dict['Critical'] + 1

        summary['health'] = health_dict

        return summary

    def print_health_summary(self, summary):
        if 'health' in summary:
            self.my_output.dictionary(
                summary['health'],
                title='Health',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['health'].keys(),
                start=''
            )

    def get_locator_summary(self, summary, servers):
        locator_dict = {}
        locator_dict['On'] = 0
        locator_dict['Off'] = 0

        supported = False
        for server in servers:
            if 'LocatorLedOn' in server:
                supported = True
                if server['LocatorLedOn']:
                    locator_dict['On'] = locator_dict['On'] + 1
                else:
                    locator_dict['Off'] = locator_dict['Off'] + 1

        if supported:
            summary['locator'] = locator_dict

        return summary

    def print_locator_summary(self, summary):
        if 'locator' in summary:
            self.my_output.dictionary(
                summary['locator'],
                title='Locator',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['locator'].keys(),
                start=''
            )

    def get_management_summary(self, summary, servers):
        management_dict = {}
        management_dict['Standalone'] = 0
        management_dict['UCSM'] = 0

        for server in servers:
            if server['ManagementMode'] == 'UCSM':
                management_dict['UCSM'] = management_dict['UCSM'] + 1
            else:
                management_dict['Standalone'] = management_dict['Standalone'] + 1

        summary['management'] = management_dict

        return summary

    def print_management_summary(self, summary):
        if 'management' in summary:
            self.my_output.dictionary(
                summary['management'],
                title='Management Mode',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['management'].keys(),
                start=''
            )

    def get_fan_summary(self, summary, servers):
        if not self.settings['fan']:
            return summary

        fan_dict = {}
        fan_dict['All up'] = 0
        fan_dict['Some down'] = 0

        for server in servers:
            if server['FanHealthy']:
                fan_dict['All up'] = fan_dict['All up'] + 1
            else:
                fan_dict['Some down'] = fan_dict['Some down'] + 1

        summary['fan'] = fan_dict

        return summary

    def print_fan_summary(self, summary):
        if 'fan' in summary:
            self.my_output.dictionary(
                summary['fan'],
                title='Server Fans',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['fan'].keys(),
                start=''
            )

    def get_psu_summary(self, summary, servers):
        if not self.settings['psu']:
            return summary

        psu_dict = {}
        psu_dict['All up'] = 0
        psu_dict['Some down'] = 0

        for server in servers:
            if server['PsuHealthy']:
                psu_dict['All up'] = psu_dict['All up'] + 1
            else:
                psu_dict['Some down'] = psu_dict['Some down'] + 1

        summary['psu'] = psu_dict

        return summary

    def print_psu_summary(self, summary):
        if 'psu' in summary:
            self.my_output.dictionary(
                summary['psu'],
                title='Server Psus',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['psu'].keys(),
                start=''
            )

    def get_pci_summary(self, summary, servers):
        if not self.settings['pci']:
            return summary

        pci_dict = {}

        for server in servers:
            for pci_model in server['PciModels']:
                if pci_model not in pci_dict:
                    pci_dict[pci_model] = 1
                    continue

                pci_dict[pci_model] = pci_dict[pci_model] + 1

        summary['pci'] = dict(sorted(pci_dict.items()))

        return summary

    def print_pci_summary(self, summary):
        if 'pci' in summary:
            self.my_output.dictionary(
                summary['pci'],
                title='PCI Models',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['pci'].keys(),
                start=''
            )

    def get_fw_summary(self, summary, servers):
        if not self.settings['fw']:
            return summary

        fw_dict = {}
        for server in servers:
            fw_name = server['FirmwareVersion']
            if fw_name not in fw_dict:
                fw_dict[fw_name] = 1
                continue

            fw_dict[fw_name] = fw_dict[fw_name] + 1

        summary['fw'] = dict(sorted(fw_dict.items()))

        return summary

    def print_fw_summary(self, summary):
        if 'fw' in summary:
            self.my_output.dictionary(
                summary['fw'],
                title='Firmware',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['fw'].keys(),
                start=''
            )

    def get_workflow_summary(self, summary, servers):
        if not self.settings['workflow']:
            return summary

        workflow_running_count = 0
        workflow_success_count = 0
        workflow_failed_count = 0
        workflow_names_dict = {}
        workflow_servers_count = 0
        workflow_no_servers_count = 0

        for server in servers:
            if server['Workflow']['Running'] is None and len(server['Workflow']['Last']) == 0:
                workflow_no_servers_count = workflow_no_servers_count + 1
                continue

            workflow_servers_count = workflow_servers_count + 1

            if server['Workflow']['Running'] is not None:
                workflow_running_count = workflow_running_count + 1
                workflow_name = server['Workflow']['Running']['Name']
                if workflow_name not in workflow_names_dict:
                    workflow_names_dict[workflow_name] = 1
                else:
                    workflow_names_dict[workflow_name] = workflow_names_dict[workflow_name] + 1

            for workflow_item in server['Workflow']['Last']:
                if workflow_item['Completed']:
                    workflow_success_count = workflow_success_count + 1
                else:
                    workflow_failed_count = workflow_failed_count + 1

                workflow_name = workflow_item['Name']
                if workflow_name not in workflow_names_dict:
                    workflow_names_dict[workflow_name] = 1
                else:
                    workflow_names_dict[workflow_name] = workflow_names_dict[workflow_name] + 1

        summary['workflow'] = {}
        summary['workflow']['running_count'] = workflow_running_count
        summary['workflow']['success_count'] = workflow_success_count
        summary['workflow']['failed_count'] = workflow_failed_count
        summary['workflow']['names'] = workflow_names_dict
        summary['workflow']['servers_count'] = workflow_servers_count
        summary['workflow']['no_servers_count'] = workflow_no_servers_count

        return summary

    def print_workflow_summary(self, summary):
        if 'workflow' in summary:
            self.my_output.dictionary(
                summary['workflow'],
                title='Last Workflows Summary',
                underline=False,
                prefix="- ",
                justify=True,
                keys=[
                    'running_count',
                    'success_count',
                    'failed_count',
                    'servers_count',
                    'no_servers_count'
                ],
                title_keys=[
                    'Running',
                    'Success',
                    'Failed',
                    'Servers with workflows',
                    'Servers with no workflows'
                ],
                start=''
            )

            self.my_output.dictionary(
                summary['workflow']['names'],
                title='Workflow Names',
                underline=False,
                prefix="- ",
                justify=True,
                keys=summary['workflow']['names'].keys(),
                start=''
            )

    def get_tags_summary(self, summary, servers):
        tags = {}

        for server in servers:
            for tag in server['Tags']:
                if tag['Key'] == 'Intersight.LicenseTier':
                    continue

                tag_kv = '%s:%s' % (
                    tag['Key'],
                    tag['Value']
                )

                if tag_kv not in tags:
                    tags[tag_kv] = {}
                    tags[tag_kv]['count'] = 0
                    tags[tag_kv]['server'] = []

                tags[tag_kv]['count'] = tags[tag_kv]['count'] + 1
                tags[tag_kv]['server'].append(server['Name'])

        summary['tags'] = tags
        return summary

    def print_tags_summary(self, summary):
        self.my_output.default(
            'Tag'
        )

        tags = sorted(
            summary['tags']
        )
        for tag in tags:
            self.my_output.default(
                '- %s: %s' % (
                    tag,
                    summary['tags'][tag]['count']
                )
            )

    def get_summary(self, servers):
        summary = {}

        summary['count'] = len(servers)
        summary = self.get_type_summary(summary, servers)
        summary = self.get_model_summary(summary, servers)
        summary = self.get_max_summary(summary, servers)
        summary = self.get_power_summary(summary, servers)
        summary = self.get_health_summary(summary, servers)
        summary = self.get_locator_summary(summary, servers)
        summary = self.get_management_summary(summary, servers)
        summary = self.get_fan_summary(summary, servers)
        summary = self.get_psu_summary(summary, servers)
        summary = self.get_pci_summary(summary, servers)
        summary = self.get_fw_summary(summary, servers)
        summary = self.get_workflow_summary(summary, servers)
        summary = self.get_tags_summary(summary, servers)

        return summary

    def print_summary(self, summary):
        self.my_output.default('\nSelected servers count: %s\n' % (summary['count']))
        self.print_type_summary(summary)
        self.print_model_summary(summary)
        self.print_power_summary(summary)
        self.print_max_summary(summary)
        self.print_health_summary(summary)
        self.print_locator_summary(summary)
        self.print_management_summary(summary)
        self.print_fan_summary(summary)
        self.print_psu_summary(summary)
        self.print_pci_summary(summary)
        self.print_fw_summary(summary)
        self.print_workflow_summary(summary)
        self.print_tags_summary(summary)
