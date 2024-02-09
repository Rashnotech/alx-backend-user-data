#!/usr/bin/env python3
"""a module that handles Regex-ing"""
import re


def filter_datum(fields: list, redaction: str, message: str, separator: str):
    """
    A function that log message obfuscated
    Args:
        fields: a list of str representing all field obfuscate
        redaction: a str represent.. what the field will obfuscate
        message: a str representing the log line
        seperator: a str representing by all fields in the log line
    """
    pattern = '|'.join(map(re.escape, fields))
    replace = re.compile(r'{}{}[^{}]*'.format(separator, pattern, separator))
    return replace.sub(separator + redaction, message)
