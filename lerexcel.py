import xlrd

file = open("testfile4.txt", "w")

book = xlrd.open_workbook("lista.xlsx")
print("Número de abas: ", book.nsheets)
print("Nomes das Planilhas:", book.sheet_names())

for y in range(book.nsheets):
    sh = book.sheet_by_index(y)

    for x in range(sh.nrows):
        linha = ""
        for k in range(sh.ncols):
            coluna = sh.cell_value(rowx=x, colx=k)
            if (str(coluna) != ""):
                linha = linha + str(coluna) + ";"

        if (len(linha.strip()) != ""):
            file.write(linha+"\n")

file.close()
