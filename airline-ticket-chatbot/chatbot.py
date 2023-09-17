# chatbot helps while customer purchase the ticket online.
# if the selected specific date or airline compnay plane does not match then this chatbot will help to solve the issue.

from datetime import datetime


def chatbot():
    print('Welcome to the chatbot')

    #ask the user for their name

    name = input('What is your name?')
    return date_prob()

def date_prob():
    print('what is your desire date?')
    date = input('Here is my desire date: (YYYY-MM-DD)')
    try:
        date_obj = datetime.strptime(date,"%Y-%M-%D")
        print('You entered',date_obj.strptime("%Y-%M-%D"))

    except ValueError:
        print('You Entered wrong values')










#call the chatbot function
chatbot()



    


#%%
