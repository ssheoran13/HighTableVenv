from flask import Flask, render_template, request, redirect, url_for, session
import re
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import RadioField
import random

def id_gen():
    a=random.randint(10,99)
    b=random.randint(100,999)
    c=random.randint(1000,9999)
    return (str(a)+'-'+str(b)+'-'+str(c))
    # print(str(a)+'-'+str(b)+'-'+str(c))

mydb = mysql.connector.connect(host="Shikhars-MacBook-Pro.local",user="shikhar",password="1234ball",database="db")
print(mydb)

class HitmanForm(FlaskForm):
    # style={'style':'font-size:larger'}
    example = RadioField('Label', choices=[
        (1,'Have a look at your Past Deals'), 
        (2,'Check your account to see the past payments you have received from past deals'),
        (3,' Search for a specific type of deals available'),
        (4,'See all currently available deals')],
         coerce=int
         )

class ContinentalForm(FlaskForm):
    example = RadioField('Label', choices=[
        (1,'Add a new deal to the available deals'), 
        (2,'Add a new hitman to the database'),
        (3,'Add a new supplier to the database'),
        (4,'Edit an available deals details')],
         coerce=int)

class ClientForms(FlaskForm):
    example = RadioField('Label',choices=[
        (1,'Edit an available deals details'),
        (2,'Search the  database for types of hitmen according to a specific type of work'),
        (3,'Propose a new deal for hire'),
        (4,'Check your past deal history ')
    ],coerce=int)

class ServicesForm(FlaskForm):
    example = RadioField('Label',choices=[
        (1,'Find the number of unique goods provided by all the dealers'),
        (2,'Search for deals for specific goods'),
        (3,'Search for the deals in the ascending order of price, or search for the cheapest deals'),
        (4,'Target areas of the cleanup orgs for new dealers')],
        coerce=int)


Hitman_Query_Msg = {1:"You have chosen to search for all your past deals. Leave the below box empty and click submit.",
                    2:"You have chosen to search for the rewards from your past deals. Leave the below box empty and click submit.",
                    3:"You have chosen to search for a particular type of deal from Analysis, Cyber Security, Assassination, Scouting. Enter the category of the type you want to search for in the box below.",
                    4:"You have chosen to search for all types of deals currently available. Please leave the below box empty and click submit."}


Continental_Query_Msg = {1:"You have chosen to add a new deal. Enter the Name of the client, type of work associated with the deal, the payment and the contact information of the client, in this order, in the below box.", 
                        2:"You have chosen to add a new Hitman to the database. Please enter the Name, work he specializes in, region he works in, and contact information of the hitman in the box below, in this order.",
                        3:"You have chosen to add a new supplier to the database. Please enter the Name, goods they provide, their specialization, and contact info in the below box in this order.",
                        4: "You have chosen to edit the details of a deal put up. Enter first the ID of the Bounty, then the detail (Min Time alloted, Price), followed by the new value, in the box below in this order."}

Client_Query_Msg = {1:"You have chosen to edit the details of a deal put up. Enter first the ID of the Deal, then the detail ( Min reward | Client Contact), followed by the new value, in the box below in this order.",
                    2:"You have chosen to search for hitmen for a specific tye of work. Enter the work type (Analysis, Cyber Security, Assassination, Scouting) in the box below.",
                    3:"You have chosen to add a new deal. Enter the your name, type of work associated with the deal, the payment and your contact information, in this order, in the below box.",
                    4:"You have chosen to search for all your past deals. Leave the below box empty and click submit."}

Services_Query_Msg = {1:"You have chosen to search for the number of unique goods provided by all dealers. Leave the below box empty and click submit.",
                      2:"You have chosen to search for deals of specific goods. Enter the type of goods in the box below.",
                      3:"You have chosen to search for the cheapest deals. Leave the box below empty and click on the submit button.",
                      4:"You have chosen to search for the target areas of cleanup organisations for the new dealers. Leave the box below empty and click on the submit button."}


UserType_QueryMsg={"Hitman":Hitman_Query_Msg,"Continental":Continental_Query_Msg,"Client":Client_Query_Msg,"Services":Services_Query_Msg}

# hitmanform=HitmanForm()
# continentalform=ContinentalForm()

# Dict_Forms={"Hitman":hitmanform,"Continental":continentalform}


app = Flask(__name__)

