OK_FORMAT = True
test = {   'name': 'q1b',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> "|" not in regx2\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> re.match(regx2, 'can').group()\n'can'", 'hidden': False, 'locked': False},
                                   {'code': ">>> re.match(regx2, 'fan').group()\n'fan'", 'hidden': False, 'locked': False},
                                   {'code': ">>> re.match(regx2, 'man').group()\n'man'", 'hidden': False, 'locked': False},
                                   {'code': ">>> re.match(regx2, 'dan') is None\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> re.match(regx2, 'ran') is None\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> re.match(regx2, 'pan') is None\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
