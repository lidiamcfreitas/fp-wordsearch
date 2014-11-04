from janela_sopa_letras import *



# _______________________________DIRECAO_____________________________________

# RECONHECEDORES

def e_direcao(direcao):
    """ e_direcao: universal -> logico
    e_direcao(direcao) tem o valor verdadeiro se o arg for do tipo 
    direcao e falso caso contrario. """
    
    DIRECOES = ('N', 'S', 'E', 'W', 'NE', 'SW', 'SE', 'NW')    
    
    return isinstance(direcao, str) and (direcao in DIRECOES)


def e_norte(n):
    """ e_norte: direcao -> logico
    e_norte(n) tem o valor verdadeiro se o arg for o elemento 'N' e falso 
    caso contrario. """
    
    return isinstance(n, str) and n == 'N'


def e_sul(s):
    """ e_sul: direcao -> logico
    e_sul(s) tem o valor verdadeiro se o arg for o elemento 'N' e falso 
    caso contrario. """ 
    
    return isinstance(s, str) and s == 'S'

    
def e_leste(e):
    """ e_leste: direcao -> logico
    e_leste(e) tem o valor verdadeiro se o arg for o elemento 'E' e falso 
    caso contrario. """    
    
    return isinstance(e, str) and e == 'E'


def e_oeste(w):
    """ e_oeste: direcao -> logico
    e_oeste(w) tem o valor verdadeiro se o arg for o elemento 'W' e falso 
    caso contrario. """    
    
    return isinstance(w, str) and w == 'W'


def e_nordeste(ne):
    """ e_nordeste: direcao -> logico
    e_nordeste(ne): tem o valor verdadeiro se o arg for o elemento 'NE'
    e falso caso contrario. """ 
    
    return isinstance(ne, str) and ne == 'NE'


def e_noroeste(nw): 
    """ e_noroeste: direcao -> logico
    e_noroeste(n) tem o valor verdadeiro se o arg for o elemento 'NW' e falso
    caso contrario. """
    
    return isinstance(nw, str) and nw == 'NW'


def e_sudeste(se):
    """ e_sudoeste: direcao -> logico
    e_sudoeste(n) tem o valor verdadeiro se o arg for o elemento 'SE' e falso 
    caso contrario. """ 
    
    return isinstance(se, str) and se == 'SE'


def e_sudoeste(sw):   
    """ e_sudoeste: direcao -> logico
    e_sudoeste(n) tem o valor verdadeiro se o arg for o elemento 'SW' e falso 
    caso contrario. """
    
    return isinstance(sw, str) and sw == 'SW'


# TESTES

def direcoes_iguais(d1, d2):
    """ direcoes_iguais: direcao x direcao -> logico
    direcoes_iguais(d1, d2) devolve o valor verdadeiro se as direcoes d1 e d2
    forem iguais e falso caso contrario. """
    
    return d1 == d2


# OUTRAS

def direcao_oposta(d):    
    """ direcao_oposta: direcao -> direcao
    direcao_oposta(d) devolve a direcao oposta de d de acordo com a rosa dos
    ventos. """
    
    DIRECOESEOPOSTAS = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E', 'NE': 'SW', 
                       'NW': 'SE', 'SE': 'NW', 'SW': 'NE'}  
    
    return DIRECOESEOPOSTAS[d]





# _______________________________COORDENADA__________________________________

# CONSTRUTOR

def coordenada(l, c, d):
    """ coordenada : N0 x N0 x direcao -> coordenada
    coordenada(l, c, d) tem como valor a coordenada referente a posicao (l,c)
    e direcao d. Em caso de argumentos invalidos levanta um erro."""
    
    if (isinstance(l, int) and l >= 0 and
        isinstance(c, int) and c >= 0 and
        e_direcao(d)):
        
        return (l, c, d)
    
    else:
        raise ValueError('coordenada: argumentos invalidos')
    
    
# SELECTORES

def coord_linha(coordenada):
    """ coord_linha: coordenada |-> N0
    coord_linha(coordenada) tem como valor a linha da coordenada. """
    
    return coordenada[0]


def coord_coluna(coordenada):
    """ coord_coluna : coordenada |-> N0
    coord_coluna(coordenada) tem como valor a coluna da coordenada. """
    
    return coordenada[1]


