a = [1,2,3]
b = a.append(3)
c = a.insert(3, 5)

A = [a, b, c]
for i in A:
    if isinstance(i, list):
        print("my_variable is a list.")
    else:
        print("my_variable is not a list.")