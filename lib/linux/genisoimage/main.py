import os
import uuid


class LinuxGenIsoImage():
    def __init__(self):
        pass

    def genisoimage(self, source_filepath, iso_filepath):
        remote_directory = '/tmp/%s' % (str(uuid.uuid4()))
        if not self.ssh_handler.create_directory(remote_directory):
            self.log.error(
                'genisoimage',
                'Upload directory create failed: %s' % (remote_directory)
            )
            return False

        remote_filepath = '%s/%s' % (
            remote_directory,
            os.path.basename(source_filepath)
        )

        success = self.ssh_handler.scp_file(
            source_filepath,
            remote_filepath,
            put=True
        )
        if not success:
            self.log.error(
                'genisoimage',
                'Iso source upload failed: %s => %s' % (source_filepath, remote_filepath)
            )
            return False

        remote_iso_filepath = '%s/%s' % (
            remote_directory,
            os.path.basename(iso_filepath)
        )
        command = 'genisoimage -r -o %s %s' % (
            remote_iso_filepath,
            remote_filepath
        )
        success, output, error = self.ssh_handler.run_cmd(
            command,
            live_output=False
        )
        if not success:
            self.log.error(
                'genisoimage',
                'Iso generation failed: %s' % (remote_iso_filepath)
            )
            self.log.error(
                'genisoimage',
                output
            )
            self.log.error(
                'genisoimage',
                error
            )
            return False

        self.log.debug(
            'genisoimage',
            'Iso generated: %s' % (remote_iso_filepath)
        )
        self.log.debug(
            'genisoimage',
            output
        )

        success = self.ssh_handler.scp_file(
            remote_iso_filepath,
            iso_filepath,
            put=False
        )
        if not success:
            self.log.error(
                'genisoimage',
                'Iso download failed: %s => %s' % (remote_iso_filepath, iso_filepath)
            )
            return False

        return True
