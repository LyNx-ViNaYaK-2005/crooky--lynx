
def comparision(x,y,remaining_guesses):
    if remaining_guesses>=1:
        y = int(input('ENTER YOUR ANOTHER GUESS:'))
        remaining_guesses -= 1 
        print('THE NUMBER YOU NOW GUESSED IS:',y)
        if x==y:
            print('NOW THE GUESSED NUMBER IS RIGHT THE ANSWER WAS:',x)
            
        
        elif x!=y:
            if x-y>=50:
                print('YOU ARE TOO FAR AWAY')
                comparision(x,y,remaining_guesses)
            elif x-y>=30 and x-y<50:
                print('YOU ARE MUCH FAR FROM NUMBER')
                comparision(x,y,remaining_guesses)
            elif x-y>=20 and x-y<30:
                print('YOU ARE STILL FAR')
                comparision(x,y,remaining_guesses)
            elif x-y>=10 and x-y<20:
                print('YOU ARE SOMEWHAT CLOSER TO THE NUMBER')
                comparision(x,y,remaining_guesses)
            elif x-y>=5 and x-y<10:
                print('YOU ARE CLOSE')
                comparision(x,y,remaining_guesses)
            elif x-y>=1 and x-y<5:
                print('YOU ARE VERY CLOSE')
                comparision(x,y,remaining_guesses)
            elif x-y<=-50:
                print('YOU ARE TOO FAR AWAY')
                comparision(x,y,remaining_guesses)
            elif x-y<=-30 and x-y>-50:
                print('YOU ARE MUCH FAR FROM NUMBER')
                comparision(x,y,remaining_guesses)
            elif x-y<=-20 and x-y>-30:
                print('YOU ARE STILL FAR')
                comparision(x,y,remaining_guesses)
            elif x-y<=-10 and x-y>-20:
                print('YOU ARE SOMEWHAT CLOSER TO THE NUMBER')
                comparision(x,y,remaining_guesses)
            elif x-y<=-5 and x-y>-10:
                print('YOU ARE CLOSE')
                comparision(x,y,remaining_guesses)
            elif x-y<=-1 and x-y>-5:
                print('YOU ARE VERY CLOSE')
                comparision(x,y,remaining_guesses)
    else:
        print("YOUR GUESSING LIMIT HAS EXCEEDED 8\nTHE CORRECT ANSWER IS:",x)

   
def number_guesser():
        x= int(input('ASK YOUR FRIEND TO ENTER A NUMBER THAT HE WANT YOU TO GUESS BTW 1 TO 51'))
        y=int(input('ENTER THE NUMBER YOU GUESSED:-'))
        print('YOUR GUESS IS:',y)
        remaining_guesses = 8

        if x==y:
            print('YOU GUESSED THE RIGHT NUMBER IN THE FIRST INSTANCE')
            print('THE RIGHT NUMBER IS',x)
        else:
            if x-y>=50:
                print('YOU ARE TOO FAR AWAY')
            elif x-y>=30 and x-y<50:
                print('YOU ARE MUCH FAR FROM NUMBER')
            elif x-y>=20 and x-y<30:
                print('YOU ARE STILL FAR')
            elif x-y>=10 and x-y<20:
                print('YOU ARE SOMEWHAT CLOSER TO THE NUMBER')
            elif x-y>=5 and x-y<10:
                print('YOU ARE CLOSE')
            elif x-y>=1 and x-y<5:
                print('YOU ARE VERY CLOSE')
            elif x-y<=-50:
                print('YOU ARE TOO FAR AWAY')
            elif x-y<=-30 and x-y>-50:
                print('YOU ARE MUCH FAR FROM NUMBER')
            elif x-y<=-20 and x-y>-30:
                print('YOU ARE STILL FAR')
            elif x-y<=-10 and x-y>-20:
                print('YOU ARE SOMEWHAT CLOSER TO THE NUMBER')
            elif x-y<=-5 and x-y>-10:
                print('YOU ARE CLOSE')
            elif x-y<=-1 and x-y>-5:
                print('YOU ARE VERY CLOSE')
        comparision(x,y,remaining_guesses)
            

            

       
    
number_guesser()
