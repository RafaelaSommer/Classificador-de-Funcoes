from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
#Funções de deletar dos botoes 
class Funcs():
    def limpar_tela(self):
        self.dominioa_entry.delete(0, END)
        self.contradomiob_entry.delete(0, END)
        self.combo_tipo.set("")
        self.lbl_resultado.config(text="", bg="white")

    def limpar_grafico(self):
        self.canvas.delete("all")
        self.resposta_correta = None
        self.lbl_resultado.config(text="", bg="white")
#logica matematica
    def calcular_classificacao(self, elementos_a, elementos_b, mapeamento):
        if len(mapeamento) != len(elementos_a):
            return "Não é função"

        contagem_b = {b: 0 for b in elementos_b}
        for destino in mapeamento.values():
            contagem_b[destino] += 1

        eh_injetora = all(qtd <= 1 for qtd in contagem_b.values())
        eh_sobrejetora = all(qtd >= 1 for qtd in contagem_b.values())

        if eh_injetora and eh_sobrejetora:
         return "Bijetora"
        elif eh_injetora:
         return "Injetora"
        elif eh_sobrejetora:
         return "Sobrejetora"
        else:
         return "Função Comum" 

       
#geração de exercicio aleatorio 
    def gerar_exercicio_aleatorio(self):
        qtd_a = random.choice([5, 5])
        qtd_b = random.choice([5, 5])

        elementos_a = [f"x{i+1}" for i in range(qtd_a)]
        elementos_b = [f"y{i+1}" for i in range(qtd_b)]

        self.dominioa_entry.delete(0, END)
        self.dominioa_entry.insert(0, ", ".join(elementos_a))
        
        self.contradomiob_entry.delete(0, END)
        self.contradomiob_entry.insert(0, ", ".join(elementos_b))

        self.combo_tipo.set("")
        self.lbl_resultado.config(text="Analise o gráfico e selecione a classificação.", fg="#333333", bg="white")

        tipo_geracao = random.choice(["funcao_valida", "funcao_valida", "invalida"])

        while True:
            mapeamento = {}
            if tipo_geracao == "funcao_valida":
                for a in elementos_a:
                    mapeamento[a] = random.choice(elementos_b)
            else:
                for a in elementos_a[:-1]:
                    mapeamento[a] = random.choice(elementos_b)

            classificacao = self.calcular_classificacao(elementos_a, elementos_b, mapeamento)
            break


        self.resposta_correta = classificacao
        self.desenhar_no_canvas(elementos_a, elementos_b, mapeamento)

