# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista de dicionários
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    dict_reader = csv.DictReader(file_read)
    data_list = list(dict_reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo as chaves do dicionário
print("Cabeçalho dos dados: ")
print(','.join('{}'.format(key) for key in data_list[0].keys()))
# É o cabeçalho dos dados, para que possamos identificar as colunas

# Imprimindo a primeira linha de data_list, ela contem alguns dados
print("Linha 1: ")
print(','.join('{}'.format(value) for value in data_list[0].values()))

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
#for index in range(20):
for index in range(3):
    print(','.join('{}'.format(value) for value in data_list[index].values()))

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
#for index in range(20):
for index in range(3):
    print(data_list[index]["Gender"])

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for amostra in data:
        amostra_list = list(amostra.values())
        column_list.append(amostra_list[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
#assert len(column_to_list(data_list, -2)) == 999, "TAREFA 3: Tamanho incorreto retornado."
#assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = sum(1 for data in column_to_list(data_list, -2) if data == "Male")
female = sum(1 for data in column_to_list(data_list, -2) if data == "Female")


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
#assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
#assert male == 541 and female == 237, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    male = sum(1 for data in data_list if data["Gender"] == "Male")
    female = sum(1 for data in data_list if data["Gender"] == "Female")
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
#assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
#assert count_gender(data_list)[0] == 541 and count_gender(data_list)[1] == 237, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    if count_gender(data_list)[0] > count_gender(data_list)[1]:
        answer = "Male"
    elif count_gender(data_list)[0] < count_gender(data_list)[1]:
        answer = "Female"
    else:
        answer = "Equal"
        
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
def count_user_types(data_list,user_types):
    count_list = []
    user_types_list = list(user_types)
    
    for type in user_types_list:
        count_type = sum(1 for data in data_list if data["User Type"] == type)
        count_list.append(count_type)

    return count_list

user_types_list = column_to_list(data_list,-3)
user_types = set(user_types_list)
quantity = count_user_types(data_list,user_types)
y_pos = list(range(len(user_types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo')
plt.xticks(y_pos, user_types)
plt.title('Quantidade por Tipo')
plt.show(block=True)

print("\nTAREFA 7: Verifique o gráfico!")

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "É falsa porque existem amostras que possuem a coluna Gender em branco."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = list(map(int,trip_duration_list))

min_trip = trip_duration_list[0]
max_trip = trip_duration_list[0]
mean_trip = 0.
median_trip = 0.

for trip_duration in trip_duration_list:
    if  trip_duration < min_trip:
        min_trip = trip_duration
    if trip_duration > max_trip:
        max_trip = trip_duration
    
    mean_trip += trip_duration

mean_trip = (mean_trip/len(trip_duration_list))

trip_duration_list = sorted(trip_duration_list)
length = len(trip_duration_list)
median_index = int(length/2)
if (length%2 == 0):
    median_trip = (trip_duration_list[median_index] + trip_duration_list[median_index-1])/2
else:
    median_trip = trip_duration_list[median_index]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
#assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
#assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
#assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
#assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations_list = column_to_list(data_list,3)
start_stations = set(start_stations_list)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
#assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? yes")
answer = "yes"

def count_items(column_list):
    item_types = list(set(column_list))
    count_items = []

    for type in item_types:
        count_type = sum(1 for column in column_list if column == type)
        count_items.append(count_type)

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    print(len(types))
    print(sum(counts))
    #assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
    