class K8sDataScienceClusterDelete():
    def __init__(self):
        pass

    def delete_data_science_clusters(self, my_output=None, wait=True):
        clusters = self.get_data_science_clusters(
            cache_enabled=False
        )
        if clusters is None:
            if my_output is not None:
                my_output.default('Delete Data Science Cluster', before_newline=True, underline=True)
                my_output.error('Failed to get data science clusters')
            return False

        if len(clusters) == 0:
            if my_output is not None:
                my_output.default('Delete Data Science Cluster', before_newline=True, underline=True)
                my_output.default('- no cluster found')
            return True
        
        for cluster in clusters:
            success = self.delete_data_science_cluster(cluster['name'], wait=wait)
            if not success:
                return False
            
        return True

    def delete_data_science_cluster(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Data Science Cluster', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        if not self.is_data_science_cluster(name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        success = self.delete_data_science_cluster_mo(
            name
        )
        if not success:
            if my_output is not None:
                my_output.error('Data science cluster delete failed')

            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no data science cluster')

            if not self.wait_no_data_science_cluster(name):
                if my_output is not None:
                    my_output.error('Time out')
                return False
            
        return True
    