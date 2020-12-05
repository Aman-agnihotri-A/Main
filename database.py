import sqlite3
from main_script import students
from main_script import teachers
from main_script import rooms
from main_script import datesheet
from itertools import permutations
import random
import eel
import csv

conn=sqlite3.connect('exam_seats.db')
c=conn.cursor()
eel.init('web')
#admin table creation for password and username login
def load_admin():
    with conn:
        c.execute("Insert into admin values(?,?,?)",("aman","aman","AMC_001"))
#admin_create table load up
def admin_create_Table():
    with conn:
        c.execute("""create table admin (
            admin_id text Primary key,
            admin_pwd text,
            colg_id text
            );""")
        load_admin()

@eel.expose
def create_Table():
    with conn:
        c.execute("""create table rooms (
            room_id text Primary key,
            room_name text,
            colg_id text
            );""")
        c.execute("""create table student(
          stud_uin text primary key,
          stud_first text,
          colg_id text
        );""")
        c.execute("""create table college(
        colg_id  text,
        colg_name text,
        colg_address text)
        """)

        c.execute("""
        create table teachers(

            teacher_id text primary key,
            teacher_name text,
            branch text,
            max_duty text,
            colg_id text)
            """)
        c.execute("""
        create table datesheet(

            date text,
            session text,
            room_no text)
            """)

        
   
@eel.expose
def mass_load_student():
    with conn:
        with open('student_data.csv','rt')as f:
            data = csv.reader(f)
            for row in data:
                std=students(str(row[0]),str(row[1]),str(row[2]))
                print(str(std))
                c.execute("Insert into student values(?,?,?)",(std.uin,std.first,std.colg_id))
          
@eel.expose
def mass_load_rooms():
    with conn:
        try:
            with open('std_rooms.csv','rt')as f:
                data = csv.reader(f)
                for row in data:
                    std_rooms=rooms(str(row[0]),str(row[1]),str(row[2]))

                    c.execute("Insert into rooms values(?,?,?)",(std_rooms.room_id,std_rooms.room_name,std_rooms.colg_id))
            mass_load_datesheet()

        except:
            pass
def mass_load_datesheet():
    with conn:
        
        with open('new.csv','rt')as f:
            data = csv.reader(f)
            for row in data:
                print(str(row))
                print(str(row[0]),str(row[1]),str(row[2]))
                std_date=datesheet(str(row[0]),str(row[1]),str(row[2]))
                print(std_date.date,std_date.session,std_date.room_no)
                c.execute("Insert into datesheet values(?,?,?)",(std_date.date,std_date.session,std_date.room_no))
        c.execute(" select * from datesheet")

        room_lis=(c.fetchall())
        print(str(room_lis))
       
# mass_load_datesheet("20-09-2020","AM","15")
@eel.expose
def mass_load_Teachers():
    with conn:
        with open('Teacher.csv','rt')as f:
            data = csv.reader(f)
            for row in data:
                teachers_p=teachers(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]))
                print(str(teachers_p))
                c.execute("Insert into teachers values(?,?,?,?,?)",(teachers_p.teacher_id,teachers_p.teacher_first,teachers_p.branch,teachers_p.max_duty,teachers_p.colg_id))
@eel.expose
def single_load_Teachers(teacher_id,Teacher_First,branch,max_duty,colg_id):
    with conn:
        teachers_p=teachers(teacher_id,Teacher_First,branch,max_duty,colg_id)
        c.execute("Insert into teachers values(?,?,?,?,?)",(teachers_p.teacher_id,teachers_p.teacher_first,teachers_p.branch,teachers_p.max_duty,teachers_p.colg_id))
#single_load_Teachers('1AM17cs','amanns','fjfjfj','AMC_001')
@eel.expose
def delete_single_Teachers(teach):
    with conn:
        c.execute("delete from teachers where teacher_id =(?)",(teach,))
