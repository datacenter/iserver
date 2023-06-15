import sys
import click

from lib import self_doc


@click.command("doc")
@click.pass_obj
@click.option("--directory", is_flag=False, show_default=False, default="results")
@click.option("--template", "template_names", multiple=True, help="Select template")
@click.option("--no-redfish", is_flag=True, show_default=True, default=False, help="Disable redfish tests")
@click.option("--generate", is_flag=True, show_default=True, default=False, help="Generate template from template")
def utils_doc_command(ctx, directory, template_names, no_redfish, generate):
    """Generate documentation"""

    # iserver utils doc

    if generate:
        success = self_doc.generate_template_docs(
            template_names
        )

    success = self_doc.generate_docs(
        directory,
        template_names,
        redfish_tests=not no_redfish
    )

    if not success:
        sys.exit(1)
