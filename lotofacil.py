import itertools
from itertools import groupby, count


def cria_list_seguencia(num):
    """
    Cria uma lista sequencial iniciando no número 1 e terminando no número passado pela variável 'num'
    :param num: int
    :return: list
    Exemplo: num = 10 -> return {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    """
    list_numeros = [itens_numero+1 for itens_numero in range(num)]
    return list_numeros


def cria_dict_seguencia(num):
    """
    Cria um dicionário sequencial iniciando no número 1 e terminando no número passado pela variável 'num' as chaves
    são o número e o valor inicial é 0
    :param num: int
    :return: dictionary
    Exemplo: num = 10 -> return {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    """
    dict_numeros = {chave+1: 0 for chave in range(num)}
    return dict_numeros


def grupo_seguencia(lista_numerica):
    """
    Retorna uma string separada por virgula, a quantidade de números de cada qrupo sequêncial. Ex.1,2,3 - 1º grupo,
    4,5,6 - 2º grupo - 8,9,10 - 3º grupo.
    :param lista_numerica: list
    :return: strng
    Exemplo:{1, 2, 3, 5, 6, 9, 10) -> 3,2,2
    """
    return ' '.join(as_range(g) for _, g in groupby(lista_numerica, key=lambda n, c=count(): n-next(c)))


def as_range(iterable):
    """ Utilizada pela função grupo_sequencia retorna a quantidade de números do grupo atual"""
    lista = list(iterable)
    return '{}'.format(len(lista))


def list_string_to_list_int(list):
    for itens in range(0, len(list)):
        list[itens] = int(list[itens])
    return list


def carregra_lista_resultados():
    lotofacil_resultados = open('lotofacil-resultados.txt', 'r')
    carrega_lista_resultado = []
    for line in lotofacil_resultados:
        line = line.rstrip('\n')  # remove a quebra de linha
        carrega_lista_resultado.append(line.replace(' ', '').split('-'))
    lotofacil_resultados.close()
    return carrega_lista_resultado


if __name__ == '__main__':
    numeros_lotofacil = cria_list_seguencia(25)
    combinacao = set(itertools.combinations(numeros_lotofacil, 15))
    # lista_combinacao = list(combinacao)
    lista_remove = []
    # for index, value in enumerate(combinacao):
    #     lista = value
    #     if int(max(grupo_seguencia(lista).split())) > 7:
    #         lista_remove.append(index)
    #     print(index)
    # lista_remove.sort(reverse=True)
    # for x in lista_remove:
    #     print(x)
    #     del combinacao[x]
    print(len(combinacao))
    lista_resultado = carregra_lista_resultados()
    lista_numeros_sorteados = []
    for itens in lista_resultado:
        itens[1] = list(itens[1].split(','))
        lista_numeros_sorteados.append(itens[1])
    for itens in lista_numeros_sorteados:
        list_string_to_list_int(itens)
    max_sequencia = cria_dict_seguencia(15)
    for valor in max_sequencia:
        vezes = 0
        for itens in lista_numeros_sorteados:
            lista = itens
            resultado = grupo_seguencia(lista)
            resultado = resultado.split(' ')
            resultado = list_string_to_list_int(resultado)
            if max(resultado) == valor:
                vezes += 1
        max_sequencia[valor] = vezes
    print(max_sequencia)
