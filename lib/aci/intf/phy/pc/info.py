class InterfacePhyPcInfo():
    def __init__(self):
        self.interface_phy_pc = {}

    def get_interface_phy_pc_info(self, managed_object):
        # {
        #     "bdlPortNum": "255",
        #     "bfdState": "5",
        #     "channelingSt": "unknown",
        #     "childAction": "",
        #     "dn": "topology/pod-1/node-205/sys/phys-[eth1/33]/aggrmbrif",
        #     "flags": "",
        #     "ltlProgrammed": "no",
        #     "modTs": "never",
        #     "monPolDn": "uni/fabric/monfab-default",
        #     "name": "",
        #     "nameAlias": "",
        #     "operSt": "down",
        #     "pcMode": "on",
        #     "status": "",
        #     "summOperSt": "down",
        #     "uptime": "00:00:00:00.000"
        # },
        keys = [
            'dn',
            'channelingSt',
            'pcMode'
        ]

        info = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # "dn": "topology/pod-1/node-205/sys/phys-[eth1/33]/aggrmbrif"
        info['pod_id'] = info['dn'].split('/')[1]
        info['node_id'] = info['dn'].split('/')[2]
        info['interface_id'] = None
        if 'phys-[' in info['dn']:
            info['interface_id'] = info['dn'].split('phys-[')[1].split(']')[0]

        if 'aggr-[' in info['dn']:
            info['interface_id'] = info['dn'].split('aggr-[')[1].split(']')[0]

        if info['interface_id'] is None:
            self.log.error(
                'get_interface_phy_pc_info',
                'Unsupported dn: %s' % (info['dn'])
            )

        return info

    def get_interfaces_phy_pc_info(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_phy_pc:
            return self.interface_phy_pc[key]

        managed_objects = self.get_interface_phy_pc_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        self.interface_phy_pc[key] = []
        for managed_object in managed_objects:
            self.interface_phy_pc[key].append(
                self.get_interface_phy_pc_info(
                    managed_object
                )
            )

        return self.interface_phy_pc[key]

    def get_interface_phy_pc_stats(self, pod_id, node_id, interface_id):
        interfaces_info = self.get_interfaces_phy_pc_info(pod_id, node_id)
        if interfaces_info is None:
            return None

        for interface_info in interfaces_info:
            if interface_id == interface_info['interface_id']:
                return interface_info

        return None
