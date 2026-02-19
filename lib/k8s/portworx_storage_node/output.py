class K8sPortworxStorageNodeOutput():
    def __init__(self):
        pass

    # Note: one object expected
    def print_portworx_storage_nodes(self, info):
        if info is None:
            return

        if len(info) == 0:
            self.my_output.default('No storage cluster', before_newline=True)
            return 
                
        for item in info:
            self.print_portworx_storage_node(item)

    def print_portworx_storage_node(self, item):
        self.my_output.dictionary_ng(
            'Storage Cluster',
            item, 
            [
                ['Namespace', 'namespace'],
                ['Name', 'name'],
                ['Owner', 'owner'],
                ['Phase', 'phase'],
                ['Ready', 'readyTick'],
                ['Current monitors', 'current_mon_count'],
                ['Expected OSD', 'expected_osd_count'],
                ['Nodes', 'hostnamesT'],
                ['Version', 'version'],
                ['LSO Storage Class', 'local_storage_sc'],
                ['ODF Storage Class', 'storage_class']
            ]
        )
