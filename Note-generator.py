import random
def computer_music_3():
    notes = ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'A5', 'B5', 'C5', 'D5', 'E5', 
             'F5', 'G5', 'rest'] #list of notes in Cmaj within treble clef
    notes_minus_rest = ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'A5', 'B5', 'C5', 'D5', 'E5', 
             'F5', 'G5'] #same but without rest, for re-rolling out-of-range notes
    lengths = [1.0, .5, .25, 1/8, 1/16] #list of note lengths
    sheet_notes = []
    sheet_lens = []
    sheet = [] #empty sheet music
    last_note = None #no notes in list
    
    for y in range(4): #repeats to make 4 measures

        x = 0 #start for measure length
        
        while x < 1: #a measure = 1 and is made up of fraction notes. Add notes until measure is filled
            note_len = random.choice(lengths) #randome length
            if note_len + x > 1: #if note_len is added, will it make the measure > 1 long?
                continue #if so pick a different note length
            else:
                sheet_lens.append(note_len) #append length to len list
            
            note = random.choice(notes) #random note
            
            try: #checks if last note has been assigned
                last_note_index = notes.index(last_note) # gets position value of prev note in notes list
                if note != 'rest': 
                    while ('B' in note and 'F' in last_note) or ('F' in note and 'B' in last_note): #checking for tritone
                        print('tritone')
                        note = random.choice(notes_minus_rest) #pick again
                        continue

                    if last_note_index >= 4: #create a range of notes based on previous note, w/o 'rest'
                        note_range = notes_minus_rest[last_note_index - 4: last_note_index + 4] 
                    else:
                        note_range = notes_minus_rest[:last_note_index + 4]
                        
                    if note not in note_range: #check if not is in above rant
                        print('Not in range')
                        note = random.choice(note_range) #re-rolls a random note but within above constraints
                        sheet_notes.append(note)
                    else:
                        print("In range")
                        sheet_notes.append(note)
                else:
                    print('rest')
                    sheet_notes.append(note)

            except ValueError: #first loop doesn't have a "last note" to check against
               sheet_notes.append(note)
            if note != 'rest': #if this note is a rest, keep the last note value from prev loop
                last_note = note
            x += note_len #adding the note length to the measure length
        print('Measure %d complete' % y)    
    
    sheet = list(zip(sheet_notes, sheet_lens))
    print(sheet)
