# pylint: disable=no-name-in-module
from pyVmomi import vim


class VcVmCluster():
    def __init__(self):
        pass

    def is_vm_cluster(self, cluster_name):
        cluster_obj = self.get_vm_cluster_object(cluster_name)
        if cluster_obj is None:
            return False

        return True

    def get_vm_clusters(self):
        if not self.vc_connect():
            return None

        clusters = []
        content = self.vc_service_instance.RetrieveContent()

        # Get the list of all datacenters we have available to us
        clusters_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.ClusterComputeResource],
            True
        )

        for cluster_obj in clusters_object_view.view:
            cluster = {}
            cluster['name'] = cluster_obj.name
            clusters.append(cluster)

        return clusters

    def get_vm_cluster_object(self, cluster_name):
        if not self.vc_connect():
            return None

        content = self.vc_service_instance.RetrieveContent()
        clusters_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.ClusterComputeResource],
            True
        )

        for cluster_obj in clusters_object_view.view:
            if cluster_obj.name == cluster_name:
                clusters_object_view.Destroy()
                return cluster_obj

        clusters_object_view.Destroy()

        return None

    def get_vm_cluster_hosts(self, cluster_name):
        cluster_obj = self.get_vm_cluster_object(cluster_name)
        if cluster_obj is None:
            return None

        cluster_hosts = []
        for cluster_host in cluster_obj.host:
            cluster_hosts.append(
                cluster_host.name
            )

        return cluster_hosts
