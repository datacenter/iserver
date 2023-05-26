class Lldp():
    def __init__(self):
        pass

    def get_lldp_neighbors(self):
        command = 'show lldp neighbors'
        neighbors = self.get_command_cache(command)
        if neighbors is not None:
            return neighbors

        if not self.connect():
            return None

        response = self.run_show_command(command)
        if response is not None:
            neighbors = response['TABLE_nbor']['ROW_nbor']
            self.set_command_cache(command, neighbors)

        return neighbors

    def print_lldp_neighbors(self, info):
        order = [
            'l_port_id',
            'chassis_id',
            'port_id',
            'hold_time',
            'system_capability'
        ]

        headers = [
            'Local Interface',
            'Device ID',
            'Port ID',
            'Hold Time',
            'Capability'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
