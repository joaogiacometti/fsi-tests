# FSI-Tests: Calculadora com testes automatizados

Esse projeto é uma calculadora simples em Python que realiza cinco operações matemáticas: soma (+), subtração (-), multiplicação (\*), divisão (/) e potenciação (^).
O objetivo é validar a entrada dos valores e garantir que a operação fornecida seja válida.

## Como funciona

A calculadora recebe dois valores e um operador. Ela valida se:

- Os dois valores são numéricos (inteiros ou decimais, positivos ou negativos).
- O operador fornecido é um dos cinco válidos.

Se algum dos dados fornecidos for inválido, a função retorna 'None'.

## Testes automatizados

Para garantir que a calculadora funciona corretamente, criamos mais de 20 testes automatizados. Esses testes verificam:

- Operações válidas com inteiros e decimais.
- Casos envolvendo números negativos.
- Casos de erro, como entrada inválida ou operação inexistente.

Os testes estão localizados na pasta test/.

## Integração Contínua (CI)

A integração com GitHub Actions foi configurada para rodar os testes automaticamente sempre que houver um push ou pull request. Você pode acompanhar o status dos testes no badge abaixo:

![Testes Automatizados](https://github.com/sthefaniarcaro/fsi-tests/actions/workflows/python-app.yml/badge.svg)

Desenvolvido por:
joaogiacometti
sthefaniarcaro
