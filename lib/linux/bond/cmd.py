class LinuxBondCmd():
    def __init__(self):
        self.bond_cmd = None

    def get_bond_cmd(self):
        if self.bond_cmd is not None:
            return self.bond_cmd

        cache = self.get_cmd_cache(
            'bond'
        )
        if cache is not None:
            self.bond_cmd = cache
            return self.bond_cmd

        directory_name = '/proc/net/bonding'
        bond_filenames = self.ssh_handler.get_filenames(
            directory_name
        )
        if bond_filenames is None:
            self.log.debug(
                'get_bond_cmd',
                'No bonding files: %s' % (directory_name)
            )
            return None

        self.bond_cmd = {}
        success = True
        for bond_filename in bond_filenames:
            bond_name = bond_filename.split('/')[-1]
            content = self.ssh_handler.get_file(
                bond_filename
            )
            if content is None:
                success = False
                self.log.error(
                    'get_bond_cmd',
                    'Failed to get file: %s' % (bond_filename)
                )
                continue

            self.bond_cmd[bond_name] = content

        if success:
            self.set_cmd_cache(
                'bond',
                self.bond_cmd
            )

        return self.bond_cmd
