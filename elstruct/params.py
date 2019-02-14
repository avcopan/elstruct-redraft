""" common elstruct parameters
"""


class BASIS():
    """ electronic structure basis sets """
    STO3G = 'sto-3g'
    P321G = '3-21g'
    P631G = '6-31g'
    PVDZ = 'cc-pvdz'
    PVTZ = 'cc-pvtz'


class METHOD():
    """ electronic structure methods """

    class SCF():
        """ scf method names """
        RHF = 'rhf'
        UHF = 'uhf'
        ROHF = 'rohf'

    class CORR():
        """ correlation method names """
        MP2 = 'mp2'
        RMP2 = 'rmp2'

    # RHF Methods
    RHF = SCF.RHF
    RHF_MP2 = '-'.join([SCF.RHF, CORR.MP2])
    # UHF Methods
    UHF = SCF.UHF
    UHF_MP2 = '-'.join([SCF.UHF, CORR.MP2])
    # ROHF Methods
    ROHF = SCF.ROHF
    ROHF_MP2 = '-'.join([SCF.ROHF, CORR.MP2])
    ROHF_RMP2 = '-'.join([SCF.ROHF, CORR.RMP2])

    @staticmethod
    def split_name(method_name):
        """ split a method name into an scf method and a correlated method
        """
        split = method_name.split('-')
        assert len(split) <= 2
        scf_method, corr_method = (split if len(split) == 2 else
                                   (split, None))
        return scf_method, corr_method


class PROGRAM():
    """ Programs to be called """
    PSI4 = 'psi4'