#delete_single_Teachers()
@eel.expose
def assign_rooms():
    with conn:
        c.execute("select stud_uin,stud_first from student where stud_uin like '%CS%'")
        stud=(c.fetchall())
        
        
        c.execute("select stud_uin,stud_first from student where stud_uin like '%ME%'")
        stud1=(c.fetchall())

        c.execute("select stud_uin,stud_first from student where stud_uin like '%IS%'")
        stud2=(c.fetchall())
        
        c.execute("select stud_uin,stud_first from student where stud_uin like '%EE%'")
        stud3=(c.fetchall())

        c.execute("select stud_uin,stud_first from student where stud_uin like '%EC%'")
        stud4=(c.fetchall())

        c.execute("select room_id,room_name from rooms")
        room_io=(c.fetchall())
        

        file2=open("student_room_allotment_export.csv","w")
        # file2.writelines("STUDENT UIN,FIRST NAME,STUDENT UIN,FIRST NAME,ROOM ALOTTED ")
        # file2.writelines("\n")
        counter=1
        l=0
        k=1
        # for i in range (len(stud)-1):
            
        #     j=0
            
        #     count_check=16
        #     if counter<count_check:
        #         if i>=len(stud1):
        #             string1=str(stud[i][j])+","+str(stud[i][j+1])+","+str(stud[i][j+2])+","+""+","+""+","+""+","+str(room_io[l][1])
        #             print(string1)
        #             file2.writelines(string1)
        #             file2.writelines('\n')
        #         else:
        #             string1=str(stud[i][j])+","+str(stud[i][j+1])+","+str(stud[i][j+2])+","+str(stud1[i][j])+","+str(stud1[i][j+1])+","+str(stud1[i][j+2])+","+str(room_io[l][1])
        #             print(string1)
        #             file2.writelines(string1)
        #             file2.writelines('\n')
        #         counter=counter+1
        #     if counter==16:
        #         counter=1
        #         l=l+1
        cse=len(stud)
        me=len(stud1)
        ise=len(stud2)
        ee=len(stud3)
        ec=len(stud4)
        stud_count=0
        d={"stud":cse,"stud1":me,"stud2":ise,"stud3":ee,"stud4":ec}
        print(str(d))
        
        k=0
        o=0
        for i in range (len(room_io)*16):
            
            j=0
            print(i)
            count_check=16
            if counter<count_check:
                for e in range(0,2):         
                    if e%2==0:
                        if i>=cse:
                            if k>=ise:
                                try:
                                    string1=""+","+""+","+""+","+""+","+str(room_io[l][1])
                                    print(string1)
                                    file2.writelines(string1)
                                    file2.writelines('\n')
                                except:
                                    break
                                

                            
                            else:
                                try:
                                    string1=str(stud2[k][j])+","+str(stud2[k][j+1])+","+""+","+""+","+str(room_io[l][1])
                                    print(string1)
                                    file2.writelines(string1)
                                    file2.writelines('\n')
                                    k+=1
                                except:
                                    pass


                        else:
                            try:
                                string1=str(stud[i][j])+","+str(stud[i][j+1])+","+""+","+""+","+str(room_io[l][1])
                                print(string1)
                                
                                file2.writelines(string1)
                                file2.writelines('\n')
                                
                            except:
                                pass
                        
                        
                        

                    else:
                        if i >=me:
                            if k >=ee:
                                try:
                                    string1=""+","+""+","+str(stud4[o][j])+","+str(stud4[o][j+1])+","+str(room_io[l][1])
                                    print(string1)
                                    
                                    file2.writelines(string1)
                                    file2.writelines('\n')
                                    o+=1
                                except:
                                    pass
                            else:
                                string1=""+","+""+","+str(stud3[k][j])+","+str(stud3[k][j+1])+","+str(room_io[l][1])
                                print(string1)
                                
                                file2.writelines(string1)
                                file2.writelines('\n')
                                k+=1

                        else:
                            string1=""+","+""+","+str(stud1[i][j])+","+str(stud1[i][j+1])+","+str(room_io[l][1])
                            print(string1)
                            
                            file2.writelines(string1)
                            file2.writelines('\n')
                counter=counter+1
            if counter==9:
                counter=1
                l=l+1

###########################for next branch####################################################################################################
        # file2.seek(0,2)
        # for i in range (len(room_io)*16):
            
        #     j=0
        #     print(i)
        #     count_check=16
        #     if counter<count_check:
        #         for e in range(0,2):         
        #             if e%2==0:
        #                 try:
        #                     string1=str(stud[i][j])+","+str(stud[i][j+1])+","+""+","+""+","+str(room_io[l][1])
        #                     print(string1)
        #                     file2.writelines(string1)
        #                     file2.writelines('\n')
                            
        #                 except:
        #                     break
                        

        #             else:
        #                 if i >=me:
        #                     string1=""+","+""+","+""+","+""+","+str(room_io[l][1])
        #                     print(string1)
        #                     file2.writelines(string1)
        #                     file2.writelines('\n')

        #                 else:
        #                     string1=""+","+""+","+str(stud1[i][j])+","+str(stud1[i][j+1])+","+str(room_io[l][1])
        #                     print(string1)
        #                     file2.writelines(string1)
        #                     file2.writelines('\n')
        #         counter=counter+1
        #     if counter==9:
        #         counter=1
        #         l=l+1
        print(str(d))
        file2.close() 
        with open('student_room_allotment_export.csv', 'r') as f:
            csvfile = f.readlines()

        linesPerFile = 16
        filename = 1
        # this is better then your former loop, it loops in 1000000 lines a peice,
        # instead of incrementing 1000000 times and only write on the millionth one
        for i in range(0,len(csvfile),linesPerFile):
            l=0
            with open(str(filename) + '.csv', 'w+') as f:
                l+=1
                if filename == 1:
                    f.write("STUDENT UIN,FIRST NAME,STUDENT UIN,FIRST NAME,ROOM ALOTTED ") 
                    f.write("\n")
                elif filename > 1: # this is the second or later file, we need to write the
                    f.write("STUDENT UIN,FIRST NAME,STUDENT UIN,FIRST NAME,ROOM ALOTTED ") 
                    f.write("\n")# header again if 2nd.... file
                f.writelines(csvfile[i:i+linesPerFile])
            filename += 1
    return("Room allotment file is created in the root directory")
