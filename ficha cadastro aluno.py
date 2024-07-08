class Aluno:
    def __init__(self, nome="Indefinido", idade=0, curso="Indefinido", numero_matricula="0000"):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.numero_matricula = numero_matricula

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}, Número de Matrícula: {self.numero_matricula}"

def main():
    alunos = []

    while True:
        print("\nSistema de Registro de Alunos")
        print("1. Criar uma nova instância de Aluno")
        print("2. Exibir informações de um Aluno")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            curso = input("Digite o curso do aluno: ")
            numero_matricula = input("Digite o número de matrícula do aluno: ")
            aluno = Aluno(nome, idade, curso, numero_matricula)
            alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")

        elif escolha == "2":
            if not alunos:
                print("Nenhum aluno cadastrado.")
            else:
                for i, aluno in enumerate(alunos):
                    print(f"{i + 1}. {aluno.nome}")
                indice = int(input("Selecione o número do aluno para exibir informações: ")) - 1
                if 0 <= indice < len(alunos):
                    print(alunos[indice].exibir_informacoes())
                else:
                    print("Índice inválido.")

        elif escolha == "3":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()