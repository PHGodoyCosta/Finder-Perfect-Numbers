from itertools import count

class PerfectNumbers:
    def __init__(self):
        self.perfect_numbers = []
    
    def find_divisores(self, num):
        divisores = [1]
        for i in range(1, num):
            if num % i == 0 and num / i != num:
                divisores.append(int(num/i))
        return divisores
                
    def soma_dos_divisores(self, divisores):
        result = 0
        for d in divisores:
            result += d
        
        return result

    def find_perfect_number(self, number):
        divisores = self.find_divisores(number)
        soma = self.soma_dos_divisores(divisores)
        if soma == number:
            print(f"PERFEITO! --> {int(number)}")
            self.perfect_numbers.append(int(number))
            return {"status": True, "number": int(number)}
        return {"status": False, "number": int(number)}

    def find_perfect_numbers(self, limit):
        if limit > 0:
            limiter = range(2, limit)
        else:
            limiter = count(2)
        
        for i in limiter:
            self.find_perfect_number(i)
        print("\n")
        print("=--"*20)
        print("Busca concluída!")
        print(self.perfect_numbers)
        
        return self.perfect_numbers
        
if __name__ == "__main__":
    starter = PerfectNumbers()
    print("Escolha um modo:\n")
    print("0: Testar apenas um número\n1: Testar um range de números\n")
    mode = int(input("> "))
    if mode == 0:
        num = int(input(("\nEscolha um número: ")))
        result = starter.find_perfect_number(num)
        if not result["status"]:
            print(f"Não é um número perfeito :( -> {num}")
    if mode == 1:
        print("[0: Sem limite]")
        limit = str(input("Algum limite para busca? [10000: default] "))
        if limit.isnumeric() and int(limit) > 0:
            print(f"Limite: {int(limit)}\n")
            starter.find_perfect_numbers(limit=int(limit))
        elif limit == "":
            print("Limite: 10000")
            starter.find_perfect_numbers(limit=10000)
        elif int(limit) == 0:
            print("Limite: Infinito")
            starter.find_perfect_numbers(limit=0)
    else:
        print("ERRO! Escolha um modo válido!")