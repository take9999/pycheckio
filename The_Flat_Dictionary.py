import collections

def flatten(dictionary):
    sep = "/"
    obj = {}

    def recurse_dict(t, parent_key=""):
        if isinstance(t, dict):
            for k, v in t.items():
                if isinstance(v, dict):
                    recurse_dict(v, parent_key + sep + k)
                elif v == {}:
                    obj[parent_key + sep + k] = {}
                else:
                    obj[parent_key + sep + k] = v
        else:
            print("not dict")

    for dk, dv in dictionary.items():
        if isinstance(dv, dict):
            recurse_dict(dv, parent_key=dk)
        elif dv == {}:
            obj[dk] = {}
        else:
            obj[dk] = dv

    print(obj)

    return obj


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
