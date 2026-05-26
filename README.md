# Leitor de Dados CSV

Aplicação Python com interface gráfica para visualizar dados de arquivo CSV com navegação entre registos.

## 📋 Funcionalidades

- ✅ Leitura de ficheiro CSV com separador `;`
- ✅ Interface gráfica com 4 campos (ID, Nome, Idade, Telefone)
- ✅ Navegação entre registos com botões "Anterior" e "Seguinte"
- ✅ Indicador de posição (ex: 1/3)
- ✅ Campos de somente leitura
- ✅ Botões desabilitados nas extremidades

## 🚀 Como Utilizar

### Requisitos
- Python 3.6 ou superior
- `tkinter` (incluído na maioria das instalações de Python)

### Execução

1. Clone o repositório:
```bash
git clone https://github.com/Prof-Eduardo-Figueiredo/Leitor-dados-csv.git
cd Leitor-dados-csv
```

2. Execute o programa:
```bash
python leitor_dados.py
```

## 📄 Formato do Ficheiro CSV

O ficheiro `dados.csv` deve ter o seguinte formato:

```
ID;Nome;Idade;Telefone
99;Eduardo Figueiredo;50;986445332
87;Ana Sousa;67;999555333
37;Rui Lopes;23;913555444
```

**Separador**: Ponto e vírgula (`;`)  
**Campos**: ID, Nome, Idade, Telefone

## 🔧 Personalização

Pode editar o ficheiro `dados.csv` com um editor de texto e adicionar novos registos seguindo o formato acima.

## 📝 Estrutura do Projeto

```
Leitor-dados-csv/
├── leitor_dados.py    # Programa principal
├── dados.csv          # Ficheiro de dados
└── README.md          # Este ficheiro
```

## 📚 Tecnologias Utilizadas

- **Python 3** - Linguagem de programação
- **Tkinter** - Biblioteca para interface gráfica
- **CSV** - Formato de ficheiro de dados

## 👨‍💻 Autor

Prof. Eduardo Figueiredo

## 📄 Licença

Este projeto está disponível sob licença MIT.
