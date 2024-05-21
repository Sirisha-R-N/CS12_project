import mysql.connector as sql
import registration

connect = sql.connect(user='root', host='localhost', password='xxxx', database='residents')
cursor = connect.cursor()

print('*********vaccine registration and appointment system***********')

def appointment():
    
    ans = input('have you already registered?(y/n): ')
    
    if ans == 'n':
        registration.root.mainloop()
        print('please enter your details in the form')
        print('successfully registered')
    
    cursor.execute('select * from residents.resident')
    data = cursor.fetchall()
    resultlist = []
    
    for row in data:
        row = list(row)
        resultlist.append(row)
    length = len(resultlist)
    
    if ans == 'y':
        print("enter the following details: ")
        userid = input('enter your name: ')
        aadhar = input('enter your aadhar number: ')
        
        for i in range(length):
            if userid in resultlist[i]:
                print('user exists')
                break

        fdapp = sdapp = None
        cursor.execute('insert into appointments (Name,
                        aadhar_no, fdappointmnet,
                        sdappointmnet) values(%s,%s,%s,%s)', 
                        (userid, aadhar, fdapp, sdapp))
        while ans == 'y':
            n = int(input('choose one of the following \n 
                           1.set vaccine appointment \n 
                           2.update appointment date\n 
                           3.cancel appointment\n 
                           4.view resident table\n 
                           5.view appointment table\n 
                           6.exit'))
            if n == 1:
                n1 = int(input('1.first dose appointment\n
                                2.second dose appointment \n
                                enter: '))
                if n1 == 1:
                    fdapp = input("enter a date convinient for
                                   you(yyyy-mm-dd): ")
                    cursor.execute('update appointments set 
                                    fdappointmnet = %s where
                                    Name = %s',
                                    (fdapp, userid))
                    print("appointment has been set on ",
                           fdapp)
                if n1 == 2:
                    sdapp = input("enter a date convinient for
                                   you(yyyy-mm-dd): ")
                    cursor.execute('update appointments set
                                   sdappointmnet = %s where
                                   Name = %s',(sdapp, userid))
                    print('appointment has been set on',
                           sdapp)
            if n == 2:
                n1 = int(input('1.first dose appointment\n 
                                2.second dose
                                appointment \n enter: '))
                if n1 == 1:
                    fdapp = input("enter a new date convenient
                                   for you(yyyy-mm-dd): ")
                    cursor.execute('update appointments set
                                   fdappointmnet = %s where
                                  Name = %s', (fdapp, userid))
                    print('appointment has been updated to',
                           fdapp)
                if n1 == 2:
                    sdapp = input("enter a new date convenient
                                   for you(yyyy-mm-dd): ")
                    cursor.execute('update appointments set
                                  sdappointmnet = %s where
                                  Name = %s',(sdapp, userid))
                    print('appointment has been updated to', 
                           sdapp)

            if n == 3:
                n1 = int(input('1.first dose appointment\n
                                2.second dose
                                appointment \n enter: '))
                if n1 == 1:
                    cursor.execute('update appointments set
                                   fdappointmnet = NULL where
                                   Name = %s', (userid,))
                    print('your appointment has been
                           cancelled')
                if n1 == 2:
                    cursor.execute('update appointments set
                                    sdappointmnet = NULL where
                                    Name = %s', (userid,))
                    print('your appointment has been
                           cancelled')
            if n == 4:
                cursor.execute('select * from resident')
                data = cursor.fetchall()
                resultlist = []
                for row in data:
                    row = list(row)
                    resultlist.append(row)
                print(resultlist)

            if n == 5:
                cursor.execute('select * from appointments')
                info = cursor.fetchall()
                relist = []
                for k in info:
                    k = list(k)
                    relist.append(k)
                print(relist)

            if n == 6:
                ans = 'n'
                print('thank you for visiting')
            connect.commit()
            ans = input('do you want to continue (y/n)')


appointment()
