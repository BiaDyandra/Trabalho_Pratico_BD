import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# --- CONFIGURAÇÕES DO BANCO ---
HOST = "localhost"
USER = "root"
PASSWORD = ""  # <--- VERIFIQUE SUA SENHA
DATABASE = "clinica_vet_db"

# --- PALETA DE CORES (Baseada na Logo) ---
COLOR_PRIMARY = "#004aad"     # Azul Escuro
COLOR_ACCENT = "#ffc107"      # Amarelo/Dourado
COLOR_BG_MAIN = "#f0f2f5"     # Cinza Fundo
COLOR_WHITE = "#ffffff"
COLOR_TEXT = "#333333"

class SistemaVet:
    def __init__(self):
        self.conn = None
        self.conectar_banco()
        
        # Janela Login
        self.login_window = tk.Tk()
        self.login_window.title("Login - VetSys")
        self.login_window.geometry("360x480")
        self.login_window.configure(bg=COLOR_BG_MAIN)
        self.login_window.resizable(False, False)
        
        self.montar_tela_login()
        self.login_window.mainloop()

    def conectar_banco(self):
        try:
            self.conn = mysql.connector.connect(
                host=HOST, user=USER, password=PASSWORD, database=DATABASE
            )
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de Conexão", f"{err}")

    def carregar_logo(self, scale=3):
        try:
            img = tk.PhotoImage(file="hin.png")
            return img.subsample(scale, scale)
        except:
            return None

    # ==========================
    # TELA DE LOGIN
    # ==========================
    def montar_tela_login(self):
        self.login_window.bind('<Return>', lambda e: self.verificar_login())
        card = tk.Frame(self.login_window, bg=COLOR_WHITE, padx=30, pady=40)
        card.place(relx=0.5, rely=0.5, anchor="center", width=300)
        
        self.img_logo_login = self.carregar_logo(scale=4)
        if self.img_logo_login:
            tk.Label(card, image=self.img_logo_login, bg=COLOR_WHITE).pack(pady=(0, 15))
        else:
            tk.Label(card, text="VetSys", font=("Arial", 22, "bold"), fg=COLOR_PRIMARY, bg=COLOR_WHITE).pack(pady=10)

        tk.Label(card, text="Acesso ao Sistema", font=("Arial", 10), fg="#666", bg=COLOR_WHITE).pack(pady=(0, 20))

        tk.Label(card, text="Usuário", bg=COLOR_WHITE, anchor="w", font=("Arial", 9, "bold")).pack(fill="x")
        self.entry_user = tk.Entry(card, font=("Arial", 11), bd=1, relief="solid")
        self.entry_user.pack(fill="x", pady=(5, 15), ipady=3)

        tk.Label(card, text="Senha", bg=COLOR_WHITE, anchor="w", font=("Arial", 9, "bold")).pack(fill="x")
        self.entry_pass = tk.Entry(card, font=("Arial", 11), bd=1, relief="solid", show="*")
        self.entry_pass.pack(fill="x", pady=(5, 25), ipady=3)

        btn = tk.Button(card, text="ENTRAR", bg=COLOR_PRIMARY, fg=COLOR_WHITE, 
                        font=("Arial", 10, "bold"), relief="flat", cursor="hand2",
                        command=self.verificar_login)
        btn.pack(fill="x", ipady=5)
        tk.Label(card, text="admin / admin", fg="#ccc", bg=COLOR_WHITE, font=("Arial", 7)).pack(pady=5)

    def verificar_login(self):
        if self.entry_user.get() == "admin" and self.entry_pass.get() == "admin":
            self.login_window.destroy()
            self.abrir_sistema_principal()
        else:
            messagebox.showerror("Erro", "Login inválido!")

    # ==========================
    # SISTEMA PRINCIPAL
    # ==========================
    def abrir_sistema_principal(self):
        self.root = tk.Tk()
        self.root.title("VetSys - Gestão Veterinária")
        self.root.state("zoomed")
        self.root.configure(bg=COLOR_BG_MAIN)

        # Header
        header = tk.Frame(self.root, bg=COLOR_WHITE, height=70)
        header.pack(fill="x", side="top")
        self.img_logo_main = self.carregar_logo(scale=5)
        if self.img_logo_main:
            tk.Label(header, image=self.img_logo_main, bg=COLOR_WHITE).pack(side="left", padx=20)
        tk.Label(header, text="Painel Administrativo", font=("Helvetica", 18, "bold"), 
                 fg=COLOR_PRIMARY, bg=COLOR_WHITE).pack(side="left", padx=10)
        tk.Frame(self.root, bg=COLOR_ACCENT, height=3).pack(fill="x")

        # Estilos
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background=COLOR_BG_MAIN, borderwidth=0)
        style.configure("TNotebook.Tab", background="#e1e4e8", foreground="#555", padding=[20, 10], font=("Arial", 10))
        style.map("TNotebook.Tab", background=[("selected", COLOR_WHITE)], foreground=[("selected", COLOR_PRIMARY)])
        style.configure("Treeview", background="white", fieldbackground="white", rowheight=25, font=("Arial", 10))
        style.configure("Treeview.Heading", background=COLOR_PRIMARY, foreground="white", font=("Arial", 10, "bold"))

        # Abas
        abas = ttk.Notebook(self.root)
        abas.pack(fill="both", expand=True, padx=20, pady=20)

        # Aba 1: Tutores
        frame_cad = tk.Frame(abas, bg=COLOR_WHITE)
        abas.add(frame_cad, text="  ✚  Tutores  ")
        self.aba_cadastros(frame_cad)

        # Aba 2: Animais (NOVA!)
        frame_animais = tk.Frame(abas, bg=COLOR_WHITE)
        abas.add(frame_animais, text="  🐾  Pacientes (Animais)  ")
        self.aba_animais(frame_animais)

        # Aba 3: Relatórios
        frame_rel = tk.Frame(abas, bg=COLOR_WHITE)
        abas.add(frame_rel, text="  📊  Relatórios  ")
        self.aba_relatorios(frame_rel)

        self.root.mainloop()

    # --- ABA 1: CADASTRO DE TUTORES ---
    def aba_cadastros(self, parent):
        tk.Label(parent, text="Novo Tutor", font=("Arial", 16, "bold"), fg=COLOR_PRIMARY, bg=COLOR_WHITE).pack(pady=20)
        form = tk.Frame(parent, bg=COLOR_WHITE)
        form.pack()

        def add_field(label, row):
            tk.Label(form, text=label, font=("Arial", 10), bg=COLOR_WHITE, anchor="w").grid(row=row, column=0, sticky="w", pady=(10, 0))
            entry = tk.Entry(form, width=35, font=("Arial", 12), bd=1, relief="solid")
            entry.grid(row=row+1, column=0, pady=(5, 10), ipady=4)
            return entry

        self.ent_nome = add_field("Nome Completo:", 0)
        self.ent_tel = add_field("Telefone:", 2)
        self.ent_email = add_field("E-mail:", 4)

        btn = tk.Button(form, text="SALVAR TUTOR", bg=COLOR_ACCENT, fg="#000",
                        font=("Arial", 11, "bold"), relief="flat", cursor="hand2", width=30, command=self.salvar_tutor)
        btn.grid(row=6, column=0, pady=30, ipady=8)

    def salvar_tutor(self):
        if not self.ent_nome.get(): return
        try:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO Tutor (nome, telefone, email) VALUES (%s,%s,%s)",
                        (self.ent_nome.get(), self.ent_tel.get(), self.ent_email.get()))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Tutor salvo!")
            self.ent_nome.delete(0,tk.END); self.ent_tel.delete(0,tk.END); self.ent_email.delete(0,tk.END)
            # Atualiza a lista de tutores na aba de animais se ela já estiver carregada
            self.carregar_tutores_combobox()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # --- ABA 2: CADASTRO DE ANIMAIS (NOVA) ---
    def aba_animais(self, parent):
        # Layout: Esquerda (Formulário) | Direita (Tabela)
        frame_esquerda = tk.Frame(parent, bg=COLOR_WHITE, padx=20, pady=20)
        frame_esquerda.pack(side="left", fill="y")
        
        frame_direita = tk.Frame(parent, bg="#f9f9f9", padx=20, pady=20)
        frame_direita.pack(side="right", fill="both", expand=True)

        # --- Formulário ---
        tk.Label(frame_esquerda, text="Cadastrar Animal", font=("Arial", 14, "bold"), fg=COLOR_PRIMARY, bg=COLOR_WHITE).pack(pady=(0,20))

        # Seleção de Tutor
        tk.Label(frame_esquerda, text="Selecione o Tutor:", bg=COLOR_WHITE, anchor="w").pack(fill="x")
        self.cb_tutor = ttk.Combobox(frame_esquerda, font=("Arial", 11), state="readonly")
        self.cb_tutor.pack(fill="x", pady=(0, 10))
        self.carregar_tutores_combobox()

        # Campos de Texto
        def criar_entry(lbl):
            tk.Label(frame_esquerda, text=lbl, bg=COLOR_WHITE, anchor="w").pack(fill="x")
            e = tk.Entry(frame_esquerda, font=("Arial", 11), bd=1, relief="solid")
            e.pack(fill="x", pady=(0, 10))
            return e

        self.ent_pet_nome = criar_entry("Nome do Pet:")
        self.ent_pet_raca = criar_entry("Raça:")
        self.ent_pet_nasc = criar_entry("Data Nasc. (AAAA-MM-DD):")
        self.ent_pet_peso = criar_entry("Peso (kg):")

        # Comboboxes pequenas
        frame_combos = tk.Frame(frame_esquerda, bg=COLOR_WHITE)
        frame_combos.pack(fill="x")
        
        tk.Label(frame_combos, text="Espécie:", bg=COLOR_WHITE).grid(row=0, column=0)
        self.cb_especie = ttk.Combobox(frame_combos, values=["Cão", "Gato", "Outro"], width=10)
        self.cb_especie.grid(row=1, column=0, padx=5)
        
        tk.Label(frame_combos, text="Sexo:", bg=COLOR_WHITE).grid(row=0, column=1)
        self.cb_sexo = ttk.Combobox(frame_combos, values=["Macho", "Fêmea"], width=10)
        self.cb_sexo.grid(row=1, column=1, padx=5)

        tk.Label(frame_esquerda, text="Castrado?", bg=COLOR_WHITE).pack(anchor="w", pady=(10,0))
        self.cb_castrado = ttk.Combobox(frame_esquerda, values=["SIM", "NÃO"], state="readonly")
        self.cb_castrado.pack(fill="x")

        btn_pet = tk.Button(frame_esquerda, text="SALVAR PET", bg=COLOR_ACCENT, fg="black", font=("Arial", 10, "bold"),
                            command=self.salvar_animal)
        btn_pet.pack(fill="x", pady=20, ipady=5)

        # --- Tabela (Lista de Animais) ---
        tk.Label(frame_direita, text="Lista de Animais Cadastrados", font=("Arial", 12, "bold"), bg="#f9f9f9", fg="#555").pack(anchor="w", pady=(0,10))
        
        cols = ("ID", "Nome", "Espécie", "Raça", "Tutor")
        self.tree_animais = ttk.Treeview(frame_direita, columns=cols, show="headings")
        for c in cols:
            self.tree_animais.heading(c, text=c)
            self.tree_animais.column(c, width=80)
        
        self.tree_animais.column("Tutor", width=150) # Tutor precisa de mais espaço
        self.tree_animais.pack(fill="both", expand=True)

        # Botão Atualizar
        tk.Button(frame_direita, text="🔄 Atualizar Lista", command=self.atualizar_lista_animais).pack(pady=5)
        
        # Carregar lista inicial
        self.atualizar_lista_animais()

    def carregar_tutores_combobox(self):
        """Busca tutores no banco e preenche o combobox"""
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT id_Tutor, nome FROM Tutor")
            tutores = cur.fetchall()
            # Formato: "1 - João Silva"
            lista = [f"{t[0]} - {t[1]}" for t in tutores]
            self.cb_tutor['values'] = lista
        except:
            pass

    def salvar_animal(self):
        tutor_str = self.cb_tutor.get()
        nome = self.ent_pet_nome.get()
        especie = self.cb_especie.get()
        
        if not tutor_str or not nome or not especie:
            messagebox.showwarning("Aviso", "Preencha Tutor, Nome e Espécie!")
            return

        # Extrair ID do Tutor (pega o número antes do traço)
        id_tutor = int(tutor_str.split(' - ')[0])

        try:
            sql = """INSERT INTO Animal (nome, especie, raca, data_nascimento, peso, porte, sexo, castrado, id_Tutor)
                     VALUES (%s, %s, %s, %s, %s, 'Médio', %s, %s, %s)"""
            val = (nome, especie, self.ent_pet_raca.get(), 
                   self.ent_pet_nasc.get() if self.ent_pet_nasc.get() else None,
                   self.ent_pet_peso.get() if self.ent_pet_peso.get() else 0.0,
                   self.cb_sexo.get(), self.cb_castrado.get(), id_tutor)
            
            cur = self.conn.cursor()
            cur.execute(sql, val)
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Pet cadastrado!")
            self.atualizar_lista_animais()
            
            # Limpar campos
            self.ent_pet_nome.delete(0, tk.END)
            self.ent_pet_raca.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def atualizar_lista_animais(self):
        self.tree_animais.delete(*self.tree_animais.get_children())
        try:
            cur = self.conn.cursor()
            # JOIN para mostrar o Nome do Tutor em vez do ID
            sql = """SELECT a.id_Animal, a.nome, a.especie, a.raca, t.nome 
                     FROM Animal a 
                     JOIN Tutor t ON a.id_Tutor = t.id_Tutor
                     ORDER BY a.id_Animal DESC"""
            cur.execute(sql)
            for row in cur.fetchall():
                self.tree_animais.insert("", tk.END, values=row)
        except:
            pass

    # --- ABA 3: RELATÓRIOS ---
    def aba_relatorios(self, parent):
        menu = tk.Frame(parent, bg="#f7f9fc", width=260)
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)
        tk.Label(menu, text="SELECIONE A CONSULTA", font=("Arial", 9, "bold"), fg="#aaa", bg="#f7f9fc").pack(pady=(25,10), padx=20, anchor="w")

        def add_btn(text, cmd):
            tk.Button(menu, text=text, command=cmd, bg="white", fg=COLOR_TEXT,
                      font=("Arial", 10), anchor="w", padx=15, relief="solid", bd=0, cursor="hand2")\
                      .pack(fill="x", pady=2, padx=10, ipady=10)

        add_btn("📅  Detalhes de Agendamentos", self.q1)
        add_btn("⚖️  Animais Acima do Peso", self.q2)
        add_btn("🏆  Top Veterinários", self.q3)
        add_btn("🔍  Busca Específica (M...)", self.q4)
        add_btn("💊  Tratamentos Recentes", self.q5)

        self.tree = ttk.Treeview(parent, columns=("c1"), show="headings")
        self.tree.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        scroll = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")

    def run_query(self, cols, query):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = cols
        for c in cols: 
            self.tree.heading(c, text=c)
            self.tree.column(c, width=130)
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            for row in cur.fetchall(): self.tree.insert("", tk.END, values=row)
        except Exception as e: messagebox.showerror("Erro SQL", str(e))

    def q1(self): self.run_query(["Data", "Hora", "Tutor", "Animal", "Vet", "Status"], 
        "SELECT a.data_agendamento, a.hora, t.nome, an.nome, v.nome, a.status FROM Agendamento a JOIN Animal an ON a.id_Animal = an.id_Animal JOIN Tutor t ON an.id_Tutor = t.id_Tutor JOIN Veterinario v ON a.id_Veterinario = v.id_Veterinario WHERE a.status = 'CONFIRMADO' OR a.status = 'CONCLUIDO'")
    def q2(self): self.run_query(["Animal", "Espécie", "Peso (kg)"], 
        "SELECT nome, especie, peso FROM Animal WHERE peso > (SELECT AVG(peso) FROM Animal) ORDER BY peso DESC")
    def q3(self): self.run_query(["Veterinário", "Total Consultas"], 
        "SELECT v.nome, COUNT(c.id_Consulta) FROM Veterinario v JOIN Consulta c ON v.id_Veterinario = c.id_Veterinario GROUP BY v.nome")
    def q4(self): self.run_query(["Nome", "Espécie", "Raça"], 
        "SELECT nome, especie, raca FROM Animal WHERE especie IN ('Cão', 'Gato') AND nome LIKE 'M%'")
    def q5(self): self.run_query(["Tratamento", "Início", "Animal"], 
        "SELECT t.descricao, t.data_inicio, a.nome FROM Tratamento t JOIN Consulta c ON t.id_Consulta = c.id_Consulta JOIN Animal a ON c.id_Animal = a.id_Animal ORDER BY t.data_inicio DESC LIMIT 5")

if __name__ == "__main__":
    app = SistemaVet()