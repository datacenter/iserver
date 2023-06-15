import os
import json
import traceback

from lib.settings_helper import Settings


class Context(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.context_filename = os.path.join(
            self.settings_dir,
            'context'
        )

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

    def get(self, key):
        contexts = self.get_contexts()
        if contexts is None:
            return None

        if key in contexts:
            return contexts[key]

        return None

    def get_contexts(self):
        if not os.path.isfile(self.context_filename):
            return {}

        try:
            with open(self.context_filename, 'r', encoding='utf-8') as file_handler:
                contexts = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_context', traceback.format_exc())
            return None

        return contexts

    def set(self, key, value):
        contexts = self.get_contexts()
        if contexts is None:
            return False

        contexts[key] = value
        return self.set_contexts(contexts)

    def set_contexts(self, contexts):
        try:
            with open(self.context_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(contexts, indent=4))

        except BaseException:
            self.log.error('set_contexts', traceback.format_exc())
            return False

        return True
