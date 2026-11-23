class ConfigBotOutput():
    def __init__(self):
        pass

    def print_configs(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Configuration [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        output = self.my_output.get_output()

        self.my_output.clear_output()

        html_output = self.my_output.get_output()

        return output, html_output