#parte visual com canva e janelas de mensagens
    def gerar_diagramas(self):
        texto_a = self.dominioa_entry.get()
        texto_b = self.contradomiob_entry.get()

        elementos_a = [item.strip() for item in texto_a.split(",") if item.strip()]
        elementos_b = [item.strip() for item in texto_b.split(",") if item.strip()]

        if not elementos_a or not elementos_b:
            messagebox.showwarning("Aviso", "Digite os elementos de A e B separados por vírgula.")
            return

        mapeamento = {a: random.choice(elementos_b) for a in elementos_a}
        self.resposta_correta = self.calcular_classificacao(elementos_a, elementos_b, mapeamento)
        self.lbl_resultado.config(text="Diagramas gerados! Escolha a classificação e verifique.", fg="#333333", bg="white")

        self.desenhar_no_canvas(elementos_a, elementos_b, mapeamento)

    def desenhar_no_canvas(self, elementos_a, elementos_b, mapeamento=None):
        self.canvas.delete("all")
        self.canvas.update_idletasks()
        largura = self.canvas.winfo_width()
        altura = self.canvas.winfo_height()

        centro_x_a = largura * 0.25
        centro_x_b = largura * 0.75
        raio_x = largura * 0.15

        topo_y = altura * 0.14
        base_y = altura * 0.86

        self.canvas.create_text(centro_x_a, topo_y - 25, text="Domínio A", font=("Arial", 12, "bold"), fill="#1f2d3d")
        self.canvas.create_oval(
            centro_x_a - raio_x, topo_y,
            centro_x_a + raio_x, base_y,
            fill="#d6eaf8", outline="#5dade2", width=2
        )

        self.canvas.create_text(centro_x_b, topo_y - 25, text="Contradomínio B", font=("Arial", 12, "bold"), fill="#1f2d3d")
        self.canvas.create_oval(
            centro_x_b - raio_x, topo_y,
            centro_x_b + raio_x, base_y,
            fill="#d5f5e3", outline="#58d68d", width=2
        )

        coords_a = {}
        coords_b = {}
        raio_bolinha = 20

        espaco_a = (base_y - topo_y) / (len(elementos_a) + 1)
        for i, item in enumerate(elementos_a):
            y = topo_y + espaco_a * (i + 1)
            coords_a[item] = (centro_x_a, y)
            self.canvas.create_oval(
                centro_x_a - raio_bolinha, y - raio_bolinha,
                centro_x_a + raio_bolinha, y + raio_bolinha,
                fill="#ebf5fb", outline="#2e86c1", width=1.5
            )
            self.canvas.create_text(centro_x_a, y, text=item, font=("Arial", 10, "bold"), fill="#1b4f72")

        espaco_b = (base_y - topo_y) / (len(elementos_b) + 1)
        for i, item in enumerate(elementos_b):
            y = topo_y + espaco_b * (i + 1)
            coords_b[item] = (centro_x_b, y)
            self.canvas.create_oval(
                centro_x_b - raio_bolinha, y - raio_bolinha,
                centro_x_b + raio_bolinha, y + raio_bolinha,
                fill="#eafaf1", outline="#28b463", width=1.5
            )
            self.canvas.create_text(centro_x_b, y, text=item, font=("Arial", 10, "bold"), fill="#186a3b")

        if mapeamento:
            for origem, destino in mapeamento.items():
                if origem in coords_a and destino in coords_b:
                    x1, y1 = coords_a[origem]
                    x2, y2 = coords_b[destino]
                    self.canvas.create_line(
                        x1 + raio_bolinha, y1,
                        x2 - raio_bolinha, y2,
                        arrow=LAST,
                        arrowshape=(10, 12, 5),
                        width=2,
                        fill="#2c3e50"
                    )
    def verificar_resposta(self):
        if not hasattr(self, "resposta_correta") or self.resposta_correta is None:
            messagebox.showinfo("Aviso", "Clique em 'GERAR NOVA FUNÇÃO' primeiro para criar um diagrama.")
            return

        escolha_usuario = self.combo_tipo.get()
        if escolha_usuario == "":
            messagebox.showwarning("Aviso", "Selecione uma classificação na caixa antes de verificar.")
            return

        if escolha_usuario == self.resposta_correta:
            self.lbl_resultado.config(
                text="Resposta certa!",
                fg="#155724",
                bg="#d4edda"
            )
        else:
            # frame inferior resultado errado
            self.lbl_resultado.config(
                text=f"Incorreto! A resposta correta era: {self.resposta_correta}",
                fg="#721c24",
                bg="#f8d7da"
            )
            
            #janela pequena de incorreto
            messagebox.showerror(
                "Resposta Incorreta",
                f"Você errou!\nA resposta correta era: {self.resposta_correta}.\n\nClique em OK para gerar uma nova função aleatória."
            )
            
            # geração aleatoria quaando fecha 
            self.gerar_exercicio_aleatorio()


