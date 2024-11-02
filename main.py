from tests.runTests import TestEncrypt

testes = TestEncrypt()

text = "Olá! Esse é um teste de encriptação e desencriptação de textos."
input("Pressione {ENTER} para iniciar os testes")
testes.full_test(text)

input("Pressione {ENTER} para o próximo teste")
testes.noText()

input("Pressione {ENTER} para o próximo teste")
testes.charNotInTable()

input("Pressione {ENTER} para o próximo teste")
testes.speedTest(text)

input("Pressione {ENTER} para o próximo teste")
with open("./tests/archInstallationProcess", "r") as fileReader:
    text = fileReader.read()

    print("Tamanho do Texto: ", len(text))
    testes.speedTest(text)

input("Pressione {ENTER} para o último teste")
with open("./tests/someText_inPortuguese", "r") as fileReader:
    text = fileReader.read()

    print("Tamanho do Texto: ", len(text))
    testes.speedTest(text)
