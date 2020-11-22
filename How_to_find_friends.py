def check_connection(network, first, second):
    setlist = []
    for connection in network:
        s = ab = set(connection.split('-'))
        # unify all set related to a, b
        for t in setlist[:]: # we need to use copy
            if t & ab:       # check t include a, b
                s |= t
                setlist.remove(t)
        setlist.append(s)    # only s include a, b
    return any(set([first, second]) <= s for s in setlist)


if __name__ == '__main__':
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
