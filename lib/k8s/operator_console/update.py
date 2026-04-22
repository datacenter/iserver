class K8sOperatorConsoleUpdate():
    def __init__(self):
        pass

    def update_operator_console(
            self, 
            body, 
            confirmation=False, 
            my_output=None
        ):
        if not self.patch_resource(body, object_name='operator_console', my_output=my_output, confirmation=confirmation):
            return False

        return True    