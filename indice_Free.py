import struct

def criar_e_pesquisar_indice_campo6(arquivo_binario, tamanho_registro, valor_pesquisa):
    indice_campo6 = {}
    registros = []

    def criar_indice_campo6():
        nonlocal registros

        with open(arquivo_binario, "rb") as file:
            registros_bytes = file.read().split(b'\n') 
            registros = [registro_byte.decode('utf-8').strip() for registro_byte in registros_bytes]

        for i, registro in enumerate(registros):
            campos = [registro[i:i + 100] for i in range(0, len(registro), 100)]

            if len(campos) == tamanho_registro // 100:
                valor_campo6 = campos[5].strip()  

                if valor_campo6 not in indice_campo6:
                    indice_campo6[valor_campo6] = []

                indice_campo6[valor_campo6].append(i) 

        with open("indice_Free.bin", "wb") as index_file:
            for key, value in indice_campo6.items():
                key_bytes = key.encode('utf-8')
                key_length = len(key_bytes)
                value_count = len(value)
                index_file.write(struct.pack('I', key_length))
                index_file.write(key_bytes)
                index_file.write(struct.pack('I', value_count))
                for item in value:
                    index_file.write(struct.pack('I', item))

    criar_indice_campo6()

    def pesquisar_indice_campo6(valor_pesquisa):
        with open("indice_Free.bin", "rb") as index_file:
            while True:
                key_length_data = index_file.read(4)
                if not key_length_data:
                    break
                key_length = struct.unpack('I', key_length_data)[0]
                key_data = index_file.read(key_length)
                key = key_data.decode('utf-8')
                value_count = struct.unpack('I', index_file.read(4))[0]
                indices_data = index_file.read(4 * value_count)
                indices = struct.unpack(f'{value_count}I', indices_data)

                if key == valor_pesquisa:
                    for index in indices:
                        registro = registros[index].rstrip()  
                        print(registro)

    pesquisar_indice_campo6(valor_pesquisa)

arquivo_binario = "registros.bin"
tamanho_registro = 600  
valor_pesquisa = "False"
criar_e_pesquisar_indice_campo6(arquivo_binario, tamanho_registro, valor_pesquisa)
