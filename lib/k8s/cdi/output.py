class K8sCdiOutput():
    def __init__(self):
        pass

    # Note: one object expected
    def print_cdis(self, info):
        if info is None:
            return

        if len(info) == 0:
            self.my_output.default('No cdi', before_newline=True)
            return 
                
        for item in info:
            self.print_cdi(item)

    
    def print_cdi(self, item):
        self.my_output.dictionary_ng(
            'Containerized Data Importer (CDI)',
            item, 
            [
                ['Name', 'name'],
                ['Owner', 'owner'],
                ['Phase', 'phase'],
                ['Ready', 'readyTick']
            ]
        )