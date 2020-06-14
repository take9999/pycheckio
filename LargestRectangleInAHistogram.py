from typing import List


def largest_histogram(heights: List[int]) -> int:
    heights.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)

    return ans


# def largest_histogram(histogram):
#     result = 0
#     for num, i in enumerate(histogram):
#         for k in range(1, i + 1):
#             count = 1
#             for j in range(num + 1, len(histogram)):
#                 if histogram[j] >= k:
#                     count += 1
#                 else:
#                     break
#             if count * k > result:
#                 result = count * k
#
#     return result


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert largest_histogram([]) == 0, "none"
    # assert largest_histogram([5]) == 5, "one is always the biggest"
    # assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    # assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    # assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")

