""" command-line interface for elstruct
"""
import autocom


def main(sysargv):
    """ main function """
    autocom.call_subcommand(
        sysargv, calling_pos=0, subcmd_func_dct={
            'write': write,
            'run': run,
            'read': read,
        }
    )


def write(sysargv, calling_pos):
    """ the write subcommand """
    raise NotImplementedError


def run(sysargv, calling_pos):
    """ the run subcommand """
    raise NotImplementedError


def read(sysargv, calling_pos):
    """ the read subcommand """
    raise NotImplementedError
