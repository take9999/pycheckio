def reverse_ascending(items):
    ans_items = []
    tmp_items = []  # sort対象を入れる
    pre_item = -1

    while items:
        one_item = items.pop(0)
        # 初期状態 or 一つ前のitemより大きい場合のみsort対象とする
        if len(tmp_items) == 0 or pre_item < one_item:
            tmp_items.append(one_item)
            pre_item = one_item
        # 一つ前のitem以下の場合は、これまで貯めたtmp_itemsをsortして、ans_itemsの末尾へ追加
        else:
            tmp_items = sorted(tmp_items, reverse=True)
            ans_items += tmp_items
            tmp_items = [one_item]
            pre_item = one_item
    # tmp_itemsが残っていれば、sortしてans_itemsの末尾へ追加
    if len(tmp_items) >= 0:
        tmp_items = sorted(tmp_items, reverse=True)
        ans_items += tmp_items
    print(ans_items)
    return ans_items


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