# assign_rooms()


def assign_Teachers():
    with conn:
        c.execute("select * from teachers")
        tech_list=(c.fetchall())
        c.execute("select * from rooms")
        room_io=(c.fetchall())
        

def show_std():
    with conn:
        c.execute("select * from teachers")
        show=(c.fetchall())
        print(show)
       

#show_std()
#assign_rooms()
@eel.expose
def example_extract():

    with conn:

        c.execute("select teacher_name,max_duty from teachers")

        f=c.fetchall()
        # print(str(f))

        c.execute(" select date,session,room_no from datesheet")

        room_lis=(c.fetchall())
        # print(len(room_lis))

        

    teachlist=list(f)
    # print(teachlist)
    actual_room=list(room_lis)
    # print(actual_room[0][2])
    string1="Teacher Allotment Schedule"

    
    tempo_list=[]
    count=1
    d={}
    # y=[]
    for i in range(len(actual_room)-1):

        print("teacher allocated for ",str(room_lis[i][0])," schedule")
        # print(str(actual_room[i][1]))
        if len(teachlist) == 0: 
            print("the most outer loop")
            exit()
            print(len(teachlist),"file has no more teachers left")
        if i ==0:
            if actual_room[i][1] =="AM":
                tempo_list=list(teachlist)
        else:
            if actual_room[i][1] =="AM":
                tempo_list.clear()
                tempo_list=list(teachlist)
            
        
    
        

        file1=open(string1+str(room_lis[i][0])+str(room_lis[i][1])+".csv",'w')

        string3="Teacher_First"+','+"SESSION"+","+"DATE\n"

        file1.writelines(string3)

        count=count+1
        b=str(room_lis[i][2])
        # print(b)
        for k in range(int(b)):

            j=0

            

            # current=str(actual_room[i][0])

            try:
                if len(tempo_list)==0:
                    print("AMAN AMAN")
                    exit()
                else:
                    temp=random.choice(tempo_list)
            except:
                d=sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
                print(d)
            # print(temp[j][1])

            
            if str(temp[j]) in d:
                d[str(temp[j])]+=1
                # print(temp[1])
                m=temp[1]
                if d[str(temp[j])]==int(m):
                    try:
                        print("hello")
                        print(teachlist.remove(temp),temp[j])
                        print(tempo_list.remove(temp),temp[j])
                        
                        if len(tempo_list)==0 and k!=int(b):
                            print("INDEX OUT OF RANGE")
                            tempo_list.clear()
                            tempo_list=list(teachlist)
                            # exit()
                        else:
                            temp=random.choice(tempo_list)
                    except Exception as e:
                        print('Error! Code: {c}, Message, {m}'.format(c = type(e).__name__, m = str(e)))
                        print(d)
                        exit()
                    
            else:
                d[str(temp[j])]=1
            # print(str(d))
            
                
        
            string2=str(temp[j])+','+str(actual_room[i][1])+','+str(actual_room[i][0])+"\n"

            file1.writelines(string2)

            

            tempo_list.remove(temp)
        

        file1.close()
    print(d)


#example_extract()

@eel.expose
def login(uname,pwd):
    with conn:
        c.execute("select admin_id,admin_pwd from admin")
        admin_val=list(c.fetchall())
        if str(admin_val[0][0])== str(uname) and str(pwd)== str(admin_val[0][1]):
            string1="welcome, "+str(admin_val[0][0])
            return("success")
        else:
            return("please Check Your Login Details and Try again.")
# admin_create_Table()
# load_admin()
eel.start("index.html")
conn.commit()
conn.close()