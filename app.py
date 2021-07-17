from flask import Flask, render_template, request
import sqlite3 as sql
from forms import *


app = Flask(__name__)


# home
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/show', methods=['GET', 'POST'])
def show():
    form = form_show(request.form)  
    if request.method == 'POST':
        tool = form.tool.data
        text = form.text.data
        # Execute query
        result = ""
        error = ""
        con = sql.connect("db.sqlite3")
        cur = con.cursor()
        if tool == 'Id':
            cur.execute("SELECT * FROM customer WHERE Id = '%s'"%text)
            result = cur.fetchall()
            cur.close()
        elif tool == 'SQL':
            # SELECT * FROM customer
            cur.execute("%s"%text)
            result = cur.fetchall()
            cur.close()
        else:         
            error = "Please select query tool"         
        return render_template('show.html', form=form, result=result, error=error) 
    return render_template('show.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = form_show(request.form)
    error = ""
    msg = ""
    # connected
    con = sql.connect("db.sqlite3")
    cur = con.cursor() 
    # show customer data
    cur.execute("SELECT * FROM customer")
    result = cur.fetchall()
    if request.method == 'POST':
        tool = form.tool.data
        text = form.text.data
        # execute delete
        if tool == '--Select--':
            error = "Please select query tool" 
        else:
            if tool == 'Id':
                cur.execute("DELETE FROM customer WHERE Id = '%s'"%text)
            elif tool == 'SQL':
                # DELETE FROM customer WHERE Id =3
                cur.execute("%s"%text)   
            con.commit()
            msg = "Delete successful"
            # show customer data
            cur.execute("SELECT * FROM customer")
            result = cur.fetchall()
            cur.close() 
        return render_template('delete.html', form=form, result=result, error=error, msg=msg)
    return render_template('delete.html', form=form, result=result)


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    form = form_insert(request.form)
    tool = form.tool.data
    error = ""
    msg = ""
    if request.method == 'POST':
        # connected
        con = sql.connect("db.sqlite3")
        cur = con.cursor()
        # execute insert
        if tool == '--Select--':
            error = "Please select query tool" 
        else:
            if tool == 'Button':
                id = form.id.data
                name = form.name.data
                sex = form.sex.data
                age = form.age.data
                hnum = form.hnum.data
                mnum = form.mnum.data
                if mnum:
                    mnum = str((int(hnum)-1)*10 + int(mnum))
                    cur.execute("Insert INTO customer(Id, Name, Sex, Age, HNum, MNum) VALUES(?, ?, ?, ?, ?, ?)",(id, name, sex, age, hnum, mnum))
                    con.commit()
                    msg = "Insert successful"
            elif tool == 'SQL':
                text = form.text.data
                if text:
                    # Insert INTO customer(Id, Name, Sex, Age, HNum, MNum) VALUES (8, 156, 'Male', 56, 5, 46)
                    cur.execute("%s"%text)  
                    con.commit()
                    msg = "Insert successful"
            cur.execute("SELECT * FROM customer")
            result = cur.fetchall()
            cur.close()
        return render_template('insert.html', form=form, tool=tool, result=result, error=error, msg=msg)
    return render_template('insert.html', form=form, tool=tool)


@app.route('/update', methods=['GET', 'POST'])
def update():
    form = form_update(request.form)
    tool = form.tool.data
    error = ""
    msg = ""
    if request.method == 'POST':
        # connected
        con = sql.connect("db.sqlite3")
        cur = con.cursor()
        # execute insert
        if tool == '--Select--':
            error = "Please select query tool" 
        else:
            if tool == 'Id':
                id = form.id.data
                name = form.name.data
                sex = form.sex.data
                age = form.age.data
                hnum = form.hnum.data
                mnum = form.mnum.data
                # update
                if name:              
                    cur.execute("UPDATE customer SET Name = ? WHERE Id = ?", (name, id))
                    con.commit()
                    msg = "Update successful"
                if sex != '--Select--' and sex:                                    
                    cur.execute("UPDATE customer SET Sex = ? WHERE Id = ?", (sex, id))
                    con.commit()
                    msg = "Update successful"   
                if age:              
                    cur.execute("UPDATE customer SET Age = ? WHERE Id = ?", (age, id))
                    con.commit()
                    msg = "Update successful" 
                if hnum != '--Select--' and hnum:                                    
                    cur.execute("UPDATE customer SET HNum = ? WHERE Id = ?", (hnum, id))
                    con.commit()
                    msg = "Update successful"     
                if mnum != '--Select--' and mnum:
                    cur.execute("SELECT HNum FROM customer WHERE Id = ?", id)
                    hnum = cur.fetchall()[0][0]
                    mnum = str((int(hnum)-1)*10 + int(mnum))                                       
                    cur.execute("UPDATE customer SET MNum = ? WHERE Id = ?", (mnum, id))
                    con.commit()
                    msg = "Update successful"
            elif tool == 'SQL':
                text = form.text.data
                if text:
                    # UPDATE customer SET MNum = 1 WHERE Id = 1
                    cur.execute(text)  
                    con.commit()
                    msg = "Update successful"
            if tool == 'Id' and id:
                cur.execute("SELECT * FROM customer WHERE Id = ?", id)
            else:
                cur.execute("SELECT * FROM customer")         
            result = cur.fetchall()
            cur.close()
        return render_template('update.html', form=form, tool=tool, result=result, error=error, msg=msg)
    return render_template('update.html', form=form, tool=tool)


@app.route('/livein', methods=['GET', 'POST'])
def livein():
    form = form_livein(request.form)
    tool = form.tool.data
    error = ""
    msg = ""
    # connected
    con = sql.connect("db.sqlite3")
    cur = con.cursor()
    # show
    cur.execute("SELECT * FROM customer") 
    result = cur.fetchall()
    if request.method == 'POST':
        if tool == '--Select--':
            error = "Please select query tool" 
        else:
            # show
            cur.execute("SELECT * FROM customer") 
            if tool == 'Button':
                live = form.live.data
                hnum = form.hnum.data
                if hnum:
                    cur.execute("SELECT * FROM customer WHERE HNum %s (?)"%live, hnum)
                    msg = "Query successful"   
            elif tool == 'SQL':
                text = form.text.data
                if text:
                    # SELECT * FROM customer WHERE HNum IN (2,3)
                    cur.execute(text)  
                    msg = "Query successful"
            result = cur.fetchall()
            cur.close()
        return render_template('livein.html', form=form, tool=tool, result=result, error=error, msg=msg)
    return render_template('livein.html', form=form, tool=tool, result=result)


@app.route('/exists', methods=['GET', 'POST'])
def exists():
    form = form_exists(request.form)
    tool = form.tool.data
    error = ""
    msg = ""
    # connected
    con = sql.connect("db.sqlite3")
    cur = con.cursor()
    if request.method == 'POST':
        if tool == '--Select--':
            error = "Please select query tool" 
        else:
            if tool == 'Button':
                exists = form.exists.data
                if exists:
                    cur.execute("SELECT * FROM customer WHERE %s(SELECT * FROM dependent WHERE Id=CId)"%exists)
                    msg = "Query successful"   
            elif tool == 'SQL':
                text = form.text.data
                if text:
                    # SELECT * FROM customer WHERE EXISTS(SELECT * FROM dependent WHERE Id=CId)
                    cur.execute(text)  
                    msg = "Query successful"
            result = cur.fetchall()
            cur.close()
        return render_template('exists.html', form=form, tool=tool, result=result, error=error, msg=msg)
    return render_template('exists.html', form=form, tool=tool)


@app.route('/count', methods=['GET', 'POST'])
def count():
    form = form_count(request.form)
    tool = form.tool.data
    error = ""
    msg = ""
    # connected
    con = sql.connect("db.sqlite3")
    cur = con.cursor()
    if request.method == 'POST':
        if tool == '--Select--':
            error = "Please select query tool" 
        else:
            if tool == 'Button':
                cur.execute("SELECT COUNT(Id) FROM customer")
                msg = "Query successful"   
            elif tool == 'SQL':
                text = form.text.data
                if text:
                    # SELECT COUNT(Id) FROM customer
                    cur.execute(text)  
                    msg = "Query successful"
            result = cur.fetchall()
            cur.close()
        return render_template('count.html', form=form, tool=tool, result=result, error=error, msg=msg)
    return render_template('count.html', form=form, tool=tool)


@app.route('/sum', methods=['GET', 'POST'])
def sum():
    form = form_count(request.form)
    tool = form.tool.data
    error = ""
    msg = ""
    # connected
    con = sql.connect("db.sqlite3")
    cur = con.cursor()
    if request.method == 'POST':
        if tool == '--Select--':
            error = "Please select query tool" 
        else:
            if tool == 'Button':
                cur.execute("SELECT SUM(price) FROM customer, meal WHERE customer.MNum = meal.MNum")
                msg = "Query successful"   
            elif tool == 'SQL':
                text = form.text.data
                if text:
                    # SELECT SUM(price) FROM customer, meal WHERE customer.MNum = meal.MNum
                    cur.execute(text)  
                    msg = "Query successful"
            result = cur.fetchall()
            cur.close()
        return render_template('sum.html', form=form, tool=tool, result=result, error=error, msg=msg)
    return render_template('sum.html', form=form, tool=tool)


if __name__ == "__main__":
    app.run(debug=True)