class LinuxVgCmd():
    def __init__(self):
        self.vg_cmd = None

    def get_vg_cmd(self, cache_enabled=True):
        command = 'sudo vgs --reportformat json -o all'

        if cache_enabled and self.vg_cmd is not None:
            return self.vg_cmd

        if cache_enabled:
            cache = self.get_cmd_cache(
                'vg'
            )
            if cache is not None:
                self.vg_cmd = cache
                return self.vg_cmd
        
        outputs = self.run_commands([command])
        if outputs is None:
            self.log.error(
                'get_vg_cmd',
                'Commands output collection failed'
            )
            return None

        self.vg_cmd = outputs[command]

        self.set_cmd_cache(
            'vg',
            self.vg_cmd
        )

        return self.vg_cmd

    def deactivate_vg_cmd(self, vg_name):
        success, output, error = self.ssh_handler.run_cmd(
            'sudo vgchange -a n %s' % (vg_name)
        )
        
        if not success:
            return False, str(error)
        
        return True, str(output)
    
    def delete_vg_cmd(self, vg_name):
        success, output, error = self.ssh_handler.run_cmd(
            'sudo vgremove %s' % (vg_name)
        )
        
        if not success:
            return False, str(error)
        
        return True, str(output)
    