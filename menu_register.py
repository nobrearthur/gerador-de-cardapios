import os
import sqlite3
from sqlite3 import Error


def database_connection():  # Conexão com o banco de dados
    path = "menu_database.db"
    con = None
    try:
        con = sqlite3.connect(path)
    except Error as ex:
        print(ex)
    return con


def query(connection, sql):  # INSERT, DELETE e UPDATE
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação realizada com sucesso")
        os.system("pause")
        connection.close()


def just_check(connection, sql):  # SELECT
    c = connection.cursor()
    c.execute(sql)
    result = c.fetchall()
    return result


def main_options():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Visualizar Registros")
    print("5 - Buscar Registros por Nome")
    print("6 - Mostrar Cardápio Mais Barato")
    print("7 - Mostrar Cardápio Mais Caro")
    print("8 - Sair")


def inside_options():
    os.system("cls")
    print("1 - Entrada")
    print("2 - Prato Principal")
    print("3 - Sobremesa")
    print("4 - Bebida")
    print("5 - Voltar")


def choose_table(choice):
    if choice == '1':
        table = 'tb_starters'
    elif choice == '2':
        table = 'tb_main'
    elif choice == '3':
        table = 'tb_desserts'
    elif choice == '4':
        table = 'tb_drinks'
    elif choice == '5':
        table = 0
    else:
        table = None
        print("Opção inválida! Escolher novamente...")
        os.system("pause")

    return table


def menu_insert(table_name):
    os.system("cls")
    print("INSERIR NOVO REGISTRO\n\n")
    name = input("Digite o nome: ")
    code = input("Digite o código: ")
    price = input("Digite o preço: R$  ")
    vsql = "INSERT INTO '"+table_name+"'(NAME, CODE, PRICE) VALUES('" + \
        name+"', '"+code+"', '"+price+"')"
    vcon = database_connection()  # Abrir o banco de dados
    query(vcon, vsql)
    vcon.close()  # Fechar o banco de dados


def menu_delete(table_name):
    os.system("cls")
    print("DELETAR REGISTRO\n\n")
    del_code = input("Digite o código do registro a ser deletado: ")
    vsql = "DELETE FROM '"+table_name+"' WHERE CODE="+del_code
    vcon = database_connection()
    query(vcon, vsql)
    vcon.close()


def menu_update(table_name):
    os.system("cls")
    print("ATUALIZAR REGISTRO")
    up_code = input("Digite o código do registro a ser alterado: ")
    vcon = database_connection()
    check = just_check(vcon, "SELECT * FROM '"+table_name +
                       "' WHERE CODE="+up_code+" ")
    rcode = check[0][0]
    rname = check[0][1]
    rprice = check[0][2]
    print(f'Código: {rcode}')
    print(f'Nome: {rname}')
    print(f'Preço: R$ {rprice}\n')
    print("Aperte ENTER caso não queira alterar algum dos campos.")
    new_code = input("Digite o novo código: ")
    new_name = input("Digite o novo nome: ")
    new_price = input("Digite o novo preço: ")

    if (len(new_code) == 0):
        new_code = rcode
    if (len(new_name) == 0):
        new_name = rname
    if (len(new_price) == 0):
        new_price = str(rprice)

    vsql = "UPDATE '"+table_name+"' SET CODE = '"+new_code+"', NAME = '" + \
        new_name+"', PRICE = '"+new_price+"' WHERE CODE="+up_code

    query(vcon, vsql)
    vcon.close()


def menu_view(table_name):
    os.system("cls")
    print("VISUALIZAR REGISTROS\n")
    vsql = "SELECT * FROM '"+table_name+"' "
    vcon = database_connection()
    check = just_check(vcon, vsql)

    limit_size = 10
    count = 0
    print('CÓDIGO'+' '*5 + 'NOME' + ' '*26 + 'PREÇO(R$)' + ' '*4 + '\n')
    for column in check:
        print(
            f"{column[0]:<10} {column[1]:<30} {column[2]:<4}")

        count += 1
        if (count >= limit_size):
            count = 0
            os.system("pause")
            os.system("cls")

    print("\nFim da lista")
    os.system("pause")

    vcon.close()


def menu_check(table_name):
    os.system("cls")
    print("BUSCAR REGISTROS POR NOME\n")

    s_name = ''
    while len(s_name) == 0:
        s_name = input("Digite o nome: ")

    vsql = "SELECT * FROM '"+table_name+"' WHERE NAME LIKE '%"+s_name+"%'"
    vcon = database_connection()
    check = just_check(vcon, vsql)

    limit_size = 10
    count = 0
    print('\nCÓDIGO'+' '*5 + 'NOME' + ' '*26 + 'PREÇO(R$)' + ' '*4 + '\n')
    for column in check:
        print(
            f"{column[0]:<10} {column[1]:<30} {column[2]:<4}")

        count += 1
        if (count >= limit_size):
            count = 0
            os.system("pause")
            os.system("cls")

    print("\nFim da lista")
    os.system("pause")

    vcon.close()


def cheaper_calculations(t_name):
    vcon = database_connection()
    check = just_check(vcon, "SELECT * FROM '"+t_name+"'")

    cheap = {
        'NAME': '',
        'CODE': '',
        'PRICE': 9999
    }

    for iprice in check:

        a = float(iprice[2])

        if a < cheap['PRICE']:
            cheap['PRICE'] = a
            cheap['NAME'] = iprice[1]
            cheap['CODE'] = iprice[0]

    vcon.close()

    return cheap


def expensive_calculations(t_name):
    vcon = database_connection()
    check = just_check(vcon, "SELECT * FROM  '"+t_name+"'")

    expensive = {
        'NAME': '',
        'CODE': '',
        'PRICE': 0
    }

    for iprice in check:

        a = float(iprice[2])

        if a > expensive['PRICE']:
            expensive['PRICE'] = a
            expensive['NAME'] = iprice[1]
            expensive['CODE'] = iprice[0]

    vcon.close()

    return expensive


option = ''
while option != '8':
    main_options()
    option = input("Digite o número da operação que deseja realizar: ")

    if option == '1' or option == '2' or option == '3' or option == '4' or option == '5':
        choice_table = None

        while choice_table is None:
            inside_options()
            i_option = input(
                "Digite o número do banco de dados que deseja acessar: ")
            choice_table = choose_table(i_option)

        if choice_table != 0:

            if option == '1':
                menu_insert(choice_table)

            elif option == '2':
                menu_delete(choice_table)

            elif option == '3':
                menu_update(choice_table)

            elif option == '4':
                menu_view(choice_table)

            elif option == '5':
                menu_check(choice_table)

        else:
            pass

    elif option == '6':
        os.system("cls")

        menu_cheap = []

        starters_cheap = cheaper_calculations('tb_starters')
        main_cheap = cheaper_calculations('tb_main')
        desserts_cheap = cheaper_calculations('tb_desserts')
        drinks_cheap = cheaper_calculations('tb_drinks')

        total_cheap = starters_cheap['PRICE'] + main_cheap['PRICE'] + \
            desserts_cheap['PRICE'] + drinks_cheap['PRICE']

        menu_cheap.extend((starters_cheap, main_cheap,
                           desserts_cheap, drinks_cheap))

        menu_names = ['ENTRADA', 'PRATO PRINCIPAL', 'SOBREMESA', 'BEBIDA']

        print("\n**** CARDÁPIO MAIS BARATO ****\n")
        for i in range(len(menu_names)):
            print(f'**** {menu_names[i]} ****')
            print(
                f" NOME: {menu_cheap[i]['NAME']}\n CÓDIGO: {menu_cheap[i]['CODE']}\n PREÇO: R$ {menu_cheap[i]['PRICE']}\n")

        print(f'TOTAL: R$ {total_cheap:.2f}')
        os.system("pause")
        os.system("cls")

    elif option == '7':
        os.system("cls")

        menu_expensive = []

        starters_expensive = expensive_calculations('tb_starters')
        main_expensive = expensive_calculations('tb_main')
        desserts_expensive = expensive_calculations('tb_desserts')
        drinks_expensive = expensive_calculations('tb_drinks')

        total_expensive = starters_expensive['PRICE'] + main_expensive['PRICE'] + \
            desserts_expensive['PRICE'] + drinks_expensive['PRICE']

        menu_expensive.extend(
            (starters_expensive, main_expensive,
             desserts_expensive, drinks_expensive)
        )

        menu_names = ['ENTRADA', 'PRATO PRINCIPAL', 'SOBREMESA', 'BEBIDA']

        print("\n**** CARDÁPIO MAIS CARO ****\n")
        for i in range(len(menu_names)):
            print(f'**** {menu_names[i]} ****')
            print(
                f" NOME: {menu_expensive[i]['NAME']}\n CÓDIGO: {menu_expensive[i]['CODE']}\n PREÇO: R$ {menu_expensive[i]['PRICE']}\n")

        print(f'TOTAL: R$ {total_expensive:.2f}')
        os.system("pause")
        os.system("cls")

    elif option == '8':
        os.system("cls")
        print("Programa Finalizado")

    else:
        os.system("cls")
        print("Opção inválida")
        os.system("pause")


os.system("pause")
