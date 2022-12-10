#Project 1: Improved Voting machine

from gui import *

def main():
    
    window = Tk()
    window.title("Final Project 1: Improved Voting Machine")
    window.geometry("300x200")
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()
