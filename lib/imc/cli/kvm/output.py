class ImcCliKvmOutput():
    def __init__(self):
        pass

    def print_imc_kvm(self, info):
        self.print_list_dict(
            info,
            'KVM',
            add_endpoint_ip=True,
            underline=False,
            allow_order_subkeys=False
        )