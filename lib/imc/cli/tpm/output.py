class ImcCliTpmOutput():
    def __init__(self):
        pass

    def print_imc_tpm(self, info):
        self.print_list_dict(
            info,
            'TPM'
        )

    def print_imc_tpm_compare(self, info):
        self.print_compare(
            info,
            'TPM'
        )
