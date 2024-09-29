<h1 align="center">Python Challenge</h1>
<h2 align="center">Entrega da disciplina de Computational Thinking With Python</h2>
<div align="center" width="100px">

![image](https://github.com/Leandrns/python-challenge/assets/162051430/704013e4-e8d1-4782-ac57-2ac59443731b)


![image](https://github.com/Leandrns/python-challenge/assets/162051430/d646bbf7-64d9-4386-b640-1a82c17746a5)


</div>

## Tecnologias
<a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,pycharm" />
</a>

## Integrantes:
<p>Caio Alexandre dos Santos - RM: 558460</p>
<p>Leandro do Nascimento Souza - RM: 558893</p>
<p>Italo Caliari Silva - RM: 554758</p>
<p>Rafael de Mônaco Maniezo - RM: 556079</p>
<p>Vinicius Rozas Pannuci de Paula Cont - RM: 555338</p>

## Sobre o projeto
O grupo CLIRV Technologies em nome da empresa Tech Mahindra, em parceria com a FIAP desafiou os alunos do primeiro ano de Engenharia de Software a popularizar a Fórmula E.<br> 
E nossa solução foi desenvolver um site com uma interface rica em informações sobre a corrida, incluindo notícias, curiosidades, estatísticas, regras, circuitos e um calendário de corridas. O diferencial do site será um sistema gamificado, o "HitRace Fantasy FE", onde os usuários podem montar suas equipes com base em um sistema de compra com moedas fictícias e ganhar pontos conforme o desempenho real dos pilotos, motores, equipes e técnicos escolhidos.

## Funcionalidades
- Sistema de escalação da sua equipe, possuindo a seguinte estrutura: nome da equipe; piloto 1; piloto 2; equipes da corrida; motores; e técnicos; 

- O usuário pode escolher dentro de cada tópico algumas opções váriadas, descontando a quantidade de créditos referente a cada escolha;

- No final de cada experiência é demonstrado o ranking e o saldo restante e todas as escolhas do usuário.
 

## Requisitos
- É necessário o Python instalado em seu sistema. Você pode baixá-lo [aqui](https://www.python.org/downloads/)

- O sistema da plataforma do projeto foi desenvolvida no arquivo main.py na linguagem de programação Python, sendo executado diretamente no terminal.
  
- São usadas as seguintes bibliotecas:

<p><b>random</b>: Para criar eventos aleatórios durante o jogo, como definir resultados de corridas (não precisa instalar)</p>

<p><b>Matplotlib</b>: Para visualizar as estatísticas de desempenho dos usuários após algumas corridas.</p>

<p><b>Pandas:</b> Para armazenar e manipular dados sobre os pilotos, equipes e pontuações, permitindo uma análise mais fácil e organizada.</p>

<p><b>time:</b> Para criar delays na execução do jogo, aumentando a imersão e a expectativa dos jogadores. (não precisa instalar)</p>

<p><b>Colorama:</b> Para adicionar estilizações aos textos apresentados no terminal, melhorando a experiência do usuário.</p>

<p>Obs.: Todas as bibliotecas podem ser instaladas dentro do PyCharm através da aba 'Python Packages'.</p>


## Conhecimentos utilizados

- Foram utilizadas os conhecimentos básicos de Python: variáveis, fStrings, condicionais e estruturas de repetição;

- Manipulação de listas e strings: pilotos, equipes, motores, técnicos e créditos respectivamente;

- Funções: Forçar a opção do usuário, Uso dicionarios, verificar se o usuário tem saldo ou não.  

## Instruções de uso

### Criando uma equipe
<p>O usuário receberá uma mensagem de boas-vindas ao jogo e depois deverá inserir o nome da sua equipe.</p>

### Créditos
<p>O usuário recebe após se cadastrar no jogo 100 créditos para montar a sua equipe.<p>
<p>Caso o usuário escolha algum componente para sua equipe sem ter os créditos necessários para comprar, a escolha será invalidada e o sistema pedirá novamente até que o usuário faça uma escolha que seja válida.</p>

### Escolhendo pilotos
<p>Estarão disponíveis três pilotos com suas respectivas equipes e preços:</p>

- <p>Mitch EVANS, da Jaguar - 17 créditos</p>
- <p>Antônio Felix DA COSTA, da Porsche - 14 créditos</p>
- <p>Nyck DE VRIES, da Mahindra - 9 créditos</p>

<p>O usuário deverá escolher dois pilotos</p>
<p>Ao final das escolhas, aparecerá o saldo de créditos</p>

### Escolhendo equipe
<p>Estarão disponíveis cinco equipes de Formula E com seus respectivos preços:</p>

- <p>Porsche - 17 créditos</p>
- <p>Jaguar - 15 créditos</p>
- <p>Mahindra - 13 créditos</p>
- <p>Maserati - 12 créditos</p>
- <p>McLaren - 13 créditos</p>
<p>O usuário deverá escolher uma equipe</p>
<p>Após escolher a equipe, aparecerá o nome da equipe escolhida e o saldo de créditos</p>

### Escolhendo motor
<p>Estarão disponíveis três motores de Formula E com seus respectivos preços:</p>

- <p>Porsche 99X Electric - 17 créditos</p>
- <p>Mahindra M9Electro - 11 créditos</p>
- <p>Jaguar I-Type 6 - 16 créditos</p>

<p>O usuário deverá escolher um motor</p>
<p>Após escolher o motor, aparecerá o motor escolhido e o saldo de créditos</p>

### Escolhendo o Técnico da equipe
<p>Estarão disponíveis três técnicos de equipe com seus respectivos preços:</p>

- <p>Thomas Biermaier, da ABT - 11 créditos</p>
- <p>Frederic Bertrand, da Mahindra - 12 créditos</p>
- <p>Florian Modlinger, da Porsche - 18 créditos</p>
<p>O usuário deverá escolher um técnico de equipe</p>
<p>Após a escolha, aparecerá o técnico de equipe escolhido e o saldo de créditos</p>

### Equipe

<p>Após o usuário montar a sua equipe, ele poderá conferir suas escolhas.</p>

### Sistema de Pontuação do Ranking

<p>Como Funciona a Pontuação</p>

- <p>O sistema de pontuação premia os usuários com base no desempenho real dos pilotos, equipes e técnicos escolhidos. A pontuação é atribuída em diferentes categorias, refletindo eventos que ocorrem durante as corridas da Fórmula E.</p>
<b>OBS.:</b> O código atual gera uma pontuação aleatória para cada escolha, usando a lib random, porém, em futuras versões, essa atribuição de pontos deve ser feita da seguinte maneira: 

<p>Categorias de Pontuação</p>

<p>1. Pilotos:</p>

- <p>Posição de Chegada:</p>

- <p>1º lugar: 25 pontos</p>

- <p>2º lugar: 18 pontos</p>

- <p>3º lugar: 15 pontos</p>

- <p>4º lugar: 12 pontos</p>

- <p>5º lugar: 10 pontos</p>

- <p>6º a 10º lugar: 5 pontos</p>

- <p>11º a 20º lugar: 2 pontos</p>

<p>2. Equipes:</p>

- <p>Posição de Chegada da Equipe: Pontos atribuídos da mesma forma que para os pilotos.</p>
- <p>Desempenho Geral (número total de pontos dos pilotos da equipe): Bônus de 10 pontos se ambos os pilotos terminarem entre os 10 primeiros.</p>

<p>Técnicos:</p>

- <p>Desempenho da Equipe: Os pontos são calculados com base no desempenho da equipe, com uma bonificação de 5 pontos se a equipe terminar entre os 5 primeiros.</p>

<p>Exemplo de Cálculo de Pontuação</p>

- <p> O usuário montou uma equipe:</p>

- <p>Piloto 1: Mitch EVANS (1º lugar)</p>

- <p>Piloto 2: Antônio Felix DA COSTA (5º lugar)</p>

- <p>Equipe: Porsche (3ª posição)</p>

- <p>Técnico: Thomas Biermaier</p>

- <p>A pontuação total será calculada:</p>

- <p>Piloto 1 (Mitch EVANS): 25 pontos (1º lugar) + 2 pontos (participação) = 27 pontos</p>

- <p>Piloto 2 (Antônio Felix DA COSTA): 10 pontos (5º lugar) + 2 pontos (participação) = 12 pontos</p>

- <p>Equipe (Porsche): 15 pontos (3ª posição) + 10 pontos (bônus) = 25 pontos</p>

- <p>Técnico (Thomas Biermaier): 5 pontos (desempenho da equipe)</p>

- <p>Pontuação Total: 27 + 12 + 25 + 5 = 69 pontos</p>

- <p>Exibição da Pontuação</p>

<p>Após a corrida, o usuário poderá visualizar seu total de pontos acumulados e um ranking que compara seu desempenho com outros usuários do "HitRace Fantasy FE". Essa comparação incentiva a otimização das escolhas e estratégias a cada corrida.</p>

### Diagrama em blocos do funcionamento

![diagrama_python_pt1](https://github.com/user-attachments/assets/893a6956-e3f2-44ca-afb3-19477cb28090)
![diagrama_python_pt2](https://github.com/user-attachments/assets/496b9709-353f-4f24-8d09-02fe7bc71977)

