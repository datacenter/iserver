class ConfigOutput():
    def __init__(self):
        pass

    def print_versions(self, info, title=False):
        if title:
            self.my_output.default(
                'Configuration [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return
