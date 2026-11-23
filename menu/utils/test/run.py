import sys
import click

from lib import self_testing
from lib import self_doc
from menu import defaults
from menu import validations


@click.command("run")
@click.pass_obj
@click.option("--test-name", is_flag=False, show_default=False, default=None, type=click.STRING, help="Specific test selected by name")
@click.option("--test-collection", is_flag=False, show_default=False, default=None, type=click.STRING, help="Filename with test names")
@click.option("--tests", "tests_directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
@click.option("--results", "results_directory", is_flag=False, show_default=False, default='results', type=click.STRING, help="Results location")
@click.option("--environment", is_flag=False, show_default=False, default='', type=click.STRING, help="Test environment")
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--enforce", is_flag=True, show_default=True, default=False, help="Enforce cli iaccount/enviornment")
@click.option("--honor", is_flag=True, show_default=True, default=False, help="Prefer test iaccount/enviornment over collection/cli")
@click.option("--doc", is_flag=True, show_default=True, default=False, help="Documentation generation when tests are successful")
@click.option("--no-redfish", is_flag=True, show_default=True, default=False, help="Disable redfish tests doc")
@click.option("--wait", is_flag=True, show_default=True, default=False, help="Wait for keypress between tests")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug output")
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
def utils_test_run_command(ctx, test_name, test_collection, tests_directory, results_directory, environment, iaccount, enforce, honor, doc, no_redfish, wait, verbose, debug, dry_run):
    """run iserver tests"""

    # iserver utils devel self-test run

    if debug:
        verbose = True

    if test_collection is None and test_name is None:
        print('Define the scope of tests')
        sys.exit(1)

    if test_collection is not None:
        selected_tests, tests_count = self_testing.get_tests_collection(test_collection, tests_directory)
        if not enforce:
            test_iaccount = self_testing.get_test_iaccount(test_collection, tests_directory)
            if test_iaccount is not None:
                iaccount = test_iaccount

            test_environment = self_testing.get_test_environment(test_collection, tests_directory)
            if test_environment is not None:
                environment = test_environment

    else:
        selected_tests, tests_count = self_testing.get_test_by_name(test_name, tests_directory)
        if not enforce:
            test_iaccount = self_testing.get_test_iaccount(test_name, tests_directory)
            if test_iaccount is not None:
                iaccount = test_iaccount

            test_environment = self_testing.get_test_environment(test_name, tests_directory)
            if test_environment is not None:
                environment = test_environment

    if selected_tests is None:
        print('Test collection failed')
        sys.exit(1)

    if not honor:
        print('iaccount: %s' % (iaccount))
        if len(environment) > 0:
            print('environment: %s' % (environment))

    results = self_testing.run_tests(
        selected_tests,
        tests_count,
        tests_directory,
        results_directory,
        environment,
        iaccount,
        honor,
        verbose,
        debug,
        dry_run,
        wait=wait
    )
    success = 0
    for result in results:
        if result['success']:
            print("OK\t%s" % (result['command']))
            success = success + 1
        else:
            print("NOK\t%s" % (result['command']))

    print('\nSummary')
    print('- Tests: %s' % (len(results)))
    print('- Success: %s' % (success))

    failed = len(results) - success
    print('- Failed: %s' % (failed))

    if failed == 0 and doc:
        success = self_doc.generate_docs(
            results_directory,
            redfish_tests=not no_redfish
        )

        if not success:
            sys.exit(1)
