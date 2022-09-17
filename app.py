from flask import Flask, render_template, request,redirect,session
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["restro"]
r = mydb["r"]
r2 = mydb["r2"]
r3 = mydb["r3"]
r4 = mydb["r4"]
r5 = mydb["r5"]


app = Flask(__name__)
app.config['SECRET_KEY']="gdfgdfgdfg"

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/home.html', methods=['GET', 'POST'])
def home():

    return render_template("home.html", **locals())

@app.route('/alldata.html', methods=['GET', 'POST'])
@app.route('/input', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        id = request.form['id']
        itemname = request.form['itemname']
        itemdetails = request.form['itemdetails']
        price = request.form['price']


        data = {"id": id, "itemname": itemname, "itemdetails": itemdetails, "price": price}
        r.insert_one(data)

    return render_template("alldata.html", **locals())

@app.route('/showitem', methods=['GET', 'POST'])
@app.route('/stdinfo.html', methods=['GET', 'POST'])
@app.route('/show', methods=['GET', 'POST'])
def input_show():
    list = []
    for st in r.find():
        list.append(st)
    return render_template("stdinfo.html", **locals())


@app.route('/another.html', methods=['GET', 'POST'])
@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        itemid = request.form['itemid']
        orderaddress = request.form['orderaddress']
        orderphone = request.form['orderphone']



        sata = {"itemid": itemid, "orderaddress": orderaddress, "orderphone": orderphone}
        r3.insert_one(sata)

        list = []
        for odr in r3.find():
            list.append(odr)
    return render_template("another.html", **locals())

@app.route('/signup', methods=['GET', 'POST'])
@app.route('/registration', methods=['GET', 'POST'])
@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        uname = request.form["name"]
        pass1 = request.form["pass1"]
        pass2 = request.form["pass2"]
        email = request.form["email"]
        okay = 1
        passMsg = 0
        unameMsg = 0
        scsmsg = ""
        if pass1 != pass2:
            passMsg = 1
            okay = 0
        elif len(uname) < 8:
            unameMsg = 1
            okay = 0
        else:
            if okay == 1:
                data = {"uname": uname, "pass": pass2}
                r4.insert_one(data)
                scsmsg += "Successfully Registered"
                return render_template("r1.html", **locals())
    return render_template("signup.html", **locals())


@app.route('/login', methods=['GET', 'POST'])
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form["name"]
        pass1 = request.form["pass"]
        find = list(r4.find({"uname": uname, "pass": pass1}))
        scsmsg = 0
        if bool(find):
            print(request.form)
            session["name"] = request.form["name"]
            return redirect("/index.html")
        else:
            scsmsg = 1
    return render_template("login.html", **locals())

@app.route('/timer.html', methods=['GET', 'POST'])
def timer():

    return render_template("timer.html", **locals())
@app.route('/booking', methods=['GET', 'POST'])
@app.route('/booking.html', methods=['GET', 'POST'])
@app.route('/book', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        bkname = request.form['bkname']
        bknmbr = request.form['bknmbr']
        bkevent = request.form['bkevent']
        bkphone = request.form['bkphone']
        gender = request.form['gender']
        bkname2 = request.form['bkname2']
        bktrnsnmbr2 = request.form['bktrnsnmbr2']
        bkamount = request.form['bkamount']



        lata = {"bkname": bkname, "bknmbr": bknmbr, "bkevent": bkevent, "bkphone": bkphone,"gender": gender, "bkname2": bkname2, "bktrnsnmbr2": bktrnsnmbr2, "bkamount": bkamount, }
        r2.insert_one(lata)
    return render_template("booking.html", **locals())

@app.route('/index')
@app.route('/index.html')
def index():
    if "name" in session.keys():
        name= session["name"]


    else:
        name="name not found"
    return render_template("index.html", name=name)


@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    session.clear()
    return redirect("/")





#admin

@app.route('/admin', methods=['GET', 'POST'])
@app.route('/adminsign', methods=['GET', 'POST'])
@app.route('/adminsign.html', methods=['GET', 'POST'])
def adminsignup():
    if request.method == 'POST':
        uname = request.form["name"]
        pass1 = request.form["pass1"]
        pass2 = request.form["pass2"]
        email = request.form["email"]
        okay = 1
        passMsg = 0
        unameMsg = 0
        scsmsg = ""
        if pass1 != pass2:
            passMsg = 1
            okay = 0
        elif len(uname) < 8:
            unameMsg = 1
            okay = 0
        else:
            if okay == 1:
                data = {"uname": uname, "pass": pass2}
                r5.insert_one(data)
                scsmsg += "Successfully Registered"
                return render_template("adminr1.html", **locals())
    return render_template("adminsign.html", **locals())


@app.route('/adminlog', methods=['GET', 'POST'])
@app.route('/adminlog.html', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        uname = request.form["name"]
        pass1 = request.form["pass"]
        find = list(r5.find({"uname": uname, "pass": pass1}))
        scsmsg = 0
        if bool(find):
            print(request.form)
            session["name"] = request.form["name"]
            return redirect("/alldata.html")
        else:
            scsmsg = 1
    return render_template("adminlog.html", **locals())















if __name__ == '__main__':
    app.run(debug=True)
