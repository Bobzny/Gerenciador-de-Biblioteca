import os
from database import engine
from models.base import Base
from view.menus import *

if not os.path.exists("instance/biblioteca.db"):
    os.makedirs("instance", exist_ok=True) 
    Base.metadata.create_all(engine)
    print("Tudo na paz meu amigo")

while True:
    opcao = menuPrincipal()
    if opcao == '1':
        print("Livros")
    elif opcao == '2':
        print("Usuários")
    elif opcao == '3':
        print("Empréstimos")
    elif opcao == '4':
        break
    else:
        print("Opção inválida")