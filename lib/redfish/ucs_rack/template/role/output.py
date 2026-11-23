class RedfishEndpointUcsRackTemplateRoleOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_role_properties(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Role', 'id'],
                ['RID', 'role_id'],
                ['Description', 'description'],
                ['Role Privileges', 'privileges'],
                ['Role Oem Privileges', 'oem'],
                ['Members', 'username']
            ]
        )
