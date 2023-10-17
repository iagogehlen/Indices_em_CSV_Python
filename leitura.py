def ler_arquivo_binario(arquivo_binario, tamanho_registro, tamanho_campo, nomes_campos):
    with open(arquivo_binario, "rb") as file:
        registros_bytes = file.read().split(b'\n')  

    for registro_byte in registros_bytes:
        registro = registro_byte.decode('utf-8').strip()

        campos = [registro[i:i + tamanho_campo] for i in range(0, len(registro), tamanho_campo)]
        
        if len(campos) == tamanho_registro // tamanho_campo:
            for nome_campo, campo in zip(nomes_campos, campos):
                print(f"{nome_campo}: {campo}")
        else:
            print("Registro de tamanho incorreto:", campos)

arquivo_binario = "reduzido.bin"
tamanho_registro = 600
tamanho_campo = 100  
nomes_campos = ["ID", "App Name", "App Id", "Category","Rating","Free"] 

ler_arquivo_binario(arquivo_binario, tamanho_registro, tamanho_campo, nomes_campos)
