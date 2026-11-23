class K8sCsrOutput():
    def __init__(self):
        pass

    def print_csrs_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['CSR', 'name'],
                ['Age', 'age'],
                ['Flag', 'flagT'],
                ['Signer', 'signer'],
                ['Username', 'username']
            ]
        )

    def print_csrs_verbose(self, info):
        for item in info:
            self.print_csr(item)
    
    def print_csr(self, info):
        self.my_output.dictionary_ng(
            'Certificate Signing Request',
            info,
            [
                ['Name', 'name'],
                ['Age', 'age'],
                ['Flag', 'flagT'],
                ['Signer', 'signer'],
                ['Username', 'username'],
                ['Usage', 'usageT'],
                ['Group', 'groupT']
            ]
        )
        self.print_csr_request(info)
        self.print_csr_certificate(info)

    def print_csr_request(self, info):
        if info['csr_info'] is None:
            return

        self.my_output.dictionary_ng(
            'Request',
            info['csr_info'],
            [
                ['Subject', 'subject'],
                ['Sign Algo', 'sign_algo'],
                ['Hash Algo', 'hash_algo'],
                ['Valid', 'valid']
            ],
            underline=False,
            start=''
        )

    def print_csr_certificate(self, info):
        if info['certificate_info'] is None:
            return

        self.my_output.dictionary_ng(
            'Certificate',
            info['certificate_info'],
            [
                ['Version', 'version'],
                ['Subject', 'subject'],
                ['Issuer', 'issuer'],
                ['Serial', 'serial'],
                ['Sign Algo', 'sign_algo'],
                ['Hash Algo', 'hash_algo'],
                ['Valid From', 'valid_from'],
                ['Valid To', 'valid_to']
            ],
            underline=False,
            start=''
        )