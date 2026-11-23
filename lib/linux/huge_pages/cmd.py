class LinuxHugePagesCmd():
    def __init__(self):
        self.huge_pages_cmd = None

    def get_huge_pages_cmd(self):
        if self.huge_pages_cmd is not None:
            return self.huge_pages_cmd

        cache = self.get_cmd_cache(
            'huge_pages'
        )
        if cache is not None:
            self.huge_pages_cmd = cache
            return self.huge_pages_cmd

        self.huge_pages_cmd = {}
        self.huge_pages_cmd['node0'] = {}
        self.huge_pages_cmd['node0']['2M'] = {}
        self.huge_pages_cmd['node0']['2M']['total'] = self.ssh_handler.get_file(
            '/sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages'
        ).rstrip('\n')
        self.huge_pages_cmd['node0']['2M']['free'] = self.ssh_handler.get_file(
            '/sys/devices/system/node/node0/hugepages/hugepages-2048kB/free_hugepages'
        ).rstrip('\n')
        self.huge_pages_cmd['node0']['1G'] = {}
        self.huge_pages_cmd['node0']['1G']['total'] = self.ssh_handler.get_file(
            '/sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages'
        ).rstrip('\n')
        self.huge_pages_cmd['node0']['1G']['free'] = self.ssh_handler.get_file(
            '/sys/devices/system/node/node0/hugepages/hugepages-1048576kB/free_hugepages'
        ).rstrip('\n')

        self.huge_pages_cmd['node1'] = {}
        self.huge_pages_cmd['node1']['2M'] = {}
        self.huge_pages_cmd['node1']['2M']['total'] = self.ssh_handler.get_file(
            '/sys/devices/system/node/node1/hugepages/hugepages-2048kB/nr_hugepages'
        ).rstrip('\n')
        self.huge_pages_cmd['node1']['2M']['free'] = self.ssh_handler.get_file(
            '/sys/devices/system/node/node1/hugepages/hugepages-2048kB/free_hugepages'
        ).rstrip('\n')
        self.huge_pages_cmd['node1']['1G'] = {}
        self.huge_pages_cmd['node1']['1G']['total'] = self.ssh_handler.get_file(
            '/sys/devices/system/node/node1/hugepages/hugepages-1048576kB/nr_hugepages'
        ).rstrip('\n')
        self.huge_pages_cmd['node1']['1G']['free'] = self.ssh_handler.get_file(
            '/sys/devices/system/node/node1/hugepages/hugepages-1048576kB/free_hugepages'
        ).rstrip('\n')

        self.set_cmd_cache(
            'huge_pages',
            self.huge_pages_cmd
        )

        return self.huge_pages_cmd
