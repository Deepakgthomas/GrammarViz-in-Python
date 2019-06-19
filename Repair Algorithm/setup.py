from distutils.core import setup, Extension


repair_module = Extension('repair',
                           sources=['repair_wrap.cxx', 'repair.cpp'],
                           )

setup (name = 'repair',
       version = '01',
       author      = "Deepak Thomas",
       description = """Converting repair code from C++ to  Python""",
       ext_modules = [repair_module],
       py_modules = ["repair"],
       )