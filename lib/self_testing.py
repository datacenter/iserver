import json
import datetime
import os
import re
import sys
import time
import subprocess
import traceback
import shutil
import platform

from progress.bar import Bar

from lib import log_helper
from lib import template_helper
from lib import isctl_helper


def print_traceback(info):
    print(info)


def print_error(output):
    print('[ERROR] %s' % (output))


def tests_fixup(directory):
    if not os.path.isdir(directory):
        return

    for test_filename in os.listdir(directory):
        print('Test: %s' % (test_filename))

        filename = os.path.join(directory, test_filename)
        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = json.loads(file_handler.read())

        except BaseException:
            print('Read failed: %s' % (filename))
            sys.exit(1)

        try:
            if 'name' in content:
                del content['name']

                with open(filename, 'w', encoding='utf-8') as file_handler:
                    file_handler.write(json.dumps(content, indent=4))

                print('- name key removed')
        except BaseException:
            print('Fixup failed: %s' % (filename))
            sys.exit(1)

        if filename.endswith('.json'):
            dst = os.path.join(directory, test_filename.rstrip('json').rstrip('.'))
            shutil.move(filename, dst)
            print('- filename changed %s' % (dst))

        if filename.endswith('.collection'):
            dst = os.path.join(directory, test_filename.rstrip('collection').rstrip('.'))
            shutil.move(filename, dst)
            print('- filename changed %s' % (dst))


def get_test_iaccount(test_filename, directory):
    test_definition = get_test(
        test_filename,
        directory
    )

    if test_definition is None:
        print('Test not found: %s' % (test_filename))
        sys.exit(1)

    if 'iaccount' not in test_definition:
        return None

    return test_definition['iaccount']


def get_test_environment(test_filename, directory):
    test_definition = get_test(
        test_filename,
        directory
    )

    if 'environment' not in test_definition:
        return None

    return test_definition['environment']


def get_test_commands(test):
    iserver_prefix = get_iserver_prefix()
    commands = []
    if 'help' in test:
        filename = '%s.%s' % (test['name'], 'help')
        command = '%s %s' % (iserver_prefix, test['help'])
        commands.append(command)

    if 'functionality' in test:
        for key in test['functionality']:
            filename = '%s.%s' % (test['name'], key)
            command = '%s %s' % (iserver_prefix, test['functionality'][key])
            commands.append(command)

    if 'negative' in test:
        for key in test['negative']:
            filename = '%s.%s' % (test['name'], key)
            command = '%s %s' % (iserver_prefix, test['negative'][key])
            commands.append(command)

    return commands


def get_summary(directory, replace=True):
    results = get_test_results()
    duration = 0
    for result in results:
        duration = duration + result['duration']

    tests, tests_count = get_tests_collection('all', directory)
    commands = []
    for test in tests:
        test_commands = get_test_commands(test)
        for test_command in test_commands:
            if replace:
                test_command = replace_variables(test, test_command)
            if test_command not in commands:
                commands.append(test_command)

    print('Defined test commands: %s' % (len(commands)))

    successful = []
    failed = []
    missed = []
    for command in commands:
        found = False
        for result in results:
            if result['command'] == command:
                found = True
                if result['success']:
                    successful.append(command)
                else:
                    failed.append(command)

                break

        if not found:
            missed.append(command)

    print('Successul tests: %s/%s' % (len(successful), len(commands)))
    print('Failed tests: %s/%s' % (len(failed), len(commands)))
    print('Missed tests: %s/%s' % (len(missed), len(commands)))
    seconds = int(duration / 1000)
    print('Total durarion: %s' % (datetime.timedelta(seconds=seconds)))

    print('\nSuccessful tests:')
    for success in successful:
        print('- %s' % (success))

    print('\nFailed tests:')
    for failure in failed:
        print('- %s' % (failure))
    print('\nMissed tests:')
    for miss in missed:
        print('- %s' % (miss))

    references = []
    for test in tests:
        if test['command'] not in references:
            references.append(test['command'])
        references = sorted(references)

    print('\nDefined cli groups: %s' % (len(references)))

    not_tested = []
    rs_missed = {}
    for reference in references:
        rs_missed[reference] = []
        for test in tests:
            success = True
            if test['command'] == reference:
                test_commands = get_test_commands(test)
                for test_command in test_commands:
                    if test_command in failed or test_command in missed:
                        success = False
                        rs_missed[reference].append(test_command)

            if not success:
                if reference not in not_tested:
                    not_tested.append(reference)

    tested = []
    for reference in references:
        if reference not in not_tested:
            if reference not in tested:
                tested.append(reference)

    print('Tested cli groups: %s' % (len(tested)))
    for item in tested:
        print('- %s' % (item))
    print('Not-tested cli groups: %s' % (len(not_tested)))
    for item in not_tested:
        print('- %s' % (item))
        for miss in rs_missed[item]:
            print('\t%s' % (miss))


