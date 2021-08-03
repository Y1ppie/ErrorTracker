'''
Classes File
To make all the classes for easy retrieval in the execution python file
Josh Yip
'''
#imports
from configparser import ConfigParser;

import cx_Oracle;
from flask_table import table
from flask_table.columns import Col
from flask_table.table import Table


#from auth0.v3.authentication import Social; #could have used auth0 for simpler authentication
#classes
class Connect:
    """
    -------------------------------------------------------
    Provides Python connection to oracle
[database]
user = ab
password = abcd1234
host = 192.168.29.161
database = PYTHON_FIRST
    Note: must actually connect and startup database (wherever it is hosted) before initializing the database
          if aready started database, dont worry about it then
    -------------------------------------------------------
    """
    connection = None
    cursor = None
    #this ensures there was no previous connection

    
    def please(user, pswrd): #dont neccessarily need self for methods
 
        # Read the contents of the option file
        files=open("logintemp.txt", "w")
        files.write("[database]"+ "\n"+"username = "+str(user)+"\n"+"password = " +str(pswrd)+"\n"+"database = PYTHON_FIRST")
        return files.close()
    
    
    
    
    
    def attempt(): #dont neccessarily need self for methods
        """
        -------------------------------------------------------
        Initialize a MySQL database connection object.
        Use: connection = Connect(option_file)
        -------------------------------------------------------
        Parameters:
            logininfo = login info provided by portal(both username and password)
                        would be part of the connection string in the cx_Oracle.connect("...")
        Returns:
            A database connection object (Connect)
        -------------------------------------------------------
        """
        # Read the contents of the option file
        '''config = ConfigParser()
        config.read_file(open(logininfo))
        # Extract the database section into a dictionary
        params = dict(config['database'])
        params['raise_on_warnings'] = True
        params['use_unicode'] = True
        params['autocommit'] = True
        
        username=params['username']
        password=params['password']'''
        logininfod='ab'+"/"+'abcd1234'+"@//wcp12cr2:1521/orcl"
        return logininfod
        #conn = cx_Oracle.connect("ab/abcd1234@//192.168.29.160:1521/orcl");


   
class converter:#converts oracle output to html table
    def printing(param):
        items=[]
        items2=[]
        finallist=[]   
        for i in range(len(param)):
            rowstr=str(param[i])
            rowstr=rowstr.replace('(', '')
            rowstr=rowstr.replace(')', '')
            rowstr=rowstr.replace('(', '')
            rowstr=rowstr.replace(')', '')
            rowstr=rowstr.replace('[', '')
            rowstr=rowstr.replace(']', '')
            rowstr=rowstr.replace("'", '')
            #print(rowstr)
            array=list(rowstr.split(','))
            #print(array)
            items.append([])
            items[i].append(array[0])
            items[i].append(array[1])
            items[i].append(array[2])
            items[i].append(array[3])
            items[i].append(array[4])
            items[i].append(array[5])
        for i in range(len(items)):
            items2=items[i]
            newlist = [] 
            newlist.append(items2[0])
            newlist.append(items2[1])
            newlist.append(items2[2])
            newlist.append(items2[3])
            newlist.append(items2[4])
            newlist.append(items2[5])  
            finallist.append(newlist)    
    # Print the html
        return(finallist)
    
    
    
        #return(table.__html__())
    def find(user, pwd): #dont neccessarily need self for methods
      
        statement = """SELECT * FROM USERS_LIST WHERE USERS=:users AND PASSWORD=:pwds"""
        conn=cx_Oracle.connect('ab'+"/"+'abcd1234'+"@//wcp12cr2:1521/orcl")
        cur=conn.cursor()#created cursor
        cur.execute(statement, {'users':user,'pwds':pwd})
        params= cur.fetchall()
        #conn.commit() #CONN.COMMIT acts as a ending punctuation to any SQL attempted statements EXCEPT SELECT
       
        #params= "please"
        if params == []:
            return False
       
        else:
            return True
    
       # conn.commit()#created cursor
    
    
        

        
#class insert:        
   # def plug(param):
        #cur=conn.cursor()#created cursor
        #table should have entries in format: "NAME. ERROR TITLE, CONTACT, PRIORITY, STATUS, INFO, DATE"
        #insert test
        #to be edited out
       # sql_insert="""INSERT INTO PYTHON_FIRST VALUES('bob','Bug Report','7325168926','High','Open','xxxxxxxxxxx', '07/18/21')"""
        #cur.execute(sql_insert)
        
        
        