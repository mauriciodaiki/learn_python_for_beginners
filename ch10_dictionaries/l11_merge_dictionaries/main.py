def merge(dict1, dict2):
    merge = {}
    for key in dict1:
        merge[key] = dict1[key]
    for key in dict2:
        merge[key] = dict2[key]

    return merge

