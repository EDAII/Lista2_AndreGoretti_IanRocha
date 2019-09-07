from tkinter import *
from functions import *
from tkinter import ttk

# s=ttk.Style()
# s.theme_use('clam')


 
def abrirBusca():

   def clickedN():
      ContatoBusca.config(state="normal")
      ContatoBusca.delete('1.0', END)
      Nome = EntradaN.get()
      
      i = 0
      while(i <= 50):
            
            if person[i] == Nome:
               
               ContatoBusca.insert(INSERT, "--------------------")
               ContatoBusca.insert(INSERT, "\n ")
               ContatoBusca.insert(INSERT, "Nome: ")
               ContatoBusca.insert(INSERT, person[i])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "CPF: ")
               ContatoBusca.insert(INSERT, cpf[i])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "idade: ")
               ContatoBusca.insert(INSERT, age[i])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Cidade: ")
               ContatoBusca.insert(INSERT, city[i])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Numero Telefone: ")
               ContatoBusca.insert(INSERT, tel[i])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Nascimento: ")
               ContatoBusca.insert(INSERT, date[i])
               ContatoBusca.insert(INSERT, "\n")
            i += 1       

      ContatoBusca.config(state="disabled")                  

      #ContatoBusca.insert(INSERT, )

   def clickedA():

      ContatoBusca.config(state="normal")
      ContatoBusca.delete('1.0', END)
      AgeB = int(EntradaA.get())
      j = 0
      while(j <= 50):
            if age[j] == AgeB:
               ContatoBusca.insert(INSERT, "--------------------")
               ContatoBusca.insert(INSERT, "\n ")
               ContatoBusca.insert(INSERT, "Nome: ")
               ContatoBusca.insert(INSERT, person[j])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "CPF: ")
               ContatoBusca.insert(INSERT, cpf[j])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "idade: ")
               ContatoBusca.insert(INSERT, age[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Cidade: ")
               ContatoBusca.insert(INSERT, city[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Numero Telefone: ")
               ContatoBusca.insert(INSERT, tel[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Nascimento: ")
               ContatoBusca.insert(INSERT, date[j])
               ContatoBusca.insert(INSERT, "\n")
            j += 1

      ContatoBusca.config(state="disabled")      

   def clickedC():

      ContatoBusca.config(state="normal")
      ContatoBusca.delete('1.0', END)
      Cidade = EntradaC.get()
      j = 0
      while(j <= 50):
            
            if Cidade == city[j]:
               ContatoBusca.insert(INSERT, "--------------------")
               ContatoBusca.insert(INSERT, "\n ")
               ContatoBusca.insert(INSERT, "Nome: ")
               ContatoBusca.insert(INSERT, person[j])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "CPF: ")
               ContatoBusca.insert(INSERT, cpf[j])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "idade: ")
               ContatoBusca.insert(INSERT, age[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Cidade: ")
               ContatoBusca.insert(INSERT, city[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Numero Telefone: ")
               ContatoBusca.insert(INSERT, tel[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Nascimento: ")
               ContatoBusca.insert(INSERT, date[j])
               ContatoBusca.insert(INSERT, "\n")
            j += 1   
     
      ContatoBusca.config(state="disabled")

   janelaBusca = Toplevel()
   janelaBusca.geometry('470x550')

   lblN = Label(janelaBusca, text="Nome")
   lblN.place(x = 1, y = 15)

   lblA = Label(janelaBusca, text="Idade")
   lblA.place(x = 1, y = 40)

   lblC = Label(janelaBusca, text="Cidade")
   lblC.place(x = 1, y = 70)
   
   EntradaN = Entry(janelaBusca,width=10)
   EntradaN.place(x = 50, y = 15)

   EntradaA = Entry(janelaBusca,width=10)
   EntradaA.place(x = 50, y = 40)

   EntradaC = Entry(janelaBusca,width=10)
   EntradaC.place(x = 50, y = 70)   

   ContatoBusca = Text(janelaBusca, width = 30, height = 30)
   ContatoBusca.place(x = 220, y = 0)
   ContatoBusca.config(state="disabled")

   btnNome = Button(janelaBusca, text="Buscar", command=clickedN)
   btnAge = Button(janelaBusca, text="Buscar", command=clickedA)
   
   btnCity = Button(janelaBusca, text="Buscar", command=clickedC)

   btnAge.place(x = 140, y = 40)
   btnNome.place(x = 140, y = 10)
   
   btnCity.place(x = 140, y = 70)

   btnClose = Button(janelaBusca, text="Fechar", command=janelaBusca.destroy)
   btnClose.place(x = 100, y = 500)     



def clickedG():

   ContatoPrin.delete('1.0', END)
   ContatoPrin.config(state="normal")

   
   j = 0
   while(j <= 50):

      ContatoPrin.insert(INSERT, "--------------------") 
      ContatoPrin.insert(INSERT, "\n ")      
      ContatoPrin.insert(INSERT, "Nome: ")
      ContatoPrin.insert(INSERT, person[j])
      ContatoPrin.insert(INSERT, "\n ")

      ContatoPrin.insert(INSERT, "CPF: ")
      ContatoPrin.insert(INSERT, cpf[j])
      ContatoPrin.insert(INSERT, "\n ")

      ContatoPrin.insert(INSERT, "idade: ")
      ContatoPrin.insert(INSERT, age[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Cidade: ")
      ContatoPrin.insert(INSERT, city[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Numero Telefone: ")
      ContatoPrin.insert(INSERT, tel[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Nascimento: ")
      ContatoPrin.insert(INSERT, date[j])
      ContatoPrin.insert(INSERT, "\n")
      j += 1

   ContatoPrin.config(state="disabled")    
   
   

   

window1 = Tk()

window1.title("Agenda")
 
window1.geometry('470x550')

ContatoPrin = Text(window1, width = 30, height = 30)
ContatoPrin.place(x = 220, y = 0)
ContatoPrin.config(state="disabled")

clickedG()


btnBusca = Button(window1, text="Buscas", command=abrirBusca)
btnBusca.place(relx = 0.25, rely = 0.3, anchor = CENTER)

btnOrdenaidade = Button(window1, text="Ordenar por Idade",) #command=ordenaIdade)      
btnOrdenaidade.place(relx = 0.25, rely = 0.5, anchor = CENTER)

btnOrdenaNome = Button(window1, text="Ordenar por Nome",) #command=ordenaNome)      
btnOrdenaNome.place(relx = 0.25, rely = 0.6, anchor = CENTER)

btnOrdenacidade = Button(window1, text="Ordenar por Cidade",) #command=ordenacidade)      
btnOrdenacidade.place(relx = 0.25, rely = 0.7, anchor = CENTER)

 
window1.mainloop()