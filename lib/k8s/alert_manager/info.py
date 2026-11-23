class K8sAlertManagerInfo():
    def __init__(self):
        self.alert_manager = None

    def get_alert_manager_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        info['version'] = self.get(
            managed_object,
            'metadata:labels:app.kubernetes.io/version'
        )

        info['replicas'] = self.get(
            managed_object,
            'spec:replicas'
        )
        return info

    def get_alert_managers(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'alert_manager', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_alert_manager(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'alert_manager', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_alert_manager(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_alert_manager(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_alert_manager(self, cache_enabled=True):
        infos = self.get_alert_managers(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True