import sys
import os
import platform
import uuid
import yaml


def get_main_dir():
    if getattr(sys, 'frozen', False):
        main_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return main_dir

    main_dir = os.path.dirname(
        getattr(sys, '_MEIPASS', os.path.abspath(__file__))
    )

    while True:
        if os.path.basename(main_dir) == 'lib':
            break
        main_dir = os.path.dirname(main_dir)

    main_dir = os.path.dirname(main_dir)
    return main_dir


def get_file(filename):
    if not os.path.isfile(filename):
        return False, 'File not found: %s' % (filename)

    my_os = platform.system()
    try:
        with open(filename, 'rb') as file_handler:
            content = file_handler.read()

        if my_os == 'Windows':
            content.replace(b'\r\n', b'\n')

        content = content.decode('utf-8')

    except BaseException:
        return False, 'File read failed: %s' % (filename)

    return True, content


def get_file_yaml(filename):
    if not os.path.isfile(filename):
        return False, 'File not found: %s' % (filename)

    try:
        with open(filename, 'rb') as file_handler:
            content = yaml.safe_load(file_handler)

    except BaseException:
        return False, 'YAML format required: %s' % (filename)

    return True, content


def set_file(filename, content):
    if not os.path.isfile(filename):
        return False, 'File not found: %s' % (filename)

    try:
        with open(filename, 'w', encoding='utf-8') as file_handler:
            file_handler.write(content)

    except BaseException:
        return False

    return True


def set_tmp_file(content):
    filename = '/tmp/%s' % (str(uuid.uuid4()))
    try:
        with open(filename, 'w', encoding='utf-8') as file_handler:
            file_handler.write(content)

    except BaseException:
        return None

    return filename
