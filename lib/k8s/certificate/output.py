class K8sCertificateOutput():
    def __init__(self):
        pass

    def print_certificates_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Certificate', 'namespace_nameT'],
                ['Issuer', 'issuerT'],
                ['Secret', 'secretT'],
                ['Certificate', 'crtT'],
                ['Ready', 'readyT']
            ]
        )