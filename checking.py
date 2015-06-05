def is_all_instance(iterable, aclass):
    ok = True
    for element in iterable:
        ok &= isinstance(element, aclass)
    return ok