def coord_direcao(coordenada):
    """ coord_direcao : coordenada |-> direcao
    coord_direcao(coordenada) tem como valor a direcao da coordenada. """
    
    return coordenada[2]


# RECONHECEDORES

def e_coordenada(c):
    """ e_coordenada : universal -> logico
    e_coordenada(c) tem o valor verdadeiro se o arg for do tipo coordenada 
    e falso caso contrario. """
    
    return (isinstance(c, tuple) and len(c) == 3 and
            isinstance(c[0], int) and c[0] >= 0 and 
            isinstance(c[1], int) and c[1] >= 0 and
            e_direcao(c[2]))

        
# TESTES

def coordenadas_iguais(c1, c2):
    """ coordenadas_iguais : coordenada x coordenada -> logico
    coordenadas_iguais(c1, c2) devolve o valor verdadeiro se as coordenadas
    c1 e c2 forem iguais e falso caso contrario. """
    
    return c1[0] == c2[0] and c1[1] == c2[1] and direcoes_iguais(c1[2], c2[2])


# OUTRAS

def coordenada_string(c):
    """ coordenada_string : coordenada -> string
    coordenada_string(c) devolve a representacao externa de c. """
    
    return ('(' + str(coord_linha(c)) + ', ' + str(coord_coluna(c)) +
            ')-' + str(coord_direcao(c)))





# _______________________________GRELHA______________________________________

# CONSTRUTOR

def grelha(lst):
    """ grelha : lista de strings -> grelha
    grelha(lst) tem como valor uma grelha mxn, em que m e o numero de 
    elementos da lista lst e n o numero de caracteres de cada string na 
    lista. """
    
    if lst == [] or (not isinstance(lst, list)):
            raise ValueError('grelha: argumentos invalidos')
    else:
        for elem in lst:
            if not isinstance(elem, str):
                raise ValueError('grelha: argumentos invalidos')
            
        for i in range(len(lst) - 1):
            if len(lst[i]) != len(lst[i + 1]):
                raise ValueError('grelha: argumentos invalidos')
            
        grelha = []
        
        for linha in lst:
            lista_linha = []
            for i in range(len(linha)):
                if linha[i] != ' ':
                    lista_linha = lista_linha + [linha[i]]
            grelha = grelha + [lista_linha]
            
        return grelha 
    
# SELETORES
                    
def grelha_nr_linhas(g):
    """ grelha_nr_linhas : grelha |-> N0
    grelha_nr_linhas(g) devolve o numero de linhas da grelha g. """
    
    return len(g)


def grelha_nr_colunas(g):
    """ grelha_nr_colunas : grelha |-> N0
    grelha_nr_colunas(g) devolve o numero de colunas da grelha g. """
    
    return len(g[0])


def grelha_elemento(g, l, c):
    """ grelha_elemento : grelha x N0 x N0 |-> caracter
    grelha_elemento(g, l, c) devolve o caracter que esta na posicao (l , c)
    da grelha g.
    No caso de (l , c) nao ser uma posicao valida para a grelha, o seletor 
    gera um erro de valor. """
    
    if not ( l in range(grelha_nr_linhas(g))  and 
             c in range(grelha_nr_colunas(g)) ):
        raise ValueError('grelha_elemento: argumentos invalidos')
    
    else:
        return g[l][c]
    
    
