import tkinter as tk

def add(a, b):
    return a + b

def run_app():
    def on_add():
        try:
            result = add(float(entry1.get()), float(entry2.get()))
            label_result.config(text=f"Résultat: {result}")
        except ValueError:
            label_result.config(text="Entrée invalide")

    window = tk.Tk()
    window.title("Additionneur simple")

    tk.Label(window, text="Nombre 1").pack()
    entry1 = tk.Entry(window)
    entry1.pack()

    tk.Label(window, text="Nombre 2").pack()
    entry2 = tk.Entry(window)
    entry2.pack()

    tk.Button(window, text="Additionner", command=on_add).pack()
    label_result = tk.Label(window, text="Résultat: ")
    label_result.pack()

    window.mainloop()

if __name__ == "__main__":
    run_app()
