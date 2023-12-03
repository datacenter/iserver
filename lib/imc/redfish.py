class ImcRedfish():
    def __init__(self):
        pass

    def enable_redfish(self):
        commands = [
            'scope redfish',
            'set enabled yes',
            'commit'
        ]

        success, output = self.run_commands(
            commands
        )

        return success

    def disable_redfish(self):
        commands = [
            'scope redfish',
            'set enabled no',
            'commit'
        ]

        success, output = self.run_commands(
            commands
        )

        return success