def grelha_linha(g, c):
    """ grelha_linha : grelha x coordenada |-> string
    grelha_linha(g, c) devolve a cadeia de caracteres que corresponde a linha
    definida segundo a direcao dada pela coordenada c, e que inclui a posicao
    dada pela mesma coordenada.
    No caso de c nao definir uma posicao valida para a grelha g o seletor gera
    um erro de valor. """
    
    if not (coord_linha(c) <= grelha_nr_linhas(g) - 1):
        raise ValueError('grelha_linha: argumentos invalidos')
    elif not (coord_coluna(c) <= grelha_nr_colunas(g) - 1):
        raise ValueError('grelha_linha: argumentos invalidos')        
    
    def escreve_sul():
        """escreve_sul: sub-funcao que vai devolver uma cadeia de
        caracteres que corresponde a coluna definida na
        coordenada X, na direcao Sul.
        """
        frase = ''
        for elem in g:
            frase = frase + elem[coord_coluna(c)]
        return frase
        
    def escreve_norte():
        """escreve_norte: sub-funcao que vai devolver uma cadeia de
        caracteres que corresponde a coluna definida na
        coordenada X, na direcao Norte. """        
        return inverte_palavra(escreve_sul())
    
    def escreve_este():
        """escreve_este: sub-funcao que vai devolver uma cadeia de
        caracteres que corresponde a linha definida na
        coordenada X, na direcao Este. 
        """        
        frase = ''
        for elem in g[coord_linha(c)]:
            frase = frase + elem
        return frase
    
    def escreve_oeste():
        """escreve_oeste: sub-funcao que vai devolver uma cadeia de
        caracteres que corresponde a coluna definida na
        coordenada X, na direcao Oeste."""         
        return inverte_palavra(escreve_este())
    
    def escreve_sudeste():
        """escreve_sudeste: sub-funcao que vai devolver uma cadeia de
        caracteres definida na coordenada X, na direcao Sudeste. 
        """         
        frase = ''
        col = coord_coluna(c)
        lin = coord_linha(c)
        
        while col != 0 and lin != 0:
            col = col - 1
            lin = lin - 1
        
        while col != grelha_nr_colunas(g) and lin != grelha_nr_linhas(g):
            frase = frase + grelha_elemento(g, lin, col)
            col = col + 1
            lin = lin + 1
            
        return frase
    
    def escreve_noroeste():
        """escreve_noroeste: sub-funcao que vai devolver uma cadeia de
        caracteres definida na coordenada X, na direcao Noroeste. 
        """         
        return inverte_palavra(escreve_sudeste())
    
    def escreve_sudoeste():
        """escreve_sudoeste: sub-funcao que vai devolver uma cadeia de
        caracteres que corresponde a coluna definida na
        coordenada X, na direcao Sudoeste. 
        """         
        frase = ''
        col = coord_coluna(c)
        lin = coord_linha(c)
        
        while col !=  grelha_nr_colunas(g) - 1 and lin != 0:
            col = col + 1
            lin = lin - 1
        
        while col != 0 and lin != grelha_nr_linhas(g) - 1:
            frase = frase + grelha_elemento(g, lin, col)
            col = col - 1
            lin = lin + 1
            
        frase = frase + grelha_elemento(g, lin, col)        
            
        return frase
    
    def escreve_nordeste():
        """escreve_nordeste: sub-funcao que vai devolver uma cadeira de
        caracteres que corresponde a coluna definida na
        coordenada X, na direcao Nordeste. Para tornar mais eficiente, e usada
        uma sub-funcao que inverte a cadeia de caracteres escrita a Sudoeste.
        """         
        return inverte_palavra(escreve_sudoeste())
        
    
    if e_coordenada(c) and e_grelha(g):
        direcao = coord_direcao(c)
        
        if e_sul(direcao):
            return escreve_sul()
        
        elif e_norte(direcao):
            return escreve_norte()
        
        elif e_leste(direcao):
            return escreve_este()
        
        elif e_oeste(direcao):
            return escreve_oeste()
        
        elif e_sudeste(direcao):
            return escreve_sudeste()
        
        elif e_noroeste(direcao):
            return escreve_noroeste()
        
        elif e_sudoeste(direcao):
            return escreve_sudoeste()
        
        elif e_nordeste(direcao):
            return escreve_nordeste()
    else:
        raise ValueError('grelha_linha: argumentos invalidos')
            

# RECONHECEDOR

def e_grelha(grelha):
    """ e_grelha : universal -> logico
    e_grelha(grelha) tem o valor verdadeiro se o arg for do tipo grelha 
    e falso caso contrario. """
    
    if isinstance(grelha, list):
        for linha in grelha:
            if not isinstance(linha, list):
                return False
            for elem in linha:
                if not isinstance(elem, str):
                    return False
  
        for i in range(len(grelha) - 1):
            if len(grelha[i]) != len(grelha[i + 1]):
                return False   
    else:
        return False
    
    return True



# TESTES

def grelhas_iguais(g1, g2):
    """ grelhas_iguais : grelha x grelha -> logico
    grelhas_iguais(g1, g2) devolve o valor verdadeiro se as grelhas forem
    iguais e falso caso contrario. """

    return g1 == g2


# _______________________________RESPOSTA____________________________________    
    
# CONSTRUTOR

