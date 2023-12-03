class ImcPsu():
    def __init__(self):
        pass

    def get_psu(self):
        commands = [
            'scope chassis',
            'show psu detail'
        ]

        success, output = self.run_commands(
            commands
        )

        if not success:
            return None

        # Name PSU1:
        #     In. Power (Watts): 150
        #     Out. Power (Watts): 123
        #     Firmware : 10252046
        #     Status : Present
        #     Product ID : UCSC-PSU1-1050W
        # Name PSU2:
        #     In. Power (Watts): 146
        #     Out. Power (Watts): 122
        #     Firmware : 10252046
        #     Status : Present
        #     Product ID : UCSC-PSU1-1050W

        psus = []
        psu_info = None
        for line in output['show psu detail'].split('\n'):
            if line.startswith('Name '):
                if psu_info is not None:
                    psus.append(
                        psu_info
                    )

                psu_info = {}
                psu_info['Name'] = line.split(':')[0].split(' ')[-1]
                continue

            if len(line.split(':')) == 2:
                key = line.split(':')[0].strip()
                value = line.split(':')[1].strip()
                if psu_info is not None:
                    psu_info[key] = value

        if psu_info is not None:
            psus.append(
                psu_info
            )

        return psus