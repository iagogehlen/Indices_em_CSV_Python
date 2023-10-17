def pesquisa_binaria_por_id(arquivo_binario, id_alvo, tamanho_registro):
    with open(arquivo_binario, "rb") as file:
        registros_bytes = file.read().split(b'\n') 

    esquerda = 0
    direita = len(registros_bytes) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        registro = registros_bytes[meio].decode('utf-8').strip()

        campos = [registro[i:i+100] for i in range(0, len(registro), 100)]
        registro_id = int(campos[0].strip())

        if registro_id == id_alvo:
            return campos
        elif registro_id < id_alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return None

def consultar_registro_por_id(arquivo_binario, id_alvo, tamanho_registro):
    dados = pesquisa_binaria_por_id(arquivo_binario, id_alvo, tamanho_registro)
    
    if dados:
        print("Registro encontrado:")
        for campo in dados:
            print(campo)
    else:
        print(f"Registro com ID {id_alvo} não encontrado.")


id_alvo = 367  
consultar_registro_por_id("registros.bin", id_alvo, 600) 
