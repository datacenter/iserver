class ImcCliAdminOutput():
    def __init__(self):
        pass

    def print_imc_admin(self, info):
        for item in info:
            self.my_output.default(
                'Endpoint: %s' % (item['endpoint_ip']),
                before_newline=True,
                underline=True
            )

            if 'fault' in item:
                self.print_imc_fault(item['fault'])

            if 'http' in item:
                self.print_imc_http(item['http'])

            if 'ip' in item:
                self.print_imc_ip(item['ip'])

            if 'ipmi' in item:
                self.print_imc_ipmi(item['ipmi'])

            if 'kvm' in item:
                self.print_imc_kvm(item['kvm'])

            if 'ntp' in item:
                self.print_imc_ntp(item['ntp'])

            if 'redfish' in item:
                self.print_imc_redfish(item['redfish'])

            if 'sel' in item:
                self.print_imc_sel(item['sel'])

            if 'smtp' in item:
                self.print_imc_smtp(item['smtp'])

            if 'snmp' in item:
                self.print_imc_snmp(item['snmp'])

            if 'sol' in item:
                self.print_imc_sol(item['sol'])

            if 'ssh' in item:
                self.print_imc_ssh(item['ssh'])

            if 'syslog' in item:
                self.print_imc_syslog(item['syslog'])

            if 'vmedia' in item:
                self.print_imc_vmedia(item['vmedia'])

            if 'xml' in item:
                self.print_imc_xml(item['xml'])
