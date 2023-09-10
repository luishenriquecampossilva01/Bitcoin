from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

#importando bibliotecas
import requests
import json
#cores --------
co0 = "#444466" 
co1 = "#feffff"
co2 = "#6f9fbd"
fundo = "#484f60"

#criando janela --------
janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

#dividindo a janela em 2 frames ---------
ttk.Separator(janela,orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=157)
frame_cima = Frame(janela,width=320,height=50,bg = co1, pady=0, padx=0,relief=FLAT)
frame_cima.grid(row=1,column=0)

frame_baixo = Frame(janela,width=320,height=300,bg = fundo, pady=0, padx=0,relief=FLAT)
frame_baixo.grid(row=2,column=0,sticky=NW)

#função para pegar dados
def info():
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CAOA%2CBRL'

    # http requests
    response = requests.get(api_link)

    #convertendo oos dados em dicionario
    dados = response.json()

    valor_usd = float(dados['USD'])
    valor_formatado_usd = "${:,.3f}".format(valor_usd)
    l_p_usd['text']= valor_formatado_usd

    valor_euro = float(dados['EUR'])
    valor_formatado_euro = "€{:,.3f}".format(valor_euro)
    l_p_euro['text']= 'Em euros é: '+valor_formatado_euro

    valor_reais = float(dados['BRL'])
    valor_formatado_reais = "R${:,.3f}".format(valor_reais)
    l_p_reais['text']='Em Reais é: '+ valor_formatado_reais

    valor_kz = float(dados['AOA'])
    valor_formatado_kz = "Kz {:,.3f}".format(valor_kz)
    l_p_kz['text']= 'Em Kwanzas é:' +valor_formatado_kz
    frame_baixo.after(1000,info)

#configurando o frame_cima
imagem = Image.open('bitcoin.png')
imagem = imagem.resize((30,30))
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima,image=imagem,compound=LEFT, bg = co1,relief=FLAT)
l_icon.place(x=10,y=10)

l_nome = Label(frame_cima,text='Bitcoin Price Tracker', bg = co1,fg=co2,relief=FLAT,anchor='center',font=('Arial 20'))
l_nome.place(x=50,y=5)

#configurando frama_baixo --------
l_p_usd = Label(frame_baixo,text='', bg = fundo,fg=co1,relief=FLAT,anchor='center',font=('Arial 20 bold'))
l_p_usd.place(x=10,y=50)
l_p_euro = Label(frame_baixo,text='€ 10,000,00', bg = fundo,fg=co1,relief=FLAT,anchor='center',font=('Arial 12'))
l_p_euro.place(x=10,y=130)
l_p_reais = Label(frame_baixo,text='R$ 10,000,00', bg = fundo,fg=co1,relief=FLAT,anchor='center',font=('Arial 12'))
l_p_reais.place(x=10,y=160)
l_p_kz = Label(frame_baixo,text='Kz 10,000,00', bg = fundo,fg=co1,relief=FLAT,anchor='center',font=('Arial 12'))
l_p_kz.place(x=10,y=190)



info()


janela.mainloop()