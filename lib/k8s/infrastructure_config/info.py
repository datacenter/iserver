from lib import ip_helper
from lib import filter_helper


class K8sInfrastructureConfigInfo():
    def __init__(self):
        self.infrastructure_config = None

    # https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/config_apis/infrastructure-config-openshift-io-v1#infrastructure-config-openshift-io-v1
    def get_infrastructure_config_info(self, infrastructure_config_mo):
        if infrastructure_config_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            infrastructure_config_mo
        )
        info.update(metadata_info)

        info['spec'] = infrastructure_config_mo['spec']
        info['status'] = infrastructure_config_mo['status']
        info['ingress_ips'] = filter_helper.get_attr(infrastructure_config_mo, 'spec:platformSpec:baremetal:ingressIPs')
        info['api_ips'] = filter_helper.get_attr(infrastructure_config_mo, 'spec:platformSpec:baremetal:apiServerInternalIPs')

        info['ingress_ip'] = None
        info['api_ip'] = None
        if info['ingress_ips'] is not None and len(info['ingress_ips']) > 0:
            info['ingress_ip'] = info['ingress_ips'][0]
        if info['api_ips'] is not None and len(info['api_ips']) > 0:
            info['api_ip'] = info['api_ips'][0]

        info['api_url'] = None
        info['api_hostname'] = None
        api_url = filter_helper.get_attr(infrastructure_config_mo, 'status:apiServerURL')
        if api_url is not None:
            info['api_url'] = api_url
            info['api_hostname'] = api_url.split('https://')[1].split(':')[0]

        # maybe corner-case or sno related
        if info['ingress_ip'] is None and info['api_ip'] is None and info['api_hostname'] is not None:
            address = ip_helper.get_ip(info['api_hostname'])
            if address is not None:
                info['api_ip'] = address
                info['ingress_ip'] = address
                
        return info

    def get_infrastructure_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.infrastructure_config is not None:
                return self.infrastructure_config

        managed_objects = self.get_infrastructure_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.infrastructure_config = []
        for managed_object in managed_objects:
            infrastructure_config_info = {}
            infrastructure_config_info['info'] = self.get_infrastructure_config_info(
                managed_object
            )
            infrastructure_config_info['mo'] = managed_object
            self.infrastructure_config.append(
                infrastructure_config_info
            )

        return self.infrastructure_config

    def match_infrastructure_config(self, infrastructure_config_info, infrastructure_config_filter):
        if infrastructure_config_filter is None or len(infrastructure_config_filter) == 0:
            return True

        for ap_rule in infrastructure_config_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, infrastructure_config_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_infrastructure_config',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_infrastructure_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_infrastructure_configs = self.get_infrastructure_configs_info(cache_enabled=cache_enabled)
        if all_infrastructure_configs is None:
            return None

        infrastructure_configs = []

        for infrastructure_config_info in all_infrastructure_configs:
            if not self.match_infrastructure_config(infrastructure_config_info['info'], object_filter):
                continue

            if return_mo:
                infrastructure_configs.append(
                    infrastructure_config_info['mo']
                )
                continue

            infrastructure_configs.append(
                infrastructure_config_info['info']
            )

        return infrastructure_configs

    def get_infrastructure_cluster_config(self, return_mo=False, cache_enabled=True):
        object_filter=['name:cluster']
        configs = self.get_infrastructure_configs(object_filter=object_filter, return_mo=return_mo, cache_enabled=cache_enabled)
        if configs is None or len(configs) != 1:
            return None
        return configs[0]
