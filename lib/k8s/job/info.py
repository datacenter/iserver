class K8sJobInfo():
    def __init__(self):
        self.job = None

    def get_job_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

        info['completed'] = False
        conditions_mo = self.get(managed_object, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                type_mo = self.get(condition_mo, 'type')
                status_mo = self.get(condition_mo, 'status')
                if type_mo == 'Complete':
                    if status_mo == 'True':
                        info['completed'] = True
                        info['completedTick'] = '\u2713'
                        info['__Output']['completedTick'] = 'Green'
                    else:
                        info['completed'] = False
                        info['completedTick'] = '\u2717'
                        info['__Output']['completedTick'] = 'Red'

        return info

    def get_jobs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'job', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos
    
    def is_job(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_job(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_job(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'job', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )