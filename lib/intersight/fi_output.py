import csv
from lib import filter_helper
from lib import output_helper


class FiOutput():
    def __init__(self, log_id):
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def print_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Fabric Interconnect', 'Name'],
                ['Id', 'SwitchId'],
                ['Model', 'Model'],
                ['Serial', 'Serial'],
                ['Management', 'ManagementModeT'],
                ['Oper', 'OperabilityTick'],
                ['Health', 'Health'],
                ['IP', 'ManagementIp'],
                ['Version', 'Version'],
                ['Ports', 'NumEtherPortsSummary'],
                ['FanMod', 'FanModuleCount'],
                ['Psu', 'PsuCount'],
                ['Storage', 'StorageCount']
            ]
        )

    def print_eth(self, info):
        info = filter_helper.flatten(
            info,
            'Ethernet',
            {
                'NameT': 'FabricInterconnect'
            }
        )

        self.my_output.my_table_ng(
            info,
            [
                ['FI', 'FabricInterconnect'],
                ['Eth', 'Name'],
                ['Admin', 'AdminState'],
                ['Oper', 'OperState'],
                ['Speed', 'OperSpeed'],
                ['Mode', 'Mode'],
                ['Role', 'RoleT'],
                ['Mac', 'MacAddress'],
                ['Transceiver', 'TransceiverTypeT'],
                ['PC', 'PortChannelId'],
                ['Server', 'Peer.ServerName'],
                ['Port', 'Peer.ServerPort']
            ]
        )

    def print_pc(self, info):
        info = filter_helper.flatten(
            info,
            'EthernetPortChannel',
            {
                'NameT': 'FabricInterconnect'
            }
        )

        self.my_output.my_table_ng(
            info,
            [
                ['FI', 'FabricInterconnect'],
                ['PC ID', 'PortChannelId'],
                ['Name', 'Name'],
                ['Role', 'Role'],
                ['Admin', 'AdminState'],
                ['State', 'OperState'],
                ['Speed', 'OperSpeed'],
                ['Members', 'MemberSummary']
            ]
        )

    def print_fc(self, info):
        info = filter_helper.flatten(
            info,
            'FibreChannel',
            {
                'NameT': 'FabricInterconnect'
            }
        )

        self.my_output.my_table_ng(
            info,
            [
                ['FI', 'FabricInterconnect'],
                ['FC', 'Name'],
                ['WWN', 'Wwn'],
                ['Role', 'Role'],
                ['Admin', 'AdminState'],
                ['Oper', 'OperState']
            ]
        )
        
    def print_fpc(self, info):
        info = filter_helper.flatten(
            info,
            'FibrePortChannel',
            {
                'NameT': 'FabricInterconnect'
            }
        )

        self.my_output.my_table_ng(
            info,
            [
                ['FI', 'FabricInterconnect'],
                ['FPC', 'Name'],
                ['Role', 'Role'],
                ['Admin', 'AdminState'],
                ['Oper', 'OperState']
            ]
        )

    def print_fanm(self, info):
        info = filter_helper.flatten(
            info,
            'FanModule',
            {
                'NameT': 'FabricInterconnect'
            }
        )

        self.my_output.my_table_ng(
            info,
            [
                ['Fabric Interconnect', 'FabricInterconnect'],
                ['Fan Module', 'ModuleId'],
                ['# Fans', 'FanCount'],
                ['Presence', 'Presence'],
                ['OperState', 'OperState'],
                ['Model', 'Model'],
                ['PN', 'PartNumber'],
                ['Vendor', 'Vendor']
            ]
        )

    def print_fan(self, info):
        info = filter_helper.flatten(
            info,
            'FanModule',
            {
                'NameT': 'FabricInterconnect'
            }
        )

        info = filter_helper.flatten(
            info,
            'Fans',
            {
                'FabricInterconnect': 'FabricInterconnect',
                'ModuleId': 'ModuleId'
            }
        )

        self.my_output.my_table_ng(
            info,
            [
                ['Fabric Interconnect', 'FabricInterconnect'],
                ['Fan Module', 'ModuleId'],
                ['Fan', 'FanId'],
                ['Presence', 'Presence'],
                ['OperState', 'OperState'],
                ['Model', 'Model'],
                ['Serial', 'Serial'],
                ['Sku', 'Sku'],
                ['PN', 'PartNumber'],
                ['Pid', 'Pid'],
                ['Vendor', 'Vendor']
            ]
        )

    def print_psu(self, info):
        info = filter_helper.flatten(
            info,
            'Psu',
            {
                'NameT': 'FabricInterconnect'
            }
        )

        self.my_output.my_table_ng(
            info,
            [
                ['Fabric Interconnect', 'FabricInterconnect'],
                ['PSU', 'Name'],
                ['Presence', 'Presence'],
                ['Voltage', 'Voltage'],
                ['Model', 'Model'],
                ['Pid', 'Pid'],
                ['Serial', 'Serial'],
                ['Vendor', 'Vendor']
            ]
        )

    def print_storage(self, info):
        info = filter_helper.flatten(
            info,
            'Storage',
            {
                'NameT': 'FabricInterconnect'
            }
        )

        self.my_output.my_table_ng(
            info,
            [
                ['Fabric Interconnect', 'FabricInterconnect'],
                ['Storage Partition', 'Name'],
                ['Size [MiB]', 'Size'],
                ['Used', 'UsedT']
            ]
        )

    def print_inv(self, info):
        for item in info:
            self.my_output.default(
                'Fabric Interconnect: %s' % (item['NameT']),
                underline=True,
                before_newline=True
            )

            self.my_output.my_table_ng(
                item['Inventory'],
                [
                    ['Type', 'Type'],
                    ['Name', 'Name'],
                    ['Model', 'Model'],
                    ['Vendor', 'Vendor'],
                    ['Serial', 'Serial'],
                    ['Pid', 'Pid']
                ]
            )

    def print_csv(self, info, inventory_filename):
        fields = [
            'Inventory Type',
            'Inventory Name',
            'Inventory Model',
            'Inventory Vendor',
            'Inventory Serial',
            'Inventory PID',
            'FI Serial',
            'FI Model',
            'FI Name'
        ]
        rows = []

        for fi_info in info:
            for inventory_info in fi_info['Inventory']:
                row = []
                row.append(inventory_info['Type'])
                row.append(inventory_info['Name'])
                row.append(inventory_info['Model'])
                row.append(inventory_info['Vendor'])
                row.append(inventory_info['Serial'])
                row.append(inventory_info['Pid'])
                row.append(fi_info['Serial'])
                row.append(fi_info['Model'])
                row.append(fi_info['Name'])
                rows.append(
                    row
                )

        with open(inventory_filename, 'w', newline='') as file_handler:
            write = csv.writer(file_handler)
            write.writerow(fields)
            for row in rows:
                write.writerow(row)
