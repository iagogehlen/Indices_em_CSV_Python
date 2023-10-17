
def criar_e_pesquisar_indice_campo5(arquivo_binario, tamanho_registro, valor_pesquisa):
    class TreeNode:
        def __init__(self, key):
            self.key = key
            self.positions = []
            self.left = None
            self.right = None
            self.height = 1

    def create_avl_index(registros, tamanho_registro):
        avl_root = None

        for i, registro in enumerate(registros):
            campos = [registro[i:i + 100] for i in range(0, len(registro), 100)]

            if len(campos) == tamanho_registro // 100:
                valor_campo5 = campos[4].rstrip()  
                if valor_campo5 not in ["", "False"]:
                    node = TreeNode(valor_campo5)
                    node.positions.append(i)  
                    avl_root = insert(avl_root, node)

        return avl_root

    def insert(root, node):
        if not root:
            return node

        if node.key < root.key:
            root.left = insert(root.left, node)
        elif node.key > root.key:
            root.right = insert(root.right, node)
        else:
            root.positions.extend(node.positions)

        root.height = 1 + max(get_height(root.left), get_height(root.right))

        balance = get_balance(root)

        if balance > 1:
            if node.key < root.left.key:
                return rotate_right(root)
            root.left = rotate_left(root.left)
            return rotate_right(root)
        if balance < -1:
            if node.key > root.right.key:
                return rotate_left(root)
            root.right = rotate_right(root.right)
            return rotate_left(root)

        return root

    def get_height(node):
        if not node:
            return 0
        return node.height

    def get_balance(node):
        if not node:
            return 0
        return get_height(node.left) - get_height(node.right)

    def rotate_left(z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(get_height(z.left), get_height(z.right))
        y.height = 1 + max(get_height(y.left), get_height(y.right))

        return y

    def rotate_right(y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(get_height(y.left), get_height(y.right))
        x.height = 1 + max(get_height(x.left), get_height(x.right))

        return x

    with open(arquivo_binario, "rb") as file:
        registros_bytes = file.read().split(b'\n')
        registros = [registro_byte.decode('utf-8').strip() for registro_byte in registros_bytes]

    avl_root = create_avl_index(registros, tamanho_registro)

    def search_avl_index(root, key):
        if not root:
            return None
        if key == root.key:
            return root
        if key < root.key:
            return search_avl_index(root.left, key)
        return search_avl_index(root.right, key)

    def pesquisar_indice_campo5(valor_pesquisa):
        result_node = search_avl_index(avl_root, valor_pesquisa)
        if result_node:
            for index in result_node.positions:
                registro = registros[index].rstrip() 
                print(registro)
        else:
            print("Valor não encontrado no índice da árvore AVL do campo Rating.")

    pesquisar_indice_campo5(valor_pesquisa)


arquivo_binario = "registros.bin"
tamanho_registro = 600  
valor_pesquisa = "4.4"
criar_e_pesquisar_indice_campo5(arquivo_binario, tamanho_registro, valor_pesquisa)
