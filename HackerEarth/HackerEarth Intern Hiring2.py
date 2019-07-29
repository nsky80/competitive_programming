def check_string(a, b):
    if len(a) <= len(b) and a!= b:
        return "No"
    else:
        stamp = len(a)
        i = j = delete = cnt = 0
        strlen = len(b)
        ans = []
        del_ind = []
        pass1 = 0
        while stamp:
            if a[i] == b[j]:
                cnt += 1
                i += 1
                j += 1
                strlen -= 1
            else:
                delete += 1
                del_ind.append(i)
                i += 1
            if strlen == 0:             # and i != len(a)
                temp = list(a[pass1:i])
                # print("temp and delind", temp, del_ind)
                duplicate = temp.copy()
                for k in del_ind:
                    try:
                        temp.remove(duplicate[k-pass1])
                    except IndexError:
                        pass
                temp = "".join(temp)
                if temp == b:
                    cnt = i
                    ans.append(delete)
                else:
                    i = cnt
                delete = 0
                j = 0
                del_ind = []
                strlen = len(b)
                pass1 = i
                # stamp = cnt
                # print("cnt in strlen:", cnt)
            elif i == len(a) and j < len(b):
                stamp = cnt
            stamp -= 1
        if ans:
            return "Yes"+"\n"+str(min(ans))
        else:
            return "No"


# CHARS = 26
#
#
# # function to calculate minimum
# # numbers of characters
# # to be removed to make two
# # strings anagram
# def remAnagram(str1, str2):
#     # make hash array for both string
#     # and calculate
#     # frequency of each character
#     count1 = [ 0 ] * CHARS
#     count2 = [ 0 ] * CHARS
#
#     # count frequency of each character
#     # in first string
#     i = 0
#     while i < len(str1):
#         count1[ ord(str1[ i ]) - ord('a') ] += 1
#         i += 1
#
#     # count frequency of each character
#     # in second string
#     i = 0
#     while i < len(str2):
#         count2[ ord(str2[ i ]) - ord('a') ] += 1
#         i += 1
#
#     # traverse count arrays to find
#     # number of characters
#     # to be removed
#     result = 0
#     for i in range(26):
#         result += abs(count1[i] - count2[i])
#     return result


if __name__ == "__main__":
    t = int(input())
    strings = []
    for _ in range(t):
        a = input()
        b = input()
        strings.append([a, b])
    for s in strings:
        res = check_string(s[0], s[1])
        print("%s" %res)