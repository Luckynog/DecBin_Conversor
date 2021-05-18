print("**********Sistema de conversão de números binários em decimais e vice-versa**********")
resposta = input("Você deseja converter a partir do binário ou do decimal? ").casefold()
print()

if resposta == "decimal" or resposta == "d" or resposta == "dec": 
    num_decimal = int(input("Digite o número em formato decimal: "))
    num_decimal_inicial = num_decimal #Guarda o número digitado pelo usuário para o print no final do programa;
    import math
    i = 0
    contador_0 = 0
    contador_1 = 0
    binario_lista = []
    
    def expoent_count(n): #O propósito da função é meramente enumerar qual é a posição do algarismo binário dentro do número como um todo; EXP: 1101, o algarismo "0" está no índice 1(um) do número binário (pois se conta a partir do zero, de trás para frente);
        expoente = math.log2(n) #Acha qual é o expoente do número digitado pelo usuário na base 2 (base binária). EXP: usuário digita 8. 2³ = 8. math.log2(8) é capaz de descobrir o expoente "3";
        expoente = int(expoente) #Serve para "truncar" de forma não convencional o índice. Se der 2 elevado a 7,99 por exemplo, ele trunca para 7;
        return expoente
    
    while num_decimal != 0:
        i = i + 1
        binario = num_decimal % 2 #Acha os "restos" das divisões inteiras por 2;
        if binario == 0:
            contador_0 = contador_0 + 1
        elif binario == 1:
            contador_1 = contador_1 + 1
        print("Índice {} da sequência binária: {}".format(expoent_count(num_decimal), binario))
        binario_lista.append(binario) #vai adicionar os algarismos binários em uma lista para futuro "print"
        num_decimal = num_decimal // 2 #Divisão inteira do número(num_decimal) por dois, dando sequência as divisões até 0. o "resto" dos resultados, lidos de baixo para cima, é o binário proriamente dito;
    
    print()
    binario_lista = list(reversed(binario_lista))
    print("O número binário gerado possui uma sequência de {} algarismos, sendo {} zero(s) e {} um(uns).".format(i, contador_0, contador_1))
    print("O número decimal ",num_decimal_inicial," equivale a ",*binario_lista," em binário.", sep="")#Printa a lista sem "[]" e "," usando (*), e sem espaçamento entre os números com o (sep="").
    print()
    print("Fim do programa")

elif resposta == "b" or resposta == "binário" or resposta == "bin" or resposta == "binario":
    
    def conversor_bintodec(n): 
       expoente = 0
       for int in n: #Para cada inteiro em "n";
            algarism = int 
            #Para conversão multiplica-se o algarismo pelo resultado de 2 elevado a seu respectivo expoente no número, começando por zero.
            calculo = 2**expoente * algarism #Exemplo: o número binário 1000. o último algarismo, "0", deve ser multiplicado por 2 elevado a 0, o penúltimo, também "0", por 2 elevado a 1, e assim por diante;
            expoente = expoente + 1 #Contador de expoente da base 2 (base do formato binário);
            convertido_lista.append(calculo) #Adiciona os resultados a uma lista para posterior somatório;
    
    num_binario = int(input("Digite o número em formato binário: "))

    #*****Blocão de variáveis*****
    binario_string = str(num_binario) #Transformação em "string" para permitir o "extend" na lista a seguir;
    #Listas:
    binario_lista_string = []
    binario_inteiros = []
    #Extend e reverso da lista:
    binario_lista_string.extend(binario_string) #O "extend" do valor inserido permite separar os algarismos do número binário um a um, dissociando-os uns dos outros;
    binario_lista_string = list(reversed(binario_lista_string)) #O reverse serve para manter a coerência entre "expoente" e "algarismo binário", pois lê-se da direita para a esquerda. com o reverse, já não existe mais este problema.
    convertido_lista = []
    decimal = 0
    
    for str in binario_lista_string: #Para cada "string" em "binario_lista_string", 
        for char in str: #Para cada caractere nestas "string",
            binario_algarismos_int = int(char) #Converto o caractere de string para inteiro(int), adicionando-os em uma variável temporária,
            binario_inteiros.append(binario_algarismos_int) #Anexo, em cada volta no "for", a variavel temporária à lista dos algarismos binários inteiros, até o "for" percorrer toda a lista "binario_lista_string"

    conversor_bintodec(binario_inteiros)
    
    for number in convertido_lista: #Para cada número na lista "convertido_lista", onde já contem todos os resultados individualmente para cada algarismo do número binário;
        decimal = decimal + number #Soma todos os números contidos na lista citada acima, finalmente encontrando o valor convertido de fato.
    
    print()
    print(f"o número binário {num_binario} equivale a {decimal} em notação decimal.")
    print()
    print("Fim do programa")