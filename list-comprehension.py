#
# List Comprehension em python
#
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [var for var in lista1]
lista3 = [var * 2 for var in lista1]
lista4 = [(var, var2) for var in lista1 for var2 in range(10)]
# ----------------------------------------------------
lista5 = ['Gustavo', 'Pedro', 'Luiz', 'Osvaldo', 'Maria']
lista6 = [var.replace("a", "@") for var in lista5]
lista7 = [var.replace("a", "@").upper() for var in lista5]
# ----------------------------------------------------
tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
)
lista8 = [(x, y) for x, y in tupla]
lista9 = [(y, x) for x, y in tupla]  # Inverti o valor
lista10 = dict(lista8)
# ----------------------------------------------------
lista11 = list(range(100))
lista12 = [var for var in lista11 if var % 9 == 0]
lista13 = [var for var in lista11 if var % 3 == 0 if var % 5 == 0]
lista14 = [var if var % 3 == 0 else 'Negativo' for var in lista11]
lista15 = [f"[->{var}/9<-]" if var % 9 == 0 else f"{var}" for var in lista11]
lista16 = [f"[->{var}/9<-]" if var % 3 == 0 and var % 5 == 0 else f"{var}" for var in lista11]
lista17 = [f"[{var}/3 or /9]" if var % 3 == 0 or var % 9 == 0 else f"{var}" for var in lista11]
# ----------------------------------------------------
print(f'\n lista2 = [var for var in lista1]: {lista2}')
# ----------------------------------------------------
print(f'\n lista3 = [var * 2 for var in lista1]: {lista3},\n List Comprehension em python')
# ----------------------------------------------------
print(f'\n lista4 = [(v, v2) for v in lista1 for v2 in range(10)]: \n {lista4}')
# ----------------------------------------------------
print(f'\n lista6 = [var.replace("a", "@") for var in lista5]:\n {lista6}')
# ----------------------------------------------------
print(f'\n lista6 = [var.replace("a", "@") for var in lista5]:\n {lista7}')
# ----------------------------------------------------
print(f'\n lista8 = [(x, y) for x, y in tupla]:\n {lista8}')
print(f'\n lista8 = [(y, x) for x, y in tupla]:\n {lista9}\n Inverti o valor!!!')
print(f'\n lista8 = [(x, y) for x, y in tupla]:\n {lista10}\n Virou dicionário!!!')
print(f'\n {lista10["chave2"]}')
# ----------------------------------------------------
print(f'\n lista11 = list(range(100)): {lista11}')
print(f'\n lista12 = [var for var in lista11 if var % 9 == 0]:\n {lista12}')
print(f'\n lista12 = [var for var in lista11 if var % 3 == 0 if var % 5 == 0]:\n {lista13}')
print(f'\n lista14 = [var if var % 3 == 0 else "Negativo" for var in lista11]:\n {lista14}')
print(f'\n lista15 = [" var /9" if var % 9 == 0 else "Negativo" for var in lista11]:\n {lista15}')
print(f'\n lista16 = [f"[-> var /9<-]" if var % 3 == 0 and var % 5 == 0 else f" var " for var in lista11]:\n {lista16}')
print(
    f'\n lista17 = [f"[ var /3 or /9]" if var % 3 == 0 or var % 9 == 0 else f" var " for var in lista11]:\n {lista17}')
# ----------------------------------------------------
