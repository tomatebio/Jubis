from flask import render_template, request, redirect, session, flash, url_for
import bcrypt
import time

from models import Bem
from dao import *
from Jubis import db, app

bem_dao = BemDao(db)
usuario_dao = UsuarioDao(db)

@app.route('/')
def index():
    numero= usuario_dao.contar_usuario()
    bem_total= bem_dao.contar_bem()
    bem_na= bem_dao.contar_bem_na()
    relacao=round((bem_na/bem_total)*100,2)
    lista = bem_dao.listar()

    return render_template('resumo.html', titulo='Resumo do Inventário',
                           numero=numero, bem_total=bem_total,bem_na=bem_na, relacao=relacao, bens=lista)




# @app.route('/')
# def index():
#     lista = bem_dao.listar()
#     return render_template('lista.html', titulo='Bens',
#                            bens=lista)

# @app.route('/novo')
# def novo():
#     if 'usuario_logado' not in session or session['usuario_logado'] == None:
#         return redirect(url_for('login', proxima=url_for('novo')))
#     return render_template('novo.html', titulo='Novo jogo')
#
# @app.route('/criar', methods=['POST',])
# def criar():
#     nome = request.form['nome']
#     categoria = request.form['categoria']
#     console = request.form['console']
#     jogo = Jogo(nome, categoria, console)
#     jogo = jogo_dao.salvar(jogo)
#
#     arquivo = request.files['arquivo']
#     upload_path = app.config['UPLOAD_PATH']
#     timestamp = time.time()
#     arquivo.save(f'{upload_path}/capa{jogo.id}--{timestamp}.jpg')
#     return redirect(url_for('index'))
#


@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/add_login')
def add_login():
    return render_template('add_login.html')

@app.route('/autentica_login',  methods=['POST', ])
def autentica_login():
    root=request.form["root"]
    id=request.form["id"]
    usuario = request.form["usuario"]
    email=request.form["email"]
    senha1 = request.form["senha1"]
    senha2= request.form["senha2"]


    if senha1 != senha2:
        flash("As senhas do usuario não confere!")
        return render_template("add_login.html")

    senha = request.form['root_senha'].encode("utf8")
    validar = bcrypt.checkpw(senha,app.config["SENHA"].encode("utf8"))

    if root==app.config["ROOT"] and validar:
        hashed = bcrypt.hashpw(senha1.encode("utf-8"), bcrypt.gensalt())
        usuario_novo= usuario_dao.novo_usuario(id,usuario,email, hashed)
        flash("Usuário {} {} adicionado com sucesso".format(usuario_novo.id,usuario_novo.nome))
        return render_template("add_login.html")
    else:
        flash("Usuário não adicionado")
        return render_template("add_login.html")





@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    senha=request.form['senha'].encode("utf8")
    if usuario and bcrypt.checkpw(senha, usuario.senha.encode("utf8")):
        session['usuario_logado'] = usuario.id
        flash(usuario.nome + ' logou com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Não logado, tente denovo!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))

@app.route('/form_busca_patrimonio')
def form_busca_patrimonio():
    proxima=request.args.get('proxima')
    return render_template('form_busca.html', proxima=proxima)


@app.route('/buscar_num' , methods=['POST',])
def buscar_num():
    bem=bem_dao.busca_por_num(request.form["numero"])
    if type(bem) is Bem:
        return render_template("editar_bem.html", bem=bem)
    else:
        flash('Não foi encontrado o bem!')
        return render_template('form_busca.html')



@app.route('/form_busca_sala')
def form_busca_sala():
    proxima=request.args.get('proxima')
    return render_template('form_busca_sala.html', proxima=proxima)


@app.route('/buscar_sala' , methods=['POST',])
def buscar_sala():
    sala=request.form["sala"]
    lista = bem_dao.listar_sala(sala)
    if type(lista) is list:
        return render_template('lista.html', titulo='Bens na sala  {}'.format(sala),bens=lista)
    else:
        flash('Não foi encontrado a sala')
        return render_template('form_busca_sala.html')


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))

    bem = bem_dao.busca_por_num(id)
    return render_template("editar_bem.html", bem=bem)





@app.route('/atualizar', methods=['POST',])
def atualizar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('buscar_num')))

    patrimonio= request.form['patrimonio']
    descricao = request.form['descricao']
    local=request.form['local']
    status = request.form['status']
    user =  session['usuario_logado']
    data = time.strftime('%Y-%m-%d %H:%M:%S')

    bem=Bem( patrimonio, descricao, local,user, status, data)
    bem_dao.salvar(bem)
    flash("Bem atualizado com sucesso")
    return redirect(url_for('form_busca_patrimonio'))
#
# @app.route('/deletar/<int:id>')
# def deletar(id):
#     jogo_dao.deletar(id)
#     flash('O jogo foi removido com sucesso!')
#     return redirect(url_for('index'))
#
# @app.route('/uploads/<nome_arquivo>')
# def imagem(nome_arquivo):
#     return send_from_directory('uploads', nome_arquivo)