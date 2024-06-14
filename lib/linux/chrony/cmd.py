class LinuxChronyCmd():
    def __init__(self):
        self.chrony_config_cmd = None
        self.chrony_tracking_cmd = None

    def get_chrony_config_cmd(self):
        if self.chrony_config_cmd is not None:
            return self.chrony_config_cmd

        cache = self.get_cmd_cache(
            'chrony.conf'
        )
        if cache is not None:
            self.chrony_config_cmd = cache
            return self.chrony_config_cmd

        filename = '/etc/chrony.conf'
        chrony_config = self.ssh_handler.get_file(
            filename
        )
        if chrony_config is None:
            self.log.debug(
                'get_chrony_config_cmd',
                'No chrony configuration file: %s' % (filename)
            )
            return None

        self.chrony_config_cmd = chrony_config
        return self.chrony_config_cmd

    def get_chrony_tracking_cmd(self):
        if self.chrony_tracking_cmd is not None:
            return self.chrony_tracking_cmd

        cache = self.get_cmd_cache(
            'chrony.tracking'
        )
        if cache is not None:
            self.chrony_tracking_cmd = cache
            return self.chrony_tracking_cmd

        command = 'chronyc tracking -n'
        success, output, error = self.ssh_handler.run_cmd(command)
        if not success:
            self.log.debug(
                'get_chrony_tracking_cmd',
                'Failed to get chrony state'
            )
            return None

        self.chrony_tracking_cmd = output
        return self.chrony_tracking_cmd
