class Conta:
    def __init__(self, titular, numero_conta, quantidade):
        self.titular = titular
        self.numero_conta = numero_conta
        self.quantidade = quantidade

    def __str__(self):
        return f"Titular: {self.titular}, Número da Conta: {self.numero_conta}, Quantidade: {self.quantidade}"

    def comparar_quantidade(self, outra_conta):
        if self.quantidade > outra_conta.quantidade:
            return f"A conta de {self.titular} tem mais dinheiro que a conta de {outra_conta.titular}."
        elif self.quantidade < outra_conta.quantidade:
            return f"A conta de {outra_conta.titular} tem mais dinheiro que a conta de {self.titular}."
        else:
            return f"A conta de {self.titular} e a conta de {outra_conta.titular} têm a mesma quantidade de dinheiro."

# Criando duas instâncias da classe Conta
conta1 = Conta("Alice", "12345", 5000)
conta2 = Conta("Bob", "67890", 7000)

# Comparando as quantidades das duas contas
resultado = conta1.comparar_quantidade(conta2)
print(resultado)