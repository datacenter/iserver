class LinuxHelmCmd():
    def __init__(self):
        self.helm_repo_cmd = None
        self.helm_repo_cli = 'helm repo ls -o json'
        self.helm_chart_cmd = None
        self.helm_chart_cli = 'helm ls -A -o json'

    def get_helm_repo_cmd(self, cache_enabled=True):
        return self.get_cmd('helm_repo', cache_enabled=cache_enabled)
    
    def get_helm_chart_cmd(self, cache_enabled=True):
        return self.get_cmd('helm_chart', cache_enabled=cache_enabled)