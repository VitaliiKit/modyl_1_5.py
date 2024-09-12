immutable_var= ('opel', 'audi', 1, 2, True)
print(type(immutable_var))
print(immutable_var)
#immutable_var=[0]= ('lada'), кортеж- неизменяемая коллекция, относится к неизменяемым типам данным, нельзя изменять сами элементы.
immutable_list= ['toyota', 'nissan', 'mazda']
print(immutable_list)
immutable_list.append(False)
print(immutable_list)
immutable_list.extend('audi')
print(immutable_list)
immutable_list.remove('nissan')
print(immutable_list)