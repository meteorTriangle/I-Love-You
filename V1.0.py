import tkinter as tk
window = tk.Tk()
window.title('I LOVE YOU')
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
            
window.mainloop()

