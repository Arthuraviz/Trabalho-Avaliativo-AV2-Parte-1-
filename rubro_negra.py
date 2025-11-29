"""
Trabalho Avaliativo AV2 - Árvores Binárias e Balanceamento
Aluno: Arthur
Data de entrega: 29/11/2025

Implementação de Árvore Rubro-Negra em Python
Operações: Inserção, Balanceamento, Percurso in-order
Regras: uso de nó NIL preto para filhos nulos
"""

# -------------------------------
# Estrutura do nó da árvore
# -------------------------------
class Node:
    def __init__(self, key, color="RED", left=None, right=None, parent=None):
        """
        Classe que representa um nó da Árvore Rubro-Negra.
        Atributos:
        - key: valor armazenado no nó
        - color: cor do nó (RED ou BLACK)
        - left, right: filhos esquerdo e direito
        - parent: referência para o nó pai
        """
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

# Nó NIL global (sempre preto), usado para representar filhos nulos
NIL = Node(key=None, color="BLACK")
NIL.left = NIL
NIL.right = NIL

# -------------------------------
# Classe da Árvore Rubro-Negra
# -------------------------------
class RedBlackTree:
    def __init__(self):
        """Inicializa a árvore com raiz apontando para NIL."""
        self.root = NIL

    def insert(self, key):
        """
        Insere um novo nó na árvore rubro-negra.
        - O nó é inicialmente vermelho.
        - É colocado como em uma árvore binária de busca.
        - Depois chama insert_fix para corrigir violações das regras.
        """
        new_node = Node(key=key, color="RED", left=NIL, right=NIL, parent=None)
        parent = None
        current = self.root

        # Busca a posição correta para inserir
        while current != NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        # Define o pai do novo nó
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # Corrige violações das regras da rubro-negra
        self.insert_fix(new_node)

    def insert_fix(self, node):
        """
        Corrige violações após inserção.
        Casos tratados:
        1. Pai e tio vermelhos → recoloração.
        2. Pai vermelho e tio preto → rotações + recoloração.
        """
        while node.parent and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    # Caso 1: tio vermelho
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Caso 2: rotação esquerda
                        node = node.parent
                        self.rotate_left(node)
                    # Caso 3: rotação direita
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.rotate_left(node.parent.parent)

        # A raiz deve sempre ser preta
        self.root.color = "BLACK"

    def rotate_left(self, x):
        """
        Rotação à esquerda em torno do nó x.
        Necessária para corrigir desbalanceamentos.
        """
        y = x.right
        x.right = y.left
        if y.left != NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        """
        Rotação à direita em torno do nó x.
        Necessária para corrigir desbalanceamentos.
        """
        y = x.left
        x.left = y.right
        if y.right != NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder(self, node):
        """
        Percorre a árvore em ordem crescente.
        Imprime cada chave seguida da cor (RED ou BLACK).
        """
        if node != NIL:
            self.inorder(node.left)
            print(f"{node.key} ({node.color})", end=" ")
            self.inorder(node.right)


# -------------------------------
# Teste com pelo menos 21 nós
# -------------------------------
if __name__ == "__main__":
    tree = RedBlackTree()
    valores = [10, 20, 30, 15, 25, 5, 1, 50, 60, 70, 80, 90, 100,
               110, 120, 130, 140, 150, 160, 170, 180, 190]

    for v in valores:
        tree.insert(v)

    print("Árvore Rubro-Negra (in-order):")
    tree.inorder(tree.root)