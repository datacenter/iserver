class K8sRouteAdvertisementInfo():
    def __init__(self):
        self.route_advertisement = None

    def get_route_advertisement_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        info['status'] = self.get(managed_object, 'status:status')
        info = self.add_tick(info, 'status', 'Accepted', 'acceptedTick', bool_attribute='accepted')
        return info

    def route_advertisements_info(self, infos, frr_info=False, cache_enabled=True):
        if frr_info:
            for item in infos:
                item['frr'] = {}

            configs = self.get_frr_configurations(cache_enabled=cache_enabled)
            if configs is not None:
                for item in infos:
                    for config in configs:
                        if item['name'] == config['ra_name']:
                            item['frr']['%s @%s' % (config['ra_frr'], config['ra_node'])] = config['spec']

        return infos

    def get_route_advertisements(self, object_filter=None, frr_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'route_advertisement', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

        if infos is not None:
            infos = self.route_advertisements_info(
                infos,
                frr_info=frr_info,
                cache_enabled=cache_enabled
            )

        return infos

    def get_route_advertisements_summary(self, cache_enabled=True):
        items = self.get_route_advertisements(cache_enabled=cache_enabled)
        if items is None:
            summary = {}
            summary['count'] = None
            summary['accepted'] = None
            summary['summary'] = '---'
            summary['color'] = 'Red'
            return summary
        
        summary = {}
        summary['count'] = len(items)
        summary['accepted'] = 0
        for item in items:
            if item['accepted']:
                summary['accepted'] += 1
        
        summary['summary'] = '%s/%s' % (summary['count'], summary['accepted'])
        if summary['count'] == summary['accepted']:
            summary['color'] = 'Green'
        else:
            summary['color'] = 'Red'

        return summary
    
    def is_route_advertisement(self, name, cache_enabled=True):
        if self.get_route_advertisement(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_route_advertisement(self, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'route_advertisement', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )