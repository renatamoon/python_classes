#desafio
#some o valor preço

carrinho = []
carrinho.append(('produto1', 30))
carrinho.append(('produto2', 20))
carrinho.append(('produto2', 50))

#SEM LIST COMPREHENSION

# total = []
# for produto in carrinho:
#     total.append(produto[1])
# print(sum(total))

#COM LIST COMPREHENSION
# total = sum([float(y) for x, y in carrinho]) #sai o total de valores
# print(carrinho)
# print(total)

media = 0
compras = []
compras.append(('fruta 1', 40))
compras.append(('fruta 2', 60))
compras.append(('fruta 3', 80))

total = sum([float(y) for x, y in compras])
print(total)


