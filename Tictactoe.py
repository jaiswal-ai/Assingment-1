import tkinter as tk
from tkinter import messagebox
 
def start_game():
    root = tk.Tk()#window of game
    root.title("Tic-Tac-Toe")#title of game
    root.geometry("315x380")#resizing window
    root.resizable(False,False)

    global current_player #making the current player global variable
    current_player = "X"  # Initialize the first player as 'X'
    label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16)) # label that says the current player"s turn
    label.grid(row=3, column=0, columnspan=3)

    buttons = [tk.Button(root, text="", font=("normal", 25), width=5, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
    #button in given size that uses lambda command and button click function to make it work.
    for i, button in enumerate(buttons):
      button.grid(row=i//3, column=i%3)# girds of the buttons

    def check_winner():  
        for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]: #all the possible combination of buttons to be winner 
            if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
                # check if the current combination is winner
                buttons[combo[0]].config(bg="green")  #turning the background green of the winner
                buttons[combo[1]].config(bg="green")
                buttons[combo[2]].config(bg="green")
                messagebox.showinfo("Tic-Tac-Toe", f"Congratulations Player {buttons[combo[0]]['text']} Wins!")
                return
        
        if all(button["text"] != "" for button in buttons):#condition if not winner 
            messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")#pops the message box of its draw
        

    def button_click(index):  
        if buttons[index]["text"] == "": #check if the button is empty
            buttons[index]["text"] = current_player #put its mark after conforming it is empty
            check_winner()
            toggle_player()#goes to next player


    def toggle_player():# function to switch next player
        global current_player # nonlocal to define that current player is not local variable.
        current_player = "X" if current_player == "O" else "O" # update the current player to X if it is equal to O otherwise O
        label.config(text=f"Player {current_player}'s turn") # writes the current player turn in button
     
    def reset_game():#function handeling the rest 
        global current_player#not local variable
        current_player = "X"
        label.config(text=f"Player {current_player}'s turn") #update  the label to show the current player
        for button in buttons:#reset buttons to its initial position
            button.config(text="", bg="SystemButtonFace")
    
    reset_button = tk.Button(root, text="Reset", command=reset_game)# creation of reset buttons
    reset_button.grid(row=4, column=0, columnspan=3)#placement of reset buttons

    root.mainloop()

start_game()


    