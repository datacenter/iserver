class K8sNimCacheOutput():
    def __init__(self):
        pass

    def print_nim_caches(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Nim Cache', 'namespace_nameT']
            ]
        )