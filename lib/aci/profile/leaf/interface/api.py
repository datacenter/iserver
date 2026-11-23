class ProfileLeafInterfaceApi():
    def __init__(self):
        self.profile_leaf_interface_mo = None
        self.profile_leaf_interface_node_mo = {}
        self.profile_leaf_interface_node_interface_mo = {}
        self.profile_leaf_interface_reln_mo = {}

    def get_profile_leaf_interface_mo(self):
        if self.profile_leaf_interface_mo is not None:
            return self.profile_leaf_interface_mo

        cache = self.get_object_cache(
            'leafInterfaceProfile'
        )
        if cache is not None:
            self.profile_leaf_interface_mo = cache
            self.log.apic_mo(
                'leafInterfaceProfile',
                self.profile_leaf_interface_mo
            )
            return self.profile_leaf_interface_mo

        distinguished_name = 'uni/infra'
        children = [
            'infraHPortS',
            'infraPortBlk',
            'infraSubPortBlk',
            'infraRsAccBaseGrp'
        ]
        query = 'query-target=subtree&target-subtree-class=infraAccPortP&rsp-subtree=full&rsp-subtree-class=%s' % (','.join(children))

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_profile_leaf_interface_mo',
                'API failed'
            )
            return None

        self.profile_leaf_interface_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['infraAccPortP']['attributes']
            attributes['infraHPortS'] = self.get_mo_children_attributes(
                'infraAccPortP',
                managed_object,
                'infraHPortS',
                include_grandchildren=True
            )
            self.profile_leaf_interface_mo.append(
                attributes
            )

        self.log.apic_mo(
            'leafInterfaceProfile',
            self.profile_leaf_interface_mo
        )

        self.set_object_cache(
            'leafInterfaceProfile',
            self.profile_leaf_interface_mo
        )

        return self.profile_leaf_interface_mo

    def get_profile_leaf_interface_node_mo(self, profile_name):
        if profile_name in self.profile_leaf_interface_node_mo:
            return self.profile_leaf_interface_node_mo[profile_name]

        cache = self.get_object_cache(
            'leafInterfaceProfileNode.%s' % (profile_name)
        )
        if cache is not None:
            self.profile_leaf_interface_node_mo[profile_name] = cache
            self.log.apic_mo(
                'leafInterfaceProfileNode.%s' % (profile_name),
                self.profile_leaf_interface_node_mo[profile_name]
            )
            return self.profile_leaf_interface_node_mo[profile_name]

        distinguished_name = 'uni/infra/accportprof-%s' % (profile_name)
        children = [
            'AccPortPToEthIf'
        ]
        query = 'rsp-subtree-include=full-deployment&target-path=%s' % (','.join(children))

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_profile_leaf_interface_node_mo',
                'API failed'
            )
            return None

        self.profile_leaf_interface_node_mo[profile_name] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['infraAccPortP']['attributes']
            attributes['pconsNodeDeployCtx'] = self.get_mo_children_attributes(
                'infraAccPortP',
                managed_object,
                'pconsNodeDeployCtx'
            )
            self.profile_leaf_interface_node_mo[profile_name].append(
                attributes
            )

        self.log.apic_mo(
            'leafInterfaceProfileNode.%s' % (profile_name),
            self.profile_leaf_interface_node_mo[profile_name]
        )

        self.set_object_cache(
            'leafInterfaceProfileNode.%s' % (profile_name),
            self.profile_leaf_interface_node_mo[profile_name]
        )

        return self.profile_leaf_interface_node_mo[profile_name]

    def get_profile_leaf_interface_node_interface_mo(self, profile_name, node_id):
        if profile_name in self.profile_leaf_interface_node_interface_mo:
            if node_id in self.profile_leaf_interface_node_interface_mo[profile_name]:
                return self.profile_leaf_interface_node_mo[profile_name]

        cache = self.get_object_cache(
            'leafInterfaceProfileNodeInterface.%s.%s' % (profile_name, node_id)
        )
        if cache is not None:
            if profile_name not in self.profile_leaf_interface_node_interface_mo:
                self.profile_leaf_interface_node_interface_mo[profile_name] = {}

            self.profile_leaf_interface_node_interface_mo[profile_name][node_id] = cache
            self.log.apic_mo(
                'leafInterfaceProfileNodeInterface.%s.%s' % (profile_name, node_id),
                self.profile_leaf_interface_node_interface_mo[profile_name][node_id]
            )
            return self.profile_leaf_interface_node_interface_mo[profile_name][node_id]

        distinguished_name = 'uni/infra/accportprof-%s' % (profile_name)
        children = [
            'AccPortPToEthIf'
        ]
        query = 'rsp-subtree-include=full-deployment&target-node=%s&target-path=%s' % (node_id, ','.join(children))

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_profile_leaf_interface_node_interface_mo',
                'API failed'
            )
            return None

        if profile_name not in self.profile_leaf_interface_node_interface_mo:
            self.profile_leaf_interface_node_interface_mo[profile_name] = {}

        self.profile_leaf_interface_node_interface_mo[profile_name][node_id] = []
        for managed_object in managed_objects['imdata']:
            children = managed_object['infraAccPortP']['children']
            for child in children:
                if 'pconsNodeDeployCtx' in child:
                    if child['pconsNodeDeployCtx']['attributes']['nodeId'] == node_id:
                        if 'children' in child['pconsNodeDeployCtx']:
                            for grandchild in child['pconsNodeDeployCtx']['children']:
                                if 'pconsResourceCtx' in grandchild:
                                    self.profile_leaf_interface_node_interface_mo[profile_name][node_id].append(
                                        grandchild['pconsResourceCtx']['attributes']
                                    )

        self.log.apic_mo(
            'leafInterfaceProfileNodeInterface.%s.%s' % (profile_name, node_id),
            self.profile_leaf_interface_node_interface_mo[profile_name][node_id]
        )

        self.set_object_cache(
            'leafInterfaceProfileNodeInterface.%s.%s' % (profile_name, node_id),
            self.profile_leaf_interface_node_interface_mo[profile_name][node_id]
        )

        return self.profile_leaf_interface_node_interface_mo[profile_name][node_id]

    def get_profile_leaf_interface_reln_mo(self, profile_name):
        if profile_name in self.profile_leaf_interface_reln_mo:
            return self.profile_leaf_interface_reln_mo[profile_name]

        cache = self.get_object_cache(
            'leafInterfaceProfileReln.%s' % (profile_name)
        )
        if cache is not None:
            self.profile_leaf_interface_reln_mo[profile_name] = cache
            self.log.apic_mo(
                'leafInterfaceProfileReln.%s' % (profile_name),
                self.profile_leaf_interface_reln_mo[profile_name]
            )
            return self.profile_leaf_interface_reln_mo[profile_name]

        distinguished_name = 'uni/infra/accportprof-%s' % (profile_name)
        query = 'query-target=children&target-subtree-class=relnFrom'

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_profile_leaf_interface_node_mo',
                'API failed'
            )
            return None

        self.profile_leaf_interface_reln_mo[profile_name] = []
        for managed_object in managed_objects['imdata']:
            for key in managed_object:
                mo_attributes = managed_object[key]['attributes']
                mo_attributes['reln'] = key
                self.profile_leaf_interface_reln_mo[profile_name].append(
                    mo_attributes
                )

        self.log.apic_mo(
            'leafInterfaceProfileReln.%s' % (profile_name),
            self.profile_leaf_interface_reln_mo[profile_name]
        )

        self.set_object_cache(
            'leafInterfaceProfileReln.%s' % (profile_name),
            self.profile_leaf_interface_reln_mo[profile_name]
        )

        return self.profile_leaf_interface_reln_mo[profile_name]
