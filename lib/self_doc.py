import os
import sys
import json
import shutil
import traceback

from lib import file_helper
from lib import filter_helper
from lib import ip_helper
from lib import template_helper


def get_doc_directory():
    main_dir = file_helper.get_main_dir()
    return os.path.join(
        main_dir,
        'doc'
    )


def get_templates_directory():
    return os.path.join(
        file_helper.get_main_dir(),
        'doc-templates'
    )


def get_template(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file_handler:
            content = file_handler.read()

    except BaseException:
        print('Test read failed: %s' % (filename))
        print(traceback.format_exc())
        sys.exit(1)

    return content


def get_keywords(template_content):
    keywords = []
    for line in template_content.split('\n'):
        if line.startswith('DOC_TEMPLATE:'):
            keywords.append(
                dict(
                    result=line.split(':')[1],
                    filename=line.split(':')[2]
                )
            )

    return keywords


def get_template_names(template_names, include_redfish=False):
    templates = {}
    templates_directory = get_templates_directory()
    for template_subdirectory in os.listdir(templates_directory):
        if template_subdirectory.startswith('redfish') and not include_redfish:
            continue

        if len(template_names) > 0 and template_subdirectory not in template_names:
            continue

        templates[template_subdirectory] = []
        for template_filename in os.listdir(os.path.join(templates_directory, template_subdirectory)):
            if template_filename.endswith('.md'):
                if 'Template' not in template_filename:
                    templates[template_subdirectory].append(template_filename)

    return templates


def match_templates_with_results(all_templates, results):
    templates = {}
    templates_directory = get_templates_directory()
    for template_group in all_templates:
        templates[template_group] = []

        for template_name in all_templates[template_group]:
            template_filename = os.path.join(
                os.path.join(
                    templates_directory,
                    template_group
                ),
                template_name
            )

            print('Checking template: %s' % (template_filename))
            template_content = get_template(template_filename)
            template_keywords = get_keywords(template_content)

            if len(template_keywords) == 0:
                print('- MATCH (no keywords)')
                templates[template_group].append(
                    dict(
                        filename=template_filename,
                        content=template_content,
                        keywords=template_keywords
                    )
                )

            if len(template_keywords) > 0:
                match = True
                for template_keyword in template_keywords:
                    if template_keyword['result'] not in results:
                        print('- NOK %s' % (template_keyword['result']))
                        match = False
                    else:
                        print('- OK %s' % (template_keyword['result']))

                if match:
                    print('- MATCH')
                    templates[template_group].append(
                        dict(
                            filename=template_filename,
                            content=template_content,
                            keywords=template_keywords
                        )
                    )

    return templates


def mask_password(line, pattern):
    if ' %s ' % (pattern) not in line:
        return line

    words = line.split(' ')
    if pattern not in words:
        return line

    index = words.index(pattern)
    words[index + 1] = '******'

    return ' '.join(words)


def get_command(results_base_directory, results_directory, max_command_length=80):
    filename = os.path.join(
        os.path.join(
            results_base_directory,
            results_directory
        ),
        'result'
    )
    with open(filename, 'r', encoding='utf-8') as file_handler:
        content = json.loads(file_handler.read())

    command = '# %s' % (
        mask_password(
            content['command'],
            '--password'
        )
    )
    command = command.replace('python3 iserver.py', 'iserver')
    command = command.replace('python.exe .\\iserver.py', 'iserver')
    if '--help' not in command:
        if len(command) > max_command_length:
            command = command.replace(' --', '\n    --')

    return command


def get_result(results_base_directory, results_directory, result_filename):
    filename = os.path.join(
        os.path.join(
            results_base_directory,
            results_directory
        ),
        result_filename
    )
    try:
        with open(filename, 'r', encoding='utf8', errors='ignore') as file_handler:
            content = file_handler.read()
            content = content.replace('\u2713', 'TICK_YES')
            content = content.replace('\u2717', 'TICK_NO')
            content = content.encode("ascii", "ignore")
            content = content.decode()
            content = content.replace('TICK_YES', 'V')
            content = content.replace('TICK_NO', 'X')
            content = content.lstrip('\n')
            content = content.rstrip('\n')

    except BaseException:
        print('Failed to read file: %s' % (filename))
        print(traceback.format_exc())
        sys.exit(1)

    return content


def replace_keywords(template_content, results_base_directory):
    new_content = ''
    for line in template_content.split('\n'):
        if line.startswith('DOC_TEMPLATE:'):
            results_directory = line.split(':')[1]
            result_filename = line.split(':')[2]
            command = get_command(results_base_directory, results_directory)
            result = get_result(results_base_directory, results_directory, result_filename)
            new_content = '%s\n%s\n\n%s' % (
                new_content,
                command,
                result
            )
            continue

        if line.startswith('FILE:'):
            results_directory = line.split(':')[1]
            result_filename = line.split(':')[2]

            result = get_result(results_base_directory, results_directory, result_filename)
            new_content = '%s\n%s' % (
                new_content,
                result
            )

            continue

        if line.startswith('ODATA_DEBUG:'):
            results_directory = line.split(':')[1]
            result_filename = 'odata.debug'
            odata = line.split(':')[2]

            command = get_command(results_base_directory, results_directory)
            result = json.loads(get_result(results_base_directory, results_directory, result_filename))
            if odata in result:
                new_content = '%s%s' % (
                    new_content,
                    json.dumps(result[odata], indent=4)
                )

            continue

        if line.startswith('API_DEBUG:'):
            results_directory = line.split(':')[1]
            result_filename = 'api.debug'
            api_command = ' %s ' % (line.split(':')[2])
            items_count = int(line.split(':')[3])

            command = get_command(results_base_directory, results_directory)
            result = json.loads(get_result(results_base_directory, results_directory, result_filename))
            for key in result:
                if api_command in key:
                    if items_count == 0:
                        new_content = '%s\n%s\n\n%s' % (
                            new_content,
                            key,
                            json.dumps(result[key], indent=4)
                        )

                    if items_count == 1:
                        new_content = '%s\n%s\n\n%s' % (
                            new_content,
                            key,
                            json.dumps(result[key][0], indent=4)
                        )

                    break

            continue

        if new_content == '':
            new_content = line
            continue

        new_content = '%s\n%s' % (
            new_content,
            line
        )

    return new_content


def get_results(results_directory):
    if not os.path.isdir(results_directory):
        print('Results directory not found: %s' % (results_directory))
        return None

    results = []
    for result_directory in os.listdir(results_directory):
        directory_name = os.path.join(results_directory, result_directory)
        result_filename = os.path.join(directory_name, 'result')
        if os.path.isfile(result_filename):
            try:
                with open(result_filename, 'r', encoding='utf-8') as file_handler:
                    content = json.loads(file_handler.read())

                if content['success']:
                    results.append(result_directory)

            except BaseException:
                print('[WARNING] Failed to open result file: %s' % (result_filename))

    results = sorted(results)
    return results


def get_templates_count(templates):
    count = 0
    for template_group in templates:
        count = count + len(templates[template_group])
    return count


def get_redfish_test_endpoints():
    templates_directory = get_templates_directory()
    redfish_templates_directory = os.path.join(templates_directory, 'redfish')
    redfish_test_templates_directory = os.path.join(redfish_templates_directory, 'tests')
    tests_filename = os.path.join(redfish_test_templates_directory, 'tests.yaml')
    if not os.path.isfile(tests_filename):
        print('Redfish tests definition not found: %s' % (tests_filename))
        return None

    tests = file_helper.get_file_yaml(
        tests_filename
    )
    if tests is None:
        print('Redfish tests definition read failed: %s' % (tests_filename))
        return None

    tests = sorted(tests, key=lambda i: (i['vendor'], i['model']))
    return tests


def get_redfish_test_table_content(tests):
    endpoint_map = {}
    endpoint_map['standard'] = 'EndpointStandard.md'
    endpoint_map['ucsc'] = 'EndpointUcsc.md'
    endpoint_map['fi'] = 'EndpointFi.md'
    endpoint_map['hpe'] = 'EndpointHpe.md'
    endpoint_map['dell'] = 'EndpointDell.md'

    content = ''
    for test in tests:
        resource = '[link](../redfish-tests-%s-%s/Resource.md)' % (
            test['vendor'].lower(),
            test['model'].lower()
        )
        oem = ''
        if test['oem']:
            oem = '[link](../redfish-tests-%s-%s/Oem.md)' % (
                test['vendor'].lower(),
                test['model'].lower()
            )
        action = ''
        if test['action']:
            action = '[link](../redfish-tests-%s-%s/Action.md)' % (
                test['vendor'].lower(),
                test['model'].lower()
            )
        identity = ''
        if test['identity']:
            identity = '[link](../redfish-tests-%s-%s/Identity.md)' % (
                test['vendor'].lower(),
                test['model'].lower()
            )
        power = ''
        if test['power']:
            power = '[link](../redfish-tests-%s-%s/Power.md)' % (
                test['vendor'].lower(),
                test['model'].lower()
            )
        thermal = ''
        if test['thermal']:
            thermal = '[link](../redfish-tests-%s-%s/Thermal.md)' % (
                test['vendor'].lower(),
                test['model'].lower()
            )

        line = '%s | %s | [%s](./%s) | %s | %s | %s | %s | %s | %s' % (
            test['vendor'],
            test['model'],
            test['endpoint'],
            endpoint_map[test['endpoint']],
            resource,
            oem,
            action,
            identity,
            power,
            thermal
        )
        content = '%s%s\n' % (content, line)

    return content


def generate_redfish_readme_no_tests():
    redfish_templates_directory = os.path.join(
        get_templates_directory(),
        'redfish'
    )
    redfish_readme_template_filename = os.path.join(
        redfish_templates_directory,
        'README.template_no_tests'
    )
    redfish_readme_filename = os.path.join(
        redfish_templates_directory,
        'README.md'
    )

    if not os.path.isfile(redfish_readme_template_filename):
        print('Redfish readme template not found:%s' % (redfish_readme_template_filename))
        return False

    try:
        with open(redfish_readme_template_filename, 'r', encoding='utf-8') as file_handler:
            content = file_handler.read()
    except BaseException:
        print('Redfish readme read failed:%s' % (redfish_readme_template_filename))
        print(traceback.format_exc())
        return False

    try:
        with open(redfish_readme_filename, 'w', encoding='utf-8') as file_handler:
            file_handler.write(str(content))

    except BaseException:
        print('Redfish readme file write failed:%s' % (redfish_readme_filename))
        return False

    print('Readme generated: %s' % (redfish_readme_filename))
    return True


def generate_redfish_readme_tests(tests):
    table_content = get_redfish_test_table_content(tests)
    if table_content is None:
        print('Redfish endpoints test table content generation failed')
        return False

    redfish_templates_directory = os.path.join(
        get_templates_directory(),
        'redfish'
    )
    redfish_readme_template_filename = os.path.join(
        redfish_templates_directory,
        'README.template_tests'
    )
    redfish_readme_filename = os.path.join(
        redfish_templates_directory,
        'README.md'
    )

    if not os.path.isfile(redfish_readme_template_filename):
        print('Redfish readme template not found:%s' % (redfish_readme_template_filename))
        return False

    try:
        with open(redfish_readme_template_filename, 'r', encoding='utf-8') as file_handler:
            content = file_handler.read()
    except BaseException:
        print('Redfish readme read failed:%s' % (redfish_readme_template_filename))
        print(traceback.format_exc())
        return False

    new_content = ''
    replaced = False
    for line in content.split('\n'):
        if line == 'REDFISH_TESTED_ENDPOINTS_TABLE':
            replaced = True
            new_content = '%s\n%s' % (new_content, table_content)
            continue

        new_content = '%s\n%s' % (new_content, line)

    if not replaced:
        print('Redfish readme table replacement failed')
        return False

    try:
        with open(redfish_readme_filename, 'w', encoding='utf-8') as file_handler:
            file_handler.write(str(new_content))

    except BaseException:
        print('Redfish readme file write failed:%s' % (redfish_readme_filename))
        return False

    print('Readme generated: %s' % (redfish_readme_filename))
    return True


def clean_redfish_test_templates():
    base_directory = get_templates_directory()
    for item in os.listdir(base_directory):
        if item.startswith('redfish-tests-'):
            dirname = os.path.join(
                base_directory,
                item
            )
            if os.path.isdir(dirname):
                shutil.rmtree(dirname)


def clean_redfish_test_doc():
    base_directory = get_doc_directory()
    for item in os.listdir(base_directory):
        if item.startswith('redfish-tests-'):
            dirname = os.path.join(
                base_directory,
                item
            )
            if os.path.isdir(dirname):
                shutil.rmtree(dirname)


def get_redfish_tree(test, results_directory):
    result = get_result(
        results_directory,
        '%s.tree' % (test['result']),
        'iserver.output.default'
    )
    if result is None:
        print('No result found: %s' % ('%s.tree' % (test['result'])))
        sys.exit(1)

    try:
        tree = json.loads(result)
    except BaseException:
        print('JSON format expected: %s' % ('%s.tree' % (test['result'])))
        sys.exit(1)

    return tree


def get_redfish_root_children(test, results_directory):
    result = get_result(
        results_directory,
        '%s.children' % (test['result']),
        'iserver.output.default'
    )
    return json.loads(result)


def get_redfish_root_children_links(test, results_directory):
    children = get_redfish_root_children(test, results_directory)

    children_names = []
    links = []
    for child in children:
        if test['base_uri'] not in child:
            continue

        if child == test['base_uri']:
            continue

        child_name = child.lstrip(test['base_uri']).split('/')[0]
        if child_name in children_names:
            continue

        children_names.append(child_name)
        links.append(
            dict(
                uri=child,
                name=child_name
            )
        )

    return links


def get_redfish_root_children_links_content(test, results_directory):
    links = get_redfish_root_children_links(test, results_directory)

    content = ''
    for link in links:
        line = '- [%s](./Uri%s.md)' % (
            link['uri'],
            link['name']
        )
        content = '%s%s\n' % (content, line)

    return content


def generate_redfish_test_template(redfish_test_templates_directory, test_directory_name, template_name, test, results_directory):
    template_handler = template_helper.TemplateHelper()

    template_filename = os.path.join(
        redfish_test_templates_directory,
        '%s.template' % (template_name)
    )
    if not os.path.isfile(template_filename):
        print('Template file not found: %s' % (template_filename))
        return False

    try:
        with open(template_filename, 'r', encoding='utf-8') as file_handler:
            content = file_handler.read()
    except BaseException:
        print('Redfish readme read failed:%s' % (template_filename))
        print(traceback.format_exc())
        return False

    variables = {}
    variables['TEST_VENDOR'] = test['vendor']
    variables['TEST_MODEL'] = test['model']
    variables['TEST_RESULT'] = test['result']
    variables['ROOT_CHILDREN_LINKS'] = get_redfish_root_children_links_content(test, results_directory)

    new_content = template_handler.replace_variables(content, variables)

    target_template_filename = os.path.join(
        test_directory_name,
        '%s.md' % (template_name)
    )
    try:
        with open(target_template_filename, 'w', encoding='utf-8') as file_handler:
            file_handler.write(str(new_content))

    except BaseException:
        print('Template file write failed:%s' % (target_template_filename))
        return False

    print('Template created: %s' % (target_template_filename))
    return True


def generate_redfish_resource_template(test_template_directory_name, test, results_directory):
    links = get_redfish_root_children_links(test, results_directory)
    tree = get_redfish_tree(test, results_directory)
    for link in links:
        target_template_filename = os.path.join(
            test_template_directory_name,
            'Uri%s.md' % (link['name'])
        )
        try:
            content = '# Resource: %s\n\n' % (link['uri'])
            content = '%s%s\n' % (content, 'Vendor | Model')
            content = '%s%s\n' % (content, '--- | ---')
            content = '%s%s\n\n' % (content, '%s | %s' % (test['vendor'], test['model']))
            for branch in tree:
                if branch.startswith(link['uri']):
                    content = '%s%s\n\n' % (content, '## %s' % (branch))
                    content = '%s%s\n' % (content, '```')
                    content = '%s%s\n' % (content, 'ODATA_DEBUG:%s.tree:%s' % (test['result'], branch))
                    content = '%s%s\n\n' % (content, '```')

            with open(target_template_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(content)

        except BaseException:
            print('Template file write failed:%s' % (target_template_filename))
            print(traceback.format_exc())
            return False

        print('Template created: %s' % (target_template_filename))

    return True


def generate_redfish_tests(tests, results_directory):
    redfish_templates_directory = os.path.join(
        get_templates_directory(),
        'redfish'
    )
    redfish_test_templates_directory = os.path.join(
        redfish_templates_directory,
        'tests'
    )

    for test in tests:
        test_template_directory_name = os.path.join(
            get_templates_directory(),
            'redfish-tests-%s-%s' % (
                test['vendor'].lower(),
                test['model'].lower()
            )
        )
        if os.path.isdir(test_template_directory_name):
            print('Test template not expected to exist: %s' % (test_template_directory_name))
            return False

        os.mkdir(test_template_directory_name)

        test_doc_directory_name = os.path.join(
            get_doc_directory(),
            'redfish-tests-%s-%s' % (
                test['vendor'].lower(),
                test['model'].lower()
            )
        )

        if os.path.isdir(test_doc_directory_name):
            print('Test doc directory not expected to exist: %s' % (test_doc_directory_name))
            return False

        os.mkdir(test_doc_directory_name)

        for template_name in ['Resource', 'Oem', 'Action', 'Identity', 'Power', 'Thermal']:
            if not generate_redfish_test_template(redfish_test_templates_directory, test_template_directory_name, template_name, test, results_directory):
                print('Generating test %s template %s failed' % (
                    test['model'],
                    template_name
                ))
                return False

        if not generate_redfish_resource_template(test_template_directory_name, test, results_directory):
            print('Generating test %s resources failed' % (
                test['model']
            ))
            return False

    return True


def generate_redfish_test_templates(results_directory):
    tests = get_redfish_test_endpoints()
    if tests is None:
        return False

    if not generate_redfish_readme_tests(tests):
        return False

    if not generate_redfish_tests(tests, results_directory):
        return False

    return True


def generate_docs_from_templates(results_directory, template_names, include_redfish=False, replace={}):
    results_directory = os.path.join(
        file_helper.get_main_dir(),
        results_directory
    )
    results = get_results(results_directory)
    if results is None:
        return False

    selected_templates = get_template_names(
        template_names,
        include_redfish=include_redfish
    )
    selected_templates_count = get_templates_count(
        selected_templates
    )

    templates = match_templates_with_results(
        selected_templates,
        results
    )
    templates_count = get_templates_count(
        templates
    )

    print('\nMatching Templates:')
    for template_group in templates:
        for template_info in templates[template_group]:
            print('- %s' % (template_info['filename']))

            content = replace_keywords(template_info['content'], results_directory)
            filename = os.path.join(
                os.path.join(
                    get_doc_directory(),
                    template_group
                ),
                os.path.basename(template_info['filename'])
            )
            for key in replace:
                content = content.replace(key, replace[key])

            with open(filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(str(content))

    if templates_count < selected_templates_count:
        print('\nFailed Templates:')
        for all_template_group in selected_templates:
            for all_template_filename in selected_templates[all_template_group]:
                found = False

                reference_filename = os.path.join(
                    os.path.join(
                        get_templates_directory(),
                        all_template_group
                    ),
                    all_template_filename
                )

                for template_group in templates:
                    for template_info in templates[template_group]:
                        if template_info['filename'] == reference_filename:
                            found = True
                            break

                if not found:
                    print('- %s' % (reference_filename))

    print('\nSummary')
    print('All templates: %s' % (selected_templates_count))
    print('Matching templates: %s' % (templates_count))
    if selected_templates_count != templates_count:
        return False

    return True


def generate_docs(results_directory, template_names=[], include_redfish=False, redfish_tests=False, replace={}):
    if include_redfish:
        clean_redfish_test_templates()
        clean_redfish_test_doc()
        if redfish_tests:
            if not generate_redfish_test_templates(results_directory):
                print('Redfish tests templates generation failed...')
                return False
        else:
            generate_redfish_readme_no_tests()

    if not generate_docs_from_templates(results_directory, template_names, include_redfish=include_redfish, replace=replace):
        print('Not all docs generated from templates...')
        return False

    return True


def generate_template_docs(template_names=[]):
    template_handler = template_helper.TemplateHelper()

    # {'aci': ['PolicyTemplate.md', 'PolicyTemplateAll.md', 'PolicyTemplateIntf.md', 'PolicyTemplateJson.md', 'PolicyTemplateName.md', 'PolicyTemplateUsage.md', 'PolicyTemplateVerbose.md']}
    for template_name in template_names:
        templates = {}
        templates_directory = get_templates_directory()
        for template_subdirectory in os.listdir(templates_directory):
            if len(template_names) > 0 and template_subdirectory not in template_names:
                continue

            templates[template_subdirectory] = []
            for template_filename in os.listdir(os.path.join(templates_directory, template_subdirectory)):
                if template_filename.endswith('.md'):
                    if 'Template' in template_filename:
                        templates[template_subdirectory].append(template_filename)

    items = []
    items.append(['Slow Drain', 'Drain', 'drain'])
    items.append(['Fibre Channel', 'Fc', 'fc'])
    items.append(['Link Flap', 'Flap', 'flap'])
    items.append(['L2', 'L2', 'l2'])
    items.append(['Port Channel', 'Lacp', 'lacp'])
    items.append(['Port Channel Member', 'Lacpm', 'lacpm'])
    items.append(['Link Level', 'Link', 'link'])
    items.append(['Link Level Flow Control', 'LinkFc', 'linkfc'])
    items.append(['LLDP', 'Lldp', 'lldp'])
    items.append(['MCP', 'Mcp', 'mcp'])
    items.append(['Priority Flow Control', 'Pfc', 'pfc'])
    items.append(['Port Security', 'Portsec', 'portsec'])
    items.append(['Storm Control', 'Storm', 'storm'])
    items.append(['Spanning Tree', 'Stp', 'stp'])
    items.append(['Synchronous Ethernet', 'Synce', 'synce'])
    items.append(['Transceiver', 'Trans', 'trans'])

    for key in templates:
        for filename in templates[key]:
            template_filename = os.path.join(
                os.path.join(
                    templates_directory,
                    key
                ),
                filename
            )

            if not os.path.isfile(template_filename):
                print('File not found: %s' % (template_filename))
                continue

            print('File found: %s' % (template_filename))
            for item in items:
                new_filename = template_filename.replace('Template', item[1])
                print(new_filename)
                if os.path.isfile(new_filename):
                    print('Already exists...')
                    continue

                try:
                    with open(template_filename, 'r', encoding='utf-8') as file_handler:
                        content = file_handler.read()
                except BaseException:
                    print('Failed to read: %s' % (template_filename))
                    return False

                variables = {}
                variables['TITLE'] = item[0]
                variables['NAME'] = item[1]
                variables['TEST'] = item[2]

                new_content = template_handler.replace_variables(content, variables)

                try:
                    with open(new_filename, 'w', encoding='utf-8') as file_handler:
                        file_handler.write(str(new_content))

                except BaseException:
                    print('Template file write failed:%s' % (new_filename))
                    return False

                print('Created')

    return True


def sanitize_anonymize_content(content):
    new_content = []
    for line in content.split('\r\n'):
        new_content.append(line)
    return '\n'.join(new_content)


def anonymize_line(line, rule, allowed):
    if rule['key'] == '__IP__':
        ips = ip_helper.get_string_ipv4s(line)
        for ip_address in ips:
            if ip_address not in allowed:
                if rule['value'] == '__MASK__':
                    line = line.replace(
                        ip_address,
                        ip_helper.get_obscured_ipv4(ip_address)
                    )
                else:
                    line = line.replace(
                        ip_address,
                        rule['value']
                    )

        return line

    if rule['key'] == '__MAC__':
        macs = ip_helper.get_string_macs(line)
        for mac in macs:
            if mac not in allowed:
                if rule['value'] == '__MASK__':
                    line = line.replace(
                        mac,
                        ip_helper.get_obscured_mac(mac)
                    )
                else:
                    line = line.replace(
                        mac,
                        rule['value']
                    )

        return line

    if filter_helper.match_string('*%s*' % (rule['key']), line):
        line = line.replace(rule['key'], rule['value'])

    return line


def anonymize_file(content, rule, allowed):
    count = 0
    started = False
    if 'after' not in rule:
        started = True

    new_content = []
    for line in content.split('\n'):
        if not started:
            new_content.append(
                line
            )
            if 'after' in rule:
                if filter_helper.match_string(rule['after'], line):
                    started = True

            continue

        new_line = anonymize_line(line, rule, allowed)
        if line != new_line:
            count = count + 1

        new_content.append(new_line)

    return '\n'.join(new_content), count


def anonymize_section(section):
    directory = get_doc_directory()
    for subdir in section['directory'].split(','):
        directory = os.path.join(
            directory,
            subdir
        )

    if not os.path.isdir(directory):
        print('Target directory not found: %s' % (directory))
        return False

    print('Directory: %s' % (directory))

    for file_in_dir in os.listdir(directory):
        filename = os.path.join(
            directory,
            file_in_dir
        )
        if not os.path.isfile(filename):
            continue

        file_match = False
        for file_match_rule in section['files']:
            if filter_helper.match_string(file_match_rule, file_in_dir):
                file_match = True

        if not file_match:
            continue

        content = file_helper.get_file(filename)
        if content is None:
            print('File read failed: %s' % (filename))
            return False

        content = sanitize_anonymize_content(content)

        total_count = 0
        for rule in section['rules']:
            content, count = anonymize_file(content, rule, section['allowed'])
            if content is None:
                return False

            total_count = total_count + count

        print('- %s [%s]' % (os.path.basename(filename), total_count))

        if total_count > 0:
            if not file_helper.set_file(filename, content):
                print('File anonymize failed')
                return False

    return True


def verify_anonymized_string(line, forbidden, allowed):
    ips = ip_helper.get_string_ipv4s(line)
    macs = ip_helper.get_string_macs(line)

    success = True

    for rule in forbidden:
        if rule == '__IP__':
            if len(ips) > 0:
                print('Failed on IP check: %s' % (ips))
                success = False

        if rule == '__MAC__':
            if len(macs) > 0:
                print('Failed on MAC check: %s' % (macs))
                success = False

        if rule not in ['__IP__', '__MAC__']:
            if filter_helper.match_string('*%s*' % (rule), line):
                overruled = False
                for item in allowed:
                    if rule in item:
                        if filter_helper.match_string('*%s*' % (item), line):
                            overruled = True

                if not overruled:
                    print('Failed on string check: %s' % (rule))
                    success = False

    if not success:
        print('Line: %s' % (line))

    return success


def verify_anonymized_content(content, forbidden, allowed, break_on_error=True):
    success = True
    for line in content.split('\n'):
        success = success and verify_anonymized_string(
            line,
            forbidden,
            allowed
        )
        if break_on_error and not success:
            return success

    return success


def verify_anonymize_docs(directory=None, break_on_error=True):
    print('Verify...')
    filename = os.path.join(
        get_doc_directory(),
        'sanity.json'
    )
    if not os.path.isfile(filename):
        print('[ERROR] Anonymize rules file not found: %s' % (filename))
        return False

    sanity_rules = file_helper.get_file_json(filename)
    if sanity_rules is None:
        print('[ERROR] Sanity rules file read failed: %s' % (filename))
        return False

    ignored_directories = ['psirt']
    success = True
    for subdirectory in os.listdir(get_doc_directory()):
        if subdirectory in ignored_directories:
            continue

        if directory is not None and subdirectory not in directory:
            continue

        directory_name = os.path.join(
            get_doc_directory(),
            subdirectory
        )
        if os.path.isdir(directory_name):
            for child_name in os.listdir(directory_name):
                if child_name.endswith('.md'):
                    filename = os.path.join(directory_name, child_name)
                    content = file_helper.get_file(filename)
                    if content is None:
                        print('File read failed: %s' % (filename))
                        return False

                    print('- %s' % (filename))
                    success = success and verify_anonymized_content(
                        content,
                        sanity_rules['forbidden'],
                        sanity_rules['allowed'],
                        break_on_error=break_on_error
                    )

                    if break_on_error and not success:
                        return success

    return success


def anonymize_docs(verify=True):
    filename = os.path.join(
        get_doc_directory(),
        'anonymize.json'
    )
    if not os.path.isfile(filename):
        print('[ERROR] Anonymize rules file not found: %s' % (filename))
        return False

    anonymize_rules = file_helper.get_file_json(filename)
    if anonymize_rules is None:
        print('[ERROR] Anonymize rules file read failed: %s' % (filename))
        return False

    for anonymize_rule in anonymize_rules:
        success = anonymize_section(anonymize_rule)
        if not success:
            return False

    success = True
    if verify:
        success = verify_anonymize_docs(
            break_on_error=True
        )

    return success
