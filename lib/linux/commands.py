from progress.bar import IncrementalBar


class LinuxCommands():
    def __init__(self):
        pass

    def run_commands(self, commands, progress_bar=False):
        outputs = {}
        if progress_bar:
            bar_handler = IncrementalBar('Command', max=len(commands))
            bar_handler.goto(0)

        for command in commands:
            success, output, error = self.ssh_handler.run_cmd(
                command
            )
            if not success:
                self.my_output.error('Command failed: %s' % (command))
                self.my_output.default(error)
                return None

            outputs[command] = output
            if progress_bar:
                bar_handler.next()

        if progress_bar:
            bar_handler.finish()

        return outputs
