import time

from lib import filter_helper


class K8sMachineConfigPoolInfo():
    def __init__(self):
        self.machine_config_pool = None

    def get_machine_config_pool_info(self, machine_config_pool_mo):
        if machine_config_pool_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['name'] = self.get(machine_config_pool_mo, 'metadata:name')

        conditions_mo = self.get(machine_config_pool_mo, 'status:conditions', on_error=[], on_none=[])

        info['updated'] = None
        info['updatedTick'] = '--'
        info['__Output']['updatedTick'] = 'Red'
        for condition_mo in conditions_mo:
            if condition_mo['type'] == 'Updated':
                if condition_mo['status'] == 'True':
                    info['updated'] = True
                    info['updatedTick'] = '\u2713'
                    info['__Output']['updatedTick'] = 'Green'

                if condition_mo['status'] == 'False':
                    info['updated'] = False
                    info['updatedTick'] = '\u2717'
                    info['__Output']['updatedTick'] = 'Red'

        info['updating'] = None
        info['updatingTick'] = '--'
        info['__Output']['updatingTick'] = 'Red'
        for condition_mo in conditions_mo:
            if condition_mo['type'] == 'Updating':
                if condition_mo['status'] == 'True':
                    info['updating'] = True
                    info['updatingTick'] = '\u2713'
                    info['__Output']['updatingTick'] = 'Red'

                if condition_mo['status'] == 'False':
                    info['updating'] = False
                    info['updatingTick'] = '\u2717'
                    info['__Output']['updatingTick'] = 'Green'

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

        keys = [
            'degradedMachineCount',
            'machineCount',
            'observedGeneration',
            'readyMachineCount',
            'unavailableMachineCount',
            'updatedMachineCount'
        ]
        for key in keys:
            info[key] = self.get(machine_config_pool_mo, 'status:%s' % (key), on_error=-1, on_none=-1)

        info['target_configuration'] = self.get(machine_config_pool_mo, 'spec:configuration:name')
        info['current_configuration'] = self.get(machine_config_pool_mo, 'status:configuration:name')

        info['source'] = self.get(machine_config_pool_mo, 'status:configuration:source', on_error=[], on_none=[])

        info['machine_config_selector'] = self.get(machine_config_pool_mo, 'spec:machineConfigSelector', on_error={}, on_none={})
        info['node_selector'] = self.get(machine_config_pool_mo, 'spec:nodeSelector', on_error={}, on_none={})

        info['ready'] = True
        if info['degraded']:
            info['ready'] = False
        if info['updating']:
            info['ready'] = False

        info['age'] = self.convert_timestamp_to_age(
            self.get(machine_config_pool_mo, 'metadata:creationTimestamp'),
            on_error='--'
        )

        return info

    def add_machine_config_pool_selector_info(self, machine_config_pool_info):
        machine_config_pool_info['candidate_machine_configs'] = []
        if 'matchLabels' in machine_config_pool_info['machine_config_selector']:
            machine_config_filter = []
            for machine_config_match_label in machine_config_pool_info['machine_config_selector']['matchLabels']:
                machine_config_filter.append(
                    'label:%s:%s' % (
                        machine_config_match_label,
                        machine_config_pool_info['machine_config_selector']['matchLabels'][machine_config_match_label]
                    )
                )

            machine_configs = self.get_machine_configs(
                object_filter=machine_config_filter
            )
            if machine_configs is not None:
                for machine_config in machine_configs:
                    machine_config_pool_info['candidate_machine_configs'].append(
                        machine_config['name']
                    )

        machine_config_pool_info['candidate_nodes'] = []
        if 'matchLabels' in machine_config_pool_info['node_selector']:
            node_filter = []
            for node_match_label in machine_config_pool_info['node_selector']['matchLabels']:
                node_filter.append(
                    'label:%s:%s' % (
                        node_match_label,
                        machine_config_pool_info['node_selector']['matchLabels'][node_match_label]
                    )
                )

            nodes = self.get_nodes(
                object_filter=node_filter
            )
            if nodes is not None:
                for node in nodes:
                    machine_config_pool_info['candidate_nodes'].append(
                        node['name']
                    )

        return machine_config_pool_info

    def get_machine_config_pools_info(self, cache_enabled=True):
        if cache_enabled:
            if self.machine_config_pool is not None:
                return self.machine_config_pool

        managed_objects = self.get_machine_config_pool_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.machine_config_pool = []
        for managed_object in managed_objects:
            machine_config_pool_info = {}
            machine_config_pool_info['info'] = self.get_machine_config_pool_info(
                managed_object
            )
            machine_config_pool_info['mo'] = managed_object
            self.machine_config_pool.append(
                machine_config_pool_info
            )

        return self.machine_config_pool

    def match_machine_config_pool(self, machine_config_pool_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, machine_config_pool_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_machine_config_pool',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_machine_config_pools(self, object_filter=None, return_mo=False, cache_enabled=True, selector_info=False):
        all_machine_config_pools = self.get_machine_config_pools_info(cache_enabled=cache_enabled)
        if all_machine_config_pools is None:
            return None

        machine_config_pools = []

        for machine_config_pool_info in all_machine_config_pools:
            if not self.match_machine_config_pool(machine_config_pool_info['info'], object_filter):
                continue

            if return_mo:
                machine_config_pools.append(
                    machine_config_pool_info['mo']
                )
                continue

            if selector_info:
                machine_config_pool_info['info'] = self.add_machine_config_pool_selector_info(
                    machine_config_pool_info['info']
                )

            machine_config_pools.append(
                machine_config_pool_info['info']
            )

        return machine_config_pools

    def is_machine_config_pool(self, name, cache_enabled=True):
        if self.get_machine_config_pool(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_machine_config_pool(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        machine_config_pools = self.get_machine_config_pools(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if machine_config_pools is None:
            return None

        if len(machine_config_pools) == 1:
            return machine_config_pools[0]

        return None

    def wait_machine_config_pool_update(self, machine_config_pools, machine_configs, output_handler=None, max_time=3600):
        target_mcp = []
        mcp_configurations = {}
        for machine_config_pool in machine_config_pools:
            mcp_configurations[machine_config_pool['name']] = machine_config_pool['current_configuration']
            for source in machine_config_pool['source']:
                if source['name'] in machine_configs:
                    if machine_config_pool['name'] not in target_mcp:
                        target_mcp.append(machine_config_pool['name'])

        if len(target_mcp) == 0:
            if output_handler is not None:
                output_handler.default('No machine config pool update expected')
            return True

        if output_handler is not None:
            output_handler.default('Wait for machine config pool update...')
            for name in target_mcp:
                output_handler.default('- %s' % (name))

        finished_mcp = []
        start_time = int(time.time())
        while True:
            for mcp in target_mcp:
                if mcp in finished_mcp:
                    continue

                mcp_info = self.get_machine_config_pool(
                    mcp,
                    cache_enabled=False
                )
                if mcp_info is None:
                    continue

                if mcp_info['updating']:
                    continue

                if mcp_info['current_configuration'] == mcp_configurations[mcp]:
                    continue

                finished_mcp.append(mcp)

            if len(target_mcp) == len(finished_mcp):
                break

            if int(time.time()) - start_time > max_time:
                if output_handler is not None:
                    output_handler.error('Max waiting time elapsed [%s seconds]' % (max_time))
                return False

            time.sleep(5)

        return True

    def is_machine_config_pools_ready(self, machine_config_pools=None, cache_enabled=False):
        if machine_config_pools is None:
            machine_config_pools = self.get_machine_config_pools(cache_enabled=cache_enabled)
            if machine_config_pools is None:
                return False

        ready = True
        for pool in machine_config_pools:
            ready = ready and pool['ready']

        return ready
