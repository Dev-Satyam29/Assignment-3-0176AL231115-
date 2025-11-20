#Quiz_logic
import random
from data_handler import save_score,save_users,result
def quiz_logic(filename):
    store=[]
    with open(filename,'r') as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts)==6:
                question=parts[0]
                option=parts[1:5]
                right=parts[5]
                store.append((question,option,right))
    return store
QUIZ_QUESTIONS={
    'DSA':quiz_logic('dsa_ques.txt'),
    'DBMS':quiz_logic('dbms_ques.txt'),
    'PYTHON':quiz_logic('python_ques.txt')
    
}

def quiz_attempt(enroll):
    print("Select a category:DSA,DBMS,PYTHON")
    choice=input("enter the category for which you want to give quiz:").upper()
    if choice not in QUIZ_QUESTIONS:
        print("invalid choice")
        return
    questions=QUIZ_QUESTIONS[choice]
    random.shuffle(questions)
    score=0
    for i,(question,option,right) in enumerate(questions,start=1):
        print(f"Q{i}.{question}")
        for j, opt in enumerate(option, start=1):
            print(f"  {j}. {opt}")
        ans=input("enter the correct the option:")
        if ans in ['1','2','3','4']:
            if ans==right:
                print("correct answer")
                score+=1
            else:
                print("wrong answer")
            
        else:
            print("invalid choice")
    print(f"Final Score:{score}/{len(questions)}")
    save_score(enroll, choice, score, len(questions))
def user_panel(enroll,users):
    while True:
        print("Welcome")
        print("Choose an optuion:")
        print("1.Attempt Quiz")
        print("2.View profile")
        print("3.Update profile")
        print("4.exit")
        choose=int(input("enter the choice:"))
        if choose==1:
            quiz_attempt(enroll)
        elif choose==2:
            u=users[enroll]
            print("User details are:")
            print(f"Name:{u['name']}")
            print(f"Email:{u['email']}")
            print(f"Branch:{u['branch']}")
            print(f"Year:{u['year']}")
            print(f"contact:{u['contact']}")
        elif choose==3:
            print("Modifications")
            users[enroll]["email"] = input("New Email: ")
            users[enroll]["contact"] = input("New Contact: ")
            users[enroll]["branch"] = input("New Branch: ")
            users[enroll]["year"] = input("New Year: ")
            save_users(users)
            print("successfully updated!")
        elif choose==4:
            print("successfully logged out!")
            break
        else:
            print("invalid choice")
def admin_panel():
    print("Welcome Admin")
    records=result()
    if not records:
        print("no record available")
        return
    print("quiz performances are:")
    print( print(f"{'Enrollment No.':<15}{'Category':<15}{'Score':<10}{'Date & Time'}"))
    print("-"*60)
    for rec in records:
        
        parts = rec.strip().split(',')
        if len(parts) == 4:
            enroll, category, score, date = parts
        print(f"{enroll:<15}{category:<15}{score:<10}{date}")
        

        

