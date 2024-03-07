def key_in_dict(key, d):
     if key in d.keys():
         return True
     else:
         for i in d.keys():
             if isinstance(d[i],dict):
                 if key_in_dict(key, d[i]):
                     return True
         return False


def value_in_dict(value, d):
    if value in d.values():
        return True
    else:
        for i in d.values():
            if isinstance(i,dict):
                if value_in_dict(value, i):
                    return True
        else:
            return False


