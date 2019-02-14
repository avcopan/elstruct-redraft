""" psi4 writer module """
import os
from . import theory

# set the path to the template files
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_PATH = os.path.join(DIR_PATH, 'templates')


def method_list():
    """ list of available electronic structure methods
    """
    return theory.METHOD_LST


def basis_list():
    """ list of available electronic structure basis sets
    """
    return theory.BASIS_LST


def energy_input_string(method, basis, geom, geom_type, charge, mult,
                        memory=1, nprocs=1, comment=1, corr_options=None,
                        scf_options=None):
    """ energy input string
    """
    assert method in method_list()
    theory_fill_dct = theory.fillvalue_dictionary(method, basis)
    print(theory_fill_dct)
    print(
        method, basis, geom, geom_type, charge, mult, memory, nprocs, comment,
        corr_options, scf_options
    )
