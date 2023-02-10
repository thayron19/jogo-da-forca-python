import random  # para sortear a palavra da lista
import tkinter  # cria a janela e os elementos
import keyboard  # teclas de atalho


# ---------------------------------------------------------------------------------------------------------------------
def recebe_letra(letra):  # função que recebe a letra escolhida pelo user

    if '_' not in mostra_texto['text']:  # caso tenha acertada a palavra, chama uma nova palavra
        sorteia()  # função que sorteia nova palavra
    else:

        if letra in resposta_texto['text']:  # se a letra escolhi contém na resposta
            acumulador = ''  # usado para reconstruir a resposta na tela
            lista2 = mostra_texto['text'].split()  # cria uma lista com a 'string' de resposta

            for x, y in enumerate(resposta_texto['text']):  # mapea a 'string'
                if letra == y:  # testa onde a letra está na 'string'
                    lista2[x] = letra  # troca na lista o '_' pela letra que está certa

            for x in lista2:  # mapea a lista criada
                acumulador += x + ' '  # salva no acumudalor

            mostra_texto['text'] = acumulador  # mostra o acumulador na tela

        else:  # caso errado, vai montando o boneco
            if cabeca_texto['text'] == '':
                cabeca_texto['text'] = 'o'
            elif tronco_texto['text'] == '':
                tronco_texto['text'] = '|'
            elif braco_d_texto['text'] == '':
                braco_d_texto['text'] = '/'
            elif braco_e_texto['text'] == '':
                braco_e_texto['text'] = '\\'
            elif perna_d_texto['text'] == '':
                perna_d_texto['text'] = '/'
            elif perna_e_texto['text'] == '':
                perna_e_texto['text'] = '\\'
            else:  # terminado o boneco, sorteia nova paçavra
                sorteia()


# ---------------------------------------------------------------------------------------------------------------------
def sorteia():  # função que sorteia nova palavra

    if len(lista) != 0:  # se a lista de palavras estiver vazia não executa essa parte

        # limpa o boneco na janela
        cabeca_texto['text'] = ''
        tronco_texto['text'] = ''
        braco_d_texto['text'] = ''
        braco_e_texto['text'] = ''
        perna_d_texto['text'] = ''
        perna_e_texto['text'] = ''

        acumulador = ''  # acumulador usado para montar os '_' na tela

        resposta_texto['text'] = lista[int(random.randint(0, len(lista) - 1))]  # recebe a 'string' da lista sorteada

        del lista[int(random.randint(0, len(lista) - 1))]  # deleta a 'string' da lista sorteada

        if '-' in resposta_texto['text']:  # mosta na tela quantas letras a palavra tem, sem contar o '-'
            num_letras_texto['text'] = str(len(resposta_texto['text']) - 1) + ' letras'
        else:
            num_letras_texto['text'] = str(len(resposta_texto['text'])) + ' letras'

        for x, y in enumerate(resposta_texto['text']):  # mapea a 'string'
            if y != '-':
                acumulador += '_ '
            else:
                acumulador += '- '

        mostra_texto['text'] = acumulador  # mostra o acumulador na tela

        if len(lista) == 1:  # mostra na tela quantos verbos ainda tem no jogo
            qtd_palavras_texto['text'] = f'{len(lista)} verbo restante'
        elif len(lista) == 0:
            qtd_palavras_texto['text'] = 'Último verbo!'
        else:
            qtd_palavras_texto['text'] = f'{len(lista)} verbos restantes'

    else:  # quando a lista zera ele fecha a janela
        janela.destroy()


