class ImcCliSmtpOutput():
    def __init__(self):
        pass

    def print_imc_smtp(self, info):
        self.print_list_dict(
            info,
            'SMTP'
        )

    def print_imc_smtp_compare(self, info):
        self.print_compare(
            info,
            'SMTP'
        )
