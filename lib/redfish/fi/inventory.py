import json


class RedfishEndpointFabricInterconnectInventory():
    def __init__(self):
        self.inventory_type = ''
        self.inventory_id = ''
        self.inventory = None

    def get_inventory_type(self):
        return self.inventory_type

    def get_inventory_id(self):
        return self.inventory_id

    def set_inventory(self, inventory_type, inventory_id):
        self.inventory_type = inventory_type
        self.inventory_id = inventory_id
        self.clear_system_id()

    def get_chassis(self):
        chassis = self.get_properties(
            'Chassis',
            fixup=False
        )
        return chassis

    def get_servers(self):
        chassis = self.get_properties(
            'Servers',
            fixup=False
        )
        return chassis

    def get_chassis_info(self):
        data = self.get_chassis()
        chassiz_info = []

        for chassis in data['Results']:
            chassis_info = {}
            chassis_info['InventoryType'] = 'Chassis'
            chassis_info['Iom1'] = chassis['Ioms'][0]['Name']
            chassis_info['Iom2'] = chassis['Ioms'][1]['Name']
            chassis_info['Name'] = chassis['chassis']['Name']
            chassis_info['Model'] = chassis['chassis']['Model']
            chassis_info['Serial'] = chassis['chassis']['Serial']
            chassis_info['Identifier'] = chassis['chassis']['Identifier']

            if chassis['chassis']['AlarmSummary']['Warning'] == 0 and chassis['chassis']['AlarmSummary']['Critical'] == 0:
                chassis_info['Health'] = 'Healthy'
                chassis_info['HealthSummary'] = 'Healthy'
            if chassis['chassis']['AlarmSummary']['Warning'] > 0 and chassis['chassis']['AlarmSummary']['Critical'] == 0:
                chassis_info['Health'] = 'Warnings'
                chassis_info['HealthSummary'] = 'Warnings (%s)' % (chassis['chassis']['AlarmSummary']['Warning'])
            if chassis['chassis']['AlarmSummary']['Critical'] > 0:
                chassis_info['Health'] = 'Critical'
                chassis_info['HealthSummary'] = 'Critical (%s)' % (chassis['chassis']['AlarmSummary']['Critical'])

            chassiz_info.append(chassis_info)

        return chassiz_info

    def get_servers_info(self):
        data = self.get_servers()
        servers_info = []

        for server in data['Results']:
            server_info = {}
            server_info['InventoryType'] = 'Server'
            server_info['Name'] = server['Name']
            server_info['Model'] = server['Model']
            server_info['Serial'] = server['Serial']
            server_info['ConnectionStatus'] = server['ConnectionStatus']
            server_info['Identifier'] = server['Identifier']
            server_info['ChassisIdentifier'] = server['Identifier'].split('/')[0]

            server_info['OperPowerState'] = server['OperPowerState']
            server_info['Power'] = False
            if server_info['OperPowerState'] == 'on':
                server_info['Power'] = True
            server_info['ServerProfile'] = server['ServerProfile']

            server_info['IP_Inband'] = None
            server_info['IP_Outband'] = None
            for kvm in server['KvmIpAddresses']:
                if kvm['Name'] == 'Inband':
                    server_info['IP_Inband'] = kvm['Address']
                if kvm['Name'] == 'Outband':
                    server_info['IP_Outband'] = kvm['Address']

            if server['AlarmSummary']['Warning'] == 0 and server['AlarmSummary']['Critical'] == 0:
                server_info['Health'] = 'Healthy'
                server_info['HealthSummary'] = 'Healthy'
            if server['AlarmSummary']['Warning'] > 0 and server['AlarmSummary']['Critical'] == 0:
                server_info['Health'] = 'Warnings'
                server_info['HealthSummary'] = 'Warnings (%s)' % (server['AlarmSummary']['Warning'])
            if server['AlarmSummary']['Critical'] > 0:
                server_info['Health'] = 'Critical'
                server_info['HealthSummary'] = 'Critical (%s)' % (server['AlarmSummary']['Critical'])

            servers_info.append(server_info)

        return servers_info

    def get_server_to_chassis_info(self):
        for server in self.inventory['servers']:
            for chassis in self.inventory['chassis']:
                if server['ChassisIdentifier'] == chassis['Identifier']:
                    server['Chassis'] = chassis

    def get_server_inventory(self, server_system_id):
        inventory = self.get_inventory()

        for server in inventory['servers']:
            if server['Serial'] == server_system_id:
                return server

        return None

    def get_blades_id(self):
        blades = []

        for chassis in self.inventory['chassis']:
            chassis_properties = self.get_properties(
                'Chassis',
                fixup=True,
                inventory_type=chassis['InventoryType'],
                inventory_id=chassis['Iom1']
            )

            if chassis_properties is None:
                self.log.error(
                    'get_blades_id',
                    'Chassis properties not found: %s %s' % (
                        chassis['InventoryType'],
                        chassis['Iom1']
                    )
                )
                continue

            self.log.debug(
                'get_blades_id',
                '%s %s properties: %s' % (
                    chassis['InventoryType'],
                    chassis['Iom1'],
                    json.dumps(chassis_properties, indent=4)
                )
            )

            for member in chassis_properties['Members']:
                if member['@odata.id'].startswith('/redfish/v1/Chassis/Blade'):
                    blade = self.get_properties(
                        member['@odata.id'],
                        fixup=True,
                        inventory_type=chassis['InventoryType'],
                        inventory_id=chassis['Iom1']
                    )
                    if blade is not None:
                        if 'SerialNumber' in blade:
                            blade_info = {}
                            blade_info['ChassisId'] = chassis['Identifier']
                            blade_info['BladeId'] = blade['Id']
                            blade_info['SerialNumber'] = blade['SerialNumber']
                            blades.append(blade_info)

            self.log.debug(
                'get_blades_id',
                'Blades %s %s properties: %s' % (
                    chassis['InventoryType'],
                    chassis['Iom1'],
                    json.dumps(blades, indent=4)
                )
            )

        return blades

    def get_server_to_blade_info(self):
        for server in self.inventory['servers']:
            server['BladeId'] = None

        blades = self.get_blades_id()
        if blades is None:
            self.log.error('get_server_to_blade_info', 'Blade IDs discovery failed')
            return

        self.log.debug(
            'get_server_to_blade_info',
            'Blade IDs: %s' % (json.dumps(blades, indent=4))
        )

        for server in self.inventory['servers']:
            for blade in blades:
                if server['Serial'] == blade['SerialNumber']:
                    server['BladeId'] = blade['BladeId']

    def get_inventory(self):
        if self.inventory is not None:
            return self.inventory

        if self.is_cache_enabled():
            return self.cache['extra']['Inventory']

        self.inventory = {}
        self.inventory['chassis'] = self.get_chassis_info()
        self.inventory['servers'] = self.get_servers_info()
        self.log.debug('get_inventory', 'Base info: %s' % (json.dumps(self.inventory, indent=4)))

        self.get_server_to_chassis_info()
        self.get_server_to_blade_info()
        self.log.debug('get_inventory', 'Extended info: %s' % (json.dumps(self.inventory, indent=4)))

        return self.inventory
