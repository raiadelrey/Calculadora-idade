def calculadoraidade():
    ficar = "sim"
    while ficar == "sim":
        import time
        i = 0
        for i in range(2,0,-1):
            time.sleep(1)
            if i == 1:
             print ("-------------------------------------------------------")
        print ("Digite seu nome:")
        nome = str(input())
        print("Digite seu ano de nascimento:")
        anonascimento= int(input())

        if anonascimento > 2021  or anonascimento < 1921:
            print("Entrada inválida! Por favor, digite um ano entre 1922 e 2021. ")
            print ("-------------------------------------------------------")
            print("Tente novamente!")
            print ("-------------------------------------------------------")
            print("Voltando ao menu inicial...Aguarde!")
            import time
            i = 0
            for i in range(2, 0, -1):
                time.sleep(1)
            if i == 1:
                print("-------------------------------------------------------")
                print(
                    "Digite seu nome")
            anonascimento = int(input())

        anoatual = 2022
        idade = anoatual - anonascimento
        print (nome,", a sua idade é:", idade,"anos")



calculadoraidade()


