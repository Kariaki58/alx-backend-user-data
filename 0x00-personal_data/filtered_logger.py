#!/usr/bin/env python3
"""Regexing"""
import re

def filter_datum(fields, redaction, message, separator):
	"""filter datum"""
    return re.sub(r'(?<=(^|{}))[^{}=]+(?={}|\Z)'.format(separator, separator, separator), redaction, message)
