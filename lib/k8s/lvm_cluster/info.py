
class K8sLvmClusterInfo():
    def __init__(self):
        self.lvm_cluster = None

    def get_lvm_cluster_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

        info['state'] = self.get(managed_object, 'status:state')
        info['ready'] = self.get(managed_object, 'status:ready', on_error=False, on_none=False)
        info = self.add_tick(
            info, 
            'ready', 
            True, 
            'readyTick'
        )

        info['resourcesAvailable'] = False
        info['resourcesAvailableReason'] = None
        info['resourcesAvailableMessage'] = None
        info['resourcesAvailableDescription'] = None

        info['vgsReady'] = False
        info['vgsReadyReason'] = None
        info['vgsReadyMessage'] = None
        info['vgsReadyDescription'] = None

        conditions_mo = self.get(managed_object, 'status:conditions', on_error=[], on_none=[])
        for condition_mo in conditions_mo:
            contition_type = self.get(condition_mo, 'type', on_error="N/A", on_none="N/A")
            condition_status = self.get(condition_mo, 'status', on_error='False', on_none='False')
            if contition_type == 'ResourcesAvailable':
                if condition_status == 'True':
                    info['resourcesAvailable'] = True

                info['resourcesAvailableReason'] = self.get(condition_mo, 'reason')
                info['resourcesAvailableMessage'] = self.get(condition_mo, 'message')
                info['resourcesAvailableDescription'] = '[%s] %s' % (
                    info['resourcesAvailableReason'],
                    info['resourcesAvailableMessage']
                )

            if contition_type == 'VolumeGroupsReady':
                if condition_status == 'True':
                    info['vgsReady'] = True

                info['vgsReadyReason'] = self.get(condition_mo, 'reason')
                info['vgsReadyMessage'] = self.get(condition_mo, 'message')
                info['vgsReadyDescription'] = '[%s] %s' % (
                    info['vgsReadyReason'],
                    info['vgsReadyMessage']
                )

        info = self.add_tick(
            info, 
            'resourcesAvailable', 
            True, 
            'resourcesAvailableTick'
        )

        info = self.add_tick(
            info, 
            'vgsReady', 
            True, 
            'vgsReadyTick'
        )

        info['deviceClass'] = []

        device_classes_mo = self.get(managed_object, 'spec:storage:deviceClasses', on_error=[], on_none=[])
        device_classes_status_mo = self.get(managed_object, 'status:deviceClassStatuses', on_error=[], on_none=[])
        for device_class_mo in device_classes_mo:
            device_class_info = {}
            device_class_info['__Output'] = {}
            device_class_info['name'] = self.get(device_class_mo, 'name')
            device_class_info['fstype'] = self.get(device_class_mo, 'fstype')
            device_class_info['default'] = self.get(device_class_mo, 'default', on_error=False, on_none=False)
            device_class_info = self.add_tick(
                device_class_info, 
                'default', 
                True, 
                'defaultTick'
            )
            
            device_class_info['nodeSelector'] = self.get(device_class_mo, 'nodeSelector')
            device_class_info['deviceSelector'] = self.get(device_class_mo, 'deviceSelector')
            device_class_info['thinPoolConfig'] = self.get(device_class_mo, 'thinPoolConfig')

            device_class_info['nodesCount'] = 0
            device_class_info['nodesReady'] = 0

            device_class_info['nodeStatus'] = []
            for device_class_status_mo in device_classes_status_mo:
                if device_class_status_mo['name'] == device_class_info['name']:
                    device_class_info['nodeStatus'] = self.get(device_class_status_mo, 'nodeStatus', on_error=[], on_none=[])
                    for node_status in device_class_info['nodeStatus']:
                        device_class_info['nodesCount'] += 1
                        node_status['__Output'] = {}
                        excluded_mo = self.get(node_status, 'excluded', on_error=[], on_none=[])
                        node_status['excludedDevices'] = []
                        node_status['excludedReasons'] = []
                        node_status['excludedCount'] = len(
                            excluded_mo
                        )
                        for excluded in excluded_mo:
                            node_status['excludedDevices'].append(
                                excluded['name']
                            )
                            for reason in excluded['reasons']:
                                node_status['excludedReasons'].append(reason)

                        if node_status['status'] == 'Ready':
                            node_status['__Output']['status'] = 'Green'
                            node_status['ready'] = True
                            device_class_info['nodesReady'] += 1
                        else:
                            node_status['__Output']['status'] = 'Red'
                            node_status['ready'] = False

            device_class_info['nodesSummary'] = '%s/%s' % (
                device_class_info['nodesReady'],
                device_class_info['nodesCount']
            )
            if device_class_info['nodesReady'] == device_class_info['nodesCount'] and device_class_info['nodesCount'] > 0:
                device_class_info['__Output']['nodesSummary'] = 'Green'
            else:
                device_class_info['__Output']['nodesSummary'] = 'Red'

            info['deviceClass'].append(
                device_class_info
            )

        info['deviceClass'] = sorted(
            info['deviceClass'],
            key=lambda i: i['name']
        )
        return info

    def get_lvm_clusters(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'lvm_cluster', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_lvm_cluster(self, cache_enabled=True):
        if self.get_lvm_cluster(cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_lvm_cluster_ready(self, cache_enabled=True):
        lvm_cluster = self.get_lvm_cluster(cache_enabled=cache_enabled)
        if lvm_cluster is None:
            return False
        
        return lvm_cluster['ready']

    def get_lvm_cluster_state(self, cache_enabled=True):
        cluster_info = self.get_lvm_cluster(cache_enabled=cache_enabled)
        if cluster_info is None:
            return None
        return cluster_info['state']

    def get_lvm_cluster(self, return_mo=False, cache_enabled=True):
        lvm_clusters = self.get_lvm_clusters(
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if lvm_clusters is None:
            return None

        if len(lvm_clusters) == 1:
            return lvm_clusters[0]

        return None