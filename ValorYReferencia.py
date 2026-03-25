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
print(my_list1)
print(my_list2)

# Funciones por datos por valor

my_int = 10

def in_int(myint: int):
    my_int1 = 20
    print(my_int1)


in_int(my_int)
print(my_int)

# Funciones por datos por referencia


def in_list(my_list1: list):
    my_list1.append(30)

    my_list4 = my_list1
    my_list4.append(40)

    print(my_list1)
    print(my_list4)

my_list3 = [10, 20]
in_list(my_list3)  
print(my_list3)

