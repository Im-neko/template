#!/usr/bin/python
#-*- coding:utf8 -*-
"""
{{_name_}}
"""

class {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}(object):

	def __init__(self{{_cursor_}}):

    def __repr__(self):
        return

    @classmethod
    def public_class_method(cls):
        """
        インスタンス化しなくても呼び出せる
        """
        pass



if __name__ == '__main__':
    ins = {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}()
    ins.public_class_method()
