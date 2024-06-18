p = True
q = True
r = True


while True:
    n = int(input("Quantas variáveis você deseja usar para a tabela verdade?\n"
              "1 - Uma variável\n"
              "2 - Duas variáveis\n"
              "3 - Três variáveis\n"
              "0 - Sair do programa\n"
              "Escolha uma opção (0, 1, 2, 3): "))

    if n == 1:
        print(p)
        print(not(p))

    elif n == 2:
        conect = str(input("Qual conectivo deseja usar? (v,^,->,<->)"))
        if conect == "v":
            print("p v q:", p or q)
            print("~p v q:", not(p) or q)
            print("p v ¬~q:", p or not(q))
            print("~p v ~q:", not(p) or not(q))
        elif conect == "^":
            print("p ^ q:", p and q)
            print("~p ^ q:", not(p) and q)
            print("p ^ ~q:", p and not(q))
            print("~p ^ ~q:", not(p) and not(q))
        elif conect == "->":
            print("p -> q:", not(p) or q)
            print("~p -> q:", not(not(p)) or q)
            print("p -> ~q:", not(p) or not(q))
            print("~p -> ~q:", not(not(p)) or not(q))
        elif conect == "<->":
            print("p <-> q:", not(p and q))
            print("p <-> ~q:",(p) and not(q))
            print("~p <-> q:", not(p) and (q))
            print("~p <-> ~q:", not(not(p) and not(q)))
        else:
            print("Inválido\n" "O código será reiniciado.")

    elif n == 3:
        conect1 = input("Qual o primeiro conectivo que deseja usar entre p e q (v, ^, ->, <->)? ")
        conect2 = input("Qual o segundo conectivo que deseja usar entre o resultado de p e q com r (v, ^, ->, <->)? ")

        for p in [True, False]:
            for q in [True, False]:
                for r in [True, False]:

                    if conect1 == "v":
                        pq = p or q
                    elif conect1 == "^":
                        pq = p and q
                    elif conect1 == "->":
                        pq = not p or q
                    elif conect1 == "<->":
                        pq = (p and q) or (not p and not q)
                  

                    if conect2 == "v":
                        final_result = pq or r
                    elif conect2 == "^":
                        final_result = pq and r
                    elif conect2 == "->":
                        final_result = not pq or r
                    elif conect2 == "<->":
                        final_result = (pq and r) or (not pq and not r)


                    print(f"p: {p}, q: {q}, r: {r} -> ({p} {conect1} {q}) {conect2} {r}: {final_result}")


    elif n == 0:
        break
    
    else:
        print("Inválido! /n" "Tente novamente.")



'''
EXPLICACAO PARA AS 3 VARIÁVEIS:

Este bloco de cpdigo utiliza três loops 'for' nested para gerar todas as combinações possíveis
das variáveis lógicas 'p', 'q', e 'r'. Cada loop corresponde a uma das variáveis.
O loop mais externo controla a variável 'p', mantendo seu valor constante enquanto nao sao finalizadas as iterações de 'q' e 'r'.
Isso garante que 'p' alterna entre True e False a cada 4 iterações, 
assim todas as combinacoes entre as 3 variaveis com o "p" com valor T sao feitas antes de mudar "p" para F.
O segundo loop controla 'q', alternando seu valor entre True e False a cada 2 iterações. Para cada valor de 'q',
o loop mais interno é executado completamente, fazendo 'r' alternar entre True e False para cada
combinação de 'p' e 'q'. Assim, 'r' altera sempre entre T e F por que esta sempre sendo interado.
Esses loops garantem que cada combinação possível de True e False para 'p', 'q', e 'r' sejam geradas.

'''