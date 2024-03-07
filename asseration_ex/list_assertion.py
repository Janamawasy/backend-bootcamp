def value_in_list(value, lst):
    if value in lst:
        return True
    else:
        for i in lst:
            if isinstance(i, list):
                if value_in_list(value, i):
                    return True
        return False

