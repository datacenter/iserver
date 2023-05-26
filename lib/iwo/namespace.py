import json


class IwoNamespace():
    def __init__(self):
        self.mo_namespace = None

    def initialize_namespace(self):
        body = {}
        body['className'] = 'Namespace'

        self.mo_namespace = self.search(body)
        if self.mo_namespace is None:
            return False

        self.log.iwo_mo(
            'Namespace.attributes',
            self.mo_namespace
        )

        return True

    def get_namespace_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_namespaces(self):
        if self.mo_namespace is None:
            if not self.initialize_namespace():
                self.log.error(
                    'get_namespaces',
                    'Managed objects must be initialized first'
                )
                return None

        namespaces = []

        for managed_object in self.mo_namespace:
            namespace_info = self.get_namespace_info(
                managed_object
            )
            if namespace_info is not None:
                namespaces.append(
                    namespace_info
                )

        self.log.iwo_mo(
            'Namespace.info',
            self.mo_namespace
        )

        return namespaces

    def print_namespaces(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
