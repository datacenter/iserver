class NodeInfo():
    def __init__(self):
        self.nodes = None

    def get_node_equipment_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['description'] = self.get_value(managed_object, 'fdtn.description', None)
        info['name'] = self.get_value(managed_object, 'fdtn.name', None)
        info['type'] = self.get_value(managed_object, 'eq.equipment-type', None)
        info['present'] = self.get_value(managed_object, 'eq.is-physically-present', None)
        info['manufactured'] = self.get_value(managed_object, 'eq.manufactured-date', None)
        info['vendor'] = self.get_value(managed_object, 'eq.manufacturer', None)
        info['pn'] = self.get_value(managed_object, 'eq.part-number', None)
        info['pid'] = self.get_value(managed_object, 'eq.product-id', None)
        info['sn'] = self.get_value(managed_object, 'eq.serial-number', None)
        info['state'] = self.get_value(managed_object, 'eq.service-state', None)
        info['assemblyNo'] = self.get_value(managed_object, 'eq.assembly-number', None)
        info['assemblyRev'] = self.get_value(managed_object, 'eq.assembly-revision', None)
        return info

    def get_node_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['commState'] = self.get_value(managed_object, 'nd.communication-state', 'Unknown')
        if info['commState'] == 'Reachable':
            info['reachable'] = True
            info['reachableTick'] = '\u2713'
            info['__Output']['reachableTick'] = 'Green'
        else:
            info['reachable'] = True
            info['reachableTick'] = '\u2717'
            info['__Output']['reachableTick'] = 'Red'

        info['lcState'] = self.get_value(managed_object, 'nd.lifecycle-state', 'Unknown')
        if info['lcState'] == 'MANAGED_AND_SYNCHRONIZED':
            info['sync'] = True
            info['syncTick'] = '\u2713'
            info['__Output']['syncTick'] = 'Green'
        else:
            info['sync'] = True
            info['syncTick'] = '\u2717'
            info['__Output']['syncTick'] = 'Red'

        info['name'] = self.get_value(managed_object, 'nd.name', None)
        info['ip'] = self.get_value(managed_object, 'nd.management-address', None)
        info['uptime'] = self.get_value(managed_object, 'nd.sys-up-time', None)
        info['description'] = self.get_value(managed_object, 'nd.description', None)
        info['id'] = self.get_value(managed_object, 'nd.instanceId', None)
        info['family'] = self.get_value(managed_object, 'nd.product-family', None)
        info['series'] = self.get_value(managed_object, 'nd.product-series', None)
        info['type'] = self.get_value(managed_object, 'nd.product-type', None)
        info['vendor'] = self.get_value(managed_object, 'nd.product-vendor', None)
        info['swType'] = self.get_value(managed_object, 'nd.software-type', None)
        info['swVersion'] = self.get_value(managed_object, 'nd.software-version', None)
        info['software'] = None
        if info['swType'] is not None and info['swVersion'] is not None:
            info['software'] = '%s %s' % (
                info['swType'],
                info['swVersion']
            )

        info['sn'] = None
        info['equipment'] = []
        if 'nd.equipment-list' in managed_object:
            for equipment_mo in managed_object['nd.equipment-list']['eq.equipment']:
                equipment_info = self.get_node_equipment_info(equipment_mo)
                info['equipment'].append(
                    equipment_info
                )
                if equipment_info['type'] == 'CHASSIS':
                    info['sn'] = equipment_info['sn']

        return info

    def get_nodes_info(self):
        if self.nodes is not None:
            return self.nodes

        nodes_mo = self.get_node_mo()
        if nodes_mo is not None:
            self.nodes = []
            for node_mo in nodes_mo:
                self.nodes.append(
                    self.get_node_info(
                        node_mo
                    )
                )

        self.nodes = sorted(
            self.nodes,
            key=lambda i: i['name'].lower()
        )

        return self.nodes

    def get_nodes(self):
        nodes = self.get_nodes_info()
        if nodes is None:
            return None

        return nodes
