import json


class IwoTarget():
    def __init__(self):
        pass

    def get_targets(self):
        url = '/wo/api/v3/targets'
        return self.get(url)

    def print_targets(self, targets):
        self.my_output.default(
            json.dumps(
                targets,
                indent=4
            )
        )
