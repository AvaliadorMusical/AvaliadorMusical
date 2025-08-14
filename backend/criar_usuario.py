import re
from datetime import datetime

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

def validar_senha(senha):
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."
    if not re.search(r'[A-Z]', senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula."
    if not re.search(r'[0-9]', senha):
        return False, "A senha deve conter pelo menos um número."
    if not re.search(r'[\W_]', senha):
        return False, "A senha deve conter pelo menos um símbolo (ex: @, #, !, ?)."
    return True, "Senha válida."

def calcular_idade(data_nascimento):
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    return idade

print("=== CRIAÇÃO DE CONTA ===")

# Nome de usuário
usuario = input("Digite seu nome de usuário: ")

# E-mail
while True:
    email = input("Digite seu e-mail: ")
    if validar_email(email):
        break
    else:
        print("❌ E-mail inválido. Tente novamente.")

# Senha
while True:
    senha = input("Crie uma senha: ")
    valido, mensagem = validar_senha(senha)
    if valido:
        break
    else:
        print(f"❌ {mensagem}")

# Data de nascimento
while True:
    try:
        data_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
        data_nasc = datetime.strptime(data_str, "%d/%m/%Y")
        idade = calcular_idade(data_nasc)
        if idade < 13:
            print("❌ Você precisa ter pelo menos 13 anos para criar uma conta.")
        elif idade > 100:
            print("❌ Você precisa estar vivo para criar uma conta.")
        else:
            # Mostrar dados finais
            print("\n✅ Conta criada com sucesso!")
            print(f"Usuário: {usuario}")
            print(f"E-mail: {email}")
            print(f"Data de nascimento: {data_nasc.strftime('%d/%m/%Y')}")
            print(f"Idade: {idade} anos")
            break
    except ValueError:
        print("❌ Formato de data inválido. Use dd/mm/aaaa.")


