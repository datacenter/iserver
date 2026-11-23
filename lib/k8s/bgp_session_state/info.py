class K8sBgpSessionStateInfo():
    def __init__(self):
        self.bgp_session_state = None

    def get_bgp_session_state_info(self, managed_object):
        info = self.get_base_info(managed_object)
        info = self.add_tick(info, 'status:bgpStatus', 'Established', 'establishedTick', bool_attribute='established')
        return info

    def get_bgp_session_states(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'bgp_session_state', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_bgp_session_states_summary(self, cache_enabled=True):
        states = self.get_bgp_session_states(cache_enabled=cache_enabled)
        if states is None:
            return None
        
        node_names = []
        for state in states:
            node_name = self.get(state, 'status:node')
            if node_name not in node_names:
                node_names.append(node_name)

        summary = {}
        summary['nodes'] = '%s/%s' % (len(node_names), self.get_node_count())
        summary['node'] = {}
        for node_name in node_names:
            summary['node'][node_name] = {}
            summary['node'][node_name]['count'] = 0
            summary['node'][node_name]['established'] = 0
            for state in states:
                if node_name == self.get(state, 'status:node'):
                    summary['node'][node_name]['count'] += 1
                    if state['established']:
                        summary['node'][node_name]['established'] += 1
            
            summary['node'][node_name]['summary'] = '%s/%s' % (summary['node'][node_name]['established'], summary['node'][node_name]['count'])
            if summary['node'][node_name]['established'] == summary['node'][node_name]['count']:
                summary['node'][node_name]['color'] = 'Green'
            else:
                summary['node'][node_name]['color'] = 'Red'

        return summary
    
    def is_bgp_session_state(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_bgp_session_state(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_bgp_session_state(self, namespace, name, storage_info=False, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'bgp_session_state', 
            name,
            namespace=namespace,
            storage_info=storage_info,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
    