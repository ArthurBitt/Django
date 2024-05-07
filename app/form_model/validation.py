def origin_same_as_destiny(origem, destino, lista_de_erros):
    '''Verifica se origem e destino são iguais'''
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser o mesmo'


def is_a_number(valor_campo,nome_campo, lista_de_erros):
    '''verica se algum dígito é numérico'''
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Origem e destino não podem ser números'

def date_validation(data_ida,data_volta,lista_de_erros):
    if data_ida > data_volta:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser depois da data de volta'