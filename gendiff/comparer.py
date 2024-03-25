def compare_data(dict1, dict2):
    """
    The function compares two dictionaries and generates
    a hierarchical difference representation.

    Args:
        dict1 (dict): The first dictionary for comparison.
        dict2 (dict): The second dictionary for comparison.

    Returns:
        dict: A hierarchical representation of the differences
        between the two dictionaries.
    """
    key_set = set(dict1) | set(dict2)
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
                'value': compare_data(dict1[key], dict2[key])
            }
        else:
            res[key] = {
                'status': 'changed',
                'value': {'old value': dict1[key], 'new value': dict2[key]}
            }
    return res
