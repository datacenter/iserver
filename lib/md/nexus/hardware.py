import os
from lib import file_helper


class MdNexusHardwareOutput():
    def __init__(self):
        pass

    def get_nexus_hardware_template_dir(self):
        main_dir = file_helper.get_main_dir()
        if main_dir is None:
            return None

        directory = os.path.join(
            os.path.join(
                os.path.join(
                    os.path.join(
                        main_dir,
                        'templates'
                    ),
                    'md'
                ),
                'nexus'
            ),
            'hw'
        )

        return directory

    def get_hardware_template_info(self, hw):
        base = self.get_nexus_hardware_template_dir()
        if base is None:
            return None

        directory = os.path.join(
            base,
            hw
        )
        if not os.path.isdir(directory):
            return None

        info = {}
        info['picture'] = {}

        for filename in os.listdir(directory):
            if filename.split('.')[-1] == 'md':
                info[filename.split('.')[0]] = file_helper.get_file_text(
                    os.path.join(directory, filename)
                )

            if filename.split('.')[-1] == 'png':
                info['picture'][filename.split('.')[0]] = os.path.join(directory, filename)

        return info

    def print_nexus_hardware_type(self, hw):
        info = self.get_hardware_template_info(hw)
        if info is None:
            return

        self.nexus_hw[hw] = hw

        self.print_page_header('Nexus Hardware - %s' % (hw))

        if 'switch' in info['picture']:
            self.my_output.print_stream(
                '![Switch](%s)' % (
                    os.path.basename(info['picture']['switch'])
                ),
                'output'
            )

        if 'description' in info:
            self.my_output.print_stream('## Description', 'output')
            self.my_output.print_stream('\n%s\n' % (info['description']), 'output')

        if 'specification' in info:
            self.my_output.print_stream('## Specification', 'output')
            self.my_output.print_stream('\n%s\n' % (info['specification']), 'output')

        if 'links' in info:
            self.my_output.print_stream('## Links', 'output')
            self.my_output.print_stream('\n%s\n' % (info['links']), 'output')

        self.save_output('README', subdir='nexus/hw/%s' % (hw))

        for key in info['picture']:
            self.copy_file(
                info['picture'][key],
                os.path.basename(info['picture'][key]),
                subdir='nexus/hw/%s' % (hw)
            )

    def print_nexus_hardware(self):
        for name in self.nexus_device_names:
            hw = self.xd_handler.nexus_hw[name]
            if hw is None or hw in self.nexus_hw:
                continue

            self.print_nexus_hardware_type(hw)
