#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
{{_name_}}
"""

class {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

	def __init__(self{{_cursor_}}):

    def __repr__(self):
        return

    @classmethod
    def public_class_method(cls, param1, param2):
        """ public method
        Args:
            param1 (int): The first parameter.
            param2 (str): The second parameter.

        Returns:
            bool: The return value. True for success, False otherwise.
        """
        return True



if __name__ == '__main__':
    ins = {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}()
    ins.public_class_method()
