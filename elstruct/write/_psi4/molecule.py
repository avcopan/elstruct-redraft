""" molecule: geometry and state
"""
import automol
from ... import params as par
from . import _keys as template_keys


def fillvalue_dictionary(geom, geom_type, charge, mult):
    """ get the template fill values for molecular geometry and state
    """
    assert geom_type in par.GEOM.TYPES

    if geom_type == par.GEOM.TYPE.CARTESIAN:
        geom_str = automol.geom.string(geom)
        zmat_vals = ''
    elif geom_type == par.GEOM.TYPE.INTERNAL:
        geom_str = automol.zmatrix.zmat_string(geom)
        zmat_vals = ''

    fill_dct = {
        template_keys.GEOMETRY: geom_str,
        template_keys.ZMATRIX_VALUES: zmat_vals,
        template_keys.CHARGE: charge,
        template_keys.MULTIPLICITY: mult,
    }
    return fill_dct
