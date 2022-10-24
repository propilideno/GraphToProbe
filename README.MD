# Transforma uma Topologia de Rede em um histograma de Overhead com alguns tipos de Source Routing.
#### Links úteis: http://www.topology-zoo.org/dataset.html
## _Modo de usar: Baixe as topologias desejadas em .GML no site do topology-zoo e coloque dentro do diretório: topologyZoo, que automaticamente ele irá ler as topologias e gerar a matriz de sondas e o overhead._

## Bibliotecas usadas:
- [matplotlib] - Usado para plotar gráficos
- [seaborn] - Usado para plotar e visualizar gŕaficos.
- [pandas] - Usado para manipular e visualizar bancos de dados.
- [requests] - Usado para hookar as topologias do topologyZoo 
- [html5lib] - Usado para hookar as topologias do topologyZoo 

## Instalação de Dependências
```sh
pip3 install --upgrade pip
pip3 install pandas, seaborn, matplotlib, requests
```

## Caso esteja usando Windows:
Para setar as variáveis de ambiente...
```sh
- Enviroment Variables:
    Add to PATH:
    C:\Users\<YOUR_USERNAME>\AppData\Local\Programs\Python\Python310
    C:\Users\<YOUR_USERNAME>\AppData\Local\Programs\Python\Python310\Scripts
- New System Variable:
    Name: PYTHONUTF8
    Value: 1
```