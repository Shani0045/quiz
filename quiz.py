# import all necessary library
import time
import sqlite3
import threading

def countdown():  #counter for timer
    global timer
    timer=30
    for i in range(30):
        timer=timer-1
        time.sleep(1)
    print("out of time") 
    
    
while True:   # loop for continuous 
    print("Do you want to take Quiz?yes/no")
    ch=input()
    if ch in ["yes","Yes","YES"]: # for choose your choice yes
        score=0
        print("-----------------Welcome to the Python Quiz----------------\n\n\n")
       
    # define the levels
        print("Choose level of Quiz\n1. Easy\n2. Medium\n3. Hard")
        level=int(input())
        if level==1:
            print("-----------------You are in Level-1 Total time 30 sec your time start now-------------")
            t=threading.Thread(target=countdown)
            t.start()
            while timer>0:
                print("Q1.")
                time.sleep(0.01)
                print("Python was develped by?")
                time.sleep(0.01)
                print("(a) Dennis Ritchie")
                time.sleep(0.01)
                print("(b) James Gosling")
                time.sleep(0.01)
                print("(c) Guido van Rossum")
                time.sleep(0.01)
                print("(d) Bjarne Stroustrup")
                ans=input("enter answer: ")
                
                # create database for matching answer
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from easy where question=1;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("Correct well done!")
                else:
                    print("Incorrect Answer!")
                time.sleep(1)
                if timer==0:
                    break

                print("Q2.")
                time.sleep(0.01)
                print("What is the extension of python file?")
                time.sleep(0.01)
                print("(a) .p ")
                time.sleep(0.01)
                print("(b) .py")
                time.sleep(0.01)
                print("(c) .python")
                time.sleep(0.01)
                print("(d) None of the above")
                ans=input("enter answer: ")
                # database
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from easy where question=2;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("Correct well done!")
                else:
                    print("Incorrect Answer!")

                time.sleep(1)
                if timer==0:
                    break

                print("Q3.")
                time.sleep(0.01)
                print("Python is Object Oriented Programming Language?")
                time.sleep(0.01)
                print("(a) False")
                time.sleep(0.01)
                print("(b) Neither True nor False")
                time.sleep(0.01)
                print("(c) True")
                time.sleep(0.01)
                print("(d) None of these")
                ans=input("enter answer: ")
                
                #database for answer matching
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from easy where question=3;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    print("Correct well done!")
                else:
                    print("Incorrect Answer")
                    score=score+1
                time.sleep(1)
                if timer==0:
                    break

                print("Q4.")
                time.sleep(0.01)
                print("What is used to define a block of code in python?")
                time.sleep(0.01)
                print("(a) Indentation")
                time.sleep(0.01)
                print("(b) Parenthesis")
                time.sleep(0.01)
                print("(c) curly braces")
                time.sleep(0.01)
                print("(d) None of the above")
                ans=input("enter answer: ")
                
                #database for matching answer
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from easy where question=4;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("correct well done!")
                else:
                    print("Incorrect Answer!")
                time.sleep(1)
                if timer==0:
                    break

                print("Q5.")
                time.sleep(0.01)
                print("Single line comment in python?")
                time.sleep(0.01)
                print("(a) *")
                time.sleep(0.01)
                print("(b) @")
                time.sleep(0.01)
                print("(c) //")
                time.sleep(0.01)
                print("(d) #")
                ans=input("enter answer: ")
                
                #database for matching answer
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from easy where question=5;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("Correct well done!") 
                else:
                    print("Incorrect answer!")
                print("plese wait we are collecting your score")
                time.sleep(10)
                if timer==0:
                    break
            if score==5:
                print(f"Very Strong {(score)}")
            elif score==4:
                print(f"Your Score is Strong {(score)}")
            elif score==3:
                print(f"Your Score is Good {(score)}")
            elif score==2:
                print(f"Your Score is Bad {(score)}")
            elif score==1:
                print(f"Your Score is Poor {(score)}")
            else:
                print(f"Your Score is Very Poor {(score)}")

        elif level==2:
            print("-----------------You are in Level-2 Total time 30 sec your time start now-------------")
            t=threading.Thread(target=countdown)
            t.start()
            while timer>0:
                print("Q1.")
                time.sleep(0.01)
                print("which of the following is a python tuple?")
                time.sleep(0.01)
                print("(a) (1,2,3)")
                time.sleep(0.01)
                print("(b) [1,2,3]")
                time.sleep(0.01)
                print("(c) {1,2,3}")
                time.sleep(0.01)
                print('(d) {1:"one",2:"two",3:"three"}')
                ans=input("enter answer: ")
                # create database for matching answer
                
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from medium where question=1;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("Correct well done!")
                else:
                    print("Incorrect Answer!")
                time.sleep(1)
                if timer==0:
                    break

                print("Q2.")
                time.sleep(0.01)
                print("Output of the l=[1,2,3,4,5]  l[-1]?")
                time.sleep(0.01)
                print("(a) (1,2,3,4)")
                time.sleep(0.01)
                print("(b) (5)")
                time.sleep(0.01)
                print("(c) (5,4,3,2,1)")
                time.sleep(0.01)
                print("(d) None of the above")
                ans=input("enter answer: ")
                # database for matchig answer
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from medium where question=2;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("Correct well done!")
                else:
                    print("Incorrect Answer!")

                time.sleep(1)
                if timer==0:
                    break

                print("Q3.")
                time.sleep(0.01)
                print("Output t=(1,2,4,3,8,9) t[1:3]?")
                time.sleep(0.01)
                print("(a) (1,2,4)")
                time.sleep(0.01)
                print("(b) (2,4,3)")
                time.sleep(0.01)
                print("(c) (1,2,4,4)")
                time.sleep(0.01)
                print("(d) (2,4)")
                ans=input("enter answer: ")
                 # database for matchig answer
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from medium where question=3;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    print("Correct well done!")
                else:
                    print("Incorrect Answer")
                    score=score+1
                time.sleep(1)
                if timer==0:
                    break

                print("Q4.")
                time.sleep(0.01)
                print("Dictionay is ?")
                time.sleep(0.01)
                print("(a) mutable")
                time.sleep(0.01)
                print("(b) imutable")
                time.sleep(0.01)
                print("(c) Both")
                time.sleep(0.01)
                print("(d) None of the above")
                ans=input("enter answer: ")
                # database for matchig answer
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from medium where question=4;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("correct well done!")
                else:
                    print("Incorrect Answer!")
                time.sleep(1)
                if timer==0:
                    break

                print("Q5.")
                time.sleep(0.01)
                print("Output t=(1,2) 2*t?")
                time.sleep(0.01)
                print("(a) (1,2,3,4)")
                time.sleep(0.01)
                print("(b) [2,4]")
                time.sleep(0.01)
                print("(c) [1,2,1,2]")
                time.sleep(0.01)
                print("(d) [1,1,2,2]")
                ans=input("enter answer: ")
                 # database for matchig answer
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from medium where question=5;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("Correct well done!") 
                else:
                    print("Incorrect answer!")
                print("Please wait we are collecting you score")
                time.sleep(10)
                if timer==0:
                    break
            if score==5:
                print(f"Your Score is Very Strong {(score)}")
            elif score==4:
                print(f"Your Score is Strong {(score)}")
            elif score==3:
                print(f"Your Score is Good {(score)}")
            elif score==2:
                print(f"Your Score is Bad {(score)}")
            elif score==1:
                print(f"Your Score is Poor {(score)}")
            else:
                print(f"Your Score is Very Poor {(score)}")
        elif level==3:
            print("-----------------You are in Level-3 Total time 30 sec your time start now-------------")
            t=threading.Thread(target=countdown)
            t.start()
            while timer>0:
                print("Q1.")
                time.sleep(0.01)
                print("Which module in python supports regular expression?")
                time.sleep(0.01)
                print("(a) pyregex")
                time.sleep(0.01)
                print("(b) pyre")
                time.sleep(0.01)
                print("(c) regex")
                time.sleep(0.01)
                print("(d) re")
                ans=input("enter answer: ")
                # create database for matching answer
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from hard where question=1;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("Correct well done!")
                else:
                    print("Incorrect Answer!")
                time.sleep(1)
                if timer==0:
                    break

                print("Q2.")
                time.sleep(0.01)
                print("how to define private variable a in python?")
                time.sleep(0.01)
                print("(a) __a")
                time.sleep(0.01)
                print("(b) private a")
                time.sleep(0.01)
                print("(c) _a")
                time.sleep(0.01)
                print("(d) (a)")
                ans=input("enter answer: ")
                # database
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from hard where question=2;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("Correct well done!")
                else:
                    print("Incorrect Answer!")

                time.sleep(1)
                if timer==0:
                    break

                print("Q3.")
                time.sleep(0.01)
                print("which of the following represent blueprint or templates?")
                time.sleep(0.01)
                print("(a) object")
                time.sleep(0.01)
                print("(b) class")
                time.sleep(0.01)
                print("(c) method")
                time.sleep(0.01)
                print("(d) data field")
                ans=input("enter answer: ")
                # database for matchig answer
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from hard where question=3;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    print("Correct well done!")
                else:
                    print("Incorrect Answer")
                    score=score+1
                time.sleep(1)
                if timer==0:
                    break

                print("Q4.")
                time.sleep(0.01)
                print("which of the following is required to create a new instance of the class?")
                time.sleep(0.01)
                print("(a) A variable")
                time.sleep(0.01)
                print("(b) a value-returning")
                time.sleep(0.01)
                print("(c) A class")
                time.sleep(0.01)
                print("(d) A constructor")
                ans=input("enter answer: ")
               # database for matchig answer
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from hard where question=4;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("correct well done!")
                else:
                    print("Incorrect Answer!")
                time.sleep(1)
                if timer==0:
                    break

                print("Q5.")
                time.sleep(0.01)
                print("which of the following used in create inheritance?")
                time.sleep(0.01)
                print("(a) classA extends classB")
                time.sleep(0.01)
                print("(b) classA:classB")
                time.sleep(0.01)
                print("(c) classA(classB):")
                time.sleep(0.01)
                print("(d) None of the above")
                ans=input("enter answer: ")
                #database
                conn=sqlite3.connect("Quiz.db")
                cur=conn.cursor()
                cur.execute("select answer from hard where question=5;")
                db_ans=cur.fetchone()[0]
                if ans==db_ans:
                    score=score+1
                    print("Correct well done!") 
                else:
                    print("Incorrect answer!")
                print("please wait  we are collecting your score")
                time.sleep(10)
                if timer==0:
                    break
            if score==5:
                print(f"Your Score is Very Strong {(score)}")
            elif score==4:
                print(f"Your Score is Strong {(score)}")
            elif score==3:
                print(f"Your Score is Good {(score)}")
            elif score==2:
                print(f"Your Score is Bad {(score)}")
            elif score==1:
                print(f"Your Score is Poor {(score)}")
            else:
                print(f"Your Score is Very Poor {(score)}")   
        else:
            print("invalid choice")

    else:
        break
