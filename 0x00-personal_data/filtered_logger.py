#!/usr/bin/env python3
"""function filter_datum:
       Arguments
           fields
           redaction
           message
           separator
   """
import re


def filter_datum(fields, redaction, message, separator):
    pattern = r'(' + '|'.join(fields) + r')=[^' + separator + r']*'
    return re.sub(
        pattern,
        lambda m: m.group().split('=')[0] +
        '=' +
        redaction,
        message)