def resposta(lst):
    """ resposta : lista de tuplos(string, coordenada) -> resposta
    resposta(lst) tem como valor a resposta que contem cada um dos tuplos que
    compoem a lista lst .
    Em caso de erro, o construtor gera um erro de valor. """
    
    if isinstance(lst, list):
        for tuplo in lst:
            if not (isinstance(tuplo, tuple) and tuplo[0] != '' and 
                    isinstance(tuplo[0], str) and e_coordenada(tuplo[1])):
                raise ValueError('resposta: argumentos invalidos')
            
    else:
        raise ValueError('resposta: argumentos invalidos')
    
    return ordena_lista(lst)


# SELETORES

def resposta_elemento(res, n):
    """ resposta_elemento : resposta x N0 |-> tuplo(string, coordenada)
    resposta_elemento(res, n) devolve o enesimo elemento da resposta res.
    Caso n seja menor que 0 ou maior ou igual que o numero de elementos da
    resposta erro, o seletor gera um erro de valor. """
    
    if n in range(len(res)):
        return res[n]
    
    else:
        raise ValueError('resposta_elemento: argumentos invalidos')
    

def resposta_tamanho(res):
    """ resposta_tamanho : resposta |-> N0
    resposta_tamanho(res) devolve o numero de elementos da resposta res. """
    
    return len(res)


# MODIFICADOR

def acrescenta_elemento(r, s, c):
    """ acrescenta_elemento : resposta x string x coordenada |-> resposta
    acrescenta_elemento(r, s, c) devolve a resposta r com mais um elemento,
    o tuplo (s, c). """
    
    return ordena_lista(r + [(s, c)])


# RECONHECEDOR

def e_resposta(lst):
    """ e_resposta : universal -> logico
    e_resposta(arg) tem o valor verdadeiro se o arg for do tipo resposta e
    falso caso contrario. """
    
    if isinstance(lst, list):
        if lst == []:
            return True
        else:
            for tuplo in lst:
                if (isinstance(tuplo, tuple) and tuplo[0] != '' and 
                        isinstance(tuplo[0], str) and e_coordenada(tuplo[1])):
                    return True 
                else:
                    return False                
    else:
        return False

# TESTES

def respostas_iguais(r1, r2):
    """ respostas_iguais : resposta x resposta -> logico
    respostas_iguais(r1, r2) devolve o valor verdadeiro se as respostas r1 e 
    r2 contiverem os mesmos tuplos e falso caso contrario. """
    
    if resposta_tamanho(r1)!=resposta_tamanho(r2):
        return False
           
    for i in range(resposta_tamanho(r1)):
            if not (resposta_elemento(r1,i)[0] == resposta_elemento(r2,i)[0] 
                    and coordenadas_iguais(resposta_elemento(r1,i)[1], 
                                           resposta_elemento(r2,i)[1])):
                    return False
    return True


def resposta_string(res):
    """ resposta_string : resposta -> string
    resposta_string(res) devolve a representacao externa da resposta res."""   
    
    res_str = '['
    for i in range(len(res)-1):
        frase = ''
        frase = ('<' + res[i][0] +':' + 
                 coordenada_string(res[i][1]) + '>, ')
        res_str = res_str + frase
    res_str = res_str + ('<' + res[-1][0] + ':' + 
                 coordenada_string(res[-1][1]) + '>]')
    return res_str


def sopa_letras(fich):
    """sopa_letras : cadeia de caracteres  resposta
    sopa_letras(fich) tem como resultado a resposta ao puzzle descrito 
    no ficheiro."""
    
    ficheiro = open(fich, 'r')
    lst_linhas = ficheiro.readlines()
    
    res = resposta([])
    grelha_ficheiro = grelha(limpa_ficheiro(lst_linhas))
    palavras_ficheiro = palavras(lst_linhas)
    
    for direcao in ('N', 'E', 'S', 'W', 'NW', 'NE', 'SE', 'SW'):
        res_dir = procura_palavras_numa_direcao(grelha_ficheiro, 
                                                palavras_ficheiro, direcao)
        for i in range(resposta_tamanho(res_dir)):
            tuplo_aux = resposta_elemento(res_dir, i)
            res = acrescenta_elemento(res, tuplo_aux[0], tuplo_aux[1])
    
    janela = janela_sopa_letras(fich)
    janela.mostra_palavras(res)
    janela.termina_jogo()
    ficheiro.close()
    
    return res


