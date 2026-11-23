class RedfishEndpointUcsRackTemplateAccountOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_account_properties(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Username', 'username'],
                ['UID', 'id'],
                ['Description', 'description'],
                ['Role Id', 'role_id'],
                ['Enabled', 'enabledTick'],
                ['Change Req', 'changeTick'],
                ['Role Privileges', 'privileges'],
                ['Role Oem Privileges', 'oem']
            ]
        )
