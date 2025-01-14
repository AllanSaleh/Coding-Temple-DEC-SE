num = 50.54

string_num = str(num)
print(type(string_num), string_num)

index_of_point = string_num.index(".")
print(index_of_point)
sliced = string_num[index_of_point + 1:]
print(len(sliced))