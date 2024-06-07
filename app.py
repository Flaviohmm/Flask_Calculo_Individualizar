from flask import Flask, render_template, request

app = Flask(__name__)


# Função para calcular individualização do FGTS
def calcular_individualizacao_fgts(saldo_fgts, meses_trabalhados):
    return saldo_fgts / meses_trabalhados

# Função para calcular individualização do PGFN
def calcular_individualizacao_pgfn(divida_pgfn, meses_em_divida):
    return divida_pgfn / meses_em_divida

@app.route('/api/individualizacao', methods=['GET', 'POST'])
def get_individualizacao():
    if request.method == 'POST':
        saldo_fgts = float(request.form['saldo_fgts'])
        meses_trabalhados = int(request.form['meses_trabalhados'])
        divida_pgfn = float(request.form['divida_pgfn'])
        meses_em_divida = int(request.form['meses_em_divida'])

        individualizacao_fgts = calcular_individualizacao_fgts(saldo_fgts, meses_trabalhados)
        individualizacao_pgfn = calcular_individualizacao_pgfn(divida_pgfn, meses_em_divida)

        data = {
            'fgts_value': individualizacao_fgts,
            'pgfn_value': individualizacao_pgfn,
            'saldo_fgts': saldo_fgts,
            'meses_trabalhados': meses_trabalhados,
            'divida_pgfn': divida_pgfn,
            'meses_em_divida': meses_em_divida
        }

        return render_template('template.html', **data)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)