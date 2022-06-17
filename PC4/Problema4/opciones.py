def opcion1(n):
    file_name = 'tabla-' + str(n) + '.txt'
    f = open(file_name, 'w')
    for i in range(1, 11):
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
    f.close()

def opcion2(n):
    file_name = 'tabla-' + str(n) + '.txt'
    try: 
        f = open(file_name, 'r')
    except FileNotFoundError:
            print('No existe el fichero con la tabla del', n)
    else:
        print(f.read())

def opcion3(n,m):
    file_name = 'tabla-' + str(n) + '.txt'
    try: 
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('No existe el fichero con la tabla del ', n)
    else:
        lines = f.readlines()
        print(lines[m - 1])  