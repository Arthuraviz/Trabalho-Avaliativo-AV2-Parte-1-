# Árvores Balanceadas em Python: Rubro-Negra, 2-3-4 e k-D

Este repositório contém a implementação das árvores Rubro-Negra e 2-3-4 em Python, além de uma explicação teórica da árvore k-d. O objetivo é comparar diferentes estratégias de balanceamento e analisar seus resultados.

##  Conteúdo
- Implementação da Árvore Rubro-Negra
- Implementação da Árvore 2-3-4
- Explicação teórica da Árvore k-d
- Testes com 21 nós
- Comparação de resultados

##  Resultados

### Árvore 2-3-4
- In-order: [1, 5, 10, 15, 20, 25, 30, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
- Altura: 4
- Estrutura por níveis:
  - Nível 1: [60]
  - Nível 2: [20], [100, 140]
  - Nível 3: [10], [30], [80], [120], [160]
  - Nível 4: folhas [1, 5], [15], [25], [50], [70], [90], [110], [130], [150], [170, 180, 190]

### Árvore Rubro-Negra
- In-order (com cores):  
  1 (RED), 5 (BLACK), 10 (BLACK), 15 (BLACK), 20 (RED), 25 (BLACK), 30 (BLACK), 50 (BLACK), 60 (BLACK), 70 (BLACK), 80 (BLACK), 90 (BLACK), 100 (RED), 110 (BLACK), 120 (RED), 130 (BLACK), 140 (BLACK), 150 (BLACK), 160 (RED), 170 (RED), 180 (BLACK), 190 (RED)
- Altura: ~5

##  Comparação

| Característica       | Rubro-Negra                  | 2-3-4                        | k-d                          |
|----------------------|------------------------------|------------------------------|------------------------------|
| Tipo de divisão      | Binária (2 filhos)           | Até 4 filhos por nó          | Binária, alternando eixos    |
| Balanceamento        | Rotações + cores             | Splits e promoção de chaves  | Divisão por coordenadas      |
| Altura (teste 21 nós)| ~5                           | 4                            | Depende dos pontos           |
| Aplicações           | Bibliotecas padrão, sistemas | Bancos de dados, didática    | Busca espacial, IA           |


##  Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/arvores-balanceadas.git

   cd arvores-balanceadas

    python rubro_negra.py
    python arvore_234.py

    python rubro_negra.py
    python arvore_234.py


---

## 6. **Referências**
```markdown
## Referências
- UFSC – Estruturas de Dados: Árvore k-d. https://www.inf.ufsc.br/~aldo.vw/estruturas/k-d/arvore-kd.html
- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. *Introduction to Algorithms*. MIT Press.
- Material da disciplina de Teoria dos grafos – Universidade.