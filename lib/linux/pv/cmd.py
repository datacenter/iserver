class LinuxPvCmd():
    def __init__(self):
        self.pv_cmd = None

    def get_pv_cmd(self, cache_enabled=True):
        command = 'sudo pvs --reportformat json'

        if cache_enabled and self.pv_cmd is not None:
            return self.pv_cmd

        if cache_enabled:
            cache = self.get_cmd_cache(
                'pv'
            )
            if cache is not None:
                self.pv_cmd = cache
                return self.pv_cmd
        
        outputs = self.run_commands([command])
        if outputs is None:
            self.log.error(
                'get_pv_cmd',
                'Commands output collection failed'
            )
            return None

        self.pv_cmd = outputs[command]

        self.set_cmd_cache(
            'pv',
            self.pv_cmd
        )

        return self.pv_cmd

    def delete_pv_cmd(self, pv_name):
        success, output, error = self.ssh_handler.run_cmd(
            'sudo pvremove -f %s' % (pv_name)
        )
        
        if not success:
            return False, str(error)
        
        return True, str(output)