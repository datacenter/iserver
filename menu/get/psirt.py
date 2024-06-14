import sys
import json
import threading
import traceback
import click

from menu import validations
from menu import progress

from lib.psirt import main as psirt
from lib.psirt import output as psirt_output
from lib.psirt import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("psirt")
@click.pass_obj
@click.option("--sev", "severity", type=click.Choice(['any', 'crit', 'high', 'med', 'low', 'info'], case_sensitive=False), default='any', show_default=True)
@click.option("--bug", default='', callback=validations.empty_string_to_none, help="Filter by bug")
@click.option("--cve", default='', callback=validations.empty_string_to_none, help="Filter by cve")
@click.option("--cwe", default='', callback=validations.empty_string_to_none, help="Filter by cwe")
@click.option("--prod", "product", default='', callback=validations.empty_string_to_none, help="Filter by product name")
@click.option("--ver", "version", default='', callback=validations.empty_string_to_none, help="Filter by product version")
@click.option("--added", type=click.INT, default=-1, show_default=True)
@click.option("--updated", type=click.INT, default=365, show_default=True)
@click.option("--limit", "-l", "output_limit", type=click.INT, default=25, show_default=True)
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--view", "-v", default=['list'], help="[list|url|sum|ver|prod|settings|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_psirt_command(
        ctx,
        severity,
        bug,
        cve,
        cwe,
        product,
        version,
        added,
        updated,
        output_limit,
        show_password,
        view,
        output,
        devel
        ):
    """Get psirt advisory"""

    # iserver get psirt adv

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'list|url|sum|ver|prod|settings|all',
        'list',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        settings_handler = settings.PsirtSettings(log_id=ctx.run_id)
        psirt_settings = settings_handler.get_psirt_settings()
        if psirt_settings is None:
            ctx.my_output.error('Failed to get psirt api settings')
            raise ErrorExit

        advisories = []
        if 'list' in view or 'url' in view or 'sum' in view or 'ver' in view or 'prod' in view:
            (key, secret) = settings_handler.get_psirt_credentials()
            if key is None or secret is None:
                ctx.my_output.error(
                    'Define psirt api key/secret'
                )
                raise ErrorExit

            if output not in ['json']:
                ctx.busy = True
                threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

            object_filter = []

            if severity != 'any':
                object_filter.append(
                    'severity:%s' % (severity)
                )

            if bug is not None:
                object_filter.append(
                    'bug:%s' % (bug)
                )

            if cve is not None:
                object_filter.append(
                    'cve:%s' % (cve)
                )

            if cwe is not None:
                object_filter.append(
                    'cwe:%s' % (cwe)
                )

            if product is not None:
                object_filter.append(
                    'product:%s' % (product)
                )

            if version is not None:
                object_filter.append(
                    'version:%s' % (version)
                )

            if added > 0:
                object_filter.append(
                    'added:%s' % (added)
                )

            if updated > 0:
                object_filter.append(
                    'updated:%s' % (updated)
                )

            psirt_handler = psirt.Psirt(key, secret, log_id=ctx.run_id)
            advisories = psirt_handler.get_advisories(
                object_filter
            )

            ctx.busy = False

            if advisories is None:
                ctx.my_output.error('Failed to get advisories')
                raise ErrorExit

            if output == 'json':
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        advisories,
                        indent=4
                    )
                )
                return

            ctx.my_output.json_output(advisories)

        output_handler = psirt_output.PsirtOutput(log_id=ctx.run_id)

        if 'settings' in view:
            output_handler.print_psirt_settings(
                psirt_settings,
                show_password=show_password
            )

        if 'list' in view and 'ver' not in view:
            if output_limit > 0:
                output_handler.print_advisory(
                    advisories[:output_limit],
                    title=True
                )
            else:
                output_handler.print_advisory(
                    advisories,
                    title=True
                )

        if 'ver' in view:
            if output_limit > 0:
                output_handler.print_advisory_version(
                    advisories[:output_limit],
                    title=True
                )
            else:
                output_handler.print_advisory_version(
                    advisories,
                    title=True
                )

        if 'url' in view:
            if output_limit > 0:
                output_handler.print_advisory_url(
                    advisories[:output_limit],
                    title=True
                )
            else:
                output_handler.print_advisory_url(
                    advisories,
                    title=True
                )

        if 'sum' in view:
            if output_limit > 0:
                output_handler.print_advisory_summary(
                    advisories[:output_limit],
                    title=True
                )
            else:
                output_handler.print_advisory_summary(
                    advisories,
                    title=True
                )

        if 'prod' in view:
            if output_limit > 0:
                output_handler.print_advisory_product(
                    advisories[:output_limit],
                    title=True,
                    product_filter=product
                )
            else:
                output_handler.print_advisory_product(
                    advisories,
                    title=True,
                    product_filter=product
                )

        if output_limit > 0 and len(advisories) >= output_limit:
            ctx.my_output.default('Output limited to %s entries' % (output_limit), before_newline=True)

        ctx.my_output.default('Filter: sev, bug, cve, cwe, prod, ver, added, updated', before_newline=True)
        ctx.my_output.default('View:   list (def), url, sum, ver, all')

        if advisories is None or len(advisories) == 0:
            raise NoResultExit

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
