 
#!/usr/bin/env python
 
 
from Tkinter import*
from ScrolledText import*
import tkMessageBox
import sys
from database import *
           
       
 
               
class Fenster:
 
 
    #Abstand der Elemente
    a_x=5 #Abstand horizontal
    a_y=5 #Abstand vertikal
 
    #Die Buttons bekommen alle dieselbe Breite
    b=20
 
    #Farbe wird auch von la verwendet
    f="#00ff00"
 
    lt=""
 
   
    def __init__(self):
 
        raise NotImplementedError("Abstract class")
 
   
 
    def prepare(self):
 
        self.root.resizable(0,0)
 
        self.root.protocol("WM_DELETE_WINDOW",self.mainexit)
 
        la=Label(self.root,bg=self.f,text="///GARO_GUI")
        la.grid(row=0,column=0,            
                     columnspan=2,
                     padx=self.a_x,pady=self.a_y)
     
        la_1=Label(self.root,bg=self.f,text=self.lt)
        la_1.grid(row=1,column=0,
                       columnspan=2,
                       padx=self.a_x,pady=self.a_y)
       
        button=Button(self.root,
                           text="Prog. Beenden",
                           width=10,command=self.ende)
        button.grid(row=15,column=0,
                         columnspan=2,
                         padx=10,pady=10)
 
 
 
    def ende(self):
 
        antwort=tkMessageBox.askyesno\
                 ("Warnung","Sicher beenden?")
        if antwort==1:
            sys.exit(0)
 
 
    def mainexit(self):
       
        self.root.withdraw()
 
   
   
 
class HauptFenster(Fenster):
 
    lt="Ausgabe"
 
       
    def __init__(self,host,user,db,db_table,passwd=''):
 
        self.root=Tk()
 
        self.root.wm_geometry('+20+20')
 
        self.prepare()
 
        self.root.title("Hauptfenster")
         
        self.database=DataBase(host,user,db,db_table,passwd)
 
        self.db_table=db_table
       
        choice=StringVar()
 
        self.cols_names=[elements[0] for elements in self.database.db_table_cols
                         if 'auto_increment' not in elements]
 
 
        li_1width=len(self.cols_names)*12
 
        self.s_cols_names=", ".join(self.cols_names)
 
 
        scb_v=Scrollbar(self.root, orient="vertical")
        scb_h=Scrollbar(self.root, orient="horizontal")
 
        self.li_1=Listbox(self.root,
                          width=li_1width,height=8,
                          yscrollcommand=scb_v.set,
                          xscrollcommand=scb_h.set)
       
        scb_v["command"]=self.li_1.yview
        scb_h["command"]=self.li_1.xview
       
        self.li_1.grid(row=2,column=0,
                       columnspan=2,
                       padx=self.a_x,pady=self.a_y)
       
        scb_v.grid(row=2,column=2,
                      padx=self.a_x,pady=self.a_y)
       
        scb_h.grid(row=3,column=0,
                        columnspan=2,
                        padx=self.a_x,pady=self.a_y)
                       
 
        b_1=Button(self.root,width=self.b,text="Alle Daten",
                        command=lambda:
                        self.list_data
                        (result=self.database.get_data
                        ("select %s from %s"%(self.s_cols_names,self.db_table))))
        b_1.grid(row=4,column=0,
                      padx=self.a_x,pady=self.a_y)
       
 
        b_2=Button(self.root,width=self.b,
                        text="Loeschen",command=self.ask)
        b_2.grid(row=4,column=1,
                      padx=self.a_x,pady=self.a_y)
       
       
        b_3=Button(self.root,width=self.b,text="Sortieren",
                        command=lambda:
                        self.list_data
                        (result=self.database.get_data
                        ("select %s from %s order by %s"%(self.s_cols_names,self.db_table,choice.get()))))
        b_3.grid(row=5,column=0,
                      padx=self.a_x,pady=self.a_y)
       
 
        b_4=Button(self.root,width=self.b,text="Eingabe",
                        command=lambda:
                        EingabeFenster
                        (self.root,self.database,
                         self.db_table,
                         self.root.winfo_width()))
        b_4.grid(row=5,column=1,
                      padx=self.a_x,pady=self.a_y)
 
 
        b_5=Button(self.root,width=self.b,text="Suchen",
                        command=lambda:
                        SuchFenster
                        (self,self.root,self.database,self.db_table))
        b_5.grid(row=6,column=0,
                      padx=self.a_x,pady=self.a_y)
 
 
        b_6=Button(self.root,width=self.b,text="Bearbeiten",
                        command=lambda:
                        BearbeitungsFenster
                        (self.root,self.database,
                         self.db_table,self.li_1.get("active"),
                         self.root.winfo_width()))
        b_6.grid(row=6,column=1,padx=self.a_x,pady=self.a_y)
 
 
        for i in range(len(self.cols_names)):
 
            rb=Radiobutton(self.root,text=self.cols_names[i],
                        value=self.cols_names[i],
                        variable=choice)
            rb.grid(row=i+7,column=1,
                         padx=self.a_x,pady=self.a_y)
 
            if i==0:
                rb.select()
 
        self.list_data(result=self.database.get_data("select %s from %s"%(self.s_cols_names,self.db_table)))
 
 
 
 
    def list_data(self,result):
       
        self.li_1.delete(0,END)
        result=[list(element) for element in result]
 
        for element in result:
            for i in range(len(element)):
                element[i]=str(element[i])
               
        result=["   ".join(element) for element in result]
 
        for elements in result:
                self.li_1.insert("end",elements)
           
 
    def get_selected(self,action):
 
        selected=self.li_1.get("active")
        selected=selected.split()
        selected=[str(selected[i]).replace(str(selected[i]),'"'+str(selected[i])+'"')
                     for i in range(len(selected))]
                     
        target=[self.cols_names[i]+"="+selected[i]
                       for i in range(len(selected))]
        target=" and ".join(target)
 
        check=self.database.get_data("select * from %s where %s"%(self.db_table,target))
        check=check[0][0]
 
        action=action%check
        return action
   
 
    def ask(self):
 
        answer=tkMessageBox.askyesno("Warnung",
                                     "Wollen Sie den gewaehlten Datensatz sicher loeschen ?")
        if answer==1:
            self.database.set_data(action=self.get_selected("delete from %s where %s = %s"%(self.db_table,
                                             self.database.db_table_cols[0][0],
                                             "%s")))
        else:
            pass
 
           
 
       
