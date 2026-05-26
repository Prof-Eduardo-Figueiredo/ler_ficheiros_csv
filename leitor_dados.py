import tkinter as tk
from tkinter import ttk
import csv

class AplicacaoDados:
    def __init__(self, root, arquivo_csv):
        self.root = root
        self.root.title("Leitor de Dados")
        self.root.geometry("400x300")
        
        # Carregar dados do CSV
        self.dados = []
        self.carregar_dados(arquivo_csv)
        self.indice_atual = 0
        
        # Criar widgets
        self.criar_interface()
        self.atualizar_exibicao()
    
    def carregar_dados(self, arquivo_csv):
        """Carrega os dados do arquivo CSV"""
        try:
            with open(arquivo_csv, 'r', encoding='utf-8') as f:
                leitor = csv.reader(f, delimiter=';')
                for linha in leitor:
                    if len(linha) == 4:
                        self.dados.append({
                            'id': linha[0],
                            'nome': linha[1],
                            'idade': linha[2],
                            'telefone': linha[3]
                        })
        except FileNotFoundError:
            print(f"Arquivo {arquivo_csv} não encontrado!")
    
    def criar_interface(self):
        """Cria a interface gráfica"""
        
        # Frame principal
        frame_principal = ttk.Frame(self.root, padding="10")
        frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Label e Entry para ID
        ttk.Label(frame_principal, text="ID:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_id = ttk.Entry(frame_principal, width=30)
        self.entry_id.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        self.entry_id.config(state='readonly')
        
        # Label e Entry para Nome
        ttk.Label(frame_principal, text="Nome:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_nome = ttk.Entry(frame_principal, width=30)
        self.entry_nome.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        self.entry_nome.config(state='readonly')
        
        # Label e Entry para Idade
        ttk.Label(frame_principal, text="Idade:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_idade = ttk.Entry(frame_principal, width=30)
        self.entry_idade.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        self.entry_idade.config(state='readonly')
        
        # Label e Entry para Telefone
        ttk.Label(frame_principal, text="Telefone:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entry_telefone = ttk.Entry(frame_principal, width=30)
        self.entry_telefone.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        self.entry_telefone.config(state='readonly')
        
        # Frame para botões
        frame_botoes = ttk.Frame(frame_principal)
        frame_botoes.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Botão Anterior
        self.btn_anterior = ttk.Button(frame_botoes, text="← Anterior", command=self.anterior)
        self.btn_anterior.pack(side=tk.LEFT, padx=10)
        
        # Label de posição
        self.label_posicao = ttk.Label(frame_botoes, text="")
        self.label_posicao.pack(side=tk.LEFT, padx=20)
        
        # Botão Seguinte
        self.btn_seguinte = ttk.Button(frame_botoes, text="Seguinte →", command=self.seguinte)
        self.btn_seguinte.pack(side=tk.LEFT, padx=10)
    
    def atualizar_exibicao(self):
        """Atualiza a exibição dos dados"""
        if self.dados:
            dado = self.dados[self.indice_atual]
            
            # Atualizar entries (com estado normal temporariamente)
            self.entry_id.config(state='normal')
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, dado['id'])
            self.entry_id.config(state='readonly')
            
            self.entry_nome.config(state='normal')
            self.entry_nome.delete(0, tk.END)
            self.entry_nome.insert(0, dado['nome'])
            self.entry_nome.config(state='readonly')
            
            self.entry_idade.config(state='normal')
            self.entry_idade.delete(0, tk.END)
            self.entry_idade.insert(0, dado['idade'])
            self.entry_idade.config(state='readonly')
            
            self.entry_telefone.config(state='normal')
            self.entry_telefone.delete(0, tk.END)
            self.entry_telefone.insert(0, dado['telefone'])
            self.entry_telefone.config(state='readonly')
            
            # Atualizar label de posição
            self.label_posicao.config(text=f"{self.indice_atual + 1}/{len(self.dados)}")
            
            # Desabilitar botões conforme necessário
            self.btn_anterior.config(state='normal' if self.indice_atual > 0 else 'disabled')
            self.btn_seguinte.config(state='normal' if self.indice_atual < len(self.dados) - 1 else 'disabled')
    
    def anterior(self):
        """Mostra o registo anterior"""
        if self.indice_atual > 0:
            self.indice_atual -= 1
            self.atualizar_exibicao()
    
    def seguinte(self):
        """Mostra o registo seguinte"""
        if self.indice_atual < len(self.dados) - 1:
            self.indice_atual += 1
            self.atualizar_exibicao()

# Executar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoDados(root, "dados.csv")
    root.mainloop()
