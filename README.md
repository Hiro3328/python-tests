# python-tests
## Aula de Engenharia de Software
- [Python](https://www.python.org/)

## Explicação do Código:

### Encriptação
> Pula o caractére um número de casas baseado na posição dele no texto e da chave de encriptação 
 

### Desencriptação
> Caminho inverso da encriptação, volta um número de casas



## Testes do Código:

| Testes                            | Resultados    |   Descrição do Evento  |
| -------------                     |:-------:      |------------------------|
| Encriptação/Desencriptação        | ✅            | Texto decriptado igual ao texto passado para encriptar |
| Sem passar parâmetros             | ✅            | Retorna None                                           |
| Passando algo que não seja string | ✅            | Retorna TypeError, funcionando como esperado           |
| Caractéres que não são suportados | ✅            | Os caractéres inválidos permanecem iguais
| Velocidade ( 61 chars)            |  0.4 ms       | Tempo para Encriptar e Decriptar
| Velocidade ( 15694 chars)         |  9.2 ms       | Tempo para Encriptar e Decriptar
| Velocidade ( 1974 chars)          |  1.3 ms       | Tempo para Encriptar e Decriptar

> \[!NOTE]
> Testes de velocidade referentes ao processador Ryzen 5 5600G

