import mysql.connector
import random

MAXTUPLES = 1000

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="loktak87",
    database="BENCHMARK_PROJECT1"
)

mycursor = mydb.cursor()
"""
mycursor.execute("CREATE DATABASE BENCHMARK_PROJECT1")


mycursor.execute("CREATE TABLE ONEKTUP\
                 (unique1 integer NOT NULL,unique2 integer NOT NULL,two integer NOT NULL,\
                  four integer NOT NULL,ten integer NOT NULL,twenty integer NOT NULL,onePercent integer NOT NULL,\
                  tenPercent integer NOT NULL,twentyPercent integer NOT NULL,fiftyPercent integer NOT NULL,\
                  unique3 integer NOT NULL,evenOnePercent integer NOT NULL,oddOnePercent integer NOT NULL, \
                  stringu1 char(52) NOT NULL, stringu2 char(52) NOT NULL, stringu4 char(52) NOT NULL )")
"""
uniqueL = []
for i in range (MAXTUPLES):
    uniqueL.append(i)
unique1_list = random.sample(uniqueL, k=1000)
unique2_list = sorted(unique1_list)
#print(unique2_list)

def unique1ToString(unique):
    a = list()
    t = ['A','A', 'A', 'A', 'A', 'A','A']
    for i in range(52):
        if (i < 7):
            a.append('A')
        else:
            a.append('x')
    i = 6
    c = 0
    j = 0
    while( i > 0):
        r = int(unique % 26)
        t[i] = chr(ord('A')+ r)
        unique = unique / 26
        i = i - 1
        c = c + 1
    while ( j < c):
        a[j] = t[6 - j]
        j = j + 1
    #convert char list to string
    n = ''
    for x in a:
        n += x
    return n

def string4_(number):
    a = list()
    n = ''
    for i in range(52):
        a.append('x')
    if( number % 4 == 0):
        for j in range (4):
            a[j] = 'A'
    #convert char list to string
        for x in a:
            n += x
    if( number % 4 == 1):
        for j in range (4):
            a[j] = 'H'
        for x in a:
            n += x
    if( number % 4 == 2):
        for j in range (4):
            a[j] = 'O'
        for x in a:
            n += x
    if( number % 4 == 3):
        for j in range (4):
            a[j] = 'V'
        for x in a:
            n += x
    return n



for i in range (MAXTUPLES):
    sql = "INSERT INTO ONEKTUP(unique1, unique2, two, four, ten , twenty, onePercent, \
                                tenPercent, twentyPercent, fiftyPercent, unique3, \
                                evenOnePercent, oddOnePercent, stringu1, stringu2, stringu4 ) \
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, \
                                %s, %s, %s, %s, %s, %s, %s)"
    string_1 = unique1ToString(unique1_list[i])
    string_2 = unique1ToString(unique2_list[i])
    string_4 = string4_(i)
    val = ( unique1_list[i], unique2_list[i], random.choice(unique1_list) % 2, random.choice(unique1_list) % 4, \
            random.choice(unique1_list)% 10, random.choice(unique1_list)% 20, random.choice(unique1_list) % 100, \
            random.choice(unique1_list) % 10, random.choice(unique1_list) % 5, random.choice(unique1_list) % 2, \
            random.choice(unique1_list), (random.choice(unique1_list) % 100) * 2 , \
            ((random.choice(unique1_list) % 100) * 2) + 1, string_1, string_2, string_4)

    mycursor.execute(sql, val)
    mydb.commit()








