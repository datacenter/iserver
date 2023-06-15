import sys
import json
import threading
import traceback
import click

from lib.iwo import main as iwo

from menu import validations
from menu import defaults
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("application")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--name", is_flag=False, show_default=True, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--cluster", is_flag=False, show_default=True, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Filter by cluster")
@click.option("--container", is_flag=False, show_default=True, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Filter by container")
@click.option("--service", is_flag=False, show_default=True, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Filter by service")
@click.option("--stale", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select stale")
@click.option("--inactive", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select inactive")
@click.option("--critical", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select critical")
@click.option("--major", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select major or critical")
@click.option("--minor", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select minor, major or critical")
@click.option("--show-container", is_flag=True, show_default=True, default=False, help="Show application containers")
@click.option("--show-service", is_flag=True, show_default=True, default=False, help="Show application services")
@click.option("--show-actions", is_flag=True, show_default=True, default=False, help="Show application actions")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_iwo_application_command(
        ctx,
        iaccount,
        name,
        cluster,
        container,
        service,
        stale,
        inactive,
        critical,
        major,
        minor,
        show_container,
        show_service,
        show_actions,
        output,
        verbose,
        debug,
        devel
        ):
    """Get iwo application"""

    # iserver get iwo application

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        iwo_handler = iwo.Iwo(
            iaccount,
            verbose=verbose,
            debug=debug,
            log_id=ctx.run_id
        )

        match_rules = []
        if name is not None:
            match_rules.append(
                'name:%s' % (name)
            )

        if cluster is not None:
            match_rules.append(
                'cluster:%s' % (cluster)
            )

        if container is not None:
            show_container = True
            match_rules.append(
                'container:%s' % (container)
            )

        if service is not None:
            show_service = True
            match_rules.append(
                'service:%s' % (service)
            )

        if stale is not None:
            match_rules.append(
                'stale'
            )

        if inactive is not None:
            match_rules.append(
                'inactive'
            )

        if critical is not None:
            match_rules.append(
                'critical'
            )

        if major is not None:
            match_rules.append(
                'major'
            )

        if minor is not None:
            match_rules.append(
                'minor'
            )

        resolve_dependencies = False
        if show_container or show_service or show_actions:
            resolve_dependencies = True

        managed_objects = iwo_handler.get_applications(
            resolve_dependencies=resolve_dependencies,
            match_rules=match_rules
        )
        if managed_objects is None:
            ctx.busy = False
            ctx.my_output.error('Failed to get application')
            raise ErrorExit

        if output == 'json':
            ctx.busy = False
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    managed_objects,
                    indent=4
                )
            )
            return

        ctx.busy = False
        ctx.my_output.json_output(managed_objects)

        iwo_handler.print_applications(
            managed_objects,
            show_service=show_service,
            show_container=show_container,
            show_actions=show_actions
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
