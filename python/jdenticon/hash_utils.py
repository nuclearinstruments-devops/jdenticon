"""
Hash utilities for Jdenticon
"""
import hashlib
import re


def is_valid_hash(hash_candidate):
    """
    Checks if the given string is a valid hash for Jdenticon.
    
    Args:
        hash_candidate: String to check
        
    Returns:
        The hash if valid, None otherwise
    """
    if isinstance(hash_candidate, str) and re.match(r'^[0-9a-f]{11,}$', hash_candidate, re.IGNORECASE):
        return hash_candidate
    return None


def compute_hash(value):
    """
    Computes a SHA1 hash for the specified value.
    
    Args:
        value: Value to hash
        
    Returns:
        Hexadecimal hash string
    """
    if value is None:
        value = ""
    value_str = str(value)
    return hashlib.sha1(value_str.encode('utf-8')).hexdigest()


def parse_hex(hash_str, start_index, length=None):
    """
    Parses a substring of a hexadecimal string as an integer.
    
    Args:
        hash_str: Hexadecimal string
        start_index: Start index (negative values count from end)
        length: Number of characters to parse (default: all remaining)
        
    Returns:
        Integer value
    """
    if start_index < 0:
        start_index = len(hash_str) + start_index
    
    if length is None:
        substring = hash_str[start_index:]
    else:
        substring = hash_str[start_index:start_index + length]
    
    if not substring:
        return 0
    
    try:
        return int(substring, 16)
    except ValueError:
        return 0
