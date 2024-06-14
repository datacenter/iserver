import os
import time
import uuid


class LinuxVirtctl():
    def __init__(self):
        pass

    def virtctl_image_upload(self, data_volume_namespace, data_volume_name, source_filename, max_attempts=1):
        attempt = 1
        while True:
            time.sleep(5)

            command = 'virtctl image-upload dv -n %s %s --no-create --insecure --image-path %s' % (
                data_volume_namespace,
                data_volume_name,
                source_filename
            )

            success, output, error = self.ssh_handler.run_cmd(
                command,
                live_output=False
            )
            if not success:
                self.log.error(
                    'virtctl_image_upload',
                    'Data volume upload failed: %s => %s' % (source_filename, data_volume_name)
                )
                self.log.error(
                    'virtctl_image_upload',
                    output
                )
                self.log.error(
                    'virtctl_image_upload',
                    error
                )
                attempt = attempt + 1
                if attempt > max_attempts:
                    return False

            if success:
                self.log.debug(
                    'virtctl_image_upload',
                    'Data volume uploaded: %s => %s' % (source_filename, data_volume_name)
                )
                self.log.debug(
                    'virtctl_image_upload',
                    output
                )

                break

        return True
