import time
#from desafios.physicsQuestion import *
#import aulas.Condições.lista_03 as lista3 
#import Libs.baseConversor as baseConverter
import src.hiroMethod as enc

start_time = time.time()

# Code to run
a = """
Significado da bandeira da Índia:

* A cor açafrão significa coragem e sacrifício;
* O branco a pureza e a verdade ;
* O verde a fé e a fertilidade;
* A roda significa justiça.

Sobre a Religião:

O Hinduísmo é a religião oficial da Índia. Os seguidores acreditam em vários deuses e na reencarnação. Segundo o hinduísmo, os seres humanos morrem e renascem várias vezes. Ao longo de muitas vidas, eles têm a oportunidade de evoluir, até chegar a um estágio em que se unem a Brahman, a realidade suprema.

O hinduísmo divide a sociedade em castas. A divisão da sociedade em castas é determinada a partir da hereditariedade. As castas se definem de acordo com a posição social que determinadas famílias hindus ocupam.

Dados Principais:

Área: 3.287.782 km²;
Capital Da Índia: Nova Délhi;
População: 1.42 bilhão (estimativa 2023);
Localização: centro-sul da Ásia;
Fuso Horário: +8h 30min em relação á Brasília.

Países vizinhos:

Bangladesh;
China;
Nepal;
Paquistão.

Taj Mahal:

Uma das 7 Maravilhas do Mundo Moderno é um dos pontos turísticos mais famosos da Índia. O significado histórico e cultural do Taj Mahal está fortemente vinculado ao amor.
"""
b = enc.encrypt(a)
# c = enc.decrypt(b)
# print(f"Original : {a}\nEncrypted: {b}\nDecrypted: {c.capitalize()}\nAre they equal = {a==c.capitalize()}")
print(b)
totalTime = time.time() - start_time

# Better string managment, this doesn't affect the final time
def beautifyTime():
   if totalTime >= 1:
    return f"{totalTime:.2f} seconds"
   else:
    return f"{totalTime*1000:.4f} milliseconds"

print(f"\nCode finished in {beautifyTime()}.")
