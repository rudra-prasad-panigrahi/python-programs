def palindrom(n):
        if str(n) == str(n)[::-1]:
                return True
        return False

print(palindrom(int(input())))