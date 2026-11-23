class LinuxCrictlOutput():
    def __init__(self):
        pass

    def print_linux_crictl_ps(self, info):
        self.my_table(
            info,
            [
                ['Container', 'id'],
                ['Name', 'name'],
                ['Image', 'image'],
                ['State', 'stateT'],
                ['POD Namespace', 'pod_namespace'],
                ['POD Name', 'pod_name'],
                ['POD Restart', 'pod_restart']
            ]
        )