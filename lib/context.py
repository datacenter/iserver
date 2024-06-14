import os

from lib.settings_helper import Settings
from lib import file_helper


class Context(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.context_dirname = os.path.join(
            self.settings_dir,
            'context'
        )

        self.initialize()

    def initialize(self):
        if os.path.isfile(self.context_dirname):
            os.remove(self.context_dirname)

        if not os.path.isdir(self.context_dirname):
            os.makedirs(self.context_dirname, exist_ok=True)

    def initialize_apic(self, apic_name):
        context = {}
        context['apic'] = [apic_name]
        context['node'] = {}
        context['node'][apic_name] = []
        context['interface'] = {}
        context['interface'][apic_name] = []
        return context

    def is_interface_defined(self, context):
        for apic_name in context['apic']:
            if len(context['interface'][apic_name]) > 0:
                return True
        return False

    def clear(self, key):
        filename = os.path.join(
            self.context_dirname,
            key
        )
        if os.path.isfile(filename):
            os.remove(filename)

        return True

    def get(self, key):
        filename = os.path.join(
            self.context_dirname,
            key
        )
        return file_helper.get_file_json(filename)

    def set(self, key, value):
        filename = os.path.join(
            self.context_dirname,
            key
        )
        return file_helper.set_file_json(filename, value)

    def append(self, key, value):
        values = self.get(key)
        if values is None:
            values = []

        if isinstance(value, list):
            values = values + value
        else:
            values.append(value)

        return self.set(key, values)
