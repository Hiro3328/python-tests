import unittest
import src.hiroMethod as mainCode
from time import perf_counter_ns as time_ns

def timeit(lambdaExpression, repeat = 1):
    start = time_ns()
    for i in range(repeat):
        lambdaExpression()

    
    nanoseconds = (time_ns() - start)/repeat
    length = len("%.0f" % nanoseconds)/3
    
    if length < 1:
        return f"{nanoseconds} nanossegundos"
    elif length < 2:
        return f"{nanoseconds/1_000} microssegundos"
    elif length < 3:
        return f"{nanoseconds/1_000_000} milissegundos"
    else:
        return f"{nanoseconds/1000_000_000} segundos"


class TestEncrypt(unittest.TestCase):
    def full_test(self, text, key = 3218):
        encryped = mainCode.encrypt(text, key)

        decrypted = mainCode.decrypt(encryped, key)

        self.assertEqual(text, decrypted)

        with open("output.txt", "w") as file:
            file.write("Texto de entrada: " + text + "\n")
            file.write("Texto criptografado: " + encryped + "\n")
            file.write("Texto descriptografado: " + decrypted + "\n")

            file.close()
    
    def noParams(self):
        self.assertRaises(TypeError, mainCode.encrypt)
        print("Quando não é passado nenhum parâmetro, ele dará TypeError")

    def noText(self):   
        self.assertRaises(TypeError, mainCode.encrypt, 120)
        print("Quando não é colocado uma String, ele dará TypeError")

    def charNotInTable(self):
        self.assertIsNotNone(mainCode.encrypt, "󰩧😲℣.")
        print("Sem caracteres na tabela: ", mainCode.encrypt("󰩧😲℣."))

    def speedTest(self, text, key = 3218, repeats = 1):
        print("Teste de velocidade:", timeit(lambda: self.full_test(text, key), repeats))

    def differentKeyTest(self, text, key1 = 319, key2 = 318):
        encryped = mainCode.encrypt(text, key1)
        decrypted = mainCode.decrypt(encryped, key2)
        self.assertNotEqual(decrypted, text)
        print("Chaves diferentes retornam diferentes textos\n", decrypted)
