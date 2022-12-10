from tkinter import *
from csv import writer
import csv
from tkinter import messagebox
class GUI:
    def __init__(self, window):
        '''
        This the the setup for the GUI using Tkinter modules
        '''
        self.window = window 
        #Window for entering Voter ID
        self.frame_voterID = Frame(self.window)
        self.label_voterID = Label(self.frame_voterID, text='Voter ID')
        self.entry_voterID = Entry(self.frame_voterID)
        self.label_voterID.pack(padx=5, side='left')
        self.entry_voterID.pack(padx=5, side='left')
        self.frame_voterID.pack(anchor='w', pady=10)
        
        self.frame_candidate_selection= Frame(self.window)
        #Radiobuttons for Candidates
        self.label_candidates = Label(self.frame_candidate_selection, text = "Candidates")
        self.radio_can = IntVar()
        self.radio_can.set(0)
        self.radio_Jane = Radiobutton(self.frame_candidate_selection, text = "Jane", variable = self.radio_can, value = 1)
        self.radio_John = Radiobutton(self.frame_candidate_selection, text = "John", variable = self.radio_can, value = 2)
        self.label_candidates.pack(padx = 10, side = "left")
        self.radio_Jane.pack(side = 'left')
        self.radio_John.pack(side = 'left')
        self.frame_candidate_selection.pack(pady = 5, anchor = 'w')

        


        self.frame_propositions = Frame(self.window)
        #label for propositions
        self.label_propositions = Label(self.frame_propositions, text = "Proposition 1")
        self.radio_prop = IntVar()
        self.radio_prop.set(0)
        self.radio_yes = Radiobutton(self.frame_propositions, text = "Yes", variable = self.radio_prop, value = 1)
        self.radio_no = Radiobutton(self.frame_propositions, text = "No", variable = self.radio_prop, value = 2)
        self.label_propositions.pack( pady = 5)
        self.radio_yes.pack(side = 'left')
        self.radio_no.pack(side = 'left')
        self.frame_propositions.pack(padx = 5,pady = 5, anchor = 'w')
        
        self.frame_submit = Frame(self.window)
        self.button_submit = Button(self.window, text = "Submit", command = self.submit)
        self.button_submit.pack(pady = 10, padx = 10)
        
    def submit(self):
        """Here we take all of the voting information and place in
            into a CSV using CSV modules"""

        #Retrieve all variables from GUI
        voter_ID = self.entry_voterID.get()
        candidate = self.radio_can.get()
        proposition = self.radio_prop.get()      

        #Determine entry for Candidate
        if candidate == 1:
            self.candidate = "Jane"
        if candidate == 2:
            self.candidate= "John"
        if candidate !=1 and candidate != 2:
            self.candidate = "Did not vote for candidate"

        
        #Determine entry for Proposition
        if proposition == 1:
            self.proposition = "Yes"
        if proposition == 2:
            self.proposition = "No"
        if proposition == 0:
            self.proposition = "Did not vote on proposition"
        
        #Enter voter submission into a data file/excel sheet
        
        
        voter_submission = [voter_ID, self.candidate,self.proposition]
        
        with open ("Voter_Submissions.csv", "a+", newline="") as file: #
            record = writer(file)
            record.writerow(voter_submission)
            file.close()
        messagebox.showinfo("Validation", "Your ballot has been submitted, thank you.")
        self.entry_voterID.delete(0,END)
        self.radio_can.set(0)
        self.radio_prop.set(0)
        
                    
                    
                    
                    
            

        