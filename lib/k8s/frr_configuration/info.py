class K8sFrrConfigurationInfo():
    def __init__(self):
        self.frr_configuration = None

    def get_frr_configuration_info(self, managed_object):
        info = self.get_base_info(managed_object)

        info['ra'] = self.get(info, 'annotation:k8s.ovn.org/route-advertisements')
        info['ra_name'] = None
        info['ra_frr'] = None
        info['ra_node'] = None
        if info['ra'] is not None and len(info['ra'].split('/')) == 3:
            (info['ra_name'], info['ra_frr'], info['ra_node']) = info['ra'].split('/')
        
        return info
    
    def get_frr_configurations(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'frr_configuration', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_frr_configurations_summary(self, cache_enabled=True):
        items = self.get_frr_configurations(cache_enabled=cache_enabled)
        if items is None:
            summary = {}
            summary['count'] = None
            summary['ra'] = None
            summary['summary'] = '---'
            summary['color'] = 'Red'
            return summary
        
        summary = {}
        summary['color'] = 'Green'
        summary['count'] = len(items)
        summary['ra'] = 0
        for item in items:
            if item['ra'] is not None:
                summary['ra'] += 1
        
        summary['summary'] = '%s incl. %s ra-generated' % (summary['count'], summary['ra'])
        return summary
    
    def is_frr_configuration(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_frr_configuration(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_frr_configuration(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'frr_configuration', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
    