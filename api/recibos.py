from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def gera_recibo(nome, dia, mes, ano, valor):
    """
    nome:Str, dia:Str, mes:int, ano:Str, valor:float
    """
    meses = [
        None,
        'Janeiro',
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro'
    ]
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('recibo.html')
    html = template.render({
        'nome': nome,
        'valor': valor,
        'dia': dia,
        'mes': meses[mes],
        'ano': ano,
    })
    # print(html)
    HTML(string=html).write_pdf('recibos/{}-{}.pdf'.format(nome.replace(' ', '_'), meses[mes]))