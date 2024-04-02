# Gerador de Comprovante

Este é um programa em Python que gera comprovantes de pagamento em formato PDF usando a biblioteca ReportLab. Ele inclui uma interface gráfica simples feita com Tkinter para inserir os detalhes do pagamento.

## Funcionalidades

- Gera comprovantes de pagamento em formato PDF.
- Interface gráfica intuitiva para inserir detalhes do pagamento.
- Opção para limpar os campos de entrada.

## Requisitos do Sistema

- Python 3.x
- Bibliotecas: tkinter, reportlab

## Instalação

1. Clone ou baixe este repositório.

```bash
git clone https://github.com/seu_usuario/gerador-de-comprovante.git
```
2. Navegue até o diretório do projeto.
```bash
cd gerador-de-comprovante
```
3. Instale as dependências usando pip.
```bash
pip install reportlab
pip install dateutil
```
## Uso
Execute o arquivo main.py para iniciar o programa.
```bash
python main.py
```
- Insira o valor do pagamento, nome do cliente, quantidade de parcelas e data de início.
- Clique no botão "Gerar Comprovante" para gerar o PDF.
- Use o botão "Limpar Campos" para limpar os campos de entrada.

## Motivação 
- A motivação para este programa é simplificar e agilizar o processo de criação de comprovantes de pagamento em PDF. Automatizando tarefas repetitivas e propensas a erros, como inserir detalhes de pagamento e datas de vencimento, o programa oferece uma solução rápida e precisa para gerar múltiplos comprovantes com facilidade.

## Exemplo
- o exemplo do comprovante pode ser encontrado no exemplo_comprovante.pdf