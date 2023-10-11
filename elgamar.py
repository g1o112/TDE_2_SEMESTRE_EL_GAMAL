import random
import math

#Função p/ exponenciação modular
def mod_exp(b, p, m):
    r = 1
    while p > 0:
        if p % 2 == 1:
            r = (r * b) % m
        b = (b * b) % m
        p //= 2
    return r

def gerar_chave():
  p = 426405985185585738245912460581 #numero primo GIGANTE
  d = random.randint(2, p-2) #chave privada deve estar entre 2 e p-2
  e1 = random.randint(2, p) #primeira parte p criptografar, inteiro aleatorio
  e2 = mod_exp(e1,d,p) #segunda parte p criptografar, calcular e1^d mod p
  return p, d, e1, e2


#transforma m para ascii
def para_ascii(m):
    m_cod = [ord(char) for char in m]
    return m_cod

def criptografar(p, e1, e2, m):
  r = random.randint(2, p-2) #inteiro aleatorio
  c1 = mod_exp(e1,r,p) #primeira cifra
  c2 = m * (mod_exp(e2,r,p)) #segunda cifra
  return c1, c2

#descriptografar a mensagemmmm
def descriptografar(p, d, c1, c2):
  s = mod_exp(c1,d,p)
  s_inverso = mod_exp(s,p-2,p)
  m = c2 * s_inverso % p
  return m

#etapa dps d descriptografar, transformar nos numeros ascii dnv e formar o texto original 
def para_string(cod_ascii):
    letra = chr(cod_ascii)
    return letra


def main():
  m = "gio" #mensagem
  m_cod = para_ascii(m) #mensagem dps de mudar para ascii
  print(m_cod) #letras em ascii
  p, d, e1, e2 = gerar_chave()

  print("Mensagem: ", m)
  print("Chave pública (p, e1, e2): ", {p},{e1},{e2})
  print("Chave privada (d): ", {d})

#criptografando o texto----------------------
  c = [
     [1,2],
     [3,4],
     [5,6]
  ]

  for i in range(len(m)):
     c1, c2 = criptografar(p, e1, e2, m_cod[i])
     c[i][0] = c1
     c[i][1] = c2

  print("Texto criptografado: ", c)
    
#descriptografando o texto----------------------
  m_descript = [
     [0],
     [0],
     [0]
  ]

  for i in range(len(m)):
     m_descod = descriptografar(p, d, c[i][0], c[i][1])
     m_descript[i] = para_string(m_descod)
     
  qualquer = '' #variavel qualquer para armazenar o texto original 
  for i in range(len(m)):
     qualquer += str(m_descript[i]) #transformando em string e concatenando

  print("Mensagem descriptografada:",qualquer)

if __name__ == '__main__':
  main()