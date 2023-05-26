import os
import sys

from lib import file_helper
from lib import template


class IwoOcpTemplateLcm():
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
                'iwo'
            ),
            'ocp'
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
            variables,
            check_remaining_variables=False
        )
        if content is None:
            self.my_output.error('Template failed: %s' % (template_filename))
            return None

        return content
