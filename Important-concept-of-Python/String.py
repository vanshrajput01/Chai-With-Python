# Palindrome or not

def palindrome_func(string):
    reverse_str = ""
    for i in range(1,len(string)+1):
        reverse_str = reverse_str + string[-i]
    if string == reverse_str:
        print(f"{string} is Palindrome.")
    else:
        print(f"{string} is not Palindrome.")


palindrome_func("mama")