#set up three dictionary lists that contain words that can be set up as the word to guess.
#easy = 5 letters, medium = 7 letters, hard =10/11 letters, expert= random difficult words
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def pick_easy_word():
    import random
    easyDict=['label','labor','macaw','fable','faced','ozone','cabin','cable','eager','jaded','pacer','paces','packs',
              'rabid','eagle','typos','tyres','oasis','wales','walks', 'tiger', 'whale', 'zeus', 'flail', 'braces', 
              'reeds', 'pages', 'nacho', 'mercy', 'joint', 'igloo', 'facia', 'bleed', 'nacho', 'rabid', 'sushi'
              'royal', 'quill', 'necks', 'laced', 'lasso', 'juror', 'imput', 'eager', 'faced', 'cable', 'baron', 'bulge']
    #print(len(easyDict))
    return random.choice(easyDict)
    
def pick_med_word():
    import random
    mediumDict=['ability','alchemy','baffled','boulder','cabaret','cougars','diaries','dusters','earache','gaboons',
                'explore','gondola','habitat','heroine','icecaps','jigsaws','jamming','indulge','karaoke','knitted',
                'lactose','ostrich','oatcake','packrat','stumped','sailers','pranked','tackled','waddled','tremble',
                'zealots','website', 'engines', 'amnesia', 'anchovy', 'blanket','buffers','corrode','cottons', 'elitism']
    #print(len(mediumDict))
    return random.choice(mediumDict)
    
def pick_hard_word():
    import random
    hardDict=['abbreviate','analytical','blackberry','backboards','corruptive','dandelions','cyberbully','diagonally',
              'earthworms','fabricates','enrichment','narcissism','semicircle','trajectile','tabernacle','hieroglyphs',
              'abomination','leapfrogged','obfuscation','misanthropy','quarrelsome','petitioning','rehydration',
              'seductively','taxidermist','undesirably','vaccination','ideological','caffeinated','zealousness',
              'multivitamin','abbreviating','earsplitting', 'alleviative', 'anaesthetic', 'disillusive']
    #print(len(hardDict))
    return random.choice(hardDict)

def pick_expert_word():
    import random
    expertDict=['fly', 'knights', 'rhythms', 'rhythmic', 'ivory', 'jiujitsu', 'blizzard', 'axoim', 'photosynthesis', 'larynx',
                'buzzings', 'voodoo', 'megahertz', 'mystify', 'wyvern', 'mithril', 'onyx', 'whiskey', 'vortex', 'vertices',
                'avenue', 'hydrogen', 'phlegm', 'wimp', 'wax', 'funny', 'pneumonia', 'icebox', 'kiosk', 'lymph', 'jazz',
                'vertex', 'mischief', 'hex', 'ichor', 'surds', 'quark', 'odium', 'larva', 'joust', 'index', 'blouses',
                'daemons', 'blasphemous', 'namelessnesses', 'ventriloquisms'] 
    #print(len(expertDict))
    return random.choice(expertDict)

#set up the word that has been chosen from the lists
def process_word(word):
    word_letters=list(word)
    #print(word_letters)  
    wordLenght=len(word)
    #print(wordLenght)

    #create a list of values that start as unknown and can be replaced by the correct letter in the right index
    hiddenword=[]
    for i in range(wordLenght):
      hiddenword.append("_")
    return word_letters, hiddenword


