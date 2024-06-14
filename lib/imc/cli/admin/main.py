class ImcCliAdmin():
    def __init__(self):
        pass

    def get_admin(
            self,
            all_info=False,
            fault_info=False,
            http_info=False,
            ip_info=False,
            ipmi_info=False,
            kvm_info=False,
            ntp_info=False,
            redfish_info=False,
            sel_info=False,
            smtp_info=False,
            snmp_info=False,
            sol_info=False,
            ssh_info=False,
            syslog_info=False,
            vmedia_info=False,
            cache_enabled=True,
            xml_info=False
        ):
        info = {}
        info['endpoint_ip'] = self.endpoint_ip

        if all_info or fault_info:
            info['fault'] = self.get_fault(cache_enabled=cache_enabled)

        if all_info or http_info:
            info['http'] = self.get_http(cache_enabled=cache_enabled)

        if all_info or ip_info:
            info['ip'] = self.get_ip(
                network_info=True,
                icmp_info=True,
                blocking_info=True,
                filtering_info=True,
                cache_enabled=cache_enabled
            )

        if all_info or ipmi_info:
            info['ipmi'] = self.get_ipmi(cache_enabled=cache_enabled)

        if all_info or kvm_info:
            info['kvm'] = self.get_kvm(cache_enabled=cache_enabled)

        if all_info or ntp_info:
            info['ntp'] = self.get_ntp(cache_enabled=cache_enabled)

        if all_info or redfish_info:
            info['redfish'] = self.get_redfish(cache_enabled=cache_enabled)

        if all_info or sel_info:
            info['sel'] = self.get_sel(cache_enabled=cache_enabled)

        if all_info or smtp_info:
            info['smtp'] = self.get_smtp(cache_enabled=cache_enabled)

        if all_info or snmp_info:
            info['snmp'] = self.get_snmp(cache_enabled=cache_enabled)

        if all_info or sol_info:
            info['sol'] = self.get_sol(cache_enabled=cache_enabled)

        if all_info or ssh_info:
            info['ssh'] = self.get_ssh(cache_enabled=cache_enabled)

        if all_info or syslog_info:
            info['syslog'] = self.get_syslog(cache_enabled=cache_enabled)

        if all_info or vmedia_info:
            info['vmedia'] = self.get_vmedia(cache_enabled=cache_enabled)

        if all_info or xml_info:
            info['xml'] = self.get_xml(cache_enabled=cache_enabled)

        return info
