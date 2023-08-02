import os
import sys
import uuid

from lib import file_helper
from lib import ip_helper
from lib import template


class OcpCommon():
    def __init__(self):
        self.template_handler = template.Template(
            debug=False
        )

    def get_template_dir(self):
        template_dir = os.path.join(
            os.path.join(
                os.path.join(
                    file_helper.get_main_dir(),
                    'templates'
                ),
                'ocp'
            ),
            self.ocp_type
        )
        return template_dir

    def get_template_filename(self, filename):
        files_dir = os.path.join(
            self.get_template_dir(),
            'files'
        )
        template_filename = os.path.join(files_dir, filename)
        if not os.path.isfile(template_filename):
            self.my_output.error('Template file not found: %s' % (template_filename))
            return None

        return template_filename

    def get_template_content(self, filename, variables):
        template_filename = self.get_template_filename(filename)
        if template_filename is None:
            return None

        content = self.template_handler.get_template(
            template_filename,
            variables
        )
        if content is None:
            self.my_output.error('Template failed: %s' % (template_filename))
            return None

        return content

    def is_template_valid(self, filename, variables):
        content = self.get_template_content(filename, variables)
        if content is None:
            return False
        return True

    def is_source_local(self, source_filename):
        if source_filename.startswith('http://') or source_filename.startswith('https://'):
            return False
        return True

    def download_source_file(self, source_filename):
        self.my_output.default('Download file', underline=True, before_newline=True, after_newline=True)
        self.my_output.default('Source: %s' % (source_filename))
        destination_filename = '/tmp/%s' % (str(uuid.uuid4()))
        self.my_output.default('Destination: %s' % (destination_filename))

        if not ip_helper.download_url(source_filename, destination_filename):
            self.my_output.error('Web download failed')
            return None

        return destination_filename