#button command that will reset the game state to full lives and no word as well as generating new words
def reset_game_btn():
    global lives, word,lettersGuessed, easy_word, med_word, hard_word, expert_word
    lives=9
    word=''     #clear the word to allow for new ones to be generated.
    lettersGuessed=[]
    difficulty=''
    
    #create a time and datre variable that is created upon making a grid and can be saved to data file
    from datetime import datetime
    global dt_string_date, dt_string_time
    # datetime object containing current date and time
    newgameTime = datetime.now()
    # dd/mm/YY H:M:S
    dt_string_date = newgameTime.strftime("%Y/%m/%d")  
    dt_string_time = newgameTime.strftime("%H:%M:%S")        
    #print(dt_string_date)
    #print(dt_string_time)
    
    #RESET EASY WORD
    easy_word=pick_easy_word().upper()
    # RESET MEDIUM WORD
    med_word=pick_med_word().upper()
    #RESET HARD WORD
    hard_word=pick_hard_word().upper()
    #RESET  EXPERT WORD
    expert_word=pick_expert_word().upper()
    # RESET WHERE THE WORD IS DISPLAYED
    lbl_word["text"]='Click difficulty to start!'
    lbl_difficulty["text"]="Difficulty: "
    #RESET DRAWING
    lbl_game_state["image"]=titlescreen
    # reset letters guessed
    lettersGuessed=[]
    lbl_let_guessed["text"]="Guesses: "
    lbl_lives_var["text"]=lives

#easy, medium and hard choice button commands, change the main_word variable to one selected from the distionaries.
def easy_btn():
    easy_word_letters, easy_hiddenword=process_word(easy_word)
    global word, hidden, difficulty
    difficulty='EASY'
    word=easy_word_letters
    hidden=easy_hiddenword
    lbl_word["text"]=' '.join(hidden)
    lbl_difficulty["text"]="Difficulty: "+str(difficulty)
    #RESET DRAWING
    lbl_game_state["image"]=startingscreen
 
def med_btn():
    med_word_letters, med_hiddenword=process_word(med_word)
    global word, hidden, difficulty
    difficulty='MEDIUM'
    word=med_word_letters
    hidden=med_hiddenword
    lbl_word["text"]=' '.join(hidden)
    lbl_difficulty["text"]="Difficulty: "+str(difficulty)
    #RESET DRAWING
    lbl_game_state["image"]=startingscreen

def hard_btb():
    hard_word_letters, hard_hiddenword=process_word(hard_word)
    global word, hidden, difficulty
    difficulty='HARD'
    word=hard_word_letters
    hidden=hard_hiddenword
    lbl_word["text"]=' '.join(hidden)
    lbl_difficulty["text"]="Difficulty: "+str(difficulty)
    #RESET DRAWING
    lbl_game_state["image"]=startingscreen

def expert_btb():
    expert_word_letters, expert_hiddenword=process_word(expert_word)
    global word, hidden, difficulty
    difficulty='EXPERT'
    word=expert_word_letters
    hidden=expert_hiddenword
    lbl_word["text"]=' '.join(hidden)
    lbl_difficulty["text"]="Difficulty: "+str(difficulty)
    #RESET DRAWING
    lbl_game_state["image"]=startingscreen

#command for  guessing the letter button when pressed
lettersGuessed=[] #keep track of all of the letters guessed, if already in this list tell user to pick again
def guess_letter_btn():
    global guess, lives
    guess=(ent_letter_guess.get()).upper()
    #print('difficulty:', difficulty)
    #print(''.join(word))       #word check
    #clear entry for next guess
    ent_letter_guess.delete(0, "end")
    ent_letter_guess.insert(0, "")
    
    #check that the guess is a single letter and not a number or more than one letter long to prevent wasting lives.
    import string
    uppercase_check=list(string.ascii_uppercase)
    if guess not in uppercase_check:    #incorrect guess type by comparing to list of correct values
        messagebox.showinfo(title="Input error", message="WARNING:  Guesses must be single letters" )
        lives=lives+1   #add a life so if subtracted at the end it doesnt effect game state

    #checks for letters already guessed
    if guess in lettersGuessed:
        messagebox.showinfo(title="Duplicate letter", message="You have already gussed,  " +  guess+ "  Try another letter." )
    else:
        if guess in word:   #check the letter is in the word
            guess_location = [i for i, x in enumerate(word) if x == guess]  #checks for multiple occuracnes of the guess
            #print(guess_location)
            for loc in guess_location:
                hidden[loc]=guess
            lbl_word["text"]=' '.join(hidden)
        else:               #lose life if not in the word and then draw the relevent parts.
            lives=lives-1
            lbl_lives_var["text"]=lives
            
            if lives==0:        #check lives are 0
                # datetime object containing current date and time
                endgameTime = datetime.now()
                # dd/mm/YY H:M:S
                endgame_string_time = endgameTime.strftime("%H:%M:%S") 
                # In same directory open file in append mode and add a new line of data
                raw_data=open('hangman_raw_data.txt',"a")
                raw_data.write("\n"+dt_string_date+','+dt_string_time+','+endgame_string_time+','+str(''.join(word))+","+difficulty+","+str(lives)+","+str(''.join(lettersGuessed))) 
                raw_data.close()
                #display a winning pop up
                messagebox.showinfo(title="GAME OVER", message="GAME OVER. The word was "+ ''.join(word)+"!")
            lbl_word["text"]=' '.join(hidden)
            
    #check to see if the entire word has been found or unhidden     
    if '_' not in hidden:
        # datetime object containing current date and time
        endgameTime = datetime.now()
        # dd/mm/YY H:M:S
        endgame_string_time = endgameTime.strftime("%H:%M:%S") 
        # In same directory open file in append mode and add a new line of data
        raw_data=open('hangman_raw_data.txt',"a")
        raw_data.write("\n"+dt_string_date+','+dt_string_time+','+endgame_string_time+','+str(''.join(word))+","+difficulty+","+str(lives)+","+str(''.join(lettersGuessed))) 
        raw_data.close()
        #display a winning pop up
        messagebox.showinfo(title="Winner", message="YOU WON! The word was "+ ''.join(word)+"!")
    
    #draw out the current state of the game based on the lives at this point
    if lives==8: #Lose second life
        lbl_game_state["image"]=_8lives
    elif lives==7: #Lose third life
        lbl_game_state["image"]=_7lives
    elif lives==6: #Lose fourth life
        lbl_game_state["image"]=_6lives
    elif lives==5: #Lose fifth life
        lbl_game_state["image"]=_5lives
    elif lives==4: #Lose sixth life
        lbl_game_state["image"]=_4lives
    elif lives==3: #Lose seventh life
        lbl_game_state["image"]=_3lives
    elif lives==2: #Lose eighth life
        lbl_game_state["image"]=_2lives
    elif lives==1:  #Lose ninth life
        lbl_game_state["image"]=_1lives
    elif lives==0: #Lose last life and the game is over
        lbl_game_state["image"]=_0lives

    #display the correct letters guessed so far, avoid duplicates
    if guess not in lettersGuessed and len(guess) == 1 and guess in uppercase_check:
        lettersGuessed.append(guess)
        lg_string=','.join(lettersGuessed)
        lbl_let_guessed["text"]="Guesses: " + lg_string


#function to allow enter to be pressed to submit letter guess
def enter_pressed_guess_letter(event):
    #run the function that is the same as the button pressed
    guess_letter_btn()

    
#command for guessing the full word button when pressed
def guess_word_btn():
    global guess_word, lives
    guess_word=(ent_word_guess.get()).upper()
    #check that a guess word has been input and not mis clicked.
    if len(guess_word) != len(word):
        messagebox.showinfo(title="Input error", message="WARNING:  Guess didnt match the words length!" )
        lives=lives+1   #add a life so if subtracted at the end it doesnt effect game state
    
    #clear entry for next guess
    ent_word_guess.delete(0, "end")
    ent_word_guess.insert(0, "")
    
    #check that the guess is a string of letters and not numbers of punctuation by mistake
    import string
    uppercase_check=list(string.ascii_uppercase)
    for letter in guess_word:
        if letter not in uppercase_check:    #incorrect guess type by comparing to list of correct strings
            messagebox.showinfo(title="Input error", message="WARNING:  Guesses must be all letters" )
            lives=lives+1   #add a life so if subtracted at the end it doesnt effect game state
    
    #check the guessed word is the word and display winner or lose life
    if guess_word==''.join(word):
        # datetime object containing current date and time
        endgameTime = datetime.now()
        # dd/mm/YY H:M:S
        endgame_string_time = endgameTime.strftime("%H:%M:%S") 
        # In same directory open file in append mode and add a new line of data
        raw_data=open('hangman_raw_data.txt',"a")
        raw_data.write("\n"+dt_string_date+','+dt_string_time+','+endgame_string_time+','+str(''.join(word))+","+difficulty+","+str(lives)+","+str(''.join(lettersGuessed))) 
        raw_data.close()
        #display a winning pop up
        messagebox.showinfo(title="Winner", message="YOU WON! The word was "+ ''.join(word)+"!")
    else:
        lives=lives-1
        lbl_lives_var["text"]=lives
    
    if lives==0:        #check lives are 0
        # datetime object containing current date and time
        endgameTime = datetime.now()
        # dd/mm/YY H:M:S
        endgame_string_time = endgameTime.strftime("%H:%M:%S") 
        # In same directory open file in append mode and add a new line of data
        raw_data=open('hangman_raw_data.txt',"a")
        raw_data.write("\n"+dt_string_date+','+dt_string_time+','+endgame_string_time+','+str(''.join(word))+","+difficulty+","+str(lives)+","+str(''.join(lettersGuessed))) 
        raw_data.close()
        #display a winning pop up
        messagebox.showinfo(title="GAME OVER", message="GAME OVER. The word was "+ ''.join(word)+"!")
    
    #draw out the current state of the game based on the lives at this point
    if lives==8: #Lose second life
        lbl_game_state["image"]=_8lives
    elif lives==7: #Lose third life
        lbl_game_state["image"]=_7lives
    elif lives==6: #Lose fourth life
        lbl_game_state["image"]=_6lives
    elif lives==5: #Lose fifth life
        lbl_game_state["image"]=_5lives
    elif lives==4: #Lose sixth life
        lbl_game_state["image"]=_4lives
    elif lives==3: #Lose seventh life
        lbl_game_state["image"]=_3lives
    elif lives==2: #Lose eighth life
        lbl_game_state["image"]=_2lives
    elif lives==1:  #Lose ninth life
        lbl_game_state["image"]=_1lives
    elif lives==0: #Lose last life and the game is over
        lbl_game_state["image"]=_0lives
    
    lbl_word["text"]=' '.join(hidden)

#function to allow enter to be pressed to word guess
def enter_pressed_guess_word(event):   
    #run the function that is the same as the button pressed
    guess_word_btn()



    
#-------------GLOBAL VARIABLES TO INITIATE APP ------------
word=''
hidden=''
lives=9  #initial variable to track the lives of the user
difficulty=''
#EASY WORD
easy_word=pick_easy_word().upper()
#MEDIUM WORD
med_word=pick_med_word().upper()
#HARD WORD
hard_word=pick_hard_word().upper()
#EXPERT WORD
expert_word=pick_expert_word().upper()
# datetime object containing current date and time to initiate the file
newgameTime = datetime.now()
# dd/mm/YY H:M:S
dt_string_date = newgameTime.strftime("%Y/%m/%d")  
dt_string_time = newgameTime.strftime("%H:%M:%S")        
#print(dt_string_date)
#print(dt_string_time)  



# ------------------------------------ ALL APP FORMATTING -------------------------------------------
# Create instance
window = tk.Tk()
# Add a title
frm_pic_colors=["#F8F8FF", "#6495ED"]   #TEXT AND BACKGROUND COLOURS
btn_colors=["#F8F8FF", "#4169E1"]       #text and background for buttons
window.title("HANGMAN - APP (jlf)")
#window.geometry('400x600')
# Disable resizing the GUI
window.resizable(0,0)  #(x,y)

