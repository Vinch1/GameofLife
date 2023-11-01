from LifeGame import LifeGame
import tkinter as tk
from UI import Set_UI, root
import profile

def rrun():
    Set_UI()
    root.mainloop()

profile.run("rrun()")
