from tests.runTests import TestEncrypt

testes = TestEncrypt()

text = "Olá! Esse é um teste de encriptação e desencriptação de textos."
input("\nPressione {ENTER} para iniciar os testes")
testes.full_test(text)

input("\nPressione {ENTER} para o próximo teste")
testes.noText()

input("\nPressione {ENTER} para o próximo teste")
testes.charNotInTable()

input("\nPressione {ENTER} para o próximo teste")
testes.differentKeyTest(text)

input("\nPressione {ENTER} para o próximo teste")
testes.speedTest(text)


input("\nPressione {ENTER} para o próximo teste")
with open("./tests/archInstallationProcess", "r") as fileReader:
    text = fileReader.read()

    print("Tamanho do Texto: ", len(text), "caracteres")
    print("Repetirá 100 vezes para média de tempo")
    testes.speedTest(text, repeats=100)

input("\nPressione {ENTER} para o último teste")
with open("./tests/someText_inPortuguese", "r") as fileReader:
    text = fileReader.read()

    print("Tamanho do Texto: ", len(text))
    print("Repetirá 100 vezes para média de tempo")
    testes.speedTest(text, key=32, repeats=100)
