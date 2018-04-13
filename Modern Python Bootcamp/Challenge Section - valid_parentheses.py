def valid_parentheses(s):
    paren = 0
    for i in s:
        paren += 1 if i == '(' else -1
        if paren < 0:
            return False
    return paren == 0


print(valid_parentheses("()"))  # True
print(valid_parentheses(")(()))"))  # False
print(valid_parentheses("("))  # False
print(valid_parentheses("(())((()())())"))  # True
print(valid_parentheses('))(('))  # False
print(valid_parentheses('())('))  # False
print(valid_parentheses('()()()()())()('))  # False)
