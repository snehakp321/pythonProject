def longestCommonPrefix(strs):
    if len(strs)==0:
        return ""

    res=""
    strs=sorted(strs)
    for i in strs[0]:
        if strs[-1].startswith(res+i):
            res+=i
        else:
            break
    return res


strs1 = ["dog","racecar","car"]
print(longestCommonPrefix(strs1))
