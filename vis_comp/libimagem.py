# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
    Nome: Gabriel Ribeiro Freitas
    NUSP: 10830482

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

"""

from copy import deepcopy

import ep01


# ------------------------------------------------------------------
def main():
    """
        Modifique essa função, escrevendo os seus testes.
    """
    # coloque aqui os seus testes

    # f = open("img_example.txt", "r")
    # M = eval(f.read())

    M = [[9, 4, 5, 0, 8],
         [10, 3, 2, 1, 7],
         [9, 1, 6, 3, 15],
         [0, 3, 8, 10, 1],
         [1, 16, 9, 12, 7]]

    print(ep01.to_string(M))
    M = segmentacao_SME(M)
    print(ep01.to_string(M))


# ------------------------------------------------------------------
#


def _get_neighborhood(m, i, j, viz):
    n = int(viz / 2)
    return [
        row[max(j - n, 0):min(j + n + 1, len(row))] for row in m[max(i - n, 0):min(i + n + 1, len(m))]
    ]


def _flatten_list(list_):
    return [item for sublist in list_ for item in sublist]


def _get_min(_list):
    flattened_list = _flatten_list(_list)
    return min(flattened_list)


def _get_max(_list):
    flattened_list = _flatten_list(_list)
    return min(flattened_list)


def _apply_filter(img, func, viz):
    aux = ep01.crie(len(img), len(img[0]))

    for i in range(len(img)):
        row = img[i]
        for j in range(len(row)):
            neighborhood = _get_neighborhood(img, i, j, viz)
            aux[i][j] = func(neighborhood)

    for i in range(len(img)):
        img[i] = aux[i]


def erosao(img, viz=3):
    """ (matriz, int) -> None

    RECEBE uma matriz `img` representando uma imagem em níveis de cinza e
    um inteiro `viz`.

    MODIFICA `img` de tal forma que, ao final, cada pixel
    [lin][col] seja o valor mínimo da vizinhança de tamanho `viz`
    centrada no pixel [lin][col] da imagem original.

    Pré-condição: a função supõe que `viz` é um número ímpar
    positivo.
    """
    _apply_filter(img, _get_min, viz)


# ------------------------------------------------------------------
#
def segmentacao_SME(img, viz=3):
    """ (matriz, int) -> matriz

    RECEBE uma matriz `img`.
    APLICA o filtro de erosão com vizinhança viz.
    RETORNA a imagem resultado da subtração entre `img` e sua erosão.
    Veja exemplos no enunciado.
    """
    E = deepcopy(img)
    erosao(E, viz)
    return ep01.subtraia(img, E)


# ------------------------------------------------------------------
#
def dilatacao(img, viz=3):
    """ (list, int) -> None
    recebe uma imagem img (lista de listas) em níveis de cinza e
    um inteiro viz.

    A função modifica img tal que, ao final, cada pixel
    img[lin][col] deve ser substituido pelo valor máximo da vizinhança de
    tamanho viz x viz centrado no pixel (lin,col) da imagem original.
    Observe que essa região é menor quando o pixel (lin,col)
    está em um canto ou perto de uma borda.

    Você pode assumir que viz será sempre um número ímpar, que define
    um quadrado centrado em um ponto (lin,col) de lado tam.
    """
    _apply_filter(img, _get_max, viz)


# ------------------------------------------------------------------
#
def segmentacao_SDM(img, viz=3):
    """ (list, int) -> list
    RECEBE uma imagem img.
    APLICA o filtro de dilatação com vizinhança viz.
    RETORNA a imagem resultado da subtração entre a dilatação e img.
    Veja exemplos no enunciado.
    """
    D = deepcopy(img)
    dilatacao(D, viz)
    return ep01.subtraia(img, D)


#######################################################
###                 FIM                             ###
#######################################################
#
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == "__main__":
    main()
