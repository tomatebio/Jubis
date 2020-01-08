from models import Bem, Usuario




#busca bem
SQL_BEM_POR_PATRIMONIO = 'SELECT numero_patrimonio, descricao, sala, verificado_por, status, verificado_em from bem where numero_patrimonio = %s'
SQL_ATUALIZA_BEM = 'UPDATE bem SET  descricao = %s, sala =%s, verificado_por =%s,  status =%s, verificado_em =%s where numero_patrimonio = %s'

SQL_BUSCA_BEM = 'SELECT numero_patrimonio, descricao, sala, verificado_por, status, verificado_em from bem'
SQL_BUSCA_SALA = 'SELECT numero_patrimonio, descricao, sala, verificado_por, status , verificado_em from bem where sala = %s'
SQL_CONTA_BEM = "SELECT COUNT(numero_patrimonio) from bem"
SQL_CONTA_BEM_NA = "SELECT COUNT( * ) FROM bem WHERE status ='Não encontrado'"



# buscas por usuario
SQL_USUARIO_POR_ID = 'SELECT  id, nome, email, senha from usuario where id = %s'
SQL_CRIAR_USUARIO = 'INSERT INTO usuario (id, nome, email, senha) values (%s,%s, %s,%s)'
SQL_CONTAR_USUARIOS = 'SELECT COUNT(nome)  from usuario'



class BemDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, bem):
        cursor = self.__db.connection.cursor()

        if (bem.patrimonio):
            cursor.execute(SQL_ATUALIZA_BEM, (bem.descricao, bem.local , bem.verificado_por,bem.status, bem.verificado_em, bem.patrimonio))
        else:
           # cursor.execute(SQL_CRIA_JOGO, (jogo.nome, jogo.categoria, jogo.console))
           # jogo.id = cursor.lastrowid
            pass
        self.__db.connection.commit()
        return bem

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_BEM)
        bem = traduz_bem(cursor.fetchall())
        return bem

    def listar_sala(self,sala):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_SALA, (sala,))
        bem = traduz_bem(cursor.fetchall())
        return bem

    def busca_por_num(self, num):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BEM_POR_PATRIMONIO, (num,))
        tupla = cursor.fetchone()
        if type(tupla) is tuple:
            return Bem(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5])
        else:
            return None

    def contar_bem(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CONTA_BEM)
        numero = cursor.fetchone()
        return numero[0]

    def contar_bem_na(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CONTA_BEM_NA)
        numero = cursor.fetchone()
        return numero[0]


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario

    def novo_usuario(self,id,nome, email,senha):

        cursor = self.__db.connection.cursor()

        cursor.execute(SQL_CRIAR_USUARIO, (id, nome, email,senha))
        self.__db.connection.commit()

        return Usuario(id,nome,email,senha)
    def contar_usuario(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CONTAR_USUARIOS)
        numero= cursor.fetchone()
        return numero[0]



def traduz_bem(bem):
    def cria_bem_com_tupla(tupla):
        return Bem(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5])
    return list(map(cria_bem_com_tupla, bem))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2], tupla[3])