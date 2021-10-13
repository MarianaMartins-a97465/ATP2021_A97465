
from random import randint #Escolher um numero aleatorio entre um nº finito de opções

j=int(input("Introduza 1 ou 2 consoante pretenda ser o primeiro ou segundo jogador, respetivamente:  "))
fos=21


def jogar (j, fos): 
    if (j!=1 and j!=2):
        print("Jogador invalido. Tente Novamente!")
    else:
        
        while fos>1: #Jogo continua até sobrar um único fosforo
        
            if j==1:  #computador é o jogador 2
                a=int(input("Introduza um valor a retirar entre 1 e 4 inclusive: "))
                b=(5-a)
                
                if a!=1 and a!=2 and a!=3 and a!=4:
                    print("Valor invalido. Tente Novamente!")
                else:
                        fos=(fos-a)  
                        print(fos)  #Retorna com quantos fosforos ficamos
                        if fos>1:
                            b= (5-a)    #soma de ambas as jogadas tem de ser 5 para jogador 2 ganhar    #b e a jogada do computador
                            print('O computador joga ' + str(b))
                            fos=(fos-b)
                            print(fos)       #Retorna com quantos fosforos ficamos                          
               
                
               
            else: #computador é o jogador 1
                c=int(randint(1,4)) 
                
                print('O computador joga ' + str(c))
                fos=(fos-c)
                print(fos)
                
                d=int(input("Introduza um valor a retirar entre 1 e 4 inclusive:  "))
                if d!=1 and d!=2 and d!=3 and d!=4:
                    print("Valor invalido. Tente Novamente!")
                else:
                        if (c+d)==5: #Erro de Raciocinio do jogador 2 se for diferente de 5
                            fos=(fos-d)
                            print(fos)
                            jogar(2,fos)
                            
                            
                        elif (c+d)>5: #Correçao erro de Raciocinio
                            fos=(fos-d)
                            print(fos)
                            c1=10-(c+d)
                                                        
                            print('O computador joga ' + str(c1))
                            fos=(fos-c1)
                            print(fos)
                            jogar(1,fos) #Depois de detetar o erro, o computador retorna a posicao vencedora
                            
                                                       
                            
                        else:  #Correçao erro de Raciocinio
                            fos=(fos-d)
                            print(fos)
                            c2=5-(c+d)
                            fos=(fos-c2)
                            
                            print('O computador joga ' + str(c2))
                            print(fos)
                            jogar(1,fos)
                             
        
        
        #decidir Vencedor
        if j==1:
            print("O computador venceu. Jogue outra vez!")
            jogar(j,21)
        else:
            print("O jogador venceu. Jogue outra vez!")
            jogar(j,21)

            
print("O jogo começa com 21 fosforos.")                     
jogar(j,fos)
            
