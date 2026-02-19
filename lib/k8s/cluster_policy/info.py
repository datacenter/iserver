import time
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sClusterPolicyInfo():
    def __init__(self):
        self.cluster_policy = None

    def get_cluster_policy_info(self, cluster_policy_mo):
        if cluster_policy_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            cluster_policy_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(cluster_policy_mo, 'spec')
        info['status'] = self.get(cluster_policy_mo, 'status')

        info['namespace'] = self.get(cluster_policy_mo, 'status:namespace')
        info['state'] = self.get(cluster_policy_mo, 'status:state')
        if info['state'] == 'ready':
            info['__Output']['state'] = 'Green'
            info['ready'] = True
        else:
            info['__Output']['state'] = 'Red'
            info['ready'] = False

        info['dcgmEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:dcgm:enabled', 
            on_error=False, 
            on_none=False
        )

        info['dcgmExporterEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:dcgmExporter:enabled', 
            on_error=False, 
            on_none=False
        )

        info['dcgmServiceMonitorEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:dcgmExporter:serviceMonitor:enabled', 
            on_error=False, 
            on_none=False
        )

        info['devicePluginEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:devicePlugin:enabled', 
            on_error=False, 
            on_none=False
        )

        info['driverEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:driver:enabled', 
            on_error=False, 
            on_none=False
        )

        info['driverEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:driver:enabled', 
            on_error=False, 
            on_none=False
        )

        info['gdrcopyEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:gdrcopy:enabled', 
            on_error=False, 
            on_none=False
        )

        info['gdsEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:gds:enabled', 
            on_error=False, 
            on_none=False
        )

        info['gfdEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:gfd:enabled', 
            on_error=False, 
            on_none=False
        )

        info['migStrategy'] = self.get(
            cluster_policy_mo, 
            'spec:mig:strategy'
        )

        info['migManagerEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:migManager:enabled'
        )

        info['nodeStatusExporterEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:nodeStatusExporter:enabled'
        )

        info['sandboxDevicePluginEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:sandboxDevicePlugin:enabled'
        )

        info['toolkitEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:toolkit:enabled'
        )

        info['vfioManagerEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:vfioManager:enabled'
        )

        info['vgpuDeviceManagerEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:vgpuDeviceManager:enabled'
        )

        info['vgpuManagerEnabled'] = self.get(
            cluster_policy_mo, 
            'spec:vgpuManager:enabled'
        )

        keys = [
            'dcgmEnabled',
            'dcgmExporterEnabled',
            'dcgmServiceMonitorEnabled',
            'devicePluginEnabled',
            'driverEnabled',
            'gdrcopyEnabled',
            'gdsEnabled',
            'gfdEnabled',
            'migManagerEnabled',
            'nodeStatusExporterEnabled',
            'sandboxDevicePluginEnabled',
            'toolkitEnabled',
            'vfioManagerEnabled',
            'vgpuDeviceManagerEnabled',
            'vgpuManagerEnabled'
        ]
        for key in keys:
            if info[key]:
                info['%sTick' % (key)] = '\u2713'
                info['__Output']['%sTick' % (key)] = 'Green'
            else:
                info['%sTick' % (key)] = '\u2717'
                info['__Output']['%sTick' % (key)] = 'Red'

        return info

    def add_cluster_policy_info(self, info, daemons_sets=None):
        if daemons_sets is not None:
            info['daemon_sets'] = []
            info['ds_desired'] = 0
            info['ds_available'] = 0

            for daemon_set in daemons_sets:
                if daemon_set['owner_kind'] is None:
                    continue

                if daemon_set['owner_kind'] != 'ClusterPolicy':
                    continue

                if daemon_set['owner_name'] != info['name']:
                    continue

                info['daemon_sets'].append(daemon_set)
                info['ds_desired'] += daemon_set['desiredNumberScheduled']
                info['ds_available'] += daemon_set['numberAvailable']

            info['ds_summary'] = '%s/%s' % (
                info['ds_desired'],
                info['ds_available']
            )
            if info['ds_desired'] == info['ds_available']:
                info['__Output']['ds_summary'] = 'Green'
            else:
                info['__Output']['ds_summary'] = 'Red'

        return info

    def get_cluster_policies_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cluster_policy is not None:
                return self.cluster_policy

        managed_objects = self.get_cluster_policy_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cluster_policy = []
        for managed_object in managed_objects:
            cluster_policy_info = {}
            cluster_policy_info['info'] = self.get_cluster_policy_info(
                managed_object
            )
            cluster_policy_info['mo'] = managed_object
            self.cluster_policy.append(
                cluster_policy_info
            )

        return self.cluster_policy

    def match_cluster_policy(self, cluster_policy_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cluster_policy_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cluster_policy',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cluster_policies(self, object_filter=None, ds_info=False, return_mo=False, cache_enabled=True):
        all_cluster_policies = self.get_cluster_policies_info(cache_enabled=cache_enabled)
        if all_cluster_policies is None:
            return None

        cluster_policies = []

        daemon_sets = None
        if ds_info:
            daemon_sets = self.get_daemon_sets(cache_enabled=cache_enabled)

        for cluster_policy_info in all_cluster_policies:
            cluster_policy_info['info'] = self.add_cluster_policy_info(
                cluster_policy_info['info'],
                daemons_sets=daemon_sets
            )
            
            if not self.match_cluster_policy(cluster_policy_info['info'], object_filter):
                continue

            if return_mo:
                cluster_policies.append(
                    cluster_policy_info['mo']
                )
                continue

            cluster_policies.append(
                cluster_policy_info['info']
            )

        return cluster_policies

    def is_cluster_policy(self, name, cache_enabled=True):
        if self.get_cluster_policy(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_cluster_policy(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        cluster_policies = self.get_cluster_policies(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if cluster_policies is None:
            return None

        if len(cluster_policies) == 1:
            return cluster_policies[0]

        return None

    def is_any_cluster_policy(self, cache_enabled=False):
        policies = self.get_cluster_policies(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True
