def compare_dicts(dict1, dict2):
    key_set_1 = set(dict1)
    key_set_2 = set(dict2)
    key_set = key_set_1 | key_set_2
    res = {}
    for key in sorted(key_set):
        if key not in dict1:
            res[key] = {
                'status': 'added',
                'value': dict2[key]
            }
        elif key not in dict2:
            res[key] = {
                'status': 'deleted',
                'value': dict1[key]
            }
        elif dict1[key] == dict2[key]:
            res[key] = {
                'status': 'unchanged',
                'value': dict1[key]
            }
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            res[key] = {
                'status': 'changed, nested',
                'value': compare_dicts(dict1[key], dict2[key])
            }
        else:
            res[key] = {
                'status': 'changed',
                'value': {'old': dict1[key], 'new': dict2[key]}
            }
    return res
