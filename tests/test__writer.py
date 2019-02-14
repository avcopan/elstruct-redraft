""" test elstruct.writer
"""
from elstruct import writer


def test__programs():
    """ test writer.programs
    """
    assert writer.programs() == ('psi4',)


def test__energy_programs():
    """ test writer.energy_programs
    """
    assert writer.energy_programs() == ('psi4',)


def test__method_list():
    """ test writer.method_list
    """
    for prog in writer.energy_programs():
        methods = writer.method_list(prog)
        assert methods  # make sure it isn't empty
        print((prog, methods))


def test__basis_list():
    """ test writer.basis_list
    """
    for prog in writer.energy_programs():
        bases = writer.basis_list(prog)
        assert bases  # make sure it isn't empty
        print((prog, bases))


def test__energy_input_string():
    """ test elstruct energy writers
    """
    for prog in writer.energy_programs():
        writer.energy_input_string(
            prog=prog, method='rhf-mp2', basis='6-31g', geom=None,
            geom_type=None, charge=None, mult=None
        )


if __name__ == '__main__':
    test__programs()
    test__method_list()
    test__basis_list()
