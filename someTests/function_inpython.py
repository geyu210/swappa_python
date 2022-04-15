def add():
    def add_2(c, d):
        return c+d
    return add_2


print(add)
e = add()(2, 3)
print(e)
