class K8sDnsOutput():
    def __init__(self):
        pass

    def print_dns(self, info):
        self.my_output.default('Base domain: %s' % (info['domain']))
        