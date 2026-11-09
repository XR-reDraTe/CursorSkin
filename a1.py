import tkinter as tk


title = 'TIP'
content = 'We just telling you that downloading the cursor skin(.cur) is the correct way of this project.\nThis message is only reminding you, not means you did something wrong.'
btnText = 'More details'
detailTitle = 'Details Info'
detailContent = 'Don′t know how to get cursor skin?\n\nGo back to the folder you downloaded where this runnable program is located, you should be able to see a folder named [Cursor Skin]. Click into it, and remember here(for convenience, we call it F).\n\nIf u don′t know how to set the skin to your cursor, read this:\nPress win+i to open Settings, then click into Devices, click the option Mouse at the left, find and click the option Additional mouse options.\nIn the new window Mouse Properties, find and click the option Pointer on the top, then select a pointer option at the middle and click the button Browse(B)..., find the folder F we just said it, and select one appropriately, and click the button Open(O), and repeat this action a few times until all the pointers are changed to the new skin. \n\nIMPORTANT! Don′t forget to close the window Mouse Properties by the button OK!\n\n\nTHANK YOU FOR DOWNLOADING OUR PROGRAM!'


def detail():
    win = tk.Toplevel(root)
    win.title(detailTitle)
    win.geometry('500x400')
    content = tk.Text(win,wrap='word')
    content.insert('1.0',detailContent)
    content.config(state='disabled')
    content.pack(expand=True,fill='both',padx=10,pady=10)


root = tk.Tk()
root.title(title)
root.geometry('300x200')

titleHead = tk.Frame(root,bg='#C2C2C2',height=40)
titleHead.pack(fill='x')
thLabel = tk.Label(titleHead,text='Don′t worry, not errors!',bg='#C2C2C2')
thLabel.pack(expand=True)

label = tk.Label(root,text=content,wraplength=250,justify='left')
label.pack(pady=15)

detailBtn = tk.Button(root,text=btnText,command=detail)
detailBtn.pack(pady=5)

root.mainloop()