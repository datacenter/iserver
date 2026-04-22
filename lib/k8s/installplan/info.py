class K8sInstallplanInfo():
    def __init__(self):
        self.installplan = None

    def get_installplan_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

        info['ready'] = False
        conditions_mo = self.get(managed_object, 'status:conditions')
        phase_mo = self.get(managed_object, 'status:phase')
        if conditions_mo is not None and phase_mo is not None:
            if phase_mo == 'Complete':
                for condition_mo in conditions_mo:
                    if condition_mo['type'] == 'Installed' and condition_mo['status'] in ['True', '"True"']:
                        info['ready'] = True

        info['approved'] = self.get(managed_object, 'spec:approved', on_error=False, on_none=False)
        info = self.add_tick(
            info, 
            'approved', 
            True, 
            'approvedTick'
        )
        return info

    def get_installplans(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'installplan', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_installplan(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_installplan(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_installplan(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        info = self.get_info(
            'installplan', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
        return info