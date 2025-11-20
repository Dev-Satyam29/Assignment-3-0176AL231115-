import os
import datetime
user_file="student.txt"
score_file="quiz_score.txt"
def fetch_user():
    users={}
    if os.path.exists(user_file):
        with open(user_file,'r')as file:
            for line in file:
                data=line.strip().split(",")
                if len(data)>=7:
                    enroll, name, email, branch, year, contact, password=data
                    users[enroll]={
                        'name':name,
                        'email':email,
                        'branch':branch,
                        'year':year,
                        'contact':contact,
                        'password':password,
                    }
    return users
def save_users(users):
    with open(user_file, "a") as f:
        for enroll, info in users.items():
            f.write(f"{enroll},{info['name']},{info['email']},{info['branch']},{info['year']},{info['contact']},{info['password']}\n")
def save_score(enroll, category, score, total):
    with open(score_file, "a") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{enroll},{category},{score}/{total},{now}\n")
def result():
    if os.path.exists(score_file):
        with open(score_file,"r") as  file:
            for lines in file.readlines():
                return(lines.strip().split(" "))
    return []

