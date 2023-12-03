class ImcVersion():
    def __init__(self):
        pass

    def get_version(self):
        commands = [
            'show version'
        ]

        success, output = self.run_commands(
            commands
        )

        if not success:
            return None

        return output['show version'].split('\n')[:-1]