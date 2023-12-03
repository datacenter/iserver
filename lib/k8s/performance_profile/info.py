from lib import filter_helper


class K8sPerformanceProfileInfo():
    def __init__(self):
        self.performance_profile = None

    def get_performance_profile_info(self, performance_profile_mo):
        if performance_profile_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            performance_profile_mo
        )
        info.update(metadata_info)

        conditions_mo = self.get(performance_profile_mo, 'status:conditions', on_error=[], on_none=[])

        info['available'] = None
        info['availableTick'] = '--'
        info['__Output']['availableTick'] = 'Red'
        for condition_mo in conditions_mo:
            if condition_mo['type'] == 'Available':
                if condition_mo['status'] == 'True':
                    info['available'] = True
                    info['availableTick'] = '\u2713'
                    info['__Output']['availableTick'] = 'Green'

                if condition_mo['status'] == 'False':
                    info['available'] = False
                    info['availableTick'] = '\u2717'
                    info['__Output']['availableTick'] = 'Red'

        info['upgradeable'] = None
        info['upgradeableTick'] = '--'
        info['__Output']['upgradeableTick'] = 'Red'
        for condition_mo in conditions_mo:
            if condition_mo['type'] == 'Upgradeable':
                if condition_mo['status'] == 'True':
                    info['upgradeable'] = True
                    info['upgradeableTick'] = '\u2713'
                    info['__Output']['upgradeableTick'] = 'Green'

                if condition_mo['status'] == 'False':
                    info['upgradeable'] = False
                    info['upgradeableTick'] = '\u2717'
                    info['__Output']['upgradeableTick'] = 'Red'

        info['progressing'] = None
        info['progressingTick'] = '--'
        info['__Output']['progressingTick'] = 'Red'
        for condition_mo in conditions_mo:
            if condition_mo['type'] == 'Progressing':
                if condition_mo['status'] == 'True':
                    info['progressing'] = True
                    info['progressingTick'] = '\u2713'
                    info['__Output']['progressingTick'] = 'Red'

                if condition_mo['status'] == 'False':
                    info['progressing'] = False
                    info['progressingTick'] = '\u2717'
                    info['__Output']['progressingTick'] = 'Green'

        info['degraded'] = None
        info['degradedTick'] = '--'
        info['__Output']['degradedTick'] = 'Red'
        for condition_mo in conditions_mo:
            if condition_mo['type'] == 'Degraded':
                if condition_mo['status'] == 'True':
                    info['degraded'] = True
                    info['degradedTick'] = '\u2713'
                    info['__Output']['degradedTick'] = 'Red'

                if condition_mo['status'] == 'False':
                    info['degraded'] = False
                    info['degradedTick'] = '\u2717'
                    info['__Output']['degradedTick'] = 'Green'

        info['cpu'] = {}
        info['cpu']['isolated'] = self.get(performance_profile_mo, 'spec:cpu:isolated', on_error=None, on_none=None)
        info['cpu']['reserved'] = self.get(performance_profile_mo, 'spec:cpu:reserved', on_error=None, on_none=None)
        info['cpu']['offlined'] = self.get(performance_profile_mo, 'spec:cpu:offlined', on_error=None, on_none=None)

        info['kernel'] = self.get(performance_profile_mo, 'spec:additionalKernelArgs', on_error=[], on_none=[])

        info['rt'] = {}
        info['rt']['enabled'] = self.get(performance_profile_mo, 'spec:realTimeKernel:enabled', on_error=False, on_none=False)
        if info['rt']['enabled']:
            info['rt']['enabledTick'] = '\u2713'
        else:
            info['rt']['enabledTick'] = '\u2717'

        info['hp'] = {}
        info['hp']['default_size'] = self.get(performance_profile_mo, 'spec:hugepages:defaultHugepagesSize', on_error=None, on_none=None)
        info['hp']['pages'] = self.get(performance_profile_mo, 'spec:hugepages:pages', on_error=[], on_none=[])
        for item in info['hp']['pages']:
            item['descr'] = 'Node:%s Size:%s Count:%s' % (
                item['node'],
                item['size'],
                item['count']
            )

        info['mcp_selector'] = []
        for key in self.get(performance_profile_mo, 'spec:machineConfigPoolSelector', on_error=[], on_none=[]):
            if key.startswith('pools.operator.machineconfiguration.openshift.io'):
                info['mcp_selector'].append(
                    'mcp:%s' % (key.split('/')[1])
                )
                continue
            info['mcp_selector'].append(key)

        info['node_selector'] = []
        for key in self.get(performance_profile_mo, 'spec:nodeSelector', on_error=[], on_none=[]):
            if key.startswith('node-role.kubernetes.io/master'):
                info['node_selector'].append(
                    'role:%s' % (key.split('/')[1])
                )
                continue
            info['node_selector'].append(key)

        info['numa'] = {}
        info['numa']['topology_policy'] = self.get(performance_profile_mo, 'spec:numa:topologyPolicy', on_error=None, on_none=None)

        info['hints'] = self.get(performance_profile_mo, 'spec:workloadHints', on_error=[], on_none=[])

        info['runtime_class'] = self.get(performance_profile_mo, 'status:runtimeClass', on_error=None, on_none=None)
        info['tuned'] = self.get(performance_profile_mo, 'status:tuned', on_error=None, on_none=None)

        return info

    def get_performance_profiles_info(self, cache_enabled=True):
        if cache_enabled:
            if self.performance_profile is not None:
                return self.performance_profile

        managed_objects = self.get_performance_profile_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.performance_profile = []
        for managed_object in managed_objects:
            performance_profile_info = {}
            performance_profile_info['info'] = self.get_performance_profile_info(
                managed_object
            )
            performance_profile_info['mo'] = managed_object
            self.performance_profile.append(
                performance_profile_info
            )

        return self.performance_profile

    def match_performance_profile(self, performance_profile_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, performance_profile_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_performance_profile',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_performance_profiles(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_performance_profiles = self.get_performance_profiles_info(cache_enabled=cache_enabled)
        if all_performance_profiles is None:
            return None

        performance_profiles = []

        for performance_profile_info in all_performance_profiles:
            if not self.match_performance_profile(performance_profile_info['info'], object_filter):
                continue

            if return_mo:
                performance_profiles.append(
                    performance_profile_info['mo']
                )
                continue

            performance_profiles.append(
                performance_profile_info['info']
            )

        return performance_profiles

    def is_performance_profile(self, name, cache_enabled=True):
        if self.get_performance_profile(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_performance_profile(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        performance_profiles = self.get_performance_profiles(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if performance_profiles is None:
            return None

        if len(performance_profiles) == 1:
            return performance_profiles[0]

        return None
