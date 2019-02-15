""" test elstruct.write
"""
import os
import tempfile
import subprocess
from elstruct import write


PROGRAM_TEST_COMMAND_DCT = {
    'psi4': ('psi4',)
}


def test__programs():
    """ test write.programs
    """
    assert write.programs() == ('psi4',)


def test__energy_programs():
    """ test write.energy_programs
    """
    assert write.energy_programs() == ('psi4',)


def test__method_list():
    """ test write.method_list
    """
    for prog in write.energy_programs():
        methods = write.method_list(prog)
        assert methods  # make sure it isn't empty
        print((prog, methods))


def test__basis_list():
    """ test write.basis_list
    """
    for prog in write.energy_programs():
        bases = write.basis_list(prog)
        assert bases  # make sure it isn't empty
        print((prog, bases))


def test__energy_input_string():
    """ test elstruct energy writes
    """
    basis = 'sto-3g'
    geoms = [
        (('O', (None, None, None), (None, None, None)),
         ('H', (0, None, None), (1.8, None, None)),
         ('H', (0, 1, None), (1.8, 1.75, None))),
        (('O', (0., 0., 0.)),
         ('H', (0., 1., 1.)),
         ('H', (0., 1., -1.))),
    ]
    geom_types = [
        'int',
        'cart',
    ]
    charge = 0
    mult = 1

    for prog in write.energy_programs():
        for method in write.method_list(prog):
            for geom, geom_type in zip(geoms, geom_types):
                print(prog, method)
                inp_str = write.energy_input_string(
                    prog=prog, method=method, basis=basis, geom=geom,
                    geom_type=geom_type, charge=charge, mult=mult
                )

                # if we have an exectuable test command, try running it
                if prog in PROGRAM_TEST_COMMAND_DCT:
                    tmp_dir = tempfile.mkdtemp()
                    print(tmp_dir)

                    inp_file_path = os.path.join(tmp_dir, 'input.dat')
                    with open(inp_file_path, 'w') as inp_file_obj:
                        inp_file_obj.write(inp_str)

                    argv = list(PROGRAM_TEST_COMMAND_DCT[prog])
                    subprocess.check_call(argv, cwd=tmp_dir)


if __name__ == '__main__':
    # test__programs()
    # test__method_list()
    # test__basis_list()
    test__energy_input_string()
