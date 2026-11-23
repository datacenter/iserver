class K8sCephClusterOutput():
    def __init__(self):
        pass

    # Note: one object expected
    def print_ceph_clusters(self, info):
        if info is None:
            return
        
        if len(info) == 0:
            self.my_output.default('No ceph cluster', before_newline=True)
            return 
        
        for item in info:
            self.print_ceph_cluster(item)

    
    def print_ceph_cluster(self, info):
        order = [
            'namespace',
            'name',
            'owner',
            'readyTick',
            'createdTick',
            'healtyTick',
            'health',
            'version',
            'manager_count',
            'monitor_count',
            'bytes_totalT',
            'bytes_usedT',
            'used_pctT',
            'bytes_availableT'
        ]

        headers = [
            'Namespace',
            'Name',
            'Owner',
            'Ready',
            'Created',
            'Healthy',
            'Health',
            'Version',
            'Manager Count',
            'Monitor Count',
            'Total Capacity',
            'Used',
            'Used pct',
            'Available'
        ]

        self.my_output.dictionary(
            info,
            title='Ceph Cluster',
            prefix='- ',
            keys=order,
            justify=True,
            values=order,
            title_keys=headers,
            start='\n\n'
        )
