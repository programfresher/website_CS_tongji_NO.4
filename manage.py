#导入flask
from flask import Flask,render_template,request,escape,url_for,redirect
import lly
import pymysql

#创建一个app应用
#__name__指向程序所在的包
app=Flask(__name__,static_folder='static',static_url_path="/static")

# #装饰器的作用：将路由映射到视图函数
# @app.route('/')
# def index():
#     return 'hello world'



#模板 ->html
#后端传数据到前端
@app.route('/',methods=['GET','POST'])
def index():
    ss=["cxk1","cxk2","cxk3"]
    # for i in cxk:
    #     if i=='':
    #         break
    #     else:
    #         conn = pymysql.connect('localhost', user="root", port=3306, password="password", database="website",
    #                                charset='utf8')
    #         cursor = conn.cursor()
    #         sql_search=('select*from ')
    return render_template("index.html")

@app.route('/2',methods=['GET','POST'])
def index2():
    if request.method == 'POST':
        wd=request.form.get("wd")
        cxk = lly.search(wd)
        print(cxk)
        return render_template("index2.html", cxk=cxk)
    cxk = lly.search("")
    return render_template("index2.html", cxk=cxk)

@app.route('/3',methods=['GET','POST'])
def index3():
    lly.rank_building()
    building1=lly.get_rank1(1)
    building2=lly.get_rank1(2)
    building3=lly.get_rank1(3)
    lly.rank_food()
    food1=lly.get_rank2(1)
    food2=lly.get_rank2(2)
    food3=lly.get_rank2(3)
    return render_template("index3.html",building1=building1,building2=building2,building3=building3,food1=food1,food2=food2,food3=food3)

@app.route('/4',methods=['GET','POST'])
def index4():
    uuu=lly.get_user_cxk()
    if uuu==():
        return redirect(url_for("login"))
    if request.method == 'POST':
        a1 = request.form.get("user_name")
        a2 = request.form.get("old_pwd")
        a3 = request.form.get("new_pwd")
        a4 = request.form.get("new_mail")
        print(a1)
        print(a2)
        print(uuu)
        if(a2==uuu[0][3]):
            if(a1):
                conn = pymysql.connect('localhost', user="root", port=3306, password="password", database="website",charset='utf8')
                cursor = conn.cursor()
                sql=('update user set username=("%s") where id=(%d)' %(a1,uuu[0][1]))
                cursor.execute(sql)
                conn.commit()
                cursor.close()
                conn.close()
            if(a3):
                conn = pymysql.connect('localhost', user="root", port=3306, password="password", database="website",charset='utf8')
                cursor = conn.cursor()
                sql=('update user set password=("%s") where id=(%d)' %(a3,uuu[0][1]))
                cursor.execute(sql)
                conn.commit()
                cursor.close()
                conn.close()
            if(a4):
                conn = pymysql.connect('localhost', user="root", port=3306, password="password", database="website",charset='utf8')
                cursor = conn.cursor()
                sql=('update user set email=("%s") where id=(%d)' %(a4,uuu[0][1]))
                cursor.execute(sql)
                conn.commit()
                cursor.close()
                conn.close()
        uuu = lly.get_user_cxk()

    return render_template("index4.html",uuu=uuu)

@app.route('/object/<name>/',methods=['GET','POST'])
def object(name):
    wyb=lly.get_object(name)
    return render_template("object.html",wyb=wyb)

@app.route('/object/<name>/1',methods=['GET','POST'])
def object2(name):
    wyb=lly.get_object(name)

    uuu = lly.get_user_cxk()
    print(uuu)
    if(uuu!=()):
        lly.give_likes(uuu[0][1],name)
        lly.rank_building()
        lly.rank_food()
        wyb = lly.get_object(name)
        print(wyb)
        return render_template("object.html",wyb=wyb)
    else:
        return redirect(url_for("login"))

@app.route('/login',methods=['GET','POST'])
def login():
    conn = pymysql.connect('localhost', user="root", port=3306, password="password", database="website",
                           charset='utf8')
    cursor = conn.cursor()
    sql = ('update id set id_yjh=-1')
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    if request.method == 'POST':
        a1=request.form.get("username")
        a2=request.form.get("pwd")
        kunkun=lly.login_user(a1, a2)
        if kunkun==0:
            return render_template("login.html",error="用户名不存在！")
        elif kunkun==2:
            return render_template("login.html",error="好家伙，密码错了！")
        else:
            conn = pymysql.connect('localhost', user="root", port=3306, password="password", database="website",
                                   charset='utf8')
            cursor = conn.cursor()
            user_list=lly.get_user(a1)
            sql=('update id set id_yjh=(%d) '%(user_list[1]))
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route('/zhuce',methods=['GET','POST'])
def zhuce():
    print("注册页面")
    if request.method == 'POST':
        c1=request.form.get("username")
        c2=request.form.get("pwd")
        lly.create_user(c1,c2,"男","好家伙"," ")
        conn = pymysql.connect('localhost', user="root", port=3306, password="password", database="website",charset='utf8')
        cursor = conn.cursor()
        user_list = lly.get_user(c1)
        print(user_list)
        sql = ('update id set id_yjh=(%d) ' % (user_list[1]))
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("index"))
    return render_template("zhuce.html")



@app.route('/photocard',methods=['GET','POST'])
def photocarddemo():
    return render_template("photocarddemo.html")

@app.route('/punish',methods=['GET','POST'])
def punish():
    return "这也能忘，还不好好反思？"

@app.route('/rank1',methods=['GET','POST'])
def rank1():
    lly.rank_building()
    building1=lly.get_rank1(1)
    building2=lly.get_rank1(2)
    building3=lly.get_rank1(3)
    building4=lly.get_rank1(4)
    building5=lly.get_rank1(5)
    building6=lly.get_rank1(6)
    building7=lly.get_rank1(7)
    building8=lly.get_rank1(8)

    print(building3)
    return render_template("rank.html",building1=building1,building2=building2,building3=building3,building4=building4,building5=building5,building6=building6,building7=building7,building8=building8)

@app.route('/rank2',methods=['GET','POST'])
def rank2():
    lly.rank_food()
    food1=lly.get_rank2(1)
    food2=lly.get_rank2(2)
    food3=lly.get_rank2(3)
    food4=lly.get_rank2(4)
    food5=lly.get_rank2(5)
    food6=lly.get_rank2(6)


    return render_template("rank2.html",food1=food1,food2=food2,food3=food3,food4=food4,food5=food5,food6=food6)

# @app.route('/login',methods=["POST"])
# def login():
#     username=request.form.get("username")
#     pwd=request.form.get("pwd")
#     #request.args.get 通过url传参
#     if username=="cxk" and pwd=="123456":
#         return url_for('profile', username=username)
#     else:
#         return render_template("index.html")

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     s="cxk"
#     return 'User %s' % s

# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(escape(username))

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))



if __name__=='__main__':
    #web服务器的入口
    app.run(debug=True)