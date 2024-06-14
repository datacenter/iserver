class ImcCliHardware():
    def __init__(self):
        pass

    def get_hardware(
            self,
            all_info=False,
            bbu_info=False,
            cpu_info=False,
            dimm_info=False,
            flex_info=False,
            hdd_info=False,
            memory_info=False,
            net_info=False,
            pci_info=False,
            psu_info=False,
            sc_info=False,
            tpm_info=False,
            vic_info=False,
            cache_enabled=True
        ):
        info = {}
        info['endpoint_ip'] = self.endpoint_ip

        if all_info or bbu_info:
            info['bbu'] = self.get_bbu(cache_enabled=cache_enabled)

        if all_info or cpu_info:
            info['cpu'] = self.get_cpu(cache_enabled=cache_enabled)

        if all_info or dimm_info:
            info['dimm'] = self.get_dimm(cache_enabled=cache_enabled)

        if all_info or hdd_info:
            info['hdd'] = self.get_hdd(cache_enabled=cache_enabled)

        if all_info or flex_info:
            info['flex'] = self.get_flex(cache_enabled=cache_enabled)

        if all_info or memory_info:
            info['memory'] = self.get_memory(cache_enabled=cache_enabled)

        if all_info or net_info:
            info['net'] = self.get_net(cache_enabled=cache_enabled)

        if all_info or pci_info:
            info['pci'] = self.get_pci(cache_enabled=cache_enabled)

        if all_info or psu_info:
            info['psu'] = self.get_psu(cache_enabled=cache_enabled)

        if all_info or sc_info:
            info['sc'] = self.get_storage_adapter(cache_enabled=cache_enabled)

        if all_info or tpm_info:
            info['tpm'] = self.get_tpm(cache_enabled=cache_enabled)

        if all_info or vic_info:
            info['vic'] = self.get_adapter(cache_enabled=cache_enabled)

        return info
