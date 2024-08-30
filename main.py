import tkinter as tk
import mainscreen  # Ana ekran fonksiyonlarını içeren modül

def main():
    root = tk.Tk()
    root.title(" Empe Desktop Wallet")
    root.geometry("600x850")
    root.configure(background='#1F0021')
    mainscreen.show_main_screen(root)  # Ana ekranı göster
    root.mainloop()

if __name__ == "__main__":
    main()
