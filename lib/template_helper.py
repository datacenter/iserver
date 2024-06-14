import json
import copy
import os
import sys
import traceback

from lib import file_helper
from lib import log_helper


class TemplateHelper():
    def __init__(self):
        self.base_directory = os.path.join(
            file_helper.get_main_dir(),
            'templates'
        )
        self.log = log_helper.Log()

    def get_global_variables(self):
        try:
            content = self.get('global_variables.json')
            if content is None:
                return None

            variables = json.loads(content)
        except BaseException:
            self.log.error('template_helper.get_global_variables', traceback.format_exc())
            return None

        return variables

    def get(self, name):
        try:
            filename = os.path.join(self.base_directory, name)
            if not os.path.isfile(filename):
                return None

            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = file_handler.read()

        except BaseException:
            self.log.error('template_helper.get', traceback.format_exc())
            return None

        return content

    def replace_variables(self, content, variables):
        try:
            if content is None:
                return None

            if variables is None:
                return content

            my_variables = copy.deepcopy(variables)
            global_variables = self.get_global_variables()
            if global_variables is not None:
                for key in global_variables:
                    if key not in variables:
                        my_variables[key] = global_variables[key]

            for key in my_variables:
                pattern = '${%s}' % (key)
                if my_variables[key] is None:
                    self.log.error('template_helper.replace_variables', 'Variable is none: %s' % (key))
                    self.log.error('template_helper.replace_variables', json.dumps(my_variables, indent=4))
                    return None

                content = content.replace(pattern, my_variables[key])

        except BaseException:
            self.log.error('template_helper.replace_variables', traceback.format_exc())
            return None

        return content
