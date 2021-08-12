# class PhoneNumber:
#     def __init__(self, number):
#         self.number = ''.join([num for num in number if num.isdigit()])
        
#         if self.number[0] == '1':
#             self.number = self.number.replace(self.number[0], '')

#         if len(self.number) != 10:
#             raise ValueError('.+')

#         if int(self.number[0]) < 2 or int(self.number[3]) < 2:
#             raise ValueError('.+')

#         self.area_code = self.number[:3]

#     def pretty(self):
#         return '('+ self.number[:3] + ')-' + self.number[3:6] + '-' + self.number[6:]

import re

class Phone(object):
    _pattern = re.compile(r'''
        ^\+?1?              # optional literal `+` and country code
        (?:[-. ]+)?         # optional separators
        \(?([2-9]\d{2})\)?  # the area code, with or without surrounding parens
        (?:[-. ]+)?         # optional separators
        ([2-9]\d{2})        # the exchange code
        (?:[-. ]+)?         # optional separators
        (\d{4})$            # the subscriber number
    ''', re.VERBOSE)

    def __init__(self, phone_number):
        try:
            self.area_code, self.exchange, self.subscriber = \
                    self._pattern.search(phone_number.strip()).groups()
        except AttributeError:
            raise ValueError('Invalid `phone_number`')

    @property
    def number(self):
        return self.area_code + self.exchange + self.subscriber
    
    def pretty(self):
        return '({}) {}-{}'.format(self.area_code, self.exchange, self.subscriber)

test = Phone('(223) 456-7890')
print(test.number)