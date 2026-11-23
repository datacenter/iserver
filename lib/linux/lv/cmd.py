class LinuxLvCmd():
    def __init__(self):
        self.lv_cmd = None

    def get_lv_cmd(self, cache_enabled=True):
        command = 'sudo lvs --reportformat json -o all'

        if cache_enabled and self.lv_cmd is not None:
            return self.lv_cmd

        if cache_enabled:
            cache = self.get_cmd_cache(
                'lv'
            )
            if cache is not None:
                self.lv_cmd = cache
                return self.lv_cmd
        
        outputs = self.run_commands([command])
        if outputs is None:
            self.log.error(
                'get_lv_cmd',
                'Commands output collection failed'
            )
            return None

        self.lv_cmd = outputs[command]

        self.set_cmd_cache(
            'lv',
            self.lv_cmd
        )

        return self.lv_cmd

    def get_lv_display_cmd(self, lv_path, my_output=None):
        command = 'sudo lvdisplay %s' % (lv_path)
        success, output, error = self.ssh_handler.run_cmd(
            command
        )

        if my_output is not None:
            my_output.default('cmd: %s' % (command), before_newline=True)
            my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
            
        if not success:
            return False, str(error)
        
        return True, str(output)
    
    def delete_lv_cmd(self, lv_path, my_output=None):
        command = 'sudo lvremove -f %s' % (lv_path)
        success, output, error = self.ssh_handler.run_cmd(
            command
        )

        if my_output is not None:
            my_output.default('cmd: %s' % (command), before_newline=True)
            my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
            
        if not success:
            return False, str(error)
        
        return True, str(output)