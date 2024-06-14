import sys
import os
import json
import platform
import uuid
import yaml
import hashlib


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
        return None

    my_os = platform.system()
    try:
        with open(filename, 'rb') as file_handler:
            content = file_handler.read()

        if my_os == 'Windows':
            content.replace(b'\r\n', b'\n')

        content = content.decode('utf-8')

    except BaseException:
        return None

    return content


def get_file_text(filename):
    if not os.path.isfile(filename):
        return None

    try:
        with open(filename, 'r', encoding='utf-8') as file_handler:
            content = file_handler.read()

    except BaseException:
        return None

    return content


def get_file_json(filename):
    if not os.path.isfile(filename):
        return None

    try:
        with open(filename, 'r', encoding='utf-8') as file_handler:
            content = json.loads(file_handler.read())

    except BaseException:
        return None

    return content


def get_file_yaml(filename):
    if not os.path.isfile(filename):
        return None

    try:
        with open(filename, 'r', encoding='utf-8') as file_handler:
            content = yaml.safe_load(file_handler)

    except BaseException:
        return None

    return content


def set_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file_handler:
            file_handler.write(content)

    except BaseException:
        return False

    return True


def set_file_json(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file_handler:
            file_handler.write(json.dumps(content, indent=4))

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


def decode_ascii(content):
    char_map = {}
    char_map['0A'] = '\n'
    char_map['20'] = ' '
    char_map['21'] = '!'
    char_map['22'] = '"'
    char_map['23'] = '#'
    char_map['24'] = '$'
    char_map['25'] = '%'
    char_map['26'] = '&'
    char_map['27'] = '\''
    char_map['28'] = '('
    char_map['29'] = ')'
    char_map['2A'] = '*'
    char_map['2B'] = '+'
    char_map['2C'] = ','
    char_map['2D'] = '-'
    char_map['2E'] = '.'
    char_map['2F'] = '/'
    char_map['30'] = '0'
    char_map['31'] = '1'
    char_map['32'] = '2'
    char_map['33'] = '3'
    char_map['34'] = '4'
    char_map['35'] = '5'
    char_map['36'] = '6'
    char_map['37'] = '7'
    char_map['38'] = '8'
    char_map['39'] = '9'
    char_map['3A'] = ':'
    char_map['3B'] = ';'
    char_map['3C'] = '<'
    char_map['3D'] = '='
    char_map['3E'] = '>'
    char_map['3F'] = '?'
    char_map['40'] = '@'
    char_map['5B'] = '['
    char_map['5C'] = '\\'
    char_map['5D'] = ']'
    char_map['5E'] = '^'
    char_map['5F'] = '_'
    char_map['60'] = '`'
    char_map['7B'] = '{'
    char_map['7C'] = '|'
    char_map['7D'] = '}'
    char_map['7E'] = '~'

    for char_key in char_map:
        content = content.replace('%%%s' % (char_key), char_map[char_key])

    return content


def get_md5(filename):
    if not os.path.isfile(filename):
        return None
    hasher = hashlib.md5()
    blocksize = 65536
    with open(filename, 'rb') as file_handler:
        buf = file_handler.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file_handler.read(blocksize)
    md5 = hasher.hexdigest()
    return md5