app.secret_key = 'neeluisthebest'


@app.route('/', methods = ['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        print(request.form,"heyyy")
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # print(account)
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            session['type'] = account[4]
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            # print("YOO")
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)


# http://localhost:5000/python/logout - this will be the logout page
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   session.pop('type',None)
   # Redirect to login page
   return redirect(url_for('login'))



# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'type' in request.form:
        # Create variables for easy access
        username = request.form['username']
        usertype = request.form['type']
        password = request.form['password']
        email = request.form['email']
		# Check if account exists using MySQL
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email or not usertype:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s,%s)', (username, password, email,usertype,))
            mydb.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/home',methods=['POST','GET'])
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        print(session)

        
        if session['type']=="Hitman":
            form=HitmanForm()
        elif session['type']=="Continental":
            form=ContinentalForm()
        elif session['type']=='Client':
            form=ClientForms()
        elif session['type']=='Services':
            form=ServicesForm()
        msg=''
        if form.validate_on_submit():
            print(request.form,"nellu")
            serialNo=form.example.data
            if serialNo!=['Not a valid choice']:
                session['queryid']=serialNo
                return redirect(url_for('query_submit'))
            elif serialNo==['Not a valid choice']:
                msg='Please select a query first.'
                # return render_template('queryinput.html',serialNo=serialNo)
            print(serialNo)
        else:
            print("lol")
            print(form.example.errors)
        return render_template('home.html', username=session['username'],form=form,msg=msg)
       
       
        # # if request.method=='POST':
        # print(request.form,"hey")
        # return render_template('home2.html')



    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


# http://localhost:5000/pythinlogin/profile - this will be the profile page, only accessible for loggedin users
@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/query')
def query_submit():
    serialNo=session['queryid']
    usertype=session['type']

    msg=UserType_QueryMsg[usertype][serialNo]
    return render_template('queryinput.html',msg=msg)

