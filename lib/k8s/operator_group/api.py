import time
import traceback


class K8sOperatorGroupApi():
    def __init__(self):
        self.operator_group_mo = None
        self.operator_group_namespace_mo = {}

    def get_operator_group_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.operator_group_mo,
            self.operator_group_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.operator_group_mo, self.operator_group_namespace_mo = self.get_namespaced_resources(
            'OperatorGroup', 
            'operators.coreos.com/v1', 
            self.operator_group_mo,
            self.operator_group_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_operator_group_mo(self, namespace, name):
        return self.delete_resource('OperatorGroup', 'operators.coreos.com/v1', name, namespace=namespace)