# Classificador de Funções

## Sobre o projeto

O **Classificador de Funções** é uma aplicação desktop desenvolvida em
Python com a biblioteca Tkinter. Seu objetivo é auxiliar no estudo de
funções matemáticas por meio de diagramas que representam as relações
entre os elementos de dois conjuntos: o domínio (A) e o contradomínio
(B).

O usuário pode gerar exercícios aleatórios, visualizar as
correspondências entre os conjuntos, selecionar uma classificação e
verificar se sua resposta está correta.

## Funcionalidades

-   **Gerar nova função:** cria automaticamente um exercício com
    elementos nos conjuntos A e B e apresenta o diagrama correspondente.
-   **Classificação da função:** permite escolher entre Injetora,
    Sobrejetora, Bijetora, Função Comum e Não é função.
-   **Verificar resposta:** compara a classificação escolhida pelo
    usuário com o resultado calculado pelo programa.
-   **Feedback:** informa quando a resposta está correta ou incorreta.
    Em caso de erro, apresenta a classificação correta e gera um novo
    exercício.
-   **Limpar gráfico:** apaga o diagrama exibido e reinicia o estado da
    resposta.
-   **Deletar campos:** limpa os campos de domínio e contradomínio e
    remove a seleção de classificação.

## Tecnologias utilizadas

-   **Python 3:** linguagem de programação utilizada no desenvolvimento.
-   **Tkinter:** biblioteca utilizada para criar a interface gráfica.
-   **ttk:** componente do Tkinter utilizado para a caixa de seleção de
    respostas.
-   **random:** módulo utilizado para gerar elementos e correspondências
    aleatórias.

As bibliotecas utilizadas fazem parte da distribuição padrão do Python,
portanto não é necessário instalar pacotes externos para executar o
programa em uma instalação comum do Python com suporte ao Tkinter.

## Como executar

### 1. Verifique a instalação do Python

Tenha o Python 3 instalado no computador.

Para verificar, abra o terminal e execute:

``` bash
python --version
```

Em alguns sistemas, pode ser necessário utilizar:

``` bash
python3 --version
```

### 2. Baixe o projeto

Salve o arquivo Python do projeto em uma pasta do computador.

### 3. Execute a aplicação

No terminal, acesse a pasta em que o arquivo está salvo e execute:

``` bash
python codigodoclassificadorthiago.py
```

Se necessário, utilize `python3` no lugar de `python`.

A janela do Classificador de Funções será aberta.

## Como utilizar

1.  Clique em **GERAR NOVA FUNÇÃO** para criar um exercício aleatório.
2.  Observe o diagrama apresentado na área principal da janela.
3.  Analise as setas que ligam os elementos do domínio A aos elementos
    do contradomínio B.
4.  Selecione a classificação que considera correta no campo **Sua
    resposta**.
5.  Clique em **VERIFICAR RESPOSTA**.
6.  Leia o resultado apresentado na tela.
7.  Em caso de resposta incorreta, o programa informa a classificação
    correta e gera outro exercício.

O botão **LIMPAR** apaga o gráfico. Já o botão **DELETAR CAMPOS** limpa
os campos de entrada e a seleção da classificação.

## Classificações matemáticas

O programa utiliza a quantidade de correspondências que chegam a cada
elemento do contradomínio para classificar a função.

### Função injetora

Uma função é injetora quando elementos diferentes do domínio possuem
imagens diferentes. Isso significa que cada elemento do contradomínio
recebe, no máximo, uma seta.

### Função sobrejetora

Uma função é sobrejetora quando todos os elementos do contradomínio
recebem pelo menos uma seta, ou seja, todos possuem uma imagem
correspondente.

### Função bijetora

Uma função é bijetora quando é simultaneamente injetora e sobrejetora.
Cada elemento do contradomínio recebe exatamente uma seta.

### Função comum

No código, essa classificação é utilizada quando a função não atende às
condições de injetividade nem de sobrejetividade.

### Não é função

O programa utiliza essa classificação quando a quantidade de elementos
mapeados não corresponde à quantidade de elementos do domínio. No
exercício aleatório, isso acontece quando um dos elementos de A fica sem
correspondência.

## Organização do código

O código está organizado principalmente em duas classes:

### Classe `Funcs`

Reúne as funções responsáveis pela lógica e pelas operações da
aplicação:

-   `limpar_tela()`: limpa os campos de entrada e a seleção.
-   `limpar_grafico()`: apaga o desenho do diagrama.
-   `calcular_classificacao()`: analisa o mapeamento e determina a
    classificação.
-   `gerar_exercicio_aleatorio()`: cria exercícios com elementos e
    correspondências aleatórias.
-   `gerar_diagramas()`: obtém os elementos digitados nos campos e cria
    um mapeamento.
-   `desenhar_no_canvas()`: desenha os conjuntos, seus elementos e as
    setas.
-   `verificar_resposta()`: verifica a escolha do usuário e apresenta o
    resultado.

### Classe `Application`

Responsável pela criação e configuração da interface gráfica:

-   `__init__()`: inicializa a aplicação e seus componentes.
-   `configuracoes_da_tela()`: define o título, o tamanho e o plano de
    fundo da janela.
-   `frames_da_tela()`: cria as áreas principais da interface.
-   `criando_botoes()`: cria o botão para limpar o gráfico.
-   `widgets_laterais()`: cria os campos de entrada, a caixa de
    classificação e os botões de interação.

## Lógica de classificação

O método `calcular_classificacao()` segue esta sequência:

1.  Verifica se todos os elementos do domínio possuem correspondência.
2.  Conta quantas vezes cada elemento do contradomínio aparece como
    destino.
3.  Verifica se cada elemento do contradomínio recebe no máximo uma
    correspondência.
4.  Verifica se todos os elementos do contradomínio recebem pelo menos
    uma correspondência.
5.  Com base nessas condições, retorna a classificação da função.

## Observações sobre a implementação

-   Os exercícios aleatórios utilizam cinco elementos no domínio e cinco
    no contradomínio.
-   O programa escolhe aleatoriamente entre gerar um mapeamento completo
    e um mapeamento incompleto.
-   O mapeamento completo pode apresentar diferentes classificações
    conforme as correspondências geradas.
-   A função `gerar_diagramas()` está definida no código para trabalhar
    com elementos informados pelo usuário, mas não está conectada a um
    botão na interface apresentada.
-   O código utiliza a janela principal do Tkinter para iniciar a
    aplicação.

## Objetivo educacional

O projeto busca tornar o estudo das classificações de funções mais
visual e interativo. Por meio dos diagramas e dos exercícios aleatórios,
o estudante pode observar as relações entre domínio e contradomínio,
testar seus conhecimentos e receber retorno imediato sobre suas
respostas.

------------------------------------------------------------------------

**Projeto:** Classificador de Funções\
**Linguagem:** Python 3\
**Interface gráfica:** Tkinter