def procura_palavras_numa_direcao(grelha, palavras, direcao):
    """ procura_palavras_numa_direcao : 
    grelha x lista de strings x direcao -> 
    resposta
    procura_palavras_numa_direcao(grelha, palavras, dir) tem como resultado
    a resposta que representa as coordenadas das palavras encontradas na
    grelha. Para cada palavra, apresenta-se a coordenada do seu primeiro
    caracter seguindo a direcao em que se encontra a palavra. """
    
    def procura_sul():
        """procura_sul: sub-funcao responsavel pela procura das palavras da
        sopa de letras na direcao Sul, devolvendo uma resposta com as palavras
        escritas nessa direcao
        """
        res = []
        for palavra in palavras:
            for coluna in range(grelha_nr_colunas(grelha)):
                coord = coordenada(0, coluna, 'S')
                frase = grelha_linha(grelha, coord)
                linha = palavra_em_frase(frase, palavra)
                if linha != -1:
                    res = res + [(palavra, coordenada(linha, coluna, 'S'))]
                    
        return resposta(res)
    
    def procura_norte():
        """procura_norte: sub-funcao responsavel pela procura das palavras da
        sopa de letras na direcao Norte, devolvendo uma resposta com as 
        palavras escritas nessa direcao.
        """        
        res = []
        for palavra in palavras:
            for coluna in range(grelha_nr_colunas(grelha)):
                coord = coordenada(0, coluna, 'N')
                frase = grelha_linha(grelha, coord)
                linha = (grelha_nr_linhas(grelha) - 1 
                         - palavra_em_frase(frase,palavra))
                if palavra_em_frase(frase, palavra) != -1:
                    res = res + [(palavra, coordenada(linha, coluna, 'N'))]
                    
        return resposta(res)
    
    def procura_este():
        """procura_este: sub-funcao responsavel pela procura das palavras da
        sopa de letras na direcao Este, devolvendo uma resposta com as 
        palavras escritas nessa direcao.
        """        
        res = []
        for palavra in palavras:
            for linha in range(grelha_nr_linhas(grelha)):
                coord = coordenada(linha, 0, 'E')
                frase = grelha_linha(grelha, coord)
                coluna = palavra_em_frase(frase, palavra)
                if coluna != -1:
                    res = res + [(palavra, coordenada(linha, coluna, 'E'))]
                    
        return resposta(res)
    
    def procura_oeste():
        """procura_oeste: sub-funcao responsavel pela procura das palavras da
        sopa de letras na direcao oeste, devolvendo uma resposta com as 
        palavras escritas nessa direcao.
        """        
        res = []
        for palavra in palavras:
            for linha in range(grelha_nr_linhas(grelha)):
                coord = coordenada(linha, 0, 'W')
                frase = grelha_linha(grelha, coord)
                coluna = (grelha_nr_colunas(grelha) - 1 
                          - palavra_em_frase(frase, palavra))
                if palavra_em_frase(frase, palavra) != -1:
                    res = res + [(palavra, coordenada(linha, coluna, 'W'))]
                    
        return resposta(res)
    
    def procura_nordeste():
        """procura_nordeste: sub-funcao responsavel pela procura das palavras da
        sopa de letras na direcao Nordeste, devolvendo uma resposta com as 
        palavras escritas nessa direcao. A funcao e dividida em dois ciclos for
        que vao procurar as palavras na metade triangular superior e inferior da
        sopa de letras.
        """        
        res = []
        nr_linhas = grelha_nr_linhas(grelha)
        nr_colunas = grelha_nr_colunas(grelha)
        
        for palavra in palavras:
            for linha in range(nr_linhas):
                coord = coordenada(linha, 0, 'NE')
                frase = grelha_linha(grelha, coord)
                find = palavra_em_frase(frase, palavra)
                
                col_res = find
                lin_res = linha - find
                
                if find != -1:
                    res = res + [(palavra, 
                                  coordenada(lin_res, col_res, 'NE'))]
                    
            for coluna in range(1, nr_colunas):
                coord = coordenada(nr_linhas - 1, coluna, 'NE')
                frase = grelha_linha(grelha, coord)
                find = palavra_em_frase(frase, palavra)
                
                col_res = coluna + find
                lin_res = nr_linhas - 1 - find
                
                if find != -1:
                    res = res + [(palavra, 
                                  coordenada(lin_res, col_res, 'NE'))]                
                
        return resposta(res)
    
    
    def procura_sudoeste():
        """procura_sudoeste: sub-funcao responsavel pela procura das palavras da
        sopa de letras na direcao Sudoeste, devolvendo uma resposta com as 
        palavras escritas nessa direcao. A funcao e dividida em dois ciclos for
        que vao procurar as palavras na metade triangular superior e inferior da
        sopa de letras.
        """         
        res = []
        nr_linhas = grelha_nr_linhas(grelha)
        nr_colunas = grelha_nr_colunas(grelha)        
                
        for palavra in palavras:
            
            for coluna in range(0, nr_colunas):
                coord = coordenada(0, coluna, 'SW')
                frase = grelha_linha(grelha, coord)
                find = palavra_em_frase(frase, palavra)
                comp_frase = len(frase)
                
                col_res = coluna - find
                lin_res = find
                
                if find != -1:
                    res = res + [(palavra, 
                                  coordenada(lin_res, col_res, 'SW'))]             
            
            for linha in range(1, nr_linhas):
                coord = coordenada(linha, nr_colunas - 1, 'SW')
                frase = grelha_linha(grelha, coord)
                find = palavra_em_frase(frase, palavra)  

                col_res = nr_colunas - 1 - find
                lin_res = linha + find
                
                if find != -1:
                    res = res + [(palavra, 
                                  coordenada(lin_res, col_res, 'SW'))]
                            

        return resposta(res)
    
    
    def procura_noroeste():
        """procura_noroeste: sub-funcao responsavel pela procura das palavras da
        sopa de letras na direcao Noroeste, devolvendo uma resposta com as 
        palavras escritas nessa direcao. A funcao e dividida em dois ciclos for
        que vao procurar as palavras na metade triangular superior e inferior da
        sopa de letras.
        """         
        res = []
        nr_linhas = grelha_nr_linhas(grelha)
        nr_colunas = grelha_nr_colunas(grelha)  
        
        for palavra in palavras:
                       
            for linha in range(0, nr_linhas - 1):
                coord = coordenada(linha, nr_colunas - 1, 'NW')
                frase = grelha_linha(grelha, coord)
                find = palavra_em_frase(frase, palavra)  

                col_res = nr_colunas - 1 - find
                lin_res = linha - find
                
                if find != -1:
                    res = res + [(palavra, 
                                  coordenada(lin_res, col_res, 'NW'))] 
                    
            for coluna in range(0, nr_colunas):
                coord = coordenada(nr_linhas - 1, coluna, 'NW')
                frase = grelha_linha(grelha, coord)
                find = palavra_em_frase(frase, palavra)
                comp_frase = len(frase)
                
                col_res = coluna - find
                lin_res = nr_linhas - 1 - find
                
                if find != -1:
                    res = res + [(palavra, 
                                  coordenada(lin_res, col_res, 'NW'))]  
        return resposta(res)
    
    
    def procura_sudeste():
        """procura_sudeste: sub-funcao responsavel pela procura das palavras da
        sopa de letras na direcao Sudeste, devolvendo uma resposta com as 
        palavras escritas nessa direcao. A funcao e dividida em dois ciclos for
        que vao procurar as palavras na metade triangular superior e inferior da
        sopa de letras.
        """         
        res = []
        nr_linhas = grelha_nr_linhas(grelha)
        nr_colunas = grelha_nr_colunas(grelha)  
        
        for palavra in palavras:
                       
            for linha in range(0, nr_linhas):
                coord = coordenada(linha, 0, 'SE')
                frase = grelha_linha(grelha, coord)
                find = palavra_em_frase(frase, palavra)  

                col_res = find
                lin_res = linha + find
                
                if find != -1:
                    res = res + [(palavra, 
                                  coordenada(lin_res, col_res, 'SE'))] 
                    
            for coluna in range(1, nr_colunas):
                coord = coordenada(0, coluna, 'SE')
                frase = grelha_linha(grelha, coord)
                find = palavra_em_frase(frase, palavra)
                comp_frase = len(frase)
                
                col_res = coluna + find
                lin_res = find
                
                if find != -1:
                    res = res + [(palavra, 
                                  coordenada(lin_res, col_res, 'SE'))]  
        return resposta(res)
    
    
    if e_sul(direcao):
        return procura_sul()
    elif e_norte(direcao):
        return procura_norte()
    elif e_leste(direcao):
        return procura_este()
    elif e_oeste(direcao):
        return procura_oeste()
    elif e_nordeste(direcao):
        return procura_nordeste()
    elif e_sudoeste(direcao):
        return procura_sudoeste()
    elif e_noroeste(direcao):
        return procura_noroeste()
    elif e_sudeste(direcao):
        return procura_sudeste()
    
            



