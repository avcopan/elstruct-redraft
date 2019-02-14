""" empty functions defining the function signatures for each writer module
"""


def method_list():
    """ list of available electronic structure methods
    """
    raise NotImplementedError


def basis_list():
    """ list of available electronic structure basis sets
    """
    raise NotImplementedError


def energy_input_string(method, basis, geom, geom_type, charge, mult,
                        memory=1, comment='', job_options='', corr_options='',
                        scf_options=''):
    """ energy input string
    """

    raise NotImplementedError(
        method, basis, geom, geom_type, charge, mult, memory, comment,
        job_options, corr_options, scf_options
    )
