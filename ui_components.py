import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_loader import carregar_dados
from plot_config import criar_grafico, gerar_grafico_comparativo, variaveis

def criar_interface(app):
    df, n_unicos = carregar_dados()

    side_frame = ctk.CTkFrame(app, fg_color="#041B5F", width=150)
    side_frame.pack(side='left', fill='y')

    ctk.CTkLabel(side_frame, text="Dashboard", fg_color="#041B5F", text_color="white", font=('Arial', 16, 'bold')).pack(pady=40)

    # Seleção de objetos
    ctk.CTkLabel(side_frame, text="Objeto N1:", text_color="white").pack()
    selected_object_1 = ctk.StringVar(value=str(n_unicos[0]))
    dropdown1 = ctk.CTkOptionMenu(side_frame, variable=selected_object_1, values=[str(n) for n in n_unicos])
    dropdown1.pack(pady=10)

    ctk.CTkLabel(side_frame, text="Objeto N2:", text_color="white").pack()
    selected_object_2 = ctk.StringVar(value=str(n_unicos[1]))
    dropdown2 = ctk.CTkOptionMenu(side_frame, variable=selected_object_2, values=[str(n) for n in n_unicos])
    dropdown2.pack(pady=10)

    # Local dos gráficos
    charts_frame = ctk.CTkFrame(app)
    charts_frame.pack(side='left', fill='both', expand=True)
    upper_frame = ctk.CTkFrame(charts_frame)
    upper_frame.pack(fill='both', expand=True, pady=5)
    lower_frame = ctk.CTkFrame(charts_frame)
    lower_frame.pack(fill='both', expand=True, pady=5)

    # Botões
    def limpar_graficos():
        for w in upper_frame.winfo_children(): w.destroy()
        for w in lower_frame.winfo_children(): w.destroy()

    def gerar_graficos():
        limpar_graficos()
        n = float(selected_object_1.get())
        df_filtrado = df[df['N'] == n].sort_values(by='t')
        frames = [upper_frame] * 3 + [lower_frame] * 3

        for i, (coluna, titulo, ylabel) in enumerate(variaveis):
            chart = criar_grafico(df_filtrado['t'], df_filtrado[coluna], titulo.format(n=int(n)), ylabel)
            canvas = FigureCanvasTkAgg(chart, master=frames[i])
            canvas.draw()
            canvas.get_tk_widget().pack(side="left", fill="both", expand=True, padx=5)

    def comparar_graficos():
        limpar_graficos()
        n1, n2 = float(selected_object_1.get()), float(selected_object_2.get())
        if n1 == n2:
            ctk.CTkLabel(side_frame, text="Selecione dois objetos N diferentes!", text_color="red").pack(pady=10)
            return
        df1 = df[df['N'] == n1].sort_values(by='t')
        df2 = df[df['N'] == n2].sort_values(by='t')
        frames = [upper_frame] * 3 + [lower_frame] * 3

        for i, (coluna, titulo, ylabel) in enumerate(variaveis):
            chart = gerar_grafico_comparativo(
                df1['t'], df1[coluna],
                df2['t'], df2[coluna],
                f"{titulo} para N = {int(n1)} e N = {int(n2)}",
                ylabel, int(n1), int(n2)
            )
            canvas = FigureCanvasTkAgg(chart, master=frames[i])
            canvas.draw()
            canvas.get_tk_widget().pack(side="left", fill="both", expand=True, padx=5)

    ctk.CTkButton(side_frame, text="Gerar Gráficos", command=gerar_graficos).pack(pady=20)
    ctk.CTkButton(side_frame, text="Comparar Objetos", command=comparar_graficos).pack(pady=20)
