#!/usr/bin/python3
"""Module for LockedClass"""


class LockedClass:
    """Empty Class without ability to add attributes except first_name"""
    __slots__ = ['first_name']
