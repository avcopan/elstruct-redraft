""" psi4 writer module """
import os
from ... import template
from . import job
from . import theory
from . import molecule

# set the path to the template files
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_DIR = os.path.join(THIS_DIR, 'templates')


def method_list():
    """ list of available electronic structure methods
    """
    return theory.METHOD_LST


def basis_list():
    """ list of available electronic structure basis sets
    """
    return theory.BASIS_LST


def energy_input_string(method, basis, geom, geom_type, charge, mult,
                        memory=1, comment='', job_options='', corr_options='',
                        scf_options=''):
    """ energy input string
    """
    assert method in method_list()
    fill_dct = {}
    fill_dct.update(job.fillvalue_dictionary(comment, memory, job_options))
    fill_dct.update(molecule.fillvalue_dictionary(geom, geom_type, charge,
                                                  mult))
    fill_dct.update(theory.fillvalue_dictionary(method, basis, scf_options,
                                                corr_options))
    inp_str = template.read_and_fill(TEMPLATE_DIR, 'all.mako', fill_dct)
    return inp_str
