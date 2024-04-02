import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfgen import canvas
from dateutil.relativedelta import relativedelta
import os

def generate_receipt_pdf(amount, name, num_installments, start_date):
    # Cria um nome de arquivo único baseado na data e hora atual
    filename = f"comprovante_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"

    # Cria um novo documento PDF com orientação portrait e tamanho A4
    c = canvas.Canvas(filename, pagesize=portrait(A4))

    # Define a fonte e tamanho da fonte
    font_size = 16  # Tamanho da fonte
    c.setFont("Helvetica", font_size)

    # Calcula a data da primeira parcela
    start_date = datetime.strptime(start_date, '%d/%m/%Y')
    next_date = start_date

    # Define o tamanho e a posição do retângulo ao redor da parcela
    x_start_left = 50
    x_start_right = A4[0] - 300  # Posição inicial para as informações à direita
    y_start_top = A4[1] - 50  # Posição inicial na parte superior da página
    rectangle_width = 250
    rectangle_height = 120

    # Espaçamento entre as linhas
    line_spacing = 8

    # Itera sobre as parcelas
    for i in range(num_installments):
        # Verifica se há espaço suficiente na página para a próxima parcela
        if i % 6 == 0 and i != 0:
            c.showPage()  # Adiciona uma nova página
            y_start_top = A4[1] - 50  # Reseta a posição para a parte superior da nova página

        # Desenha uma linha ao redor da parcela (via do cliente)
        c.setLineWidth(4)
        c.rect(x_start_left, y_start_top - rectangle_height, rectangle_width, rectangle_height)

        # Escreve informações da via do cliente
        text_width = c.stringWidth(f"nome: {name}")
        c.drawString(x_start_left + 10, y_start_top - 20 - font_size, f"nome: {name}")
        c.drawString(x_start_left + 10, y_start_top - 40 - line_spacing - font_size, f"Parcela {i+1}: R${amount:.2f}")
        c.drawString(x_start_left + 10, y_start_top - 60 - line_spacing * 2 - font_size, f"data: {next_date.strftime('%d/%m/%Y')}")

        # Desenha uma linha ao redor da parcela (via do estabelecimento)
        c.setLineWidth(4)
        c.rect(x_start_right, y_start_top - rectangle_height, rectangle_width, rectangle_height)

        # Escreve informações da via do estabelecimento
        c.drawString(x_start_right + 10, y_start_top - 20 - font_size, f"nome: {name}")
        c.drawString(x_start_right + 10, y_start_top - 40 - line_spacing - font_size, f"Parcela {i+1}: R${amount:.2f}")
        c.drawString(x_start_right + 10, y_start_top - 60 - line_spacing * 2 - font_size, f"Data: {next_date.strftime('%d/%m/%Y')}")

        # Calcula a data da próxima parcela
        next_date = start_date + relativedelta(months=i+1)  # Adiciona um mês a cada parcela

        # Atualiza a posição para a próxima parcela
        y_start_top -= 130  # Aumenta a distância entre as vias de cima

    # Salva o PDF
    c.save()

    os.system(f"start {filename}") 

    messagebox.showinfo("Sucesso", "Comprovante gerado com sucesso!")


def clear_fields():
    valor_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    parcelas_entry.delete(0, tk.END)
    data_inicio_entry.delete(0, tk.END)

def generate_receipt():
    # Obter os valores dos campos de entrada
    valor = float(valor_entry.get())
    nome = nome_entry.get()
    parcelas = int(parcelas_entry.get())
    data_inicio = data_inicio_entry.get()

    # Validar a data de início
    try:
        datetime.strptime(data_inicio, '%d/%m/%Y')
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido! Use o formato dd/mm/aaaa.")
        return

    # Chamar a função generate_receipt_pdf com os valores fornecidos
    try:
        generate_receipt_pdf(valor, nome, parcelas, data_inicio)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o comprovante: {str(e)}")

# Criar a janela principal
root = tk.Tk()
root.title("Gerador de Comprovante")
root.geometry("400x250")

# Criar e posicionar os widgets na janela
valor_label = ttk.Label(root, text="Valor:")
valor_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
valor_entry = ttk.Entry(root)
valor_entry.grid(row=0, column=1, padx=5, pady=5)

nome_label = ttk.Label(root, text="Nome:")
nome_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
nome_entry = ttk.Entry(root)
nome_entry.grid(row=1, column=1, padx=5, pady=5)

parcelas_label = ttk.Label(root, text="Quantidade de Parcelas:")
parcelas_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
parcelas_entry = ttk.Entry(root)
parcelas_entry.grid(row=2, column=1, padx=5, pady=5)

data_inicio_label = ttk.Label(root, text="Data de Início (dd/mm/aaaa):")
data_inicio_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
data_inicio_entry = ttk.Entry(root)
data_inicio_entry.grid(row=3, column=1, padx=5, pady=5)

gerar_button = ttk.Button(root, text="Gerar Comprovante", command=generate_receipt)
gerar_button.grid(row=4, column=0, padx=5, pady=10, sticky="w")

limpar_button = ttk.Button(root, text="Limpar Campos", command=clear_fields)
limpar_button.grid(row=4, column=1, padx=5, pady=10, sticky="e")

# Iniciar o loop de eventos
root.mainloop()