def get_test_results():
    results = []
    directory = './results'
    if os.path.isdir(directory):
        for item in os.listdir(directory):
            item_dir = os.path.join(directory, item)
            result_filename = os.path.join(
                os.path.join(directory, item),
                'result'
            )
            if not os.path.isfile(result_filename):
                continue

            try:
                with open(result_filename, 'r', encoding='utf-8') as file_handler:
                    content = json.loads(file_handler.read())
            except BaseException:
                print_error('Result read failed: %s' % (result_filename))
                sys.exit(1)

            results.append(content)

    return results


def get_test(test_filename, directory):
    filename = os.path.join(directory, test_filename)
    content = None
    if os.path.isfile(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = json.loads(file_handler.read())
            content['name'] = test_filename
        except BaseException:
            print_error('Test read failed: %s' % (filename))
            print_error(traceback.format_exc())

    return content


def match_test(test_definition, test_name):
    if test_name is not None and test_definition['name'] == test_name:
        return True

    return False


def get_tests_count(test_definition, skip=[], exclude_dry_run=False):
    count = 0
    if 'help' not in skip and 'help' in test_definition:
        count = count + 1

    if 'functionality' not in skip and 'functionality' in test_definition:
        if exclude_dry_run:
            for key in test_definition['functionality']:
                if '--dry-run' not in test_definition['functionality'][key]:
                    count = count + 1
        else:
            count = count + len(test_definition['functionality'])

    if 'negative' not in skip and 'negative' in test_definition:
        count = count + len(test_definition['negative'])

    return count


def get_test_by_name(test_name, directory):
    if not os.path.isdir(directory):
        print_error('Test directory not found: %s' % (directory))
        sys.exit(1)

    tests = []
    tests_count = 0
    for test_filename in os.listdir(directory):
        test_definition = get_test(test_filename, directory)
        if test_definition is not None:
            if test_definition['type'] == 'test':
                if match_test(test_definition, test_name):
                    tests_count = tests_count + get_tests_count(test_definition)
                    tests.append(test_definition)

    return tests, tests_count


def get_tests(directory, names=False):
    """Get all tests with type 'test'"""
    tests = []
    if not os.path.isdir(directory):
        return tests

    for test_filename in os.listdir(directory):
        test_definition = get_test(test_filename, directory)
        if test_definition is not None:
            if test_definition['type'] == 'test':
                if names:
                    tests.append(test_filename)
                else:
                    tests.append(test_definition)

    return tests


def get_tests_collections(directory, names=False):
    """Get all tests with type 'collection'"""
    tests = []
    if not os.path.isdir(directory):
        return tests

    for test_filename in os.listdir(directory):
        test_definition = get_test(test_filename, directory)
        if test_definition is not None:
            if test_definition['type'] == 'collection':
                if names:
                    tests.append(test_filename)
                else:
                    tests.append(test_definition)

    if names:
        tests = sorted(tests)

    return tests


def get_tests_collection_info(test_collection, directory):
    tests, tests_count = get_tests_collection(test_collection, directory)
    commands = []
    for test in tests:
        test_commands = get_test_commands(test)
        for test_command in test_commands:
            if test_command not in commands:
                commands.append(test_command)
    commands = sorted(commands)

    all_tests = get_tests(directory)
    all_commands = []
    for test in all_tests:
        test_commands = get_test_commands(test)
        for test_command in test_commands:
            if test_command not in all_commands:
                all_commands.append(test_command)
    all_commands = sorted(all_commands)

    print('Defined test commands: %s' % (len(all_commands)))
    print('Test collection commands: %s' % (len(commands)))

    print('Supported commands:')
    for command in commands:
        print('- %s' % (command))
    print()

    if len(commands) < len(all_commands):
        print('Missing commands:')
        for command in all_commands:
            if command not in commands:
                print('- %s' % (command))


def get_tests_collection(test_collection, directory, skip=[], exclude_dry_run=False):
    if not os.path.isdir(directory):
        print_error('Test directory not found: %s' % (directory))
        sys.exit(1)

    tests = []
    tests_count = 0
    collection_filename = test_collection
    collection = get_test(collection_filename, directory)
    if collection is not None:
        if collection['type'] == 'collection':
            if 'collections' in collection:
                for collection_item in collection['collections']:
                    c_tests, c_count = get_tests_collection(collection_item['name'], directory, skip=skip, exclude_dry_run=exclude_dry_run)
                    for c_test in c_tests:
                        tests.append(c_test)
                    tests_count = tests_count + c_count

            if 'tests' in collection:
                for test in collection['tests']:
                    test_definition = get_test(test['name'], directory)
                    if test_definition is not None:
                        if test_definition['type'] == 'test':
                            tests_count = tests_count + get_tests_count(test_definition, skip=skip, exclude_dry_run=exclude_dry_run)
                            tests.append(test_definition)

    return tests, tests_count


def delete_test_result(results_directory, bar_handler, test):
    if 'help' in test:
        filename = '%s.%s' % (test['name'], 'help')
        result_location = os.path.join('./%s/' % (results_directory), filename)
        if os.path.isdir(result_location):
            shutil.rmtree(result_location)
        bar_handler.next()

    if 'functionality' in test:
        for key in test['functionality']:
            filename = '%s.%s' % (test['name'], key)
            result_location = os.path.join('./%s/' % (results_directory), filename)
            if os.path.isdir(result_location):
                shutil.rmtree(result_location)
            bar_handler.next()

    if 'negative' in test:
        for key in test['negative']:
            filename = '%s.%s' % (test['name'], key)
            result_location = os.path.join('./%s/' % (results_directory), filename)
            if os.path.isdir(result_location):
                shutil.rmtree(result_location)
            bar_handler.next()

    return True


def escape_ansi(line):
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    line = ansi_escape.sub('', line)
    line = line.replace('\u2713', 'v')
    line = line.replace('\u2717', 'x')
    return line


def save_test_result(results_directory, filename, command, ref_command, success, exit_code, output, duration, version):
    result_location = os.path.join('./%s/' % (results_directory), filename)
    if not os.path.isdir(result_location):
        os.makedirs(result_location)

    output_filename = os.path.join(result_location, 'output')
    with open(output_filename, 'w', encoding='utf-8', newline='\n') as file_handler:
        file_handler.write(
            escape_ansi(
                output
            )
        )

    result = dict(
        reference=ref_command,
        command=command,
        iserver_version=version,
        success=success,
        exit_code=exit_code,
        duration=duration
    )
    result_filename = os.path.join(result_location, 'result')
    with open(result_filename, 'w', encoding='utf-8') as file_handler:
        file_handler.write(json.dumps(result, indent=4))

    if '--help' not in command:
        log = log_helper.Log()
        search_command = command.lstrip('python3').lstrip('python.exe').lstrip(' ')
        log_directory = log.get_command_directory(search_command, debug=False)
        if log_directory is None:
            print('Failed to find log directory: %s' % (search_command))
            sys.exit(1)

        for log_filename in os.listdir(log_directory):
            source = os.path.join(log_directory, log_filename)
            if os.path.isfile(source):
                dst = os.path.join(result_location, log_filename)
                shutil.copyfile(source, dst)


def extend_variables(variables, exec_section, iaccount):
    '''
    "exec": {
        "isctl": "firmware serverconfigurationutilitydistributable --name \"SCU 6.2.2a\" -o json",
        "attribute": "Moid",
        "variable": "SCU_ID"
    },
    "exec": {
        "system": "python iserver.py get workflows --serial ${WORKFLOW_SERIAL} --days 7 --count 1 -o json",
        "index": 0,
        "attribute": "workflow_id",
        "variable": "GET_WORKFLOW_ID"
    },
    '''
    template_handler = template_helper.TemplateHelper()

    if 'isctl' in exec_section:
        for key in ['attribute', 'variable']:
            if key not in exec_section:
                print('No key found in exec')
                sys.exit(1)

        isctl_handler = isctl_helper.Isctl(iaccount)
        command = template_handler.replace_variables(exec_section['isctl'], variables)
        response = isctl_handler.get(command, json_conversion=True)
        if response is None:
            print('Command failed: %s' % (command))
            sys.exit(1)

        if exec_section['attribute'] not in response:
            print('Attribute not found in response: %s' % (exec_section['attribute']))
            sys.exit(1)

        variables[exec_section['variable']] = response[exec_section['attribute']]

    if 'system' in exec_section:
        command = template_handler.replace_variables(exec_section['system'], variables)

        my_os = platform.system()
        if my_os == 'Windows':
            command = command.replace('python ', 'python.exe ')
            command = command.replace('isctl ', 'isctl.exe ')
        else:
            command = command.replace('python ', 'python3 ')

        try:
            (return_code, output, duration) = get_output(command)
        except BaseException:
            print('Failed to execute: %s' % (command))
            sys.exit(1)

        if return_code != 0:
            print('Command exit code %s: %s' % (return_code, command))
            sys.exit(1)

        try:
            response = json.loads(output.replace('\r\n', ''))
        except BaseException:
            print('Failed to JSON parse out of: %s' % (command))
            print(output)
            sys.exit(1)

        if 'index' in exec_section:
            if exec_section['attribute'] not in response[exec_section['index']]:
                print('Attribute not found in response list: %s' % (exec_section['attribute']))
                sys.exit(1)

            variables[exec_section['variable']] = response[exec_section['index']][exec_section['attribute']]

        else:
            if exec_section['attribute'] not in response:
                print('Attribute not found in response: %s' % (exec_section['attribute']))
                sys.exit(1)

            variables[exec_section['variable']] = response[exec_section['attribute']]

    return variables


def replace_variables(test, command):
    new_command = []
    for word in command.split(' '):
        if 'variables' in test and word in test['variables']:
            exit_code, output, duration = get_output(test['variables'][word])
            if exit_code > 0:
                print('Variable %s resolution failed' % (word))
                sys.exit(1)
            new_command.append(output)

        else:
            new_command.append(word)

    return ' '.join(new_command)


def get_output(command):
    try:
        start_time = int(time.time() * 1000)
        with subprocess.Popen(
            args=command,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
            env=os.environ
        ) as process:
            output, error = process.communicate()
            duration = int(time.time() * 1000) - start_time
            return process.returncode, output.decode('utf-8', 'ignore'), duration

    except BaseException:
        print_error(traceback.format_exc())
        sys.exit(1)


def save_script_result(results_directory, filename, key, directory, script, command, success, exit_code, output, duration):
    result_location = os.path.join('./%s/' % (results_directory), filename)
    if not os.path.isdir(result_location):
        os.makedirs(result_location)

    output_filename = os.path.join(result_location, 'script.%s.%s.output' % (key, script))
    with open(output_filename, 'w', encoding='utf-8') as file_handler:
        file_handler.write(output)

    result = dict(
        success=success,
        command=command,
        exit_code=exit_code,
        duration=duration
    )
    result_filename = os.path.join(result_location, 'script.%s.%s.result' % (key, script))
    with open(result_filename, 'w', encoding='utf-8') as file_handler:
        file_handler.write(json.dumps(result, indent=4))


def is_test_script(script, directory):
    script_directory = os.path.join(directory, 'scripts')
    script_filename = os.path.join(script_directory, script)
    if not os.path.isfile(script_filename):
        return False
    return True


def run_script(results_directory, filename, key, directory, script):
    script_directory = os.path.join(directory, 'scripts')
    script_filename = os.path.join(script_directory, script[0])

    command = './%s %s' % (script_filename, ' '.join(script[1:]))
    exit_code, output, duration = get_output(command)
    success = bool(exit_code == 0)

    save_script_result(results_directory, filename, key, directory, script[0], command, success, exit_code, output, duration)
    return success


def run_pre_scripts(results_directory, filename, test, key, tests_directory, dry_run=False):
    if 'scripts' not in test or key not in test['scripts']:
        return True

    if 'pre' not in test['scripts'][key] or len(test['scripts'][key]['pre']) == 0:
        return True

    for script in test['scripts'][key]['pre']:
        if dry_run:
            if is_test_script(script[0], tests_directory):
                print('[%s] pre: %s' % (test['name'], script[0]))
            else:
                print('[%s] pre [NOT FOUND]: %s' % (test['name'], script[0]))

        else:
            if not run_script(results_directory, filename, key, tests_directory, script):
                print('Pre script failed: [%s] [%s] %s' % (test['name'], key, script[0]))
                return False

    return True


def run_post_scripts(results_directory, filename, test, key, tests_directory, dry_run=False):
    if 'scripts' not in test or key not in test['scripts']:
        return True

    if 'post' not in test['scripts'][key] or len(test['scripts'][key]['post']) == 0:
        return True

    for script in test['scripts'][key]['post']:
        if dry_run:
            if is_test_script(script[0], tests_directory):
                print('[%s] post: %s' % (test['name'], script[0]))
            else:
                print('[%s] post [NOT FOUND]: %s' % (test['name'], script[0]))

        else:
            if not run_script(results_directory, filename, key, tests_directory, script):
                print('Post script failed: [%s] [%s] %s' % (test['name'], key, script[0]))
                return False

    return True


def run_test(bar_handler, test, tests_directory, results_directory, variables, iaccount, verbose, debug, dry_run, iserver_prefix, iserver_version, save_result=True, skip=[], exclude_dry_run=False, wait=False):
    results = []
    template_handler = template_helper.TemplateHelper()

    if 'help' not in skip and 'help' in test:
        filename = '%s.%s' % (test['name'], 'help')
        command = '%s %s' % (iserver_prefix, test['help'])
        command = template_handler.replace_variables(command, variables)

        if dry_run:
            print('[%s] %s' % (test['name'], command))
        else:
            exit_code, output, duration = get_output(command)
            success = bool(exit_code == 0)

            if save_result:
                save_test_result(results_directory, filename, command, test['command'], success, exit_code, output, duration, iserver_version)

            results.append(
                dict(
                    command=command,
                    success=success
                )
            )
            if not success:
                print('Command failed: %s' % (command))
                sys.exit(1)

            bar_handler.next()

    if 'exec' in test:
        variables = extend_variables(variables, test['exec'], iaccount)

    if 'functionality' not in skip and 'functionality' in test:
        for key in test['functionality']:
            if key.startswith('wait_'):
                time.sleep(test['functionality'][key])

                results.append(
                    dict(
                        command='sleep',
                        success=True
                    )
                )

                bar_handler.next()
                continue

            filename = '%s.%s' % (test['name'], key)
            command = '%s %s' % (iserver_prefix, test['functionality'][key])
            command = template_handler.replace_variables(command, variables)

            if exclude_dry_run and '--dry-run' in command:
                continue

            if dry_run:
                command = replace_variables(test, command)
                run_pre_scripts(results_directory, filename, test, key, tests_directory, dry_run=True)
                print('[%s] %s' % (test['name'], command))
                run_post_scripts(results_directory, filename, test, key, tests_directory, dry_run=True)
            else:
                command = replace_variables(test, command)
                if not run_pre_scripts(results_directory, filename, test, key, tests_directory):
                    sys.exit(1)

                exit_code, output, duration = get_output(command)
                success = bool(exit_code == 0)

                if save_result:
                    save_test_result(results_directory, filename, command, test['command'], success, exit_code, output, duration, iserver_version)

                results.append(
                    dict(
                        command=command,
                        success=success
                    )
                )
                if not success:
                    print('\nCommand failed: %s' % (command))
                    print(output)
                    sys.exit(1)

                if not run_post_scripts(results_directory, filename, test, key, tests_directory):
                    sys.exit(1)

                bar_handler.next()

            if wait:
                input("Press Enter to continue...")

    if 'negative' not in skip and 'negative' in test:
        for key in test['negative']:
            filename = '%s.%s' % (test['name'], key)
            command = '%s %s' % (iserver_prefix, test['negative'][key])
            command = template_handler.replace_variables(command, variables)

            if exclude_dry_run and '--dry-run' in command:
                continue

            if dry_run:
                command = replace_variables(test, command)
                run_pre_scripts(results_directory, filename, test, key, tests_directory, dry_run=True)
                print('[%s] %s' % (test['name'], command))
                run_post_scripts(results_directory, filename, test, key, tests_directory, dry_run=True)
            else:
                command = replace_variables(test, command)
                if not run_pre_scripts(results_directory, filename, test, key, tests_directory):
                    sys.exit(1)

                exit_code, output, duration = get_output(command)
                success = bool(exit_code > 0)

                if save_result:
                    save_test_result(results_directory, filename, command, test['command'], success, exit_code, output, duration, iserver_version)

                results.append(
                    dict(
                        command=command,
                        success=success
                    )
                )
                if not success:
                    print('Command failed: %s' % (command))
                    sys.exit(1)

                if not run_post_scripts(results_directory, filename, test, key, tests_directory):
                    sys.exit(1)

                bar_handler.next()

            if wait:
                input("Press Enter to continue...")

    return results


def load_test_variables(directory, environment):
    variables = {}
    bundle_dir = os.path.dirname(getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__))))
    tests_directory = os.path.join(bundle_dir, directory)

    if len(environment) > 0:
        environment_directory = os.path.join(tests_directory, 'environment')
        environment_file = os.path.join(environment_directory, environment)
        if not os.path.isfile(environment_file):
            print('Environment file not found: %s' % (environment_file))
            return None

        with open(environment_file, 'r', encoding='utf-8') as file_handler:
            variables = json.loads(file_handler.read())

    cloud_init_directory = os.path.join(tests_directory, 'cloud-init')
    variables['CLOUD_INIT_DIRECTORY'] = cloud_init_directory

    return variables


