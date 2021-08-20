print('==================================')
print('Running main.py - module name: {0}'.format(__name__))

import modulo1 as mod1
print(mod1)
mod1.pprint_dict('main.globals', globals())
print('==================================')