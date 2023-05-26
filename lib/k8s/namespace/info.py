class K8sNamespaceInfo():
    def __init__(self):
        pass

    def is_namespace_name(self, name):
        names = self.get_namespaces_name()
        if names is None:
            return False

        if name not in names:
            return False

        return True

    def get_namespaces_name(self):
        if not self.get_namespaces():
            return None

        names = []
        for namespace_mo in self.namespaces:
            names.append(
                namespace_mo['metadata']['name']
            )

        return names
