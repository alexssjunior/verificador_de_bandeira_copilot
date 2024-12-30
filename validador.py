def validar_bandeira_cartao(numero_cartao):
    numero_cartao = str(numero_cartao)
    
    if numero_cartao.startswith('4'):
        return "Visa"
    elif numero_cartao.startswith(('51', '52', '53', '54', '55')):
        return "MasterCard"
    elif numero_cartao.startswith('34') or numero_cartao.startswith('37'):
        return "American Express"
    elif numero_cartao.startswith('6'):
        return "Discover"
    else:
        return "Bandeira desconhecida"

# Exemplo de uso
numero_cartao = input("Digite o número do cartão de crédito: ")
bandeira = validar_bandeira_cartao(numero_cartao)
print(f"A bandeira do cartão é: {bandeira}")