# ---------------------------------------------------------------------------------------------------------------------
lista = ['abolir', 'abracar', 'abrir', 'abster-se', 'acabar', 'aceitar', 'acender', 'acender', 'achar', 'achar-se',
         'aconselhar', 'acontecer', 'acreditar', 'adequar', 'aderir', 'adoecer', 'adquirir', 'agradar', 'agradecer',
         'aguerrir', 'almocar', 'alvorecer', 'amanhecer', 'amar', 'andar', 'anoitecer', 'ansiar', 'ansiar', 'aparecer',
         'apiedar-se', 'aprazer', 'aprender', 'apresentar', 'arrepender-se', 'assistir', 'atinar', 'atirar', 'atirar',
         'atribuir', 'atribuir-se', 'atropelar', 'aturdir', 'avisar', 'banir', 'barbear-se', 'bastar', 'beber',
         'bramar', 'brilhar', 'brincar', 'caber', 'cacarejar', 'cair', 'caminhar', 'cantar', 'carecer', 'casar',
         'causar', 'ceder', 'chamar', 'chega', 'chegar', 'chorar', 'chover', 'chuviscar', 'coaxar', 'cobrir', 'colorir',
         'combalir', 'começar', 'comedir', 'comemorar', 'comer', 'comparecer', 'complicar', 'compor', 'comprar',
         'compreender', 'comunicar', 'concernir', 'concordar', 'condoer', 'condoer-se', 'confiar', 'confundir',
         'conseguir', 'conspirar', 'constar', 'construir', 'contar', 'contentar-se', 'continuar', 'contribuir',
         'conversar', 'convidar', 'convir', 'correr', 'corrigir', 'cortar', 'cortar-se', 'costumar', 'costurar', 'crer',
         'crer', 'crescer', 'cricrilar', 'cuidar', 'cumprir', 'custar', 'dancar', 'dar', 'debater', 'debater-se',
         'decidir', 'deitar', 'deitar-se', 'deixar', 'delinquir', 'demolir', 'demorar', 'depender', 'derrubar',
         'descobrir', 'desculpar', 'desfrutar', 'desistir', 'destruir', 'dever', 'devolver', 'dignar-se', 'discutir',
         'dividir', 'dizer', 'doar', 'doer', 'dormir', 'duvidar', 'eleger', 'elogiar', 'emendar-se', 'emitir',
         'empedernir', 'emprestar', 'encontrar', 'encontrar-se', 'encostar-se', 'enganar-se', 'ensinar', 'entrar',
         'entregar', 'entregar', 'envolver', 'envolver-se', 'enxaguar', 'esbaforir', 'escolher', 'escrever', 'esculpir',
         'escurecer', 'esperar', 'esquecer-se', 'estar', 'estiar', 'estrear', 'estudar', 'exaurir', 'exercer',
         'expelir', 'explicar', 'explodir', 'expressar', 'exprimir', 'expulsar', 'extinguir', 'extorquir', 'falar',
         'falir', 'fazer', 'feder', 'ferir-se', 'ficar', 'fingir', 'florir', 'frigir', 'fugir', 'ganhar', 'ganir',
         'garantir', 'garoar', 'gostar', 'grassar', 'haver', 'imitar', 'impingir', 'importar', 'imprimi', 'imprimir',
         'inchar', 'incluir', 'influenciar', 'informar', 'ingressar', 'insistir', 'interessar', 'intrometer-se',
         'invadir', 'ir', 'jogar', 'ladrar', 'latir', 'lavar-se', 'lembrar-se', 'ler', 'levantar', 'levantar-se',
         'levar', 'limpar', 'lutar', 'mandar', 'matar', 'medir', 'mentir', 'merecer', 'miar', 'morar', 'morrer',
         'morrer', 'mudar', 'mugir', 'murchar', 'nadar', 'namorar', 'narrar', 'nascer', 'necessitar', 'nevar',
         'obedecer', 'ocorrer', 'oferecer', 'ofertar', 'olhar', 'olhar-se', 'orvalhar', 'ouvir', 'pagar', 'parar',
         'parecer', 'participar', 'partir', 'passar', 'passear', 'pedir', 'pegar', 'pensar', 'pentear-se', 'perder',
         'perdoar', 'perguntar', 'permanecer', 'permitir', 'perseguir', 'pilotar', 'pintar', 'pintar-se', 'poder',
         'polir', 'por', 'por-se', 'precaver', 'precisar', 'prender', 'preocupar-se', 'prescindir', 'pretender',
         'proceder', 'produzir', 'progredir', 'prometer', 'propor', 'proporcionar', 'pular', 'puxar', 'quebrar',
         'queixar-se', 'querer', 'questionar', 'reaver', 'receber', 'recorrer', 'relampejar', 'relatar', 'remediar',
         'renhir', 'resistir', 'responder', 'ressequir', 'retorquir', 'revolver', 'rir', 'rosnar', 'ruir', 'saber',
         'saber', 'sacudir', 'sair', 'salvar', 'saraivar', 'sentar', 'sentar-se', 'sentir', 'ser', 'servir',
         'simpatizar', 'sofrer', 'sonhar', 'suar', 'submergir', 'suceder', 'suceder', 'suicidar-se', 'sumir',
         'suspender', 'tentar', 'ter', 'tornar', 'tornar-se', 'trabalhar', 'tratar', 'trazer', 'tremer', 'trovejar',
         'urgir', 'usar', 'valer', 'varrer', 'vazar', 'vencer', 'vender', 'ventar', 'ver', 'vestir-se', 'viajar', 'vir',
         'virar', 'visitar', 'viver', 'voltar', 'votar', 'zangar-se', 'zombar', 'zurrar']
