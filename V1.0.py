# 引入 tkinter 模組
import tkinter as tk

# 建立主視窗 Frame
window = tk.Tk()

# 設定視窗標題
window.title('I LOVE YOU')

# 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("900x900")

A=[[0,0,1,0,0,0,0,1,0,0],
   [0,1,1,1,0,0,1,1,1,0],
   [1,1,1,1,1,1,1,1,1,1],
   [1,1,1,1,1,1,1,1,1,1],
   [1,1,1,1,1,1,1,1,1,1],
   [0,1,1,1,1,1,1,1,1,0],
   [0,1,1,1,1,1,1,1,1,0],
   [0,0,1,1,1,1,1,1,0,0],
   [0,0,0,1,1,1,1,0,0,0],
   [0,0,0,0,1,1,0,0,0,0],]
for i in range(10):
    for j in range(10):
        if A[i][j] == 0:
            print(A[i][j])
            tk.Frame(window, width='90', height='90', bg='white', bd=2).grid(row=i, column=j)
        else:
            print(A[i][j])
            tk.Frame(window, width='90', height='90', bg='red', bd=2).grid(row=i, column=j)
# 執行主程式
window.mainloop()

