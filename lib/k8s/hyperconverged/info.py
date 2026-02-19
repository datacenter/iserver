from lib import filter_helper


class K8sHyperConvergedInfo():
    def __init__(self):
        self.hyperconverged = None

    def get_hyperconverged_info(self, hyperconverged_mo):
        if hyperconverged_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            hyperconverged_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(hyperconverged_mo, 'spec')
        info['status'] = self.get(hyperconverged_mo, 'status')

        info['health_status'] = self.get(hyperconverged_mo, 'status:systemHealthStatus')
        if info['health_status'] is not None and info['health_status'].lower() == 'healthy':
            info['healthy'] = True
            info['healthyTick'] = '\u2713'
            info['__Output']['healthyTick'] = 'Green'
        else:
            info['healthy'] = False
            info['healthyTick'] = '\u2717'
            info['__Output']['healthyTick'] = 'Red'

        if self.get(hyperconverged_mo, 'status:infrastructureHighlyAvailable', on_error=False, on_none=False):
            info['ha'] = True
            info['haTick'] = '\u2713'
        else:
            info['ha'] = False
            info['haTick'] = '\u2717'

        info['error'] = []
        conditions_mo = self.get(hyperconverged_mo, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                condition_type = self.get(condition_mo, 'type')
                if condition_type is not None:
                    if condition_type == 'ReconcileComplete':
                        if self.get(condition_mo, 'status') == 'False':
                            info['error'].append('%s [%s]' % (condition_mo['message'], condition_mo['reason']))

                    if condition_type == 'Available':
                        if self.get(condition_mo, 'status') == 'False':
                            info['error'].append('%s [%s]' % (condition_mo['message'], condition_mo['reason']))

                    if condition_type == 'Progressing':
                        if self.get(condition_mo, 'status') == 'True':
                            info['error'].append('%s [%s]' % (condition_mo['message'], condition_mo['reason']))

                    if condition_type == 'Degraded':
                        if self.get(condition_mo, 'status') == 'True':
                            info['error'].append('%s [%s]' % (condition_mo['message'], condition_mo['reason']))

                    if condition_type == 'Upgradeable':
                        if self.get(condition_mo, 'status') == 'False':
                            info['error'].append('%s [%s]' % (condition_mo['message'], condition_mo['reason']))

        return info

    def get_hyperconvergeds_info(self, cache_enabled=True):
        if cache_enabled:
            if self.hyperconverged is not None:
                return self.hyperconverged

        managed_objects = self.get_hyperconverged_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.hyperconverged = []
        for managed_object in managed_objects:
            hyperconverged_info = {}
            hyperconverged_info['info'] = self.get_hyperconverged_info(
                managed_object
            )
            hyperconverged_info['mo'] = managed_object
            self.hyperconverged.append(
                hyperconverged_info
            )

        return self.hyperconverged

    def match_hyperconverged(self, hyperconverged_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, hyperconverged_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_hyperconverged',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_hyperconvergeds(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_hyperconvergeds = self.get_hyperconvergeds_info(cache_enabled=cache_enabled)
        if all_hyperconvergeds is None:
            return None

        hyperconvergeds = []

        for hyperconverged_info in all_hyperconvergeds:
            if not self.match_hyperconverged(hyperconverged_info['info'], object_filter):
                continue

            if return_mo:
                hyperconvergeds.append(
                    hyperconverged_info['mo']
                )
                continue

            hyperconvergeds.append(
                hyperconverged_info['info']
            )

        return hyperconvergeds

    def get_hyperconverged(self, return_mo=False, cache_enabled=True):
        hyperconvergeds = self.get_hyperconvergeds(
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if hyperconvergeds is None:
            return None

        if len(hyperconvergeds) != 1:
            return None

        return hyperconvergeds[0]
    
    def is_hyperconverged(self, cache_enabled=True):
        if self.get_hyperconverged(cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_hyperconverged_ready(self):
        for deployment in self.hyperconverged_deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name']):
                return False

        for daemon_set in self.hyperconverged_daemon_sets:
            if not self.is_daemon_set_ready(daemon_set['namespace'], daemon_set['name']):
                return False
            
        return True
    