#Verificar se um CPF é válido 
import re # regular expression
#PRIMEIRO DIGITO
#Multiplicando os 9 primeiros digitos do CPF por uma contagem regressiva começando por 10
def multiplying_cpf_numbers_n1(new_number_list,descending_number,cpf):
    for number in cpf[:9]:
        int_number = int(number)
        new_number = int_number * descending_number
        descending_number = descending_number - 1
        new_number_list.append(new_number)
        
def getting_the_final_result_n1(new_number_list):
    #Somando os resultados da multiplicação
    sum_numbers = 0
    for number in new_number_list:
        sum_numbers = sum_numbers + number
    
    #Multiplicando o resultado da soma por 10
    multiplicated_sum = sum_numbers * 10
    
    #Obtendo o resto da divisão da conta anterior por 11
    rest_division_n1 = multiplicated_sum % 11
    
    #Checando resultado, se o resultado for > 9, o resultado vira 0, se não segue sendo o número que é
    if rest_division_n1 > 9:
        rest_division_n1 == 0
    new_number_list.clear()
    return rest_division_n1

#SEGUNDO DIGITO
#Multiplicando os 9 primeiros digitos do CPF(MAIS O NOVO DIGITO), por uma contagem regressiva começando por 11
def multiplying_cpf_numbers_n2(new_number_list,descending_number,cpf):
    descending_number = descending_number + 1
    for number in cpf[:10]:
        int_number = int(number)
        new_number = int_number * descending_number
        descending_number = descending_number - 1
        new_number_list.append(new_number)
        
def getting_the_final_result_n2(new_number_list):
    #Somando os resultados da multiplicação
    sum_numbers = 0
    for number in new_number_list:
        sum_numbers = sum_numbers + number
    
    #Multiplicando o resultado da soma por 10
    multiplicated_sum = sum_numbers * 10
    
    #Obtendo o resto da divisão da conta anterior por 11
    rest_division_n2 = multiplicated_sum % 11
    
    #Checando resultado, se o resultado for > 9, o resultado vira 0, se não segue sendo o número que é
    if rest_division_n2 > 9:
        rest_division_n2 == 0
    return rest_division_n2

def cpf_check(cpf,rest_division_n1,rest_division_n2):
    #Checando se o cpf é valido
    cpf_calculated = cpf[:9] + str(rest_division_n1) + str(rest_division_n2)
    print(rest_division_n1)
    print(rest_division_n2)
    print(cpf)
    print(cpf_calculated)
    if cpf == cpf_calculated:
        print("CPF VÁLIDO")
    else:
        print("CPF INVÁLIDO")

def main():
    #cpf 746.824.890-70
    cpf = input("Digite seu cpf: ")
    cpf = re.sub(r'[^0-9]',"",cpf)
    descending_number = 10
    new_number_list = []
    #NUMBER 1
    multiplying_cpf_numbers_n1(new_number_list,descending_number,cpf)
    rest_division_n1 = getting_the_final_result_n1(new_number_list)
    #NUMBER 2
    multiplying_cpf_numbers_n2(new_number_list,descending_number,cpf)
    rest_division_n2 = getting_the_final_result_n2(new_number_list)
    #CPF CHECK
    cpf_check(cpf,rest_division_n1,rest_division_n2)
   
    
main()
