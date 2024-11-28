import string

s = input("Enter a string with punctuation: ")
rem = set(string.punctuation)
ans = "".join(c for c in s if c not in rem)
print(ans)