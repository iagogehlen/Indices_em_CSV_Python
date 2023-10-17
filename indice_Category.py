
def criar_e_pesquisar_indice_campo3(arquivo_binario, tamanho_registro, valor_pesquisa):
 
    indice_campo3 = {}
    registros = []

    def criar_indice_campo3():
        nonlocal registros

        with open(arquivo_binario, "rb") as file:
            registros_bytes = file.read().split(b'\n')  
            registros = [registro_byte.decode('utf-8').strip() for registro_byte in registros_bytes]

        for i, registro in enumerate(registros):
            campos = [registro[i:i + 100] for i in range(0, len(registro), 100)]

            if len(campos) == tamanho_registro // 100:
                valor_campo3 = campos[3].strip()  

                if valor_campo3 not in indice_campo3:
                    indice_campo3[valor_campo3] = []

                indice_campo3[valor_campo3].append(i)  

    criar_indice_campo3()

    def pesquisar_indice_campo3(valor_pesquisa):
        if valor_pesquisa in indice_campo3:
            for index in indice_campo3[valor_pesquisa]:
                registro = registros[index].rstrip()  
                print(registro)
        else:
            print("Valor não encontrado no índice do campo 3.")

    pesquisar_indice_campo3(valor_pesquisa)

arquivo_binario = "registros.bin"
tamanho_registro = 600  
valor_pesquisa = "Arcade"
criar_e_pesquisar_indice_campo3(arquivo_binario, tamanho_registro, valor_pesquisa)
