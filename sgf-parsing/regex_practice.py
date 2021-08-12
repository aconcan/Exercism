import re

pattern = re.compile('''
    [cmf]an
''', re.VERBOSE)

print(pattern.search('can').groups)