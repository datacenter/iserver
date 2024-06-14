class RedfishEndpointUcsRackTemplateRole():
    def __init__(self):
        self.role_uri = '/redfish/v1/AccountService/Roles'
        self.role = None

    def get_role_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.role is not None:
                return self.role

        self.role = []

        role_uris = self.endpoint_handler.get_odata_ids(self.role_uri)
        for role_uri in role_uris:
            if role_uri == self.role_uri:
                continue

            role_info = self.get_role_info(
                role_uri
            )

            self.role.append(
                role_info
            )

        return self.role

    def get_role_info(self, uri):
        info = {}
        info['__Output'] = {}
        info['Uri'] = uri

        data = self.get_properties(uri)

        info['id'] = self.get_property_value(
            data,
            'Id'
        )

        info['role_id'] = self.get_property_value(
            data,
            'RoleId'
        )

        info['name'] = self.get_property_value(
            data,
            'Name'
        )

        info['description'] = self.get_property_value(
            data,
            'Description'
        )

        info['privileges'] = self.get_property_value(
            data,
            'AssignedPrivileges'
        )

        info['oem'] = self.get_property_value(
            data,
            'OemPrivileges'
        )

        return info

    def get_template_role_properties(self, account_info=False, cache_enabled=True):
        roles = self.get_role_mo(cache_enabled=cache_enabled)
        for role in roles:
            if account_info:
                role['username'] = []
                role_accounts = self.get_accounts_with_role_id(
                    role['id']
                )
                if role_accounts is not None:
                    for role_account in role_accounts:
                        role['username'].append(
                            role_account['username']
                        )

        return roles

    def get_role_by_id(self, role_id):
        roles = self.get_template_role_properties()
        for role in roles:
            if role['id'] == role_id:
                return role
        return None
