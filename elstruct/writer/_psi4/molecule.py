""" molecule: geometry and state
"""
import automol
from ... import params as par
from . import _keys as template_keys


def fillvalue_dictionary(geom, geom_type, charge, mult):
    """ get the template fill values for molecular geometry and state
    """
    assert geom_type in par.GEOM.TYPES

    # for now
    assert geom_type is par.GEOM.TYPE.CARTESIAN
    geom_str = automol.geom.string(geom)

    fill_dct = {
        template_keys.GEOMETRY: geom_str,
        template_keys.ZMATRIX_VALUES: '',
        template_keys.CHARGE: charge,
        template_keys.MULTIPLICITY: mult,
    }
    return fill_dct