#configurações da janela maior e botoes tamanho e design
class Application(Funcs):
    def __init__(self):
        self.root = root
        self.resposta_correta = None
        self.configuracoes_da_tela()
        self.frames_da_tela() 
        self.criando_botoes()
        self.widgets_laterais()
        root.mainloop()

    def configuracoes_da_tela(self):
        self.root.title("Classificador de Funções")
        self.root.configure(background="lightblue")
        self.root.geometry("850x720")
        self.root.resizable(True, True)

    def frames_da_tela(self):
        self.frame_1 = Frame(
            self.root, 
            bd=4, 
            bg="white",
            highlightbackground="black", 
            highlightthickness=3
        )
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.60, relheight=0.72)

        self.canvas = Canvas(self.frame_1, bg="white", highlightthickness=0)
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.frame_resultado = Frame(
            self.root,
            bd=2,
            bg="white",
            highlightbackground="black",
            highlightthickness=3
        )
        self.frame_resultado.place(relx=0.02, rely=0.77, relwidth=0.60, relheight=0.18)

        self.lbl_resultado = Label(
            self.frame_resultado,
            text="Clique em 'GERAR NOVA FUNÇÃO' para começar", bg="white", fg="#333333", font=("Arial", 13, "bold"), wraplength=480)
        self.lbl_resultado.place(relx=0, rely=0, relwidth=1, relheight=1)

    def criando_botoes(self):
        self.borda_limpar = Frame(self.frame_1, bg="black", padx=2, pady=2)
        self.borda_limpar.place(relx=0.98, rely=0.98, relwidth=0.15, relheight=0.08, anchor="se")
        self.bt_limpar = Button(self.borda_limpar, text="LIMPAR", bd=3, bg="#f0f0f0", activebackground="#d9d9d9", command=self.limpar_grafico)
        self.bt_limpar.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.borda_limpar.lift()

    def widgets_laterais(self):
        self.lb_dominioa = Label(
            self.root, text="Domínio (A):", bg="lightblue", font=("Arial", 10, "bold"))
        self.lb_dominioa.place(relx=0.65, rely=0.02)
        self.dominioa_entry = Entry(self.root, bd=2, relief="solid")
        self.dominioa_entry.place(relx=0.65, rely=0.06, relwidth=0.32, relheight=0.04)
        
        self.lb_contradomiob = Label(
            self.root, text="Contradomínio (B):", bg="lightblue", font=("Arial", 10, "bold"))
        self.lb_contradomiob.place(relx=0.65, rely=0.14)
        self.contradomiob_entry = Entry(self.root, bd=2, relief="solid")
        self.contradomiob_entry.place(relx=0.65, rely=0.18, relwidth=0.32, relheight=0.04)
        
        self.borda_aleatorio = Frame(self.root, bg="black", padx=2, pady=2)
        self.borda_aleatorio.place(relx=0.65, rely=0.26, relwidth=0.32, relheight=0.06)
        self.bt_aleatorio = Button(self.borda_aleatorio, text="GERAR NOVA FUNÇÃO", bd=3, bg="#fcf3cf", activebackground="#f9e79f", font=("Arial", 9, "bold"), command=self.gerar_exercicio_aleatorio)
        self.bt_aleatorio.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.borda_limpar_campos = Frame(self.root, bg="black", padx=2, pady=2)
        self.borda_limpar_campos.place(relx=0.65, rely=0.35, relwidth=0.32, relheight=0.05)
        self.bt_limpar_campos = Button(self.borda_limpar_campos,text="DELETAR CAMPOS", bd=3, bg="#f0f0f0", activebackground="#d9d9d9", command=self.limpar_tela)
        self.bt_limpar_campos.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.lb_tipo = Label(self.root, text="Sua resposta:", bg="lightblue", font=("Arial", 10, "bold"))
        self.lb_tipo.place(relx=0.65, rely=0.45)
        self.combo_tipo = ttk.Combobox(
            self.root, 
            values=["Injetora", "Sobrejetora", "Bijetora", "Não é função", "Função Comum"], 
            state="readonly", 
            font=("Arial", 10)
        )

        self.combo_tipo.place(relx=0.65, rely=0.49, relwidth=0.32, relheight=0.04)
        self.borda_verificar = Frame(self.root, bg="black", padx=2, pady=2)
        self.borda_verificar.place(relx=0.65, rely=0.57, relwidth=0.32, relheight=0.06)
        self.bt_verificar = Button(self.borda_verificar, text="VERIFICAR RESPOSTA", bd=3, bg="#d4edda", activebackground="#c3e6cb", font=("Arial", 10, "bold"), command=self.verificar_resposta)
        self.bt_verificar.place(relx=0, rely=0, relwidth=1, relheight=1)
                             


root = Tk()
Application()