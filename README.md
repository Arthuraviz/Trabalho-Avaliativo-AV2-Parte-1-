Árvores Balanceadas em Python (Jupyter Notebook)

Este repositório contém a implementação das árvores Rubro-Negra e 2-3-4 (B-tree de ordem 4) em Python, desenvolvidas e testadas em formato Jupyter Notebook (.ipynb).
O projeto inclui não apenas as operações clássicas (inserção, busca, percurso), mas também visualizações gráficas geradas com Matplotlib para facilitar a compreensão da estrutura das árvores.

------------------------------------------------------------
Conteúdo
------------------------------------------------------------
- Implementação da Árvore Rubro-Negra
- Implementação da Árvore 2-3-4
- Explicação teórica da Árvore k-d
- Testes com 21 nós
- Comparação de resultados
- Visualização gráfica com Matplotlib

------------------------------------------------------------
Como executar
------------------------------------------------------------
1. Clone este repositório:
   git clone https://github.com/seu-usuario/arvores-balanceadas.git

2. Entre na pasta:
   cd arvores-balanceadas

3. Abra o notebook no Jupyter:
   jupyter notebook arvores_balanceadas.ipynb

4. Execute célula por célula para ver:
   - Inserções e percursos
   - Estrutura textual por níveis
   - Gráficos gerados com Matplotlib

------------------------------------------------------------
Resultados
------------------------------------------------------------
Árvore 2-3-4
- In-order: [1, 5, 10, 15, 20, 25, 30, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
- Altura: 4
- Estrutura por níveis exibida no notebook
- Visualização gráfica (Matplotlib): imagens/arvore_234.png

Árvore Rubro-Negra
- In-order (com cores): 1 (RED), 5 (BLACK), 10 (BLACK), 15 (BLACK), 20 (RED), ... 190 (RED)
- Altura: ~5
- Visualização gráfica (Matplotlib): imagens/rubro_negra.png

------------------------------------------------------------
Comparação
------------------------------------------------------------
Característica       | Rubro-Negra                  | 2-3-4                        | k-d
---------------------|------------------------------|------------------------------|------------------------------
Tipo de divisão      | Binária (2 filhos)           | Até 4 filhos por nó          | Binária, alternando eixos
Balanceamento        | Rotações + cores             | Splits e promoção de chaves  | Divisão por coordenadas
Altura (teste 21 nós)| ~5                           | 4                            | Depende dos pontos
Aplicações           | Bibliotecas padrão, sistemas | Bancos de dados, didática    | Busca espacial, IA

------------------------------------------------------------
Referências
------------------------------------------------------------
- UFSC – Estruturas de Dados: Árvore k-d
- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. Introduction to Algorithms. MIT Press.
- Material da disciplina de Estruturas de Dados – Universidade