# Por Valor y Por Referencia

# tipos de dato por valor

int_a = 10
int_b = int_a
int_a = 26
print(int_a)
print(int_b)

# tipos de dato por referencia

my_list1 = [20, 70]
my_list2 = my_list1
my_list2.append(100)
#print(my_list1)
print(my_list2)
