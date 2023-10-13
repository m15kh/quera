
import pandas as pd
import re

df = pd.DataFrame({
                        'participant':[],
                        'esm':[],                     
                        'famil':[],
                        'keshvar':[],
                        'rang':[],
                        'ashia':[],
                        'ghaza':[],
                     })

score = {}

def remove_whitespace(cell): #remove white space  between two charector
    pattern = r'([\u0600-\u06FF]+)\s+([\u0600-\u06FF]+)'
    if isinstance(cell, str):
        cell = re.sub('آ', 'ا', cell)
        return re.sub(pattern, r'\1\2', cell)
    else:
        return cell



def ready_up():
    pure_file = pd.read_csv('esm_famil_data.csv', encoding='utf-8')    
    pure_file = pure_file.applymap(remove_whitespace)
    pure_file.to_csv('edit_database.csv', index=False)
   


def add_participant(participant, answers):
    cleaned_answers = {key: remove_whitespace(value) for key, value in answers.items()}
    df.loc[len(df)] = [participant, cleaned_answers['esm'], cleaned_answers['famil'], cleaned_answers['keshvar'], cleaned_answers['rang'], cleaned_answers['ashia'], cleaned_answers['ghaza']]
    score[participant] = 0




def score_table(header):
    username_has_empty = df[df[header].str.isspace()]['participant']#list of username of participant that have empty value("")
    # username_has_empty = df[df[header] == 0]['participant']

    if len(username_has_empty) == 0: #this means have no empty field ! all participant fill data
        #score for mode that haven't ''  in answers

        score_unique= 10
        score_repetition = 5
        
    else:

        #score for mode that have ''  in answers
        score_unique = 15
        score_repetition = 10

    return  username_has_empty, score_unique, score_repetition



def valid_user_ans(header):
    file  = pd.read_csv('edit_database.csv', encoding='utf-8') #read edit_database
    lst_username_valid_ans = []
    lst_each_row_words = df[header] #return all answer of  dedicated header
    for index, ans in enumerate(lst_each_row_words):
        if (file == ans).any().any(): #valid word 
            lst_username_valid_ans.append(df['participant'][index])

    return lst_username_valid_ans


def calculate_score(header,  username_has_empty,lst_username_valid_ans, score_unique, score_repetition):

    count_word_repeat = df[header].value_counts() #count all  words that how many times repeat in local dataset(get from user)
    

    unique_ans = count_word_repeat[count_word_repeat == 1].index  #return unique value
    for user in df[df[header].isin(unique_ans)]['participant']: #return username of the participant that unique answer
        if user not in list(username_has_empty) and user  in lst_username_valid_ans:#condition1: for a example have empty field (it's mean unique! that's bug!)condotion2: cheack if  user in valid list for coreect answer
            score[user] += score_unique


    repetitious_ans = count_word_repeat[count_word_repeat > 1].index #return Repetitious value #count_word_repeat > 1 its mena more than one time repeat!
    for user in df[df[header].isin(repetitious_ans)]['participant']:#return username of the participant that Repetitious answer
            if user not in list(username_has_empty) and user  in lst_username_valid_ans:#condition1:for a example have 2 value is  empty  (it's mean unique! that's bug!) condotion2: cheack if  user in valid list for coreect answer
                score[user] += score_repetition


all_headers = ['esm', 'famil', 'keshvar', 'rang', 'ashia', 'ghaza']
def calculate_all():
    for i, header in enumerate(all_headers):
        username_has_empty, score_unique, score_repetition = score_table(header=header)
        lst_username_valid_ans = valid_user_ans(header)
        calculate_score(header,  username_has_empty, lst_username_valid_ans, score_unique, score_repetition)


    return score


