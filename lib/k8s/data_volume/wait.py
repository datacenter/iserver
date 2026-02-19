import time


class K8sDataVolumeWait():
    def __init__(self):
        pass

    def wait_data_volume(self, namespace, name, max_time=60, log_error_on_timeout=True):
        start_time = int(time.time())
        while True:
            info = self.get_data_volume(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    self.log.error(
                        'k8s.wait_data_volume',
                        'Max time reached: %s/%s' % (namespace, name)
                    )
                return False

            time.sleep(5)

    def wait_data_volume_upload_ready(self, namespace, name, max_time=300, log_error_on_timeout=True):
        start_time = int(time.time())
        while True:
            info = self.get_data_volume(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                if info['phase'] == 'UploadReady':
                    return True

                if info['phase'] == 'ImportInProgress':
                    return True
                
            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    self.log.error(
                        'k8s.wait_data_volume_upload_ready',
                        'Max time reached: %s/%s' % (namespace, name)
                    )
                return False

            time.sleep(5)

    def wait_data_volume_uploaded(self, namespace, name, max_time=900, log_error_on_timeout=True, my_output=None):
        start_time = int(time.time())
        last_progress = None
        while True:
            info = self.get_data_volume(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                if info['phase'] == 'Succeeded':
                    return True
                
                if my_output is not None:
                    if last_progress is None:
                        last_progress = info['progress']

                    if last_progress is not None and last_progress != info['progress']:
                        my_output.default('- progress: %s' % (info['progress']))
                
            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    self.log.error(
                        'k8s.wait_data_volume_upload_ready',
                        'Max time reached: %s/%s' % (namespace, name)
                    )
                return False

            time.sleep(5)

    def wait_no_data_volume(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_data_volume(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_data_volume',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
