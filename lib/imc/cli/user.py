class ImcCliUser():
    def __init__(self):
        pass

    def add_user(self, user_id, username, password, role):
        commands = [
            'scope user %s' % (user_id),
            'set enabled yes',
            'set name %s' % (username),
            'set password',
            password,
            password,
            'set role %s' % (role),
            'commit'
        ]

        success, output = self.run_commands(
            commands
        )

        return success

    def set_user(self, user_id, password, role):
        commands = [
            'scope user %s' % (user_id),
            'set password',
            password,
            password,
            'set role %s' % (role),
            'commit'
        ]

        success, output = self.run_commands(
            commands
        )

        return success

    def delete_user(self, user_id):
        commands = [
            'scope user %s' % (user_id),
            'restore',
            'yes'
        ]

        success, output = self.run_commands(
            commands
        )

        return success
