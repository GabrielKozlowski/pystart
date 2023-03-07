numb = (1, '2,3', 4, '5,6', 10)

result = sum(sum(int(c) for c in n.split(',')) if isinstance(n, str) else n for n in numb)
print(result)