""" job: memory, parallelism, etc.
"""
from . import _keys as template_keys


def fillvalue_dictionary(comment, memory, job_options):
    """ get the template fill values for job directives
    """
    fill_dct = {
        template_keys.COMMENT: comment,
        template_keys.MEMORY: memory,
        template_keys.JOB_OPTIONS: job_options,
    }
    return fill_dct
