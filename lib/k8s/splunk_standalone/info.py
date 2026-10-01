import base64


class K8sSplunkStandaloneInfo():
    def __init__(self):
        self.splunk_standalone = None

    def get_splunk_standalone_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        info['phase'] = self.get(managed_object, 'status:phase')
        info = self.add_tick(
            info, 
            'phase', 
            'Ready', 
            'readyTick', 
            bool_attribute='ready'
        )
        return info

    def get_splunk_standalone_extended_info(self, info):
        info['urlT'] = []
        if 'pod' in info:
            if info['pod'] is None:
                info['__Output']['podTick'] = 'Red'
                info['podTick'] = '\u2717'

            if info['pod'] is not None:
                if not info['pod']['running']:
                    info['__Output']['podTick'] = 'Red'
                    info['podTick'] = '\u2717'
                else:
                    info['__Output']['podTick'] = 'Green'
                    info['podTick'] = '\u2713'

        if 'pvc' in info:
            if info['pvc'] is None:
                info['__Output']['pvcTick'] = 'Red'
                info['pvcTick'] = '---'

            if info['pvc'] is not None:
                ready = 0
                for item in info['pvc']:
                    if item['ready']:
                        ready += 1

                if ready > 0 and ready == len(info['pvc']):
                    info['__Output']['pvcTick'] = 'Green'
                else:
                    info['__Output']['pvcTick'] = 'Red'

                info['pvcTick'] = '%s/%s' % (ready, len(info['pvc']))

        if 'service' in info:
            if info['service'] is None:
                info['__Output']['serviceTick'] = 'Red'
                info['serviceTick'] = '\u2717'

            if info['pod'] is not None:
                info['__Output']['serviceTick'] = 'Green'
                info['serviceTick'] = '\u2713'

        if 'route' in info:
            if info['route'] is None:
                info['__Output']['routeTick'] = 'Red'
                info['routeTick'] = '---'

            if info['route'] is not None:
                ready = 0
                for item in info['route']:
                    info['urlT'].append('http://%s' % (item['route']))
                    if item['ready']:
                        ready += 1

                if ready > 0 and ready == len(info['route']):
                    info['__Output']['routeTick'] = 'Green'
                else:
                    info['__Output']['routeTick'] = 'Red'

                info['routeTick'] = '%s/%s' % (ready, len(info['route']))

        info['credentials'] = {}
        if 'secret' in info and info['secret'] is not None:
            keys = [
                'hec_token',
                'idxc_secret',
                'pass4SymmKey',
                'password',
                'shc_secret'
            ]
            for key in keys:
                info['credentials'][key] = None
                key_mo = self.get(info['secret'], 'data:%s' % (key))
                if key_mo is not None:
                    info['credentials'][key] = base64.b64decode(
                        key_mo.encode('utf-8')
                    ).decode('utf-8')
            
            if info['credentials']['password'] is not None:
                info['urlT'].append('(admin, %s)' % (info['credentials']['password']))
                
        return info
    
    def get_splunk_standalones(self, object_filter=None, pod_info=False, pvc_info=False, service_info=False, route_info=False, secret_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'splunk_standalone', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        if infos is None or return_mo:
            return infos
        
        for info in infos:
            if pod_info:
                info['pod'] = self.get_pod(
                    info['namespace'],
                    'splunk-%s-standalone-0' % (info['name'])
                )

            if service_info:
                info['service'] = self.get_service(
                    info['namespace'],
                    'splunk-%s-standalone-service' % (info['name'])
                )

            if route_info:
                object_filter = []
                object_filter.append('namespace:%s' % (info['namespace']))
                object_filter.append('service:splunk-%s-standalone-service' % (info['name']))
                info['route'] = self.get_routes(
                    object_filter=object_filter
                )

            if secret_info:
                info['secret'] = self.get_secret(
                    info['namespace'],
                    'splunk-%s-standalone-secret-v1' % (info['name'])
                )

            if pvc_info:
                info['pvc'] = []
                
                pvc = self.get_pvc(
                    info['namespace'],
                    'pvc-etc-splunk-%s-standalone-0' % (info['name'])
                )
                if pvc is not None:
                    info['pvc'].append(pvc)

                pvc = self.get_pvc(
                    info['namespace'],
                    'pvc-var-splunk-%s-standalone-0' % (info['name'])
                )
                if pvc is not None:
                    info['pvc'].append(pvc)

            info = self.get_splunk_standalone_extended_info(
                info
            )

        return infos

    def get_splunk_standalone_names(self, cache_enabled=False):
        names = []
        standalones = self.get_splunk_standalones(cache_enabled=cache_enabled)
        if standalones is None:
            return None
        
        for standalone in standalones:
            names.append(
                dict(
                    namespace=standalone['namespace'],
                    name=standalone['name']
                )
            )

        return names

    def is_splunk_standalone(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_splunk_standalone(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_splunk_standalone(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'splunk_standalone', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )