import json


class IwoCluster():
    def __init__(self):
        self.mo_cluster = None

    def initialize_cluster(self):
        body = {}
        body['className'] = 'ContainerPlatformCluster'

        self.mo_cluster = self.search(body)
        if self.mo_cluster is None:
            return False

        self.log.iwo_mo(
            'ContainerPlatformCluster.attributes',
            self.mo_cluster
        )

        return True

    def get_cluster_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_clusters(self):
        if self.mo_cluster is None:
            if not self.initialize_cluster():
                self.log.error(
                    'get_clusters',
                    'Managed objects must be initialized first'
                )
                return None

        clusters = []

        for managed_object in self.mo_cluster:
            cluster_info = self.get_cluster_info(
                managed_object
            )
            if cluster_info is not None:
                clusters.append(
                    cluster_info
                )

        self.log.iwo_mo(
            'ContainerPlatformCluster.info',
            self.mo_cluster
        )

        return clusters

    def print_clusters(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
