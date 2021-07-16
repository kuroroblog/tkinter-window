import tkinter as tk

# 複数Windowを取得する関数
def getMultiWindow():
    # メインWindowの生成
    root = tk.Tk()
    # メインWindowに紐づく、サブWindowを生成する。
    tk.Toplevel()

    # メインWindowをループさせて、継続的にメインWindowを表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    root.mainloop()

# Windowを取得する関数
def getWindow():
    # Windowの生成
    root = tk.Tk()
    # Windowをループさせて、継続的にWindowを表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    root.mainloop()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # getWindow()
    # getMultiWindow()
