"""
Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf e idade
Cada conta possui um cliente, saldo, limite. 
    Métodos sacar, depositar e consultar saldo.
"""
from conta import Conta


pessoa1 = Conta('Marcos', 10430760426, 1200, 100)
#pessoa1.setNome('Allysson')
#pessoa1.setCpf(1234)
#pessoa1.setSaldo(990)
#pessoa1.setLimite(1000)

#print(pessoa1.getNome())
#print(pessoa1.getCpf())
#print(pessoa1.getSaldo())
#print(pessoa1.getLimite())

pessoa1.sacar(1200)
print(pessoa1.getSaldo())
pessoa1.depositar(-1)

print(pessoa1)
