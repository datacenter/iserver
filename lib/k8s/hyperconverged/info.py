class K8sHyperConvergedInfo():
    def __init__(self):
        self.hyperconverged = None

    def get_hyperconverged_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        info = self.add_tick(
            info, 
            'status:systemHealthStatus', 
            'healthy', 
            'healthyTick', 
            bool_attribute='healthy'
        )
        info = self.add_tick(
            info, 
            'status:infrastructureHighlyAvailable', 
            True, 
            'haTick', 
            bool_attribute='ha'
        )

        info['error'] = []
        conditions_mo = self.get(managed_object, 'status:conditions')
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

    def get_hyperconvergeds(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'hyperconverged', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_hyperconverged(self, return_mo=False, cache_enabled=True):
        hyperconvergeds = self.get_hyperconvergeds(
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if hyperconvergeds is None or len(hyperconvergeds) != 1:
            return None

        return hyperconvergeds[0]
    
    def is_hyperconverged(self, cache_enabled=True):
        if self.get_hyperconverged(cache_enabled=cache_enabled) is None:
            return False
        return True