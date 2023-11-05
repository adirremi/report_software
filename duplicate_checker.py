def has_duplicate_keys(my_dict):
    seen = set()
    duplicates = set()

    for key in my_dict:
        str_key = str(key["address"])
        if str_key in seen and str_key!= "":
            duplicates.add(str_key)
        else:
            seen.add(str_key)

    return duplicates
