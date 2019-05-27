def cmp_ignore_case(s1, s2):
    if s1.lower() > s2.lower():
        return 1
    elif s1.lower() < s2.lower():
        return -1
    else:
        return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
