class K8sDataScienceClusterInitializationDelete():
    def __init__(self):
        pass

    def delete_data_science_cluster_initializations(self, my_output=None, wait=True):
        clusters = self.get_data_science_cluster_initializations(
            cache_enabled=False
        )
        if clusters is None:
            if my_output is not None:
                my_output.default('Delete Data Science Cluster Initialization', before_newline=True, underline=True)
                my_output.error('Failed to get data science cluster initializations')
            return False

        if len(clusters) == 0:
            if my_output is not None:
                my_output.default('Delete Data Science Cluster Initialization', before_newline=True, underline=True)
                my_output.default('- no instance found')
            return True
        
        for cluster in clusters:
            success = self.delete_data_science_cluster_initialization(cluster['name'], wait=wait)
            if not success:
                return False
            
        return True

    def delete_data_science_cluster_initialization(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Data Science Cluster Initialization', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        if not self.is_data_science_cluster_initialization(name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        success = self.delete_data_science_cluster_initialization_mo(
            name
        )
        if not success:
            if my_output is not None:
                my_output.error('Data science cluster initialization instance delete failed')

            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no data science cluster initialization instance')

            if not self.wait_no_data_science_cluster_initialization(name):
                if my_output is not None:
                    my_output.error('Time out')
                return False
            
        return True
    