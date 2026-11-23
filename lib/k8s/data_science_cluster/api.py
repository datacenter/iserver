import time
import traceback


class K8sDataScienceClusterApi():
    def __init__(self):
        self.data_science_cluster_mo = None

    def get_data_science_cluster_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.data_science_cluster_mo
        )
        if cache_hit:
            return response

        response, self.data_science_cluster_mo = self.get_resources(
            'DataScienceCluster', 
            'datasciencecluster.opendatahub.io/v1', 
            self.data_science_cluster_mo,
            name=name
        )

        return response

    def delete_data_science_cluster_mo(self, name):
        success, _ = self.delete_resource('DataScienceCluster', 'datasciencecluster.opendatahub.io/v1', name)
        return success