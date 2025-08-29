import customtkinter as ctk
from ui_components import criar_interface

def fechar_app():
    print("Fechando aplicação...")
    app.quit()
    app.destroy()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    
    app = ctk.CTk()
    app.title("Asteroides")
    app.geometry("1920x1080")

    app.protocol("WM_DELETE_WINDOW", fechar_app)

    criar_interface(app)
    app.mainloop()