# ---------------------------------------------------------------------------------------------------------------------
janela = tkinter.Tk()  # objeto janela do tkinter
janela.title('Forca')
janela.resizable(width=False, height=False)  # bloqueia o resize da janela

# posiciona a janela no centro da tela,
# 285 largura, 350 altura, resoução da tela divido por 2
janela.geometry("%dx%d%d%d" % (285, 350, float(285 / 2 - janela.winfo_screenwidth() / 2),
                               float(350 / 2 - janela.winfo_screenheight() / 2)))
# ---------------------------------------------------------------------------------------------------------------------
resposta_texto = tkinter.Label(janela, text='')  # 'string' do tkinter usado para evitar global
# ---------------------------------------------------------------------------------------------------------------------
# mosta na tela quantas letras a palavra tem, sem contar o '-'
num_letras_texto = tkinter.Label(janela, text='', font=('', 15), justify='center')
num_letras_texto.place(x=0, y=20, width=285)  # posição do elemento e largura
# ---------------------------------------------------------------------------------------------------------------------
mostra_texto = tkinter.Label(janela, text='', font=('', 15), justify='center')
mostra_texto.place(x=0, y=60, width=285)  # posição do elemento e largura
# ---------------------------------------------------------------------------------------------------------------------
# elementos usado para criação do boneco na tela
cabeca_texto = tkinter.Label(janela, text='', font=('', 12), justify='center')
cabeca_texto.place(x=20, y=10)  # posição do elemento
tronco_texto = tkinter.Label(janela, text='', font=('', 12), justify='center')
tronco_texto.place(x=23, y=28)  # posição do elemento
braco_d_texto = tkinter.Label(janela, text='', font=('', 12), justify='center')
braco_d_texto.place(x=16, y=28)  # posição do elemento
braco_e_texto = tkinter.Label(janela, text='', font=('', 12), justify='center')
braco_e_texto.place(x=29, y=28)  # posição do elemento
perna_d_texto = tkinter.Label(janela, text='', font=('', 12), justify='center')
perna_d_texto.place(x=16, y=45)  # posição do elemento
perna_e_texto = tkinter.Label(janela, text='', font=('', 12), justify='center')
perna_e_texto.place(x=29, y=45)  # posição do elemento
# ---------------------------------------------------------------------------------------------------------------------
a_btn = tkinter.Button(janela, text='A', command=lambda: recebe_letra('a'), font=('', 20))
a_btn.place(x=10, y=100, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('a', lambda _: recebe_letra('a'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
b_btn = tkinter.Button(janela, text='B', command=lambda: recebe_letra('b'), font=('', 20))
b_btn.place(x=55, y=100, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('b', lambda _: recebe_letra('b'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
c_btn = tkinter.Button(janela, text='C', command=lambda: recebe_letra('c'), font=('', 20))
c_btn.place(x=100, y=100, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('c', lambda _: recebe_letra('c'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
d_btn = tkinter.Button(janela, text='D', command=lambda: recebe_letra('d'), font=('', 20))
d_btn.place(x=145, y=100, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('d', lambda _: recebe_letra('d'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
e_btn = tkinter.Button(janela, text='E', command=lambda: recebe_letra('e'), font=('', 20))
e_btn.place(x=190, y=100, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('e', lambda _: recebe_letra('e'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
f_btn = tkinter.Button(janela, text='F', command=lambda: recebe_letra('f'), font=('', 20))
f_btn.place(x=235, y=100, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('f', lambda _: recebe_letra('f'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
g_btn = tkinter.Button(janela, text='G', command=lambda: recebe_letra('g'), font=('', 20))
g_btn.place(x=10, y=145, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('g', lambda _: recebe_letra('g'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
h_btn = tkinter.Button(janela, text='H', command=lambda: recebe_letra('h'), font=('', 20))
h_btn.place(x=55, y=145, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('g', lambda _: recebe_letra('h'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
i_btn = tkinter.Button(janela, text='I', command=lambda: recebe_letra('i'), font=('', 20))
i_btn.place(x=100, y=145, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('i', lambda _: recebe_letra('i'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
j_btn = tkinter.Button(janela, text='J', command=lambda: recebe_letra('j'), font=('', 20))
j_btn.place(x=145, y=145, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('j', lambda _: recebe_letra('j'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
k_btn = tkinter.Button(janela, text='K', command=lambda: recebe_letra('k'), font=('', 20))
k_btn.place(x=190, y=145, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('k', lambda _: recebe_letra('k'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
l_btn = tkinter.Button(janela, text='L', command=lambda: recebe_letra('l'), font=('', 20))
l_btn.place(x=235, y=145, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('l', lambda _: recebe_letra('l'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
m_btn = tkinter.Button(janela, text='M', command=lambda: recebe_letra('m'), font=('', 20))
m_btn.place(x=10, y=190, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('m', lambda _: recebe_letra('m'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
n_btn = tkinter.Button(janela, text='N', command=lambda: recebe_letra('n'), font=('', 20))
n_btn.place(x=55, y=190, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('n', lambda _: recebe_letra('n'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
o_btn = tkinter.Button(janela, text='O', command=lambda: recebe_letra('o'), font=('', 20))
o_btn.place(x=100, y=190, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('o', lambda _: recebe_letra('o'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
p_btn = tkinter.Button(janela, text='P', command=lambda: recebe_letra('p'), font=('', 20))
p_btn.place(x=145, y=190, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('p', lambda _: recebe_letra('p'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
q_btn = tkinter.Button(janela, text='Q', command=lambda: recebe_letra('q'), font=('', 20))
q_btn.place(x=190, y=190, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('q', lambda _: recebe_letra('q'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
r_btn = tkinter.Button(janela, text='R', command=lambda: recebe_letra('r'), font=('', 20))
r_btn.place(x=235, y=190, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('r', lambda _: recebe_letra('r'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
s_btn = tkinter.Button(janela, text='S', command=lambda: recebe_letra('s'), font=('', 20))
s_btn.place(x=10, y=235, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('s', lambda _: recebe_letra('s'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
t_btn = tkinter.Button(janela, text='T', command=lambda: recebe_letra('t'), font=('', 20))
t_btn.place(x=55, y=235, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('t', lambda _: recebe_letra('t'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
u_btn = tkinter.Button(janela, text='U', command=lambda: recebe_letra('u'), font=('', 20))
u_btn.place(x=100, y=235, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('u', lambda _: recebe_letra('u'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
v_btn = tkinter.Button(janela, text='V', command=lambda: recebe_letra('v'), font=('', 20))
v_btn.place(x=145, y=235, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('v', lambda _: recebe_letra('v'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
w_btn = tkinter.Button(janela, text='W', command=lambda: recebe_letra('w'), font=('', 20))
w_btn.place(x=190, y=235, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('w', lambda _: recebe_letra('w'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
x_btn = tkinter.Button(janela, text='X', command=lambda: recebe_letra('x'), font=('', 20))
x_btn.place(x=235, y=235, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('x', lambda _: recebe_letra('x'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
y_btn = tkinter.Button(janela, text='Y', command=lambda: recebe_letra('y'), font=('', 20))
y_btn.place(x=100, y=280, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('y', lambda _: recebe_letra('y'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
z_btn = tkinter.Button(janela, text='Z', command=lambda: recebe_letra('z'), font=('', 20))
z_btn.place(x=145, y=280, width=40, height=40)  # posição do elemento, largura e altura
keyboard.on_press_key('z', lambda _: recebe_letra('z'))  # atalho de teclado
# ---------------------------------------------------------------------------------------------------------------------
qtd_palavras_texto = tkinter.Label(janela, text='', font=('', 12), justify='center')
qtd_palavras_texto.place(x=0, y=325, width=285)  # posição do elemento e largura
# ---------------------------------------------------------------------------------------------------------------------
sorteia()  # função que sorteia nova palavra
# ---------------------------------------------------------------------------------------------------------------------
janela.mainloop()  # mantém a janela aberta
