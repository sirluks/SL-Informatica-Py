from tkinter import *
import tkinter.messagebox as msgbox
import mysql.connector as mysql

def insert():
    id = e_id.get()
    nome = e_nome.get()
    valor = e_valor.get()

    if(id == "" or nome == "" or valor == ""):
        msgbox.showinfo("Aviso", "Não são permitidos campos vazios. Informe um dado válido")
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            password="senac123456789",
            database="registro"
            )
        cursor = con.cursor()
        cursor.execute("INSERT INTO produto (nome, valor) VALUES ('" + nome +"','" + valor +"')")
        con.commit()
        msgbox.showinfo("Aviso", "Dados inseridos com sucesso")

        e_id.delete(0, 'end')
        e_nome.delete(0, 'end')
        e_valor.delete(0, 'end')
        show()
        
        con.close()

def delete():
    if(e_id.get() == ""):
        msgbox.showinfo("Aviso", "Informe um ID Válido")
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            password="senac123456789",
            database="registro"
            )
        cursor = con.cursor()
        cursor.execute("DELETE FROM produto WHERE id='"+ e_id.get() +"'")
        con.commit()
        msgbox.showinfo("Aviso", "Dados deletados com sucesso")

        e_id.delete(0, 'end')
        e_nome.delete(0, 'end')
        e_valor.delete(0, 'end')
        show()
        
        con.close()

def update():
    id = e_id.get()
    nome = e_nome.get()
    valor = e_valor.get()
    
    if(id == "" or nome == "" or valor == ""):
        msgbox.showinfo("Aviso", "Não são permitidos campos vazios. Informe um dado válido")
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            password="senac123456789",
            database="registro"
            )
        cursor = con.cursor()
        cursor.execute("UPDATE produto SET nome ='"+ nome +"', valor ='"+ valor +"' WHERE id='"+ id +"'")
        con.commit()
        msgbox.showinfo("Aviso", "Dados atualizados com sucesso")

        e_id.delete(0, 'end')
        e_nome.delete(0, 'end')
        e_valor.delete(0, 'end')
        show()
        
        con.close()

def get():

    if(e_id.get() == ""):
        msgbox.showinfo("Aviso", "Informe um ID Válido")
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            password="senac123456789",
            database="registro"
            )
        cursor = con.cursor()
        cursor.execute("SELECT * FROM produto WHERE id='"+ e_id.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
            e_nome.insert(0, row[1])
            e_valor.insert(0, row[2])

        show()
        msgbox.showinfo("Aviso", "Dados pesquisados com sucesso")
        
        con.close()

def show():        
        con = mysql.connect(
            host="localhost",
            user="root",
            password="senac123456789",
            database="registro"
            )
        cursor = con.cursor()
        cursor.execute("SELECT * FROM produto")
        rows = cursor.fetchall()
        list.delete(0,list.size())

        for row in rows:
            insertData = str(row[0])+'  '+row[1]+'   '+str(row[2])
            list.insert(list.size()+1, insertData)                        
        con.close()


root = Tk()
root.geometry("800x600")
root.title("Catalogo de produtos - Python & MySQL")

id = Label(root, text='ID do Produto', font=("bold", 12))
id.place(x=20,y=30)

nome = Label(root, text='Nome do Produto', font=('bold', 12))
nome.place(x=20,y=60)

valor = Label(root, text='Valor do Produto', font=('bold', 12))
valor.place(x=20,y=90)

e_id = Entry()
e_id.place(x=160,y=30)

e_nome = Entry()
e_nome.place(x=160,y=60)

e_valor = Entry()
e_valor.place(x=160,y=90)

insert = Button(root, text="Adicionar", font=("italic",12), bg="gray", command=insert)
insert.place(x=20,y=140)

delete = Button(root, text="Excluir", font=("italic",12), bg="red", command=delete)
delete.place(x=140,y=140)

update = Button(root, text="Atualizar", font=("italic",12), bg="white", command=update)
update.place(x=260,y=140)

get = Button(root, text="Consultar", font=("italic",12), bg="yellow", command=get)
get.place(x=380,y=140)

list = Listbox(root)
list.place(x=500,y=30)
show()

root = mainloop()