@app.route('/queryresult',methods=['POST','GET'])
def run_query():
    if request.method=='POST':
        if session['type']=='Hitman':
            if session['queryid']==1:
                mycursor=mydb.cursor()
                mycursor.execute("select * from `Past Deals`")
                result=mycursor.fetchall()
                print(result)
                head=[ 'Deal ID','Type of deal','Reward','Client Feedback','Date of deal','Client Contact']
                return render_template('queryresult.html',data=result,head=head)
            elif session['queryid']==2:
                mycursor=mydb.cursor()
                mycursor.execute("select `Deal ID`,Reward from `Past Deals`")
                result=mycursor.fetchall()
                head=['Deal ID','Reward']
                return render_template('queryresult.html',data=result,head=head)
            elif session['queryid']==3:
                mycursor=mydb.cursor()
                data=request.form['querydata']
                mycursor.execute("select * from `Deals Proposed` where Work=%s",(data,))
                result=mycursor.fetchall()
                head=['Deal ID','Client ID','idContinentals','Client Name','Work','Min reward','Client Contact']
                return render_template('queryresult.html',data=result,head=head)
            elif session['queryid']==4:
                mycursor=mydb.cursor()
                mycursor.execute("select * from `Deals Proposed`")
                result=mycursor.fetchall()
                head=['Deal ID','Client ID','idContinentals','Client Name','Work','Min reward','Client Contact']

                return render_template('queryresult.html',data=result,head=head)
        elif session['type']=='Continental':
            if session['queryid']==1:
                mycursor=mydb.cursor()
                dealid=id_gen()
                # clientid=id_gen()
                mycursor.execute('select `Client ID` from Clients')
                result=mycursor.fetchall()
                index=random.randint(0,19)
                clientid=result[index][0]
                mycursor.execute('select idContinentals from Continentals')
                result=mycursor.fetchall()
                index=random.randint(0,19)
                contid=result[index][0]
                data=request.form['querydata']
                data=data.split(',')
                mycursor.execute('insert into `Deals Proposed`  values (%s, %s, %s, %s,%s, 	%s, %s)',(dealid,clientid,contid,data[0],data[1],data[2],data[3]))
                mydb.commit()
                row=[(dealid,clientid,contid,data[0],data[1],data[2],data[3])]
                head=['Deal ID','Client ID','idContinentals','Client Name','Work','Min reward','Client Contact']
                msg = 'You have successfully added this deal.'
                return render_template('queryresult.html',data=row,msg=msg,head=head)
            elif session['queryid']==2:
                mycursor=mydb.cursor()
                hitmanid=id_gen()
                mycursor.execute('select `Bounty ID` from Hitman_Bounty')
                result=mycursor.fetchall()
                index=random.randint(0,19)
                bountid=result[index][0]
                data=request.form['querydata']
                data=data.split(',')
                mycursor.execute('insert into All_Hitmans values (%s, %s,%s,%s,%s,%s)',(hitmanid,data[0],data[1],data[2],bountid,data[3]))
                mydb.commit()
                row=[(hitmanid,data[0],data[1],data[2],bountid,data[3])]
                head=['Hitman ID','Name','Specialization','Region','BountyID','Contact']
                msg = 'You have successfully added this hitman.'
                return render_template('queryresult.html',data=row,msg=msg,head=head)
            elif session['queryid']==3:
                dealerid=id_gen()
                mycursor=mydb.cursor()
                data=request.form['querydata']
                data=data.split(',')
                mycursor.execute('insert into Arms_dealer values (%s, %s, 	%s,%s, %s)',(dealerid,data[0],data[1],data[2],data[3]))
                mydb.commit()
                row=[(dealerid,data[0],data[1],data[2],data[3])]
                head=['Dealer ID','Name','Goods Providing','Specialization','Contact']
                msg = 'You have successfully added this dealer.'
                return render_template('queryresult.html',data=row,msg=msg,head=head)
            elif session['queryid']==4:
                mycursor=mydb.cursor()
                data=request.form['querydata']
                data=data.split(',')
                if len(data)==3:
                    if data[1]=='Min Time alloted':
                        mycursor.execute('update `Hitman_Bounty` set `Min Time alloted`=(%s) where `Bounty ID`=(%s)',(data[2],data[0]))
                        mydb.commit()
                        # row=[(dealerid,data[0],data[1],data[2],data[3])]
                        msg = 'You have successfully edited this deal.'
                        return render_template('queryresult.html',data='',msg=msg,head='')
                    elif data[1]=='Price':
                        mycursor.execute('update `Hitman_Bounty` set Price=(%s) where `Bounty ID`=(%s)',(data[2],data[0]))
                        mydb.commit()
                        # row=[(dealerid,data[0],data[1],data[2],data[3])]
                        msg = 'You have successfully edited this deal.'
                        return render_template('queryresult.html',data='',msg=msg,head='')
                elif len(data)==5:
                    mycursor.execute('update `Hitman_Bounty` set `Min Time alloted`=(%s),Price=(%s) where `Bounty ID`=(%s)',(data[2],data[4],data[0]))
                    mydb.commit()
                    # row=[(dealerid,data[0],data[1],data[2],data[3])]
                    msg = 'You have successfully edited this deal.'
                    return render_template('queryresult.html',data='',msg=msg,head='')

        elif session['type']=='Client':
            msg=''
            # print("in client")
            if session['queryid']==1:
                # print("lolol")
                mycursor=mydb.cursor()
                data=request.form['querydata']
                data=data.split(',')
                if len(data)==3:
                    # print("coolio")
                    if data[1]=='Min reward':
                        # print("ok im")
                        mycursor.execute('update `Deals Proposed` set `Min reward`=(%s) where `Deal ID`=(%s)',(data[2],data[0]))
                        mydb.commit()
                        # row=[(dealerid,data[0],data[1],data[2],data[3])]
                        msg = 'You have successfully edited this deal.'
                        return render_template('queryresult.html',data='',msg=msg,head='')
                    elif data[1]=='Client Contact':
                        mycursor.execute('update `Deals Proposed` set `Client Contact`=(%s) where `Deal ID`=(%s)',(data[2],data[0]))
                        mydb.commit()
                        # row=[(dealerid,data[0],data[1],data[2],data[3])]
                        msg = 'You have successfully edited this deal.'
                        return render_template('queryresult.html',data='',msg=msg,head='')
                elif len(data)==5:
                    mycursor.execute('update `Deals Proposed` set `Min reward`=(%s),`Client Contact`=(%s) where `Deal ID`=(%s)',(data[2],data[4],data[0]))
                    mydb.commit()
                    # row=[(dealerid,data[0],data[1],data[2],data[3])]
                    msg = 'You have successfully edited this deal.'
                    return render_template('queryresult.html',data='',msg=msg,head='')
            
            elif session['queryid']==2:
                mycursor=mydb.cursor()
                data=request.form['querydata']
                mycursor.execute('Select * from All_Hitmans where `Specialization`=%s',(data,))
                result=mycursor.fetchall()
                head=['Hitman ID','Name','Specialization','Region','BountyID','Contact']
                return render_template('queryresult.html',data=result,msg=msg,head=head)
            
            elif session['queryid']==3:
                mycursor=mydb.cursor()
                dealid=id_gen()
                # clientid=id_gen()
                mycursor.execute('select `Client ID` from Clients')
                result=mycursor.fetchall()
                index=random.randint(0,19)
                clientid=result[index][0]
                mycursor.execute('select idContinentals from Continentals')
                result=mycursor.fetchall()
                index=random.randint(0,19)
                contid=result[index][0]
                data=request.form['querydata']
                data=data.split(',')
                mycursor.execute('insert into `Deals Proposed`  values (%s, %s, %s, %s,%s, 	%s, %s)',(dealid,clientid,contid,data[0],data[1],data[2],data[3]))
                mydb.commit()
                head=['Deal ID','Client ID','idContinentals','Client Name','Work','Min reward','Client Contact']
               
                row=[(dealid,clientid,contid,data[0],data[1],data[2],data[3])]
                msg = 'You have successfully added this deal.'
                return render_template('queryresult.html',data=row,msg=msg,head=head)
            
            elif session['queryid']==4:
                mycursor=mydb.cursor()
                data=request.form['querydata']
                mycursor.execute('Select * from `Past Deals`')
                result=mycursor.fetchall()
                head=[ 'Deal ID','Type of deal','Reward','Client Feedback','Date of deal','Client Contact']

                return render_template('queryresult.html',data=result,msg=msg,head=head)
        
        elif session['type']=="Services":
            msg=''
            if session['queryid']==1:
                mycursor=mydb.cursor()
                data=request.form['querydata']
                mycursor.execute('select count(distinct(`Goods Providing`)) from Arms_dealer;')
                head=["Number of unique goods provided"]
                result=mycursor.fetchall()
                return render_template('queryresult.html',data=result,msg=msg,head=head)
            elif session['queryid']==2:
                mycursor=mydb.cursor()
                data=request.form['querydata']
                mycursor.execute('select * from `Arms_Dealer` where `Goods Providing`=%s',(data,))
                result=mycursor.fetchall()
                head=[' Dealer ID','Name','Goods Providing','Specialization','Contact']
                return render_template('queryresult.html',data=result,msg=msg,head=head)
            elif session['queryid']==3:
                mycursor=mydb.cursor()
                mycursor.execute('select * from  `Cleanup Org` order by `Min Price` asc')
                result=mycursor.fetchall()
                head=['Org ID','Deal ID','Target Areas','Min Price','Contact']
                return render_template('queryresult.html',data=result,msg=msg,head=head)
            elif session['queryid']==4:
                mycursor=mydb.cursor()
                mycursor.execute('SELECT `Cleanup Org`.`Target Areas`, `Deals Proposed`.`Client Name` FROM `Cleanup Org` INNER JOIN `Deals Proposed` ON `Cleanup Org`.`Deal ID`=`Deals Proposed`.`Deal ID`')
                result=mycursor.fetchall()
                head=['Target Areas','Client Name']
                return render_template('queryresult.html',data=result,msg=msg,head=head)



            




              



        




                




                











  



        # msg=''
        # data=request.form['querydata']
        # # print(request.form)
        # if session['queryid']==1:
        #     username=data
        #     mycursor=mydb.cursor()
        #     mycursor.execute("select * from accounts where username=%s",(username,))
        #     account=mycursor.fetchall()
        #     print(account)
        #     # print(account)
            
        #     return render_template('queryresult.html',data=account)


        # elif session['queryid']==2:
        #     acc_details=data.split(',')
        #     mycursor=mydb.cursor()
        #     mycursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s,%s)', (acc_details[0], acc_details[1], acc_details[2],acc_details[3]))
        #     mydb.commit()
        #     msg = 'You have successfully registered!'

        
        # return render_template('queryresult.html',data='',msg=msg)

if __name__=='__main__':
	app.run(debug=True)

