#!/usr/bin/python3

""" function is_same_class """


def is_same_class(obj, a_class):
    """
    returns True if the object is a_class instance; otherwise False.
    """
    return (type(obj) is a_class)
