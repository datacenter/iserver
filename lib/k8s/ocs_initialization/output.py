class K8sOcsInitializationOutput():
    def __init__(self):
        pass

    # Note: one object expected
    def print_ocs_initializations(self, info):
        if info is None:
            return
        
        for item in info:
            self.print_ocs_initialization(item)

    def print_ocs_initialization(self, info):
        order = [
            'namespace_name',
            'owner',
            'phase',
            'readyTick',
            'availableTick',
            'upgradeableTick'
        ]

        headers = [
            'Name',
            'Owner',
            'Phase',
            'Ready',
            'Available',
            'Upgradeable'
        ]

        self.my_output.dictionary(
            info,
            title='OCS Initialization',
            prefix='- ',
            keys=order,
            justify=True,
            values=order,
            title_keys=headers,
            start='\n\n'
        )
