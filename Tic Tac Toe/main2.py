import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for i in combo:
                buttons[i].config(bg="lightgreen")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            disable_all_buttons()
            return True
    return False

def check_draw():
    if all(btn["text"] != "" for btn in buttons):             #check if all buttons are filled and no winner, then it's a draw
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        disable_all_buttons()
        return True
    return False

def disable_all_buttons():
    for btn in buttons:                 #disable all buttons after game ends
        btn.config(state="disabled")

def enable_all_buttons():
    for btn in buttons:                  #enable all buttons for new game and reset background color
        btn.config(state="normal", bg="lightgray")

def button_click(index):
    global current_player
    if buttons[index]["text"] == "":                #only allow click if button is empty
        buttons[index]["text"] = current_player
        if check_winner() or check_draw():
            return
        toggle_player()

def toggle_player():                           #toggle between players after each valid move
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

def reset_game():
    global current_player                   #reset game state and UI for new game
    current_player = "X"
    enable_all_buttons()
    for btn in buttons:
        btn["text"] = ""
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")                          #set window title
root.geometry("400x500")

buttons = [tk.Button(root, text="", font=("Arial", 25, "bold"), width=5, height=2, 
                     command=lambda i=i: button_click(i), bg="lightgray") for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3, padx=5, pady=5)           #arrange buttons in 3x3 grid with padding

current_player = "X"
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 16, "bold"))
label.grid(row=3, column=0, columnspan=3, pady=10)               #display current player's turn below the grid

reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_game, bg="lightblue")
reset_btn.grid(row=4, column=0, columnspan=3, sticky="ew", padx=5, pady=5)           #add reset button below the turn label that spans across all columns and fills horizontally

root.mainloop()      #start the Tkinter event loop to run the application