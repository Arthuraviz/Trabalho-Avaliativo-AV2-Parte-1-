"""
Trabalho Avaliativo AV2 - Árvores Binárias e Balanceamento
Aluno: Arthur
Data de entrega: 29/11/2025

Implementação de Árvore 2-3-4 (B-tree de ordem 4) em Python
Operações: Inserção com balanceamento automático, busca, percurso em-ordem
Regras: todos os nós podem ter 1, 2 ou 3 chaves; folhas no mesmo nível

Observação: A árvore 2-3-4 é uma B-tree de ordem 4, onde:
- Nó-2: 1 chave, 2 filhos
- Nó-3: 2 chaves, 3 filhos
- Nó-4: 3 chaves, 4 filhos
Inserção divide nós cheios (nó-4), promovendo a chave do meio ao pai.
"""

class Node234:
    def __init__(self, keys=None, children=None, leaf=True):
        """
        Nó da árvore 2-3-4.
        Atributos:
        - keys: lista ordenada de chaves do nó (1 a 3 chaves)
        - children: lista de referências para filhos (0 a 4 filhos)
        - leaf: booleano indicando se é folha
        Invariantes:
        - len(keys) entre 1 e 3 (exceto raiz temporariamente vazia na inicialização)
        - len(children) == len(keys) + 1 quando não-leaf
        """
        self.keys = keys if keys is not None else []
        self.children = children if children is not None else []
        self.leaf = leaf

    def is_full(self):
        """Retorna True se o nó for um nó-4 (3 chaves)."""
        return len(self.keys) == 3

    def __str__(self):
        """Representação textual do nó (apenas chaves)."""
        return f"Node(keys={self.keys}, leaf={self.leaf})"


class Tree234:
    def __init__(self):
        """
        Inicializa a árvore 2-3-4 com uma raiz folha (inicialmente vazia).
        A raiz pode começar sem chave; primeiro insert cria um nó-2.
        """
        self.root = Node234()

    def search(self, key, node=None):
        """
        Busca uma chave na árvore.
        Retorna (node, index) se encontrada; caso contrário, retorna None.
        """
        if node is None:
            node = self.root

        # Busca linear dentro do nó (lista de keys está ordenada)
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node, i
        elif node.leaf:
            return None
        else:
            return self.search(key, node.children[i])

    def split_child(self, parent, child_index):
        """
        Divide um filho cheio (nó-4) do 'parent' na posição child_index.
        Promove a chave do meio para o 'parent' e cria dois nós com as chaves laterais.
        Estrutura:
        - child.keys = [k0, k1, k2]
        - k1 sobe para o pai
        - filhos e chaves são repartidos adequadamente
        """
        child = parent.children[child_index]
        assert child.is_full(), "split_child deve receber um nó cheio"

        # Chaves a serem repartidas
        k0, k1, k2 = child.keys

        # Nós resultantes após divisão
        left = Node234(keys=[k0], leaf=child.leaf)
        right = Node234(keys=[k2], leaf=child.leaf)

        # Se o nó dividido não é folha, repartimos os filhos
        if not child.leaf:
            # child.children: 4 filhos -> repartimos 2/2
            left.children = child.children[:2]
            right.children = child.children[2:]
            left.leaf = False
            right.leaf = False

        # Inserir k1 no pai e ajustar filhos
        parent.keys.insert(child_index, k1)
        parent.children[child_index] = left
        parent.children.insert(child_index + 1, right)
        parent.leaf = False  # após uma split, definitivamente não é folha

    def insert(self, key):
        """
        Insere uma chave na árvore 2-3-4 com balanceamento automático.
        Passos:
        - Se a raiz estiver cheia, dividimos antes de descer.
        - Descemos sempre garantindo que o nó onde vamos inserir não esteja cheio
          (estratégia "split ao descer").
        - Inserimos na folha apropriada mantendo a lista 'keys' ordenada.
        Nota: Esta implementação não permite chaves duplicadas (política adotada).
        """
        # Política de duplicatas: ignorar inserção se já existe
        if self.search(key) is not None:
            return

        root = self.root
        # Se a raiz está cheia, criar nova raiz e dividir
        if root.is_full():
            new_root = Node234(keys=[], children=[root], leaf=False)
            self.split_child(new_root, 0)
            self.root = new_root

        # Agora, descer garantindo que não entraremos em nó cheio
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        """
        Insere uma chave em um nó que não está cheio.
        - Se 'node' é folha, inserimos na posição correta (mantendo ordenação).
        - Se não é folha, escolhemos o filho apropriado;
          se o filho estiver cheio, dividimos antes de descer.
        """
        i = len(node.keys) - 1

        if node.leaf:
            # Inserção ordenada em folha
            node.keys.append(key)
            node.keys.sort()
            return

        # Encontrar o filho correto para descer
        while i >= 0 and key < node.keys[i]:
            i -= 1
        child_index = i + 1

        # Se o filho alvo está cheio, dividir e decidir para qual lado descer
        if node.children[child_index].is_full():
            self.split_child(node, child_index)
            # Após split, decidir se a chave deve descer para a esquerda ou direita
            if key > node.keys[child_index]:
                child_index += 1

        self._insert_non_full(node.children[child_index], key)

    def inorder(self, node=None, out=None):
        """
        Percurso em-ordem (in-order) da árvore, retornando lista de chaves em ordem crescente.
        Para nós com múltiplas chaves, intercalamos filhos e chaves:
        filhos[0], keys[0], filhos[1], keys[1], filhos[2], keys[2], filhos[3]
        """
        if out is None:
            out = []
        if node is None:
            node = self.root

        if node.leaf:
            out.extend(node.keys)
            return out

        # Intercalar filhos e chaves (generalizado)
        for i, key in enumerate(node.keys):
            self.inorder(node.children[i], out)
            out.append(key)
        # Após última chave, visitar último filho
        self.inorder(node.children[len(node.keys)], out)
        return out

    def height(self):
        """
        Retorna a altura (níveis) da árvore: raiz no nível 1.
        Em 2-3-4 todas as folhas têm a mesma profundidade.
        """
        h = 0
        node = self.root
        while True:
            h += 1
            if node.leaf:
                break
            node = node.children[0]
        return h

    def print_structure(self, node=None, level=0):
        """
        Imprime a estrutura da árvore (níveis e chaves) para inspeção visual.
        Útil para apresentação e depuração.
        """
        if node is None:
            node = self.root
        indent = "  " * level
        print(f"{indent}- Nível {level+1}: {node.keys} {'(folha)' if node.leaf else ''}")
        if not node.leaf:
            for child in node.children:
                self.print_structure(child, level + 1)


# -------------------------------
# Teste com pelo menos 21 nós
# -------------------------------
if __name__ == "__main__":
    t234 = Tree234()

    # 21 valores (sem duplicatas) para testar inserção + balanceamento
    valores = [10, 20, 30, 15, 25, 5, 1, 50, 60, 70, 80, 90, 100,
               110, 120, 130, 140, 150, 160, 170, 180, 190]

    for v in valores:
        t234.insert(v)

    print("In-order (chaves em ordem crescente):")
    print(t234.inorder())

    print("\nAltura da árvore 2-3-4:")
    print(t234.height())

    print("\nEstrutura por níveis:")
    t234.print_structure()
    