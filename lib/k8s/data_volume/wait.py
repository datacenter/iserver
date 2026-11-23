import time


class K8sDataVolumeWait():
    def __init__(self):
        pass

    def wait_data_volume(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='DataVolume', max_time=60):
        return self.wait_managed_object(
            'data_volume',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_data_volume(self, namespace, name, max_time=60, my_output=None, prompt='DataVolume'):
        return self.wait_no_managed_object(
            'data_volume',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='Wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
    
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
        if my_output is not None:
            my_output.default('Wait for data volume %s/%s uploaded...' % (namespace, name))

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