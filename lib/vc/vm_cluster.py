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

        # ['AbandonHciWorkflow', 'AddHost', 'AddHost_Task', 'ApplyRecommendation', 'Array', 'CancelRecommendation', 'ClusterEnterMaintenanceMode', 'ConfigureHCI', 'ConfigureHCI_Task',
        # 'Destroy', 'Destroy_Task', 'EnterMaintenanceMode', 'EvcManager', 'ExtendHCI', 'ExtendHCI_Task', 'FindRulesForVm', 'GetResourceUsage', 'GetSystemVMsRestrictedDatastores',
        # 'MoveHostInto', 'MoveHostInto_Task', 'MoveInto', 'MoveInto_Task', 'PlaceVm', 'RecommendHostsForVm', 'Reconfigure', 'ReconfigureCluster_Task', 'ReconfigureComputeResource_Task',
        # 'ReconfigureEx', 'RefreshRecommendation', 'Reload', 'Rename', 'Rename_Task', 'RetrieveDasAdvancedRuntimeInfo', 'SetCryptoMode', 'SetCustomValue', 'StampAllRulesWithUuid',
        # 'StampAllRulesWithUuid_Task', 'Summary', 'ValidateHCIConfiguration', '_GetMethodInfo', '_GetMethodList', '_GetMoId', '_GetPropertyInfo', '_GetPropertyList', '_GetServerGuid',
        # '_GetStub', '_InvokeAccessor', '_InvokeMethod', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
        # '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
        # '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_methodInfo', '_moId', '_propInfo', '_propList', '_serverGuid', '_stub', '_version', '_wsdlName', 'actionHistory',
        # 'alarmActionsEnabled', 'availableField', 'configIssue', 'configStatus', 'configuration', 'configurationEx', 'customValue',
        # 'datastore', 'declaredAlarmState', 'disabledMethod', 'drsFault', 'drsRecommendation', 'effectiveRole', 'environmentBrowser', 'hciConfig', 'host', 'lifecycleManaged', 'migrationHistory',
        # 'name', 'network', 'overallStatus', 'parent', 'permission', 'recentTask', 'recommendation', 'resourcePool', 'setCustomValue', 'summary', 'summaryEx', 'tag', 'triggeredAlarmState', 'value']

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
