""" input writer module

(look at the module_template for the function signatures and docstrings)
"""
from . import module_template
from .. import program_modules as pm


def programs():
    """ the list of program modules implementing anything """
    # check whether they implement the `method_list()` function
    return pm.program_modules_with_functions(
        'writer', [module_template.method_list, module_template.basis_list])


def energy_programs():
    """ the list of program modules implementing energy writers """
    return pm.program_modules_with_function(
        'writer', module_template.energy_input_string)


def method_list(prog, *args, **kwargs):
    """ _ """
    return pm.call_module_function(
        prog, 'writer', module_template.method_list,
        *args, **kwargs
    )


def basis_list(prog, *args, **kwargs):
    """ _ """
    return pm.call_module_function(
        prog, 'writer', module_template.basis_list,
        *args, **kwargs
    )


def energy_input_string(prog, *args, **kwargs):
    """ _ """
    return pm.call_module_function(
        prog, 'writer', module_template.energy_input_string,
        *args, **kwargs
    )