# _______________________________AUXILIARES__________________________________

def palavra_em_frase(frase, palavra):
    """ palavra_em_frase: string x string -> int
    palavra_em_frase(frase, palavra) tem como resultado a posicao da primeira 
    letra se a palavra se encontrar na frase e -1 caso contrario. """
    
    if palavra in frase == False:
        return -1
    else:
        i = 0
        while palavra in frase:
            frase = frase[1:]
            i = i + 1
        return i - 1
    

def limpa_ficheiro(lst_linhas):
    """ limpa_ficheiro: lista de strings -> grelha
    limpa_ficheiro(lst_linhas) tem como resultado a grelha do jogo, tendo como
    argumento a lista das linhas do ficheiro da sopa de letras. """
    
    lista = lst_linhas[:]

    del lista[0]
    del lista[0]
    rsl_lista = []
    for linha in lista:
        linha = linha[:-1]
        nova_linha = ''
        for i in range(len(linha) - 1, -1, -1):
            if linha[i] != ' ':
                nova_linha = linha[i] + ' ' + nova_linha
        rsl_lista = rsl_lista + [nova_linha]
            
    return rsl_lista


def palavras(lst_linhas):
    """ palavras: lista de strings -> lista de strings
    palavras(lst_linhas) tem como resultado as palavras a serem procuradas, 
    tendo como argumento a lista das linhas do ficheiro da sopa de letras. """
    
    frase = lst_linhas[1][10:][:-1] # da string de palavras retira inicio e \n
    lst_palavras = []
    palavra = ''
    for i in range(len(frase)):
        if frase[i] != ',' and frase[i] != ' ':
            palavra = palavra + frase[i]
        elif frase[i] == ' ':
            lst_palavras = lst_palavras + [palavra]
            palavra = ''
    lst_palavras = lst_palavras + [palavra]
    
    return lista_p_maiusculas(lst_palavras) # retorna em maiusculas


