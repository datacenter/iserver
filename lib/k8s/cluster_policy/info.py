import time
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sClusterPolicyInfo():
    def __init__(self):
        self.cluster_policy = None

    def get_cluster_policy_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

        info['namespace'] = self.get(managed_object, 'status:namespace')
        info['state'] = self.get(managed_object, 'status:state')
        if info['state'] == 'ready':
            info['__Output']['state'] = 'Green'
            info['ready'] = True
        else:
            info['__Output']['state'] = 'Red'
            info['ready'] = False

        info['dcgmEnabled'] = self.get(
            managed_object, 
            'spec:dcgm:enabled', 
            on_error=False, 
            on_none=False
        )

        info['dcgmExporterEnabled'] = self.get(
            managed_object, 
            'spec:dcgmExporter:enabled', 
            on_error=False, 
            on_none=False
        )

        info['dcgmServiceMonitorEnabled'] = self.get(
            managed_object, 
            'spec:dcgmExporter:serviceMonitor:enabled', 
            on_error=False, 
            on_none=False
        )

        info['devicePluginEnabled'] = self.get(
            managed_object, 
            'spec:devicePlugin:enabled', 
            on_error=False, 
            on_none=False
        )

        info['driverEnabled'] = self.get(
            managed_object, 
            'spec:driver:enabled', 
            on_error=False, 
            on_none=False
        )

        info['driverEnabled'] = self.get(
            managed_object, 
            'spec:driver:enabled', 
            on_error=False, 
            on_none=False
        )

        info['gdrcopyEnabled'] = self.get(
            managed_object, 
            'spec:gdrcopy:enabled', 
            on_error=False, 
            on_none=False
        )

        info['gdsEnabled'] = self.get(
            managed_object, 
            'spec:gds:enabled', 
            on_error=False, 
            on_none=False
        )

        info['gfdEnabled'] = self.get(
            managed_object, 
            'spec:gfd:enabled', 
            on_error=False, 
            on_none=False
        )

        info['migStrategy'] = self.get(
            managed_object, 
            'spec:mig:strategy'
        )

        info['migManagerEnabled'] = self.get(
            managed_object, 
            'spec:migManager:enabled'
        )

        info['nodeStatusExporterEnabled'] = self.get(
            managed_object, 
            'spec:nodeStatusExporter:enabled'
        )

        info['sandboxDevicePluginEnabled'] = self.get(
            managed_object, 
            'spec:sandboxDevicePlugin:enabled'
        )

        info['toolkitEnabled'] = self.get(
            managed_object, 
            'spec:toolkit:enabled'
        )

        info['vfioManagerEnabled'] = self.get(
            managed_object, 
            'spec:vfioManager:enabled'
        )

        info['vgpuDeviceManagerEnabled'] = self.get(
            managed_object, 
            'spec:vgpuDeviceManager:enabled'
        )

        info['vgpuManagerEnabled'] = self.get(
            managed_object, 
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

    def get_cluster_policies(self, object_filter=None, ds_info=False, return_mo=False, cache_enabled=True):
        all_cluster_policies = self.get_infos(
            'cluster_policy', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        if all_cluster_policies is None:
            return None

        cluster_policies = []

        daemon_sets = None
        if ds_info:
            daemon_sets = self.get_daemon_sets(cache_enabled=cache_enabled)

        for cluster_policy_info in all_cluster_policies:
            cluster_policy_info = self.add_cluster_policy_info(
                cluster_policy_info,
                daemons_sets=daemon_sets
            )
            
            cluster_policies.append(
                cluster_policy_info
            )

        return cluster_policies

    def get_cluster_policy(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'cluster_policy', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_cluster_policy(self, name, cache_enabled=True, optimized=True):
        if self.get_cluster_policy(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_cluster_policy(self, cache_enabled=True):
        infos = self.get_cluster_policys(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True
