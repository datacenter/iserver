class K8sOperatorConsoleApi():
    def __init__(self):
        self.operator_console_mo = None

    def get_operator_console_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.operator_console_mo
        )
        if cache_hit:
            return response

        response, self.operator_console_mo = self.get_resources(
            'Console', 
            'operator.openshift.io/v1', 
            self.operator_console_mo,
            name=name
        )

        return response