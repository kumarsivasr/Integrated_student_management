import sqlite3 as sl
databs=sl.connect('management.db')
cur=databs.cursor()

# query="""
# create table student(
# sid integer primary key AutoIncrement,
# sname text not null,
# phno integer unique not null check(length(phno)=10),
# dob date not null,
# gender varchar(2) not null,
# address text not null,
# photo blob not null
# )
# """
# cur.execute(query)


import streamlit as st

def login():
    user_name=st.text_input('USER_NAME:')
    password=st.text_input('PASSWORD',type="password")
    login=st.button('LOGIN',type='primary')
    if login:
        if user_name=='admin' and password=='Admin@123':
            st.session_state.is_logged=True
            st.success('login successfull')
            st.rerun()

def add():
    sname=st.text_input('enter your name:')
    phno=st.number_input('enter your phno:',min_value=0)
    dob=st.date_input('choose the date:')
    address=st.text_area('enter your address')
    gender=st.radio('choose the gender',['male','female'])
    photo=st.file_uploader('upload your photo',type=['jpg','png','svg','img'])
    insert=st.button('BUTTON',type='primary')
    if insert:
        query='insert into student(sname,phno,dob,address,gender,photo) values(?,?,?,?,?,?)'
        photo_in_binary=photo.read()
        cur.execute(query,(sname,phno,dob,address,gender,photo_in_binary))
        databs.commit()
        st.success('data inserted......')





def rem():
    sno=st.text_input('ENTER YOUR SID:')
    delete=st.button('BUTTON',type='primary')
    if delete:
        query='delete from student where sid=?'
        cur.execute(query,(sno,))
        databs.commit()
        st.success('data removed.....')




def change_name():
    id=st.number_input('enter your sid:',min_value=0)
    new_name=st.text_input('enter your new_name:')
    upd=st.button('BUTTON',type="primary")
    if upd:
        query="update student set sname=? where sid=?"
        cur.execute(query,(new_name,id))
        databs.commit()
        st.success('updated.....')

def change_phno():
    id=st.number_input('enter your sid:',min_value=0)
    new_phno=st.number_input('enter your new phno:',min_value=0)
    upd=st.button('BUTTON',type='primary')
    if upd:
        query='update student set phno=? where sid=?'
        cur.execute(query,(new_phno,id))
        databs.commit()
        st.success('updated......')
def change_dob():
    id=st.number_input('enter your sid:',min_value=0)
    new_dob=st.date_input('enter your new_dob')
    upd=st.button('BUTTON',type='primary')
    if upd:
        query='update student set dob=? where sid=?'
        cur.execute(query,(new_dob,id))
        databs.commit()
        st.success('updated.....')
def change_gender():
    id=st.number_input('enter your sid:',min_value=0)
    change_gen=st.radio('choose the gender',['male','female'])
    upd=st.button('BUTTON',type='primary')
    if upd:
        query='update student set gender=? where sid=?'
        cur.execute(query,(change_gen,id))
        databs.commit()
        st.success('updated......')


def change_add():
    id=st.number_input('enter your sid',min_value=0)
    change_add=st.text_area('enter your add:')
    upd=st.button('BUTTON',type='primary')
    if upd:
        query='update student set address=? where sid=?'
        cur.execute(query,(change_add,id))
        databs.commit()
        st.success('updated....')

def change_pic():
    id=st.number_input('enter your sid:',min_value=0)
    change_pic=st.file_uploader('upload the photo:',type=['jpg','png','svg','img'])
    upd=st.button('BUTTON',type='primary')
    if upd:
        query='update student set photo=? where sid=?'
        photo_chg=change_pic.read()
        cur.execute(query,(photo_chg,id))
        databs.commit()
        st.success('updated.....')


def upd():
    menu=['to change the name','to change the phno','to change the dob','to change the gender','to change the address','to change the photo']
    op=st.selectbox('choose the thing to update',menu)
    if op=='to change the name':
        change_name()
    elif op=='to change the phno':
        change_phno()
    elif op=='to change the dob':
        change_dob()
    elif op=='to change the gender':
        change_gender()
    elif op=='to change the address':
        change_add()
    else:
        change_pic()



def dis():
    query="select * from student"
    data=cur.execute(query).fetchall()
    header=['SID','SNAME','PHNO','DOB','GENDER','ADDRESS','PHOTO']
    cols=st.columns(len(header))
    for column_name,column in zip(header,cols):
        column.markdown(column_name)
    for row in data:
        c1,c2,c3,c4,c5,c6,c7 = st.columns(7)
        c1.write(row[0])
        c2.write(row[1])
        c3.write(row[2])
        c4.write(row[3])
        c5.write(row[4])
        c6.write(row[5])
        c7.image(row[6])





if 'is_logged' not in st.session_state:
    st.session_state.is_logged=False

if st.session_state.is_logged:
    menu=['add the student','remove the student','update the student','display the student']
    option=st.radio('CHOOSE',menu)
    if option=='add the student':
        add()
    elif option=='remove the student':
        rem()
    elif option=='update the student':
        upd()
    elif option=='display the student':
        dis()
else:
    login()