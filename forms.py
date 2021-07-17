from wtforms import Form, StringField, SelectField

class form_show(Form):
    choices = [('--Select--', '--Select--'),
                ('Id', 'Id'),
                ('SQL', 'SQL')]
    tool = SelectField('Query Tool', choices=choices)
    text = StringField('Query Text')


class form_insert(Form):
    choices = [('--Select--', '--Select--'),
                ('Button', 'Button'),
                ('SQL', 'SQL')]
    choices_sex = [('--Select--', '--Select--'),
                ('Male', 'Male'),
                ('Female', 'Female')]                
    choices_num = [('--Select--', '--Select--')]
    for i in range(1,11):
        tmp = (str(i), str(i))
        choices_num.append(tmp)

    tool = SelectField('Tool', choices=choices)
    id = StringField('Id')
    name = StringField('Name')
    sex = SelectField('Sex', choices=choices_sex)
    age = StringField('Age')
    hnum = SelectField('Hostel Num', choices=choices_num)
    mnum = SelectField('Meal Num', choices=choices_num)
    text = StringField('Text')

class form_update(Form):
    choices = [('--Select--', '--Select--'),
                ('Id', 'Id'),
                ('SQL', 'SQL')]
    choices_sex = [('--Select--', '--Select--'),
                ('Male', 'Male'),
                ('Female', 'Female')]                
    choices_num = [('--Select--', '--Select--')]
    for i in range(1,11):
        tmp = (str(i), str(i))
        choices_num.append(tmp)

    tool = SelectField('Tool', choices=choices)
    id = StringField('Id')
    name = StringField('Name')
    sex = SelectField('Sex', choices=choices_sex)
    age = StringField('Age')
    hnum = SelectField('Hostel Num', choices=choices_num)
    mnum = SelectField('Meal Num', choices=choices_num)
    text = StringField('Text')


class form_livein(Form):
    choices = [('--Select--', '--Select--'),
                ('Button', 'Button'),
                ('SQL', 'SQL')]  
    choices_live = [('--Select--', '--Select--'),
                ('IN', 'IN'),
                ('NOT IN', 'NOT IN')]   
    choices_num = [('--Select--', '--Select--')]
    for i in range(1,11):
        tmp = (str(i), str(i))
        choices_num.append(tmp) 
    tool = SelectField('Tool', choices=choices)
    live = SelectField('Live IN or NOT', choices=choices_live)
    hnum = SelectField('Hostel Num', choices=choices_num)
    text = StringField('Text')


class form_exists(Form):
    choices = [('--Select--', '--Select--'),
                ('Button', 'Button'),
                ('SQL', 'SQL')]  
    choices_exists = [('--Select--', '--Select--'),
                ('EXISTS', 'EXISTS'),
                ('NOT EXISTS', 'NOT EXISTS')]   
    tool = SelectField('Tool', choices=choices)
    exists = SelectField('EXIST Dependent or NOT', choices=choices_exists)
    text = StringField('Text')


class form_count(Form):
    choices = [('--Select--', '--Select--'),
                ('Button', 'Button'),
                ('SQL', 'SQL')] 
    tool = SelectField('Tool', choices=choices)
    text = StringField('Text')


class form_age(Form):
    choices = [('--Select--', '--Select--'),
                ('Button', 'Button'),
                ('SQL', 'SQL')]  
    choices_age = [('--Select--', '--Select--'),
                ('MAX', 'MAX'),
                ('MIN', 'MIN'), 
                ('AVG', 'AVG')]
    tool = SelectField('Tool', choices=choices)
    age = SelectField('Find ? Customer Age', choices=choices_age)
    text = StringField('Text')