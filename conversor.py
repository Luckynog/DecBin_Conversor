print("**********Sistema de conversão de números binários em decimais e vice-versa**********")
resposta = input("Você deseja converter a partir do binário ou do decimal? ").casefold()
print()

if resposta == "decimal" or resposta == "d" or resposta == "dec": 
    num_decimal = int(input("Digite o número em formato decimal: "))
    num_decimal_inicial = num_decimal 
    import math
    i = 0
    contador_0 = 0
    contador_1 = 0
    binario_lista = []
    
    def expoent_count(n): 
        expoente = math.log2(n) 
        expoente = int(expoente)
        return expoente
    
    while num_decimal != 0:
        i = i + 1
        binario = num_decimal % 2 
        if binario == 0:
            contador_0 = contador_0 + 1
        elif binario == 1:
            contador_1 = contador_1 + 1
        print("Índice {} da sequência binária: {}".format(expoent_count(num_decimal), binario))
        binario_lista.append(binario) 
        num_decimal = num_decimal // 2 
    
    print()
    binario_lista = list(reversed(binario_lista))
    print("O número binário gerado possui uma sequência de {} algarismos, sendo {} zero(s) e {} um(uns).".format(i, contador_0, contador_1))
    print("O número decimal ",num_decimal_inicial," equivale a ",*binario_lista," em binário.", sep="")
    print()
    print("Fim do programa")

elif resposta == "b" or resposta == "binário" or resposta == "bin" or resposta == "binario":
    
    def conversor_bintodec(n): 
       expoente = 0
       for int in n: 
            algarism = int 
            
            calculo = 2**expoente * algarism 
            expoente = expoente + 1 
            convertido_lista.append(calculo) 
    
    num_binario = int(input("Digite o número em formato binário: "))

    #*****Bloco de variáveis*****
    binario_string = str(num_binario) #
   
    binario_lista_string = []
    binario_inteiros = []
   
    binario_lista_string.extend(binario_string) 
    binario_lista_string = list(reversed(binario_lista_string)) 
    convertido_lista = []
    decimal = 0
    
    for str in binario_lista_string: 
        for char in str: 
            binario_algarismos_int = int(char) 
            binario_inteiros.append(binario_algarismos_int)

    conversor_bintodec(binario_inteiros)
    
    for number in convertido_lista: 
        decimal = decimal + number 
    
    print()
    print(f"o número binário {num_binario} equivale a {decimal} em notação decimal.")
    print()
    print("Fim do programa")
