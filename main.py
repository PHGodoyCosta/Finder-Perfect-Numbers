def find_divisores(num):
    divisores = [1]
    for i in range(1, num):
        if num % i == 0 and num / i != num:
            divisores.append(int(num/i))
    return divisores
            
def soma_dos_divisores(divisores):
    result = 0
    for d in divisores:
        result += d
    
    return result

def find_perfect_numbers(limit=10000):
    perfect_numbers = []
    for i in range(2, limit):
        divisores = find_divisores(i)
        soma = soma_dos_divisores(divisores)
        if soma == i:
            print(f"PERFEITO! --> {int(i)}")
            perfect_numbers.append(int(i))
    print("\n")
    print("=--"*20)
    print("Busca concluída!")
    print(perfect_numbers)
    
    return perfect_numbers
    
    
find_perfect_numbers()
