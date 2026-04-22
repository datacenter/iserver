class K8sOperatorGroupInfo():
    def __init__(self):
        self.operator_group = None

    def get_operator_group_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

        actual_namespaces = self.get(managed_object, 'status:namespaces', on_error=[], on_none=[])
        info['ns'] = []
        for namespace_name in actual_namespaces:
            if len(namespace_name) == 0:
                continue

            ns_info = {}
            ns_info['__Output'] = {}
            ns_info['name'] = namespace_name
            info['ns'].append(
                ns_info
            )

        info['ns'] = sorted(
            info['ns'],
            key=lambda i: i['name']
        )
        info['nsCount'] = len(info['ns'])

        return info

    def get_operator_groups(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'operator_group', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos
    
    def is_operator_group(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_operator_group(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_operator_group(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'operator_group', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )