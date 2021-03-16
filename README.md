# gerador-de-cardapios
Ideia principal: A partir de sucessivos cadastros em um banco de dados, o programa gera o cardápio mais barato e o mais caro.

**Descrição:**

A essência desse programa veio do primeiro trabalho que fiz, quando estava no curso de Ciência da Computação (em 2010/2011).
O programa original consistia em registrar itens nas categorias:
 
 - 'ENTRADA'
 - 'PRATO PRINCIPAL'
 - 'SOBREMESA'
 - 'BEBIDAS'

 Cada item registrado contava com três informações:

 - NOME
 - CÓDIGO
 - PREÇO

 Desse modo, os itens iam sendo registrados, em um programa estruturado e simples, e ao final ocorria a impressão do cardápio mais barato e do cardápio mais caro.

 A ideia principal foi mantida aqui, mas como duas opções. Decidi trabalhar utilizando a linguagem Python, com funções e banco de dados(SQLITE3), e criei um 'menu' com as seguintes opções:

1. Inserir Novo Registro
2. Deletar Registro
3. Atualizar Registro
4. Visualizar Registros
5. Buscar Registros por Nome
6. Mostrar Cardápio Mais Barato
7. Mostrar Cardápio Mais Caro
8. Sair

Assim, os itens podem ser adicionados, atualizados, apagados e consultados, conforme o usuário escolha as opções do menu. Com pelo menos dois itens cadastrados em cada categoria, é possível utilizar as opções 6 e 7 e imprimir o cardápio mais barato e o cardápio mais caro.

*Obs.: Há alguns itens já registrados no banco de dados (menu_database.db), pois assim é possível checar as opções 3,4,5,6 e 7.*
