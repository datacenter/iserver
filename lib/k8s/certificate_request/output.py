class K8sCertificateRequestOutput():
    def __init__(self):
        pass

    def print_certificate_requests_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Certificate Request', 'namespace_nameT'],
                ['Approved', 'approvedTick'],
                ['Ready', 'readyTick'],
                ['Issuer', 'issuerT'],
                ['Requester', 'requester']
            ]
        )