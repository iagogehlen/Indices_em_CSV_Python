def ajustar_tamanho(texto, tamanho):
    return texto.ljust(tamanho)[:tamanho]

tamanho_registro = 600 
arquivo_binario = "reduzido.bin"

with open(arquivo_binario, "wb") as file:
    with open("modificado.csv", "r", encoding="utf-8") as csv_file:
        next(csv_file)

        registros_gravados = 0

        for line in csv_file:
            campos = line.strip().split(",")
            

            campos_ajustados = [ajustar_tamanho(campo, 100) for campo in campos]
            
            registro = "".join(campos_ajustados)
            if len(registro) <= tamanho_registro:
                file.write(registro.encode('utf-8'))
                file.write(b'\n')

                registros_gravados += 1

                if registros_gravados >= 1000:
                    break

print(f"Foram inseridos {registros_gravados} registros no arquivo binário.")
