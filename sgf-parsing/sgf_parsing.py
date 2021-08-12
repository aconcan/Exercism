import re

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other



    def parse(self,input_string):
        # if not input_string.isalpha():
        #         raise ValueError('.+')
        
        pattern = re.compile(r'''
            \(?[A-Z]\[[A-Za-z]\]\)? # find properties
        ''', re.VERBOSE)

        #find properties
        nodes = pattern.findall(input_string)



        print(nodes)
        
test = SgfTree("(;A[B];B[C])")
print(test.parse("(;A[B](;B[C])(;C[D]))"))