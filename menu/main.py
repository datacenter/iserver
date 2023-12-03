import json
import os
import sys
import uuid
import time
import subprocess
import click

from menu.create.main import create_menu
from menu.delete.main import delete_menu
from menu.get.main import get_menu
from menu.set.main import set_menu
from menu.settings.main import settings_menu
from menu.utils.main import utils_menu

from lib import output_helper
from lib import log_helper
from lib import settings_helper

COMMAND = None


class MyCliContext():
    def __init__(self, user_command):
        self.run_id = str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1]

        self.my_output = output_helper.OutputHelper(log_id=self.run_id)
        self.my_output.initialize()

        self.developer = False
        self.output = 'default'
        self.busy = False
        self.start_time = int(time.time() * 1000)

        self.log = log_helper.Log(log_id=self.run_id)
        self.log.initialize()
        self.log.set_command(user_command)
        self.log_prompt = True

        my_settings = settings_helper.Settings()
        self.defaults = {}
        self.defaults['iaccount'] = my_settings.get_setting('iaccount', default=None)


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    if getattr(sys, 'frozen', False):
        bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        version_filename = os.path.abspath(os.path.join(bundle_dir, 'version'))
    else:
        bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        main_dir = os.path.dirname(bundle_dir)
        version_filename = os.path.abspath(os.path.join(main_dir, 'version'))

    try:
        with open(version_filename, 'r', encoding='utf-8') as file_handler:
            version = file_handler.read()

    except BaseException:
        version = 'unknown'

    click.echo('Version %s' % (version))
    click.echo('Project: https://wwwin-github.cisco.com/emear-telcocloud/iserver')
    ctx.exit()


def check_isctl():
    try:
        command = 'isctl version'
        with subprocess.Popen(
            args=command,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
            env=os.environ
        ) as process:
            output, error = process.communicate()
            if process.returncode == 0:
                return True, output.decode('utf-8')
            return False, 'isctl command execution failed'
    except BaseException:
        return False, 'Exception in running isctl command'


def check_isctl_version(output, min_required):
    try:
        version_index = output.split(' ')[2].split('.')
        min_required_index = min_required.split('.')

        if len(version_index) != len(min_required_index):
            return False

        # pylint: disable=consider-using-enumerate
        for index in range(0, len(version_index)):
            if version_index[index] < min_required_index[index]:
                return False

    except BaseException:
        return False

    return True


def check_isctl_option(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    success, reason = check_isctl()
    if success:
        click.echo('[SUCCESS] isctl found')
        click.echo(reason)
    else:
        click.echo('[ERROR] %s' % (reason))

    ctx.exit()


@click.pass_obj
def _on_close(ctx):
    log_handler = log_helper.Log(log_id=ctx.run_id)

    duration = int(time.time() * 1000) - ctx.start_time

    log_analyzis = log_handler.analyze(duration)
    ctx.my_output.duration(json.dumps(log_analyzis, indent=4))

    all_logs = log_handler.get_logs()

    if ctx.developer:
        ctx.my_output.default('\nDeveloper output\n')
        ctx.my_output.default(json.dumps(log_analyzis, indent=4))
        ctx.my_output.my_logs(all_logs, stream='default')
    else:
        ctx.my_output.devel(json.dumps(log_analyzis, indent=4))
        ctx.my_output.my_logs(all_logs, stream='devel')

    command = log_handler.get_command()
    error_exit = False
    clean_logs = True
    if command is not None:
        no_log = False
        for item in ['utils devel cli']:
            if item in command:
                no_log = True

        if not no_log:
            if ctx.log_prompt:
                if log_analyzis['cache_hits'] > 0:
                    print('\nInfo: finished in %s ms and logs saved in %s incl. cache hits' % (duration, ctx.log.logs_directory))
                else:
                    print('\nInfo: finished in %s ms and logs saved in %s' % (duration, ctx.log.logs_directory))

                if ctx.log.is_log('error'):
                    print(
                        '%s: errors found in %s' % (
                            ctx.my_output.add_color('Warning', 'Red'),
                            ctx.log.get_log_filename('error')
                        )
                    )
                    error_exit = True

            clean_logs = False

    if clean_logs:
        log_handler.clean()

    if error_exit:
        sys.exit(1)


@click.group("main")
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click.option('--check-isctl', is_flag=True, callback=check_isctl_option,
              expose_value=False, is_eager=True)
@click.pass_context
def cli(ctx):
    """iServer CLI"""
    ctx.obj = MyCliContext(COMMAND)
    ctx.call_on_close(_on_close)


cli.add_command(create_menu)
cli.add_command(get_menu)
cli.add_command(delete_menu)
cli.add_command(set_menu)
cli.add_command(settings_menu)
cli.add_command(utils_menu)


def run(user_input):
    global COMMAND
    COMMAND = user_input
    cli(None)
