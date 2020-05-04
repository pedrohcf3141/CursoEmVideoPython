# DESAFIO 44

valor = int(input('valor '))
print('formas de pagamento dinheiro / cheque / cartão ')
pagamento = input('forma de pagamento ').strip().lower()

if pagamento in 'dinheiro cheque':

    print('o valor a ser pago será de {:.2f} ja com desconto'.format(valor - (valor* 0.1)))

elif pagamento == 'cartão' or 'cartao':
    vezes = int(input('quantas vezes, digite 0 para pagameto a vista '))
    if vezes == 0:
        print('o valor a ser pago será de {:.2f} ja com desconto'.format(valor - (valor * 0.05)))
    elif vezes <= 2:
        print('o valor a ser pago será de {:.2f} em parcelas de {:.2f}'.format(valor, valor/vezes))
    else:
        valor *= 0.2
        print('o valor a ser pago será de {:.2f} em parcelas de {:.2f}'.format(valor, valor / vezes))

