class ImcCliAdminOutput():
    def __init__(self):
        pass

    def print_imc_admin(self, info):
        if len(info) == 0:
            return

        # Communication services

        if 'http' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['http']
                )
            self.print_imc_http(
                values
            )

        if 'ssh' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['ssh']
                )
            self.print_imc_ssh(
                values
            )

        if 'tls' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['tls']
                )
            self.print_imc_tls(
                values
            )

        if 'xml' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['xml']
                )
            self.print_imc_xml(
                values
            )

        if 'redfish' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['redfish']
                )
            self.print_imc_redfish(
                values
            )

        if 'ipmi' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['ipmi']
                )
            self.print_imc_ipmi(
                values
            )

        if 'fault' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['fault']
                )
            self.print_imc_fault(
                values
            )

        if 'ip' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['ip']
                )
            self.print_imc_ip(
                values
            )

        if 'kvm' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['kvm']
                )
            self.print_imc_kvm(
                values
            )

        if 'ntp' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['ntp']
                )
            self.print_imc_ntp(
                values
            )

        if 'sel' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['sel']
                )
            self.print_imc_sel(
                values
            )

        if 'smtp' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['smtp']
                )
            self.print_imc_smtp(
                values
            )

        if 'snmp' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['snmp']
                )
            self.print_imc_snmp(
                values
            )

        if 'sol' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['sol']
                )
            self.print_imc_sol(
                values
            )

        if 'syslog' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['syslog']
                )
            self.print_imc_syslog(
                values
            )

        if 'vmedia' in info[0]:
            values = []
            for item in info:
                values.append(
                    item['vmedia']
                )
            self.print_imc_vmedia(
                values
            )
