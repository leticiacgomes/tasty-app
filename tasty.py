from flask import Flask, render_template

class Receita:
    def __init__(self, nome, categoria, tempo):
        self.nome=nome
        self.categoria=categoria
        self.tempo=tempo

app = Flask(__name__)

@app.route('/inicio')
def ola():
    receita_um = Receita('Bolo de cenoura', 'Doce', '60')
    receita_dois = Receita('Strogonoff', 'Salgado', '50')
    receita_tres = Receita('Banoffe', 'Doce', '80')

    lista = [receita_um, receita_dois, receita_tres]
  
    return render_template('lista.html', titulo='Tasty App', receitas=lista)

app.run()