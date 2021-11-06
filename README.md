 Atividade Desenvolvida na Disciplina de Algoritmos e Programação I

Descrição da Tarefa:

Você foi contratado para desenvolver um programa de computador para ajudar o governo a
informar a população a quantidade de casos de covid-19. O levantamento de necessidades
já foi feito e está resumido na descrição a baixo.

Menu
0- Finalizar o Programa
1- Cadastrar Estados
2- Cadastrar Cidades
3- Relatório de Estados
4- Relatório de Cidades
5- Atualizar números de casos
Escolha:

Para armazenar os dados, você poderá utilizar a lista (lst_estado) para armazenar os objetos
instanciados pelas classes.

Os atributos das classes podem ser privadas.(duplo underline no início da variável)
Você está livre para desenvolver os métodos necessários para que o código funcione
como você espera.

Descrição dos atributos da classe Estado:
- nome_estado: deve conter uma string, e significa o nome do estado
- sigla: deve conter uma string.
- qt_casos_estado: deve ser um inteiro que significa a quantidade acumulada das
cidades(qt_casos_cidade). Deve sempre ser instanciado em 0(zero). Sempre que a
quantidade na cidade for atualizada(qt_casos_cidade), você deverá também atualizar no
estado (qt_casos_estado).

Descrição dos atributos da classe Cidade:
- nome_cidade: deve conter uma string, e significa o nome da cidade.
- qt_casos_cidade: deve ser um inteiro, e significa a quantidade de casos desta cidade. Deve
ser instanciado sempre em 0(zero) e incrementado quando for atualizado.

Descrição do menu de opções:

Na opção 1, você deverá instanciar um objeto do tipo Estado com nome do estado, sua sigla
e a quantidade de doenças, que inicialmente será zero. Armazene em lst_estado.
Critérios:
- Não pode ter 2 estados com o mesmo nome ou mesma sigla.

Na opção 2, você deverá instanciar um objeto do tipo Cidade com nome da cidade, sua
quantidade de casos (iniciar em zero).
Esta instância de cidade deverá ser armazenada no atributo lst_cidades da classe
Estado.

Na opção 3, você deverá gerar um relatório com o nome do estado e a quantidade de casos
registrados. Segue um exemplo deste relatório.
=-=-=-=-=- Relatório do Estados:
--> RIO GRANDE DO SUL............. - total de Casos: 52
--> SANTA CATARINA................ - total de Casos: 7
--> PARANA........................ - total de Casos: 0
--> SÃO PAULO..................... - total de Casos: 34
--> RIO DE JANEIRO................ - total de Casos: 31
 [Enter] Retorna ao menu.

Na opção 4, você deverá gerar um relatório com o nome da cidade, e a quantidade de casos
registrados. Segue um exemplo deste relatório.
=-=-=-=-=- Relatório do Cidades:
--> SANTA MARIA......... - Casos Registrados: 11
--> PORTO ALEGRE........ - Casos Registrados: 33
--> CANOAS.............. - Casos Registrados: 8
--> FLORIANÓPOLIS....... - Casos Registrados: 7
--> RIO DE JANEIRO...... - Casos Registrados: 23
--> NITEROI............. - Casos Registrados: 8
--> SAO PAULO........... - Casos Registrados: 34
 [Enter] Retorna ao menu.
 
Na opção 5, você deverá atualizar os casos na cidade, escolhendo uma das cidades e
digitando a nova quantidade de casos detectada. Esta quantidade deverá sempre ser
somada ao atributo qt_casos_cidade da classe Cidade, e atualizada no atributo
qt_casos_estado da classe Estado.
Critérios:
- A quantidade não pode ser negativa.

