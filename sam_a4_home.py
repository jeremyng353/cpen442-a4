import hashlib
import string
def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
def permutations(arr, hashed):
    arr = Convert(arr)
    def helper(cur, arr):
        if len(cur) == 6:
            if hash("".join(cur)) == hashed:
                print(f'PASSWORD FOUND: {"".join(cur)}')
            return
        for i in range(len(arr)):
            helper(cur + [arr[i]], arr)
    helper([], arr)
    return
if __name__ == '__main__':
    possible_chars = string.printable[:-6]
    password_hash = 'e8874058f0f4890bba61024a6093b3c0e3e2f074'
    print("TESTING PERMUTATIONS OF PRINTABLE ASCII CHARS")
    permutations(possible_chars, password_hash)
    print("DONE")