class EingabeFenster(Fenster):
 
    lt="Eingabe/Bearbeitung"
 
   
    def __init__(self,root,database,db_table,hfwidth):
 
        self.root=Toplevel(root)
 
        self.root.wm_geometry('%s+20'%('+'+str(hfwidth+40)))
 
        self.root.title("Eingabefenster")
 
        self.prepare()
 
        self.database=database
        self.db_table=db_table
 
 
        self.cols_names=[elements[0] for elements in self.database.db_table_cols
                         if 'auto_increment' not in elements]
 
        self.s_cols_names=", ".join(self.cols_names)
 
        self.entrylist=[]
 
        for i in range(len(self.cols_names)):
           
            la=Label(self.root,
                          text=self.cols_names[i])
            la.grid(row=i+2,column=0)
 
            entry=Entry(self.root)
            entry.grid(row=i+2,column=1,
                            padx=self.a_x,pady=self.a_y)
            self.entrylist.append(entry)
 
        b_1=Button(self.root,width=self.b,
                        text="Eintragen",
                        command=lambda:
                        self.database.set_data
                        (action=self.set_sql
                        ("insert into %s (%s) values (%s)")))
                       
        b_1.grid(row=7,column=1,
                      columnspan=2,
                      padx=self.a_x,pady=self.a_y)
       
       
    def get_entries(self):
 
        entries=[element.get() for element in self.entrylist]
       
        for i in range(len(entries)):
            test=entries[i].find(" ")
            if test and test !=-1:
                entries[i]=entries[i].replace(entries[i][test],"/")
               
        for element in self.entrylist: element.delete(0,"end")
       
        entries=[entries[i].replace(entries[i],'"'+entries[i]+'"')
                      for i in range(len(entries))]
 
        return entries
 
   
    def set_sql(self,action):
       
        entries=self.get_entries()
 
        s_entries=", ".join(entries)
       
        action=action%(self.db_table,self.s_cols_names,s_entries)
        return action
 
 
 
 
class BearbeitungsFenster(Fenster,EingabeFenster):
 
    lt="Bearbeitung"
   
 
    def __init__(self,root,database,db_table,selected,hfwidth):
       
        self.selected=selected
        self.selected=self.selected.split()
 
        EingabeFenster.__init__(self,root,database,db_table,hfwidth)
       
        self.root.title("Bearbeitungsfenster")
 
        for i in range(len(self.entrylist)):
            self.entrylist[i].insert(0,self.selected[i])
 
        b_1=Button(self.root,width=self.b,
                        text="Eintragen",
                        command=lambda:
                        self.database.set_data
                        (action=self.set_sql
                        ("update %s set %s where %s=%s")))
                       
        b_1.grid(row=7,column=1,
                      columnspan=2,
                      padx=self.a_x,pady=self.a_y)
       
   
    def set_sql(self,action):
 
        entries=self.get_entries()
 
        result=[self.cols_names[i]+"="+entries[i]
                for i in range(len(entries))]
        result=", ".join(result)
 
        self.selected=list(self.selected)
        self.selected=[str(self.selected[i]).replace(str(self.selected[i]),'"'+str(self.selected[i])+'"')
                       for i in range(len(self.selected))]
       
        target=[self.cols_names[i]+"="+self.selected[i]
                for i in range(len(self.selected))]
        target=" and ".join(target)
 
        check=self.database.get_data("select * from %s where %s"%(self.db_table,target))
        check=check[0][0]
       
        self.cols_names_b=[elements[0] for elements in self.database.db_table_cols]
 
        action=action%(self.db_table,result,self.cols_names_b[0],check)
        return action
       
 
                   
class SuchFenster(Fenster):
 
    lt="Suche"
 
 
    def __init__(self,hf,root,database,db_table):
 
        self.root=Toplevel(root)
 
        self.root.title("Suchfenster")
 
        self.prepare()
       
        choice=StringVar()
        self.database=database
        self.db_table=db_table
 
 
        entry=Entry(self.root)
        entry.grid(row=3,column=0)
 
        for i in range(len(hf.cols_names)):
 
            rb=Radiobutton(self.root,text=hf.cols_names[i],
                                value=hf.cols_names[i],
                                variable=choice)
            rb.grid(row=i+2,column=1,
                         padx=self.a_x,pady=self.a_y)
 
            if i==0:
                rb.select()
           
 
        b_1=Button(self.root,text="Suche",
                        command=lambda:
                        hf.list_data
                        (result=self.database.get_data
                        ("select %s from %s where %s= '%s'"%(hf.s_cols_names,
                                                             self.db_table,
                                                             choice.get(),
                                                             entry.get()))))
                       
        b_1.grid(row=9,column=0)
 
 
if __name__ == "__main__":
 
    hf=HauptFenster("localhost","username","datenbank","tabelle","passwort")
    #hf=HauptFenster("localhost","username","andere datenbank", usw)
 
    mainloop()
 
