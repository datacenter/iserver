class K8sServiceInfo():
    def __init__(self):
        pass

    def get_services_with_selector(self, selector_name, selector_value, namespace=None):
        if not self.get_services():
            return None

        services_mo = []
        for service_mo in self.services:
            if namespace is not None:
                if service_mo['metadata']['namespace'] != namespace:
                    continue

            if 'selector' not in service_mo['spec']:
                continue

            if service_mo['spec']['selector'] is None:
                continue

            for key in service_mo['spec']['selector']:
                if key == selector_name:
                    if service_mo['spec']['selector'][key] == selector_value:
                        services_mo.append(service_mo)

        return services_mo