#load all of the images needed for the hangman drawings via tk.Photoimage
titlescreen = tk.PhotoImage(file='titlescreen.png')
startingscreen = tk.PhotoImage(file='startingscreen.png')
_8lives = tk.PhotoImage(file='8lives.png')
_7lives = tk.PhotoImage(file='7lives.png')
_6lives = tk.PhotoImage(file='6lives.png')
_5lives = tk.PhotoImage(file='5lives.png')
_4lives = tk.PhotoImage(file='4lives.png')
_3lives = tk.PhotoImage(file='3lives.png')
_2lives = tk.PhotoImage(file='2lives.png')
_1lives = tk.PhotoImage(file='1lives.png')
_0lives = tk.PhotoImage(file='0lives.png')

#LABEL - Choose the words difficulty
lbl_title=tk.Label(master=window, 
                text="H_NGM_N   G_ME",
                font=("Minion Pro Med", 34,  "bold italic"), 
                foreground="#FFA500",  
                background="#4169E1"
)
lbl_title.grid(row=0, column=0, sticky="ew")

#FRAME TO HOLD WORD CHOICE BUTTONS
frm_choose_button=tk.Frame(background=frm_pic_colors[1])
frm_choose_button.grid(row=1, column=0, sticky="ew")
frm_choose_button.grid_rowconfigure(0, weight=1)
frm_choose_button.grid_columnconfigure([0,1,2,3,4], weight=1)

#CLICK BUTTON TO CHOOSE AN EASY WORD
btn_new_game=tk.Button(master=frm_choose_button, text='Reset Game', font=("Lucida Sans Typewriter", 12), command=reset_game_btn)
btn_new_game.grid(row=0, column=0, pady=8)

#CLICK BUTTON TO CHOOSE AN EASY WORD
btn_easy=tk.Button(master=frm_choose_button, text='Easy',font=("Miriam", 12, "bold"),fg=btn_colors[0], bg=btn_colors[1],
                   relief=tk.RIDGE, borderwidth=3,  command=easy_btn)
btn_easy.grid(row=0, column=1, pady=8)

#CLICK BUTTON TO CHOOSE AN MEDIUM WORD
btn_med=tk.Button(master=frm_choose_button, text='Medium',font=("Miriam", 12, "bold"),fg=btn_colors[0], bg=btn_colors[1],
                   relief=tk.RIDGE, borderwidth=3, command=med_btn)
btn_med.grid(row=0, column=2, pady=8)

#CLICK BUTTON TO CHOOSE AN HARRD WORD
btn_hard=tk.Button(master=frm_choose_button, text='Hard', font=("Miriam", 12, "bold"),fg=btn_colors[0], bg=btn_colors[1],
                   relief=tk.RIDGE, borderwidth=3, command=hard_btb)
btn_hard.grid(row=0, column=3, pady=8)

#CLICK BUTTON TO CHOOSE AN EXPEPRT WORD
btn_expert=tk.Button(master=frm_choose_button, text='Expert', font=("Miriam", 12, "bold"),fg=btn_colors[0], bg=btn_colors[1],
                   relief=tk.RIDGE, borderwidth=3, command=expert_btb)
btn_expert.grid(row=0, column=4, pady=8)

#displays the difficulty of word chosen
lbl_difficulty=tk.Label(master=frm_choose_button,text="Difficulty: ",font=["Arial", 11, "bold"] ,
                        fg='black',  bg=frm_pic_colors[1])
lbl_difficulty.grid(row=1, column=0,sticky='ew')

#label- displays the current state of the word 
lbl_word = tk.Label(master=window,
    text="Click difficulty to start!",
    font=("Lucida Sans Typewriter", 20, "bold"), 
    foreground="black",  
    background="#F08080"
)
#displays the current word stats of _ _ _ _ or the letters replacing them.
lbl_word.grid(row=3, column=0, sticky='ew')

#frame to display the current word stats of _ _ _ _ or the letters replacing them.
frm_picture=tk.Frame(master=window, bg=frm_pic_colors[1])
frm_picture.grid(row=4, column=0, sticky="ew")
frm_pic_front=["Arial", 11, "bold"]     #FONT FOR WHOLE OBJECT
frm_picture.grid_rowconfigure([0,1,2,3], weight=1)
frm_picture.grid_columnconfigure(0, weight=1)

#buffer to frame image
lbl_game_buffer1=tk.Label(master=frm_picture, text=' ', font=frm_pic_front, fg=frm_pic_colors[0],  bg=frm_pic_colors[1])
lbl_game_buffer1.grid(row=0, column=0)
#holds the image for the current game state
lbl_game_state=tk.Label(master=frm_picture, image=titlescreen, font=frm_pic_front, fg=frm_pic_colors[0],  bg=frm_pic_colors[1])
lbl_game_state.grid(row=1, column=0)
#buffer to frame iamge
lbl_game_buffer2=tk.Label(master=frm_picture, text=' ', font=frm_pic_front, fg=frm_pic_colors[0],  bg=frm_pic_colors[1])
lbl_game_buffer2.grid(row=2, column=0)

#hold infomation of the letters guessed so far
lbl_let_guessed=tk.Label(master=frm_picture, text='Guesses: ', font=("Lucida Sans Typewriter", 14, "bold"),
                    fg=frm_pic_colors[0],  bg=frm_pic_colors[1])
lbl_let_guessed.grid(row=3, column=0)

#image buffer
lbl_line10=tk.Label(master=frm_picture, text=' ', font=frm_pic_front, fg=frm_pic_colors[0],  bg=frm_pic_colors[1])
lbl_line10.grid(row=4, column=0)

#botton frame that has the buttons and lives shown
frm_buttons=tk.Frame(master=window, background=frm_pic_colors[1], highlightthickness=0)
frm_buttons.grid(row=5, column=0, sticky='ew')
frm_buttons.grid_rowconfigure([0,1], weight=1)
frm_buttons.grid_columnconfigure([0,1,2], weight=1)

#left hand side button to type in a letter guess and a button to send that letter through the game
ent_letter_guess=tk.Entry(master=frm_buttons)
btb_letter_confirm=tk.Button(master=frm_buttons, text="Guess Letter!", font=("Miriam", 14, "bold"),fg=btn_colors[0], bg=btn_colors[1],
                   relief=tk.RIDGE, borderwidth=3,command=guess_letter_btn)       #guess letter button
ent_letter_guess.grid(row=0, column=0, pady=10)
btb_letter_confirm.grid(row=1, column=0, padx=3, pady=10)
ent_letter_guess.bind("<Return>", enter_pressed_guess_letter)        #bind ENTER to the entry that will run the same as button pressed

#bottom middle part of screen to keep track of lives remaining
lbl_lives=tk.Label(master=frm_buttons, text="Lives Remaining:", font=("Miriam", 15), bg=frm_pic_colors[1])
lbl_lives_var=tk.Label(master=frm_buttons, text=lives, font=("Miriam", 18, "bold"), bg=frm_pic_colors[1])
lbl_lives.grid(row=0, column=1, pady=5)
lbl_lives_var.grid(row=1, column=1, pady=5)

#right hand side entry and button to attempt to guess the entire word
ent_word_guess=tk.Entry(master=frm_buttons)
btb_word_confirm=tk.Button(master=frm_buttons, text="Guess Word!",font=("Miriam", 14, "bold"),fg=btn_colors[0], bg=btn_colors[1],
                   relief=tk.RIDGE, borderwidth=3, command=guess_word_btn)               #guess word button
ent_word_guess.grid(row=0, column=2, pady=10)
btb_word_confirm.grid(row=1, column=2, padx=3, pady=10)
ent_word_guess.bind("<Return>", enter_pressed_guess_word)        #bind ENTER to the entry which will run the same as button pressed

# Run the application
window.mainloop()
