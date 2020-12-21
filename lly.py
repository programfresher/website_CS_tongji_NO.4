import pymysql

def create_user(user_name,password,sex,sign,email):
#建立新用户
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('select max(id) from user')
    cursor.execute(sql)
    results=cursor.fetchone()
    max_id=results[0]#获取当前最大id
    '''user_name='abcde'
    #从前端获取的用户名
    password="12345678"#从前端获取的密码
    sex="男"
    sign="哈哈哈哈"
    email="111111"#从前端获取'''
    sql2="insert into user(id,username,password,sex,sign,email) values(%d,'%s','%s','%s','%s','%s')" % (max_id+1,user_name,password,sex,sign,email)
    cursor.execute(sql2)
    conn.commit()
    cursor.close()
    conn.close()

def renew_user_info(user_id,user_name_new,password_old,password_new,sign,email):
#更新用户信息
#变量名依次为用户id，新用户名，旧密码，新密码，改动后的签名，改动后的邮箱
#功能：必须旧密码输入正确才能修改信息，签名和邮箱和用户名可为空
    conn=pymysql.connect('localhost',user="root",port=3306,password="1210",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('select password from user where user_id=(%d)'%(user_id))
    cursor.execute(sql)
    results=cursor.fetchone()
    if results[0]==password_old:
        sql2=('update user set password=("%s") where id=(%d)'\
            %(password_new,user_id))
        cursor.execute(sql2)
        if user_name!="":
            sql5=('update user set username=("%s")where id=(%d)'%(user_name_new,user_id))
            cursor.execute(sql5)
        if sign!="":#签名与邮箱和用户名可以不修改，可为空
            sql3=('update user set sign=("%s") where id=(%d)'\
            %(sign,user_id))
            cursor.execute(sql3)
        if email!="":
            sql4=('update user set email=("%s") where id=(%d)'\
            %(email,user_id))
            cursor.execute(sql4)
        conn.commit()
        cursor.close()
        conn.close()
    else:
        conn.commit()
        cursor.close()
        conn.close()
        return 0#表示用户输入的原密码不匹配，返回值为0

def give_likes(user_id,building_name):
#用户点赞
#参数为用户id和建筑名字
#功能：如果用户未点过赞，则赞正常加一；如果在该建筑物点过赞，则函数返回0
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('select 1 from likes where object_name=("%s")&&user_id=(%d)'%(building_name,user_id))
    cursor.execute(sql)
    results=cursor.fetchone()
    #print(results)
    if(results!=None):
        return 0
        #表示该用户已经在该建筑物点过赞，返回值为0
    else:
        sql2=('select like_num_building from building where name=("%s")'%(building_name))
        cursor.execute(sql2)
        results2=cursor.fetchone()
        if results2!=None:
            old_like_num=results2[0]
            sql3=('update building set like_num_building=(%d) where name=("%s")' \
            %(old_like_num+1,building_name))
            cursor.execute(sql3)
        #表示未点过赞，数据库中点赞数加1
            sql4=('insert into likes values(%d,"%s")'\
            %(user_id,building_name))
            cursor.execute(sql4)
        #并在管理点赞的表中增添一条
        else:
            sql3=('select like_num_food from food where name=("%s")'%(building_name))
            cursor.execute(sql3)
            result3=cursor.fetchone()
            old_like_num=result3[0]
            sql4=('update food set like_num_food=(%d) where name=("%s")'%(old_like_num+1,building_name))
            cursor.execute(sql4)
            sql5=('insert into likes values(%d,"%s")'%(user_id,building_name))
            cursor.execute(sql5)
    conn.commit()
    cursor.close()
    conn.close()


def give_likes2(user_id,building_name):
#用户点赞
#参数为用户id和建筑名字
#功能：如果用户未点过赞，则赞正常加一；如果在该建筑物点过赞，则函数返回0
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('select 1 from likes where object_name=("%s")&&user_id=(%d)'%(building_name,user_id))
    cursor.execute(sql)
    results=cursor.fetchone()
    #print(results)
    if(results!=None):
        return 0
        #表示该用户已经在该建筑物点过赞，返回值为0
    else:
        sql2=('select like_num_food from food where name=("%s")'%(building_name))
        cursor.execute(sql2)
        results2=cursor.fetchone()
        old_like_num=results2[0]
        sql3=('update food set like_num_food=(%d) where name=("%s")' \
            %(old_like_num+1,building_name))
        cursor.execute(sql3)
        #表示未点过赞，数据库中点赞数加1
        sql4=('insert into likes values(%d,"%s")'\
            %(user_id,building_name))
        cursor.execute(sql4)
        #并在管理点赞的表中增添一条
    conn.commit()
    cursor.close()
    conn.close()

def login_user(user_name,password):
#用户登录
#如果无用户名，返回0  如果用户名和密码不匹配，返回2   如果匹配，返回1
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('SELECT `password` FROM USER WHERE username=("%s")' %(user_name))
    cursor.execute(sql)
    results=cursor.fetchone()
    if results==None:
        return 0
    else :
        passwd_final=results[0]
        if password==passwd_final:
            return 1
        else:
            return 2
    conn.commit()
    cursor.close()
    conn.close()

def get_user(user_name):
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('SELECT * FROM USER WHERE username=("%s")' %(user_name))
    cursor.execute(sql)
    results=cursor.fetchone()
    return results;
    conn.commit()
    cursor.close()
    conn.close()

def get_object(object_name):
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('SELECT * FROM building WHERE name=("%s")' %(object_name))
    cursor.execute(sql)
    results=cursor.fetchall()
    if results==():
        sql2=('SELECT * FROM food WHERE name=("%s")' %(object_name))
        cursor.execute(sql2)
        results2 = cursor.fetchall()
        return results2
    else:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    conn.commit()
    cursor.close()
    conn.close()

def get_user_cxk():
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('select id_yjh from id')
    cursor.execute(sql)
    result=cursor.fetchone()
    sql2=('select *from user where id=(%d)'%(result[0]))
    cursor.execute(sql2)
    result2=cursor.fetchall()
    return  result2
    conn.commit()
    cursor.close()
    conn.close()
print(get_user_cxk())
# conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
# cursor=conn.cursor()
# #所有调用都要加这两句话

# #建筑物部分：
# #a为你定义的变量,即想要得到的值  
# #调用建筑物投票数
# b='安楼'
# sql=('select like_num from building where name=("%s")' %(b))
# cursor.execute(sql)
# results=cursor.fetchone()
# a=results[0]
# #调用建筑物简介
# b='安楼'
# sql=('select intro from building where name=("%s")' %(b))
# cursor.execute(sql)
# results=cursor.fetchone()
# a=results[0]
# #调用建筑物图片
# b='安楼'
# sql=('select picture from building where name=("%s")' %(b))
# cursor.execute(sql)
# results=cursor.fetchone()
# a=results[0]
# #调用建筑物排名
# b='安楼'
# sql=('select rank from building where name=("%s")' %(b))
# cursor.execute(sql)
# results=cursor.fetchone()
# a=results[0]


# #个人信息部分
# #a为你定义的变量,即想要得到的值
# #调用个人的
# b=用户id
# sql=('select 想要的内容 from user where id=(%d)' %(b))
# cursor.execute(sql)
# results=cursor.fetchone()
# a=results[0]
# #其他的类似

# #调用评论
# #a为你定义的变量，即想得到的评论
# b=用户id或建筑id
# sql=('select content from user where user_id=(%d)' %(b))
# #建筑id 就把 user_id改为building_id
# #想得到用户id就把content改为user_id

def comment(contents,user_id,object_name):
    #评论功能
    #输入参数为评论内容，用户id,物的名字
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('insert into comments values(%d,"%s","%s")'%(user_id,object_name,contents))
    cursor.execute(sql)
    result=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return result

def rank_food():
    #对各个食物投票数进行排序,并把排名再储存到数据库中
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('select like_num_food from food' )
    cursor.execute(sql)
    result=cursor.fetchall()
    list=[0,0,0,0,0,0,0,0,0,0]
    list_forbid_rep=[0,0,0,0,0,0,0,0,0,0]
    for i in range(0,6):
        list[i]=result[i][0]
    list.sort(reverse=True)
    for i in range(0,6):
        sql2=('update food set rank_food=(%d) where like_num_food=(%d) '%(i+1,list[i]))
        cursor.execute(sql2)
    sql3=('select name from food order by rank_food')
    cursor.execute(sql3)
    result=cursor.fetchall()
    for i in range(0,6):
        list[i]=result[i][0]
    for i in range(0,6):
       sql3=('update food set rank_food=(%d) where name=("%s")'%(i+1,list[i]))
       cursor.execute(sql3)
    conn.commit()
    cursor.close()
    conn.close()


def rank_building():
    #对各个建筑投票数进行排序,并把排名再储存到数据库中
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('select like_num_building from building' )
    cursor.execute(sql)
    result=cursor.fetchall()
    list=[0,0,0,0,0,0,0,0,0,0]
    list_forbid_rep=[0,0,0,0,0,0,0,0,0,0]
    for i in range(0,8):
        list[i]=result[i][0]
    list.sort(reverse=True)
    for i in range(0,8):
        sql2=('update building set rank_building=(%d) where like_num_building=(%d) '%(i+1,list[i]))
        cursor.execute(sql2)
    sql3=('select name from building order by rank_building')
    cursor.execute(sql3)
    result=cursor.fetchall()
    for i in range(0,8):
        list[i]=result[i][0]
    for i in range(0,8):
       sql3=('update building set rank_building=(%d) where name=("%s")'%(i+1,list[i]))
       cursor.execute(sql3)
    conn.commit()
    cursor.close()
    conn.close()
rank_building()
def search(search_info):
    #搜索功能
    #输入参数为检索的信息
    #返回值为装载各个符合值的LIST
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    args='%'+search_info+'%'
    sql=("SELECT * FROM building WHERE `name` LIKE ('%s')"%(args) )
    sql2=("select * from food where `name` LIKE ('%s')"%(args))
    cursor.execute(sql)
    result1=cursor.fetchall()
    cursor.execute(sql2)
    result2=cursor.fetchall()
    result3=result1+result2
    result4=['','','','','','','','','','','','','','','','','','','']
    num=0
    for i in result3:
        result4[num]=i[0]
        num+=1
    conn.commit()
    cursor.close()
    conn.close()
    '''for i in result4:
        if i!='':
            print(i)'''
            #调用时参考上面这句
    return result3

def get_rank1(need_rank):
    #获取排名为need_rank的建筑信息
    #输入参数为想获得的排名
    #返回值为装载结果的List
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('SELECT * FROM building WHERE rank_building=(%d)' %(need_rank) )
    #想要获得食物排名只需把上方building换成food
    cursor.execute(sql)
    result=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return result

def get_rank2(need_rank):
    #获取排名为need_rank的食物信息
    #输入参数为想获得的排名
    #返回值为装载结果的List
    conn=pymysql.connect('localhost',user="root",port=3306,password="password",database="website",charset='utf8')
    cursor=conn.cursor()
    sql=('SELECT * FROM food WHERE rank_food=(%d)'%(need_rank) )
    cursor.execute(sql)
    result=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return result
