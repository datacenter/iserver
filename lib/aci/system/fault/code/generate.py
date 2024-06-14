import re


def sanitize_string(value):
    value = value.strip()
    value = re.sub(' +', ' ', value)
    return value


# https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/all/syslog/guide/b_ACI_System_Messages_Guide/b_ACI_System_Messages_Guide_chapter_011.html
with open('source.html', 'rb') as file_handler:
    content = file_handler.read()

codes = {}
current = None

for line in content.decode('utf-8').split('\n'):
    line = sanitize_string(line)
    if line.startswith('<h3 class="title sectiontitle">F'):
        current = line.split('<h3 class="title sectiontitle">')[1].split(':')[0]
        continue

    if line.startswith('<strong class="ph b">Explanation</strong>:'):
        explanation = sanitize_string(
            line.split('<strong class="ph b">Explanation</strong>:')[1]
        )
        if current is None:
            print('Explanation hanging:%s' % (explanation))
            continue

        codes[current] = explanation.replace('"', "'")

print('class SystemFaultCode():')
print('    def __init__(self):')
print('        self.system_fault_code = {}')
for code in codes:
    print('        self.system_fault_code["%s"] = "%s"' % (
        code,
        codes[code]
    ))
