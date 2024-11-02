import unittest
import src.hiroMethod as mainCode
from time import perf_counter_ns as time_ns

def timeit(lambdaExpression):
    start = time_ns()
    lambdaExpression()
    
    nanoseconds = time_ns() - start

    match len(str(nanoseconds))//3:
        case 0:
            return f"{nanoseconds} nanoseconds"
        case 1:
            return f"{nanoseconds/1_000} microseconds"
        case 2:
            return f"{nanoseconds/1_000_000} milliseconds"
        case _:
            return f"{nanoseconds/1000_000_000} seconds"




class TestEncrypt(unittest.TestCase):
    def full_test(self, text):
        encryped = mainCode.encrypt(text)

        decrypted = mainCode.decrypt(encryped)

        self.assertEqual(text, decrypted)

        with open("output.txt", "w") as file:
            file.write("Texto de entrada: " + text + "\n")
            file.write("Texto criptografado: " + encryped + "\n")
            file.write("Texto descriptografado: " + decrypted + "\n")

            file.close()

    def test_encrypt(self, text):
        encryped = mainCode.encrypt(text)

        self.assertNotEqual(text, encryped)

        print("Texto de entrada: ", text)
        print("Texto criptografado: ", encryped)

    def test_decrpt(self, text):
        decrypted = mainCode.decrypt(text)

        self.assertNotEqual(text, decrypted)

        print("Texto de entrada: ", text)
        print("Texto descriptografado: ", decrypted)

    def noText(self):   
        self.assertRaises(TypeError, mainCode.encrypt, 120)
        print("Quando não é colocado uma String, ele dará TypeError")

    def charNotInTable(self):
        self.assertIsNotNone(mainCode.encrypt, "󰩧😲℣.")
        print("Sem caracteres na tabela: ", mainCode.encrypt("󰩧😲℣."))

    def speedTest(self, text):
        print("Teste de velocidade:", timeit(lambda: self.full_test(text)))