def get_iserver_prefix():
    iserver_prefix = 'python3 iserver.py'
    my_os = platform.system()
    if my_os == 'Windows':
        iserver_prefix = 'python.exe .\\iserver.py'
    return iserver_prefix


def run_tests(tests, tests_count, tests_directory, results_directory, environment, iaccount, honor, verbose, debug, dry_run, wait=False):
    variables = load_test_variables(tests_directory, environment)
    if variables is None:
        return []

    results = []
    version_filename = './version'
    with open(version_filename, 'r', encoding='utf-8') as file_handler:
        iserver_version = file_handler.read().rstrip('\n')

    if not dry_run:
        bar_handler = Bar('Cleanup', max=tests_count)
        for test in tests:
            if not delete_test_result(results_directory, bar_handler, test):
                sys.exit(1)
        bar_handler.finish()

    bar_handler = Bar('Processing', max=tests_count)
    bar_handler.goto(0)
    for test in tests:
        if honor:
            test_iaccount = iaccount
            if 'iaccount' in test:
                test_iaccount = test['iaccount']

            test_variables = variables
            if 'environment' in test:
                test_variables = load_test_variables(tests_directory, test['environment'])

            test_results = run_test(
                bar_handler,
                test,
                tests_directory,
                results_directory,
                test_variables,
                test_iaccount,
                verbose,
                debug,
                dry_run,
                get_iserver_prefix(),
                iserver_version,
                wait=wait
            )
        else:
            test_results = run_test(
                bar_handler,
                test,
                tests_directory,
                results_directory,
                variables,
                iaccount,
                verbose,
                debug,
                dry_run,
                get_iserver_prefix(),
                iserver_version,
                wait=wait
            )
        for test_result in test_results:
            results.append(test_result)

        if wait:
            input("Press Enter to continue...")

    bar_handler.finish()

    return results
