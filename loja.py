import sys

cadastrados=[]

produtos = ['Monitor','Teclado','Mouse','Gabinete','Placa Mae','Processador','Memória','HD1TB','HD500GB','SSD500GB','Alto Falantes','Placa De Video','Ice Cooler']
valor = [150,30,20,180,300,250,260,450,400,480,100,600,1000]
quantidade=[]
carrinho=[]
custo=[]
total=[]

print('='*20,'LOJA DE PRODUTOS ELETRONICOS','='*20)
print('\n')
print('PRODUTOS DA LOJA:')
print('-'*30)
for i in range(len(produtos)):
    print(produtos[i],'R$',valor[i])
    print('-'*30,)
print('\n')

while True:
    compra=str(input('Quais produtos vc gostaria de comprar?:')).upper()
    carrinho.append(compra)
    print('-'*30)
    quant= int(input('Qual a quantidade desse produto?:'))
    quantidade.append(quant)
    print('-'*30)
    preco=int(input('Qual o valor do produto?:'))
    custo.append(preco)
    pagar=preco * quant
    total.append(pagar)
    pagar_total=sum(total)
    print('-'*30)
    cont=str(input('Gostaria de continuar suas compras?: [S/N]')).upper()
    print('-'*30)
    if cont == 'N':
        break

print('\n')

print('='*20,'ESSE É SEU CARRINHO','='*20)

for c in range(len(carrinho)):
    print(quantidade[c],'X',carrinho[c],'|','VALOR UNITARIO R$',custo[c],'|','VALOR TOTAL DO PRODUTO R$',total[c])
    print('-'*50)

print('\n')

cadastro1=str(input('Possui cadastro conosco?:  [S/N] '))

if cadastro1 == 'n':
    print('-'*50)
    cadastro2=str(input('Gostaria de se cadastrar?: [S/N]'))
    if cadastro2 == 's':
        cadastro()
    print('\n')
    print('-'*50,'CADASTRO FINALIZADO','-'*50)
    

verificacao=int(input('INSIRA O SEU CPF PARA RECEBER SEU DESCONTO DE R$ 40,00: '))

print('-'*50)

if verificacao in cadastrados:
    pagar_total2 = pagar_total - 40
    print('='*20,f'VALOR ANTERIOR DA COMPRA: R${pagar_total}',f'VALOR TOTAL DA COMPRA COM DESCONTO: R${pagar_total2}','='*20)
    sys.exit()

elif verificacao not in cadastrados:
    print('='*20,'VOCÊ NÃO POSSUI CADASTRO CONOSCO','='*20)
    print('-'*50)
    cadastro3=str(input('Gostaria de se cadastrar?: [S/N]'))
if cadastro3 == 's':
    cadastro()
    print('\n')
    print('-'*50,'CADASTRO FINALIZADO','-'*50)
    
    verificacao=int(input('INSIRA O SEU CPF PARA RECEBER SEU DESCONTO DE R$ 40,00: '))

print('-'*50)

if verificacao in cadastrados:
    pagar_total2 = pagar_total - 40
    print('='*20,f'VALOR ANTERIOR DA COMPRA: R${pagar_total}',f'VALOR TOTAL DA COMPRA COM DESCONTO: R${pagar_total2}','='*20)
    sys.exit()

else:
    print('='*20,f'VALOR TOTAL DA COMPRA: R${pagar_total}','='*20)

def cadastro():
    
    print('='*50,'CADASTRO','='*50)
    
    print('-'*50)
    
    nome=str(input('NOME COMPLETO: '))
    
    print('-'*50)
    
    nascimento=input('DATA DE NASCIMENTO: ')
    
    print('-'*50)
    
    cpf=int(input('CPF: '))
    cadastrados.append(cpf)
    
    print('-'*50)
    
    rg=int(input('RG: '))
    
    print('-'*50)
    
    endereco=input('ENDEREÇO: ')
    
    print('-'*50)