def inverte_palavra(palavra):
    """ inverte_palavra: string -> string
    inverte_palavra(palavra) tem como resultado a palavra do argumento
    invertida """
    
    rsl_palavra = ''
    for i in range(len(palavra)):
        rsl_palavra = palavra[i] + rsl_palavra
    return rsl_palavra  


def lista_p_maiusculas(palavras):
    """ lista_p_maiusculas: lista de strings -> lista de strings
    lista_p_maiusculas(palavras) tem como resultado a lista de palavras do
    argumento mas com as respectivas palavras em maiusculas."""
    
    def p_maiusculas(palavra):
        """ p_maiusculas: string -> string
        p_maiusculas(palavra) tem como resultado a palavra do argumento em 
        maiusculas. """
        p_mais = ''
        dic_abc = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
                   'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
                   'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 
                   's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'x': 'X', 'y': 'Y', 
                   'w': 'W', 'z': 'Z' }
        
        for i in range(len(palavra)):
            if palavra[i] in dic_abc:
                p_mais = p_mais + dic_abc[palavra[i]]
            else:
                p_mais = p_mais + palavra[i]
        return p_mais    
    
    rsl = []
    for elem in palavras:
        rsl = rsl + [p_maiusculas(elem)]
    return rsl


def ordena_lista(lst):
    """ ordena_lista: lista de tuplos -> lista de tupos
    ordena_lista(lst) tem como resultado a lista de tuplos correspondente a
    lista de tuplos do argumento ordenada """
    
    while not lista_ordenada(lst):
        maior_indice = len(lst) - 1
        for i in range(maior_indice):
            if (lst[i][0] > lst[i+1][0]):
                lst[i], lst[i+1] = lst[i+1], lst[i]
                maior_indice = maior_indice - 1
    return lst


def lista_ordenada(lst):
    """ lista_ordenada: lista -> logico
    lista_ordenada(lst) tem como resultado True se a lista de tuplos estiver
    ordenada e False se acontecer o contrario """
    
    maior_indice = len(lst) - 1
    
    for i in range(maior_indice):
        if (lst[i][0] > lst[i+1][0]):
            return False
        
    return True   