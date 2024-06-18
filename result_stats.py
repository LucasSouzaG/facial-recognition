import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from jinja2 import Template
import pytz


def buildReport(df):
    # Passo 1: Preparar os Dados

    # Exemplo de dados
    # data = {
    #     'image': ['image 1', 'image 2', 'image 3'],
    #     'feliz': [1, 0, 1],
    #     'triste': [0, 1, 0],
    #     'neutro': [0, 0, 0]
    # }

    # df = pd.DataFrame(data)
    # print(df)

    # Passo 2: Gerar Gráficos
    # Gráfico de Barras

    # Gráfico de Barras Empilhadas
    def plot_stacked_bar_chart(df):
        df.set_index('Image')[['Feliz', 'Triste', 'Neutro','Surpreso','Medo','Nojo','Raiva']].plot(kind='bar', stacked=True)
        plt.title('Distribuição de Emoções por Imagem')
        plt.xlabel('Imagem')
        plt.ylabel('Número de Ocorrências')
        plt.legend(title='Emoções')
        plt.tight_layout()
        plt.savefig('graph_barras.png')
        # plt.show()

    # Linha do Tempo

    # Gráfico de Linhas
    def plot_line_chart(df):
        df.set_index('Image')[['Feliz', 'Triste', 'Neutro','Surpreso','Medo','Nojo','Raiva']].plot(kind='line', marker='o')
        plt.title('Evolução das Emoções ao Longo das Imagens')
        plt.xlabel('Imagem')
        plt.ylabel('Número de Ocorrências')
        plt.legend(title='Emoções')
        plt.tight_layout()
        plt.savefig('graph_linhas.png')
        # plt.show()


    # Gráfico de Pizza

    # Gráfico de Pizza
    def plot_pie_chart(df):
        total_emotions = df[['Feliz', 'Triste', 'Neutro','Surpreso','Medo','Nojo','Raiva']].sum()
        plt.figure(figsize=(6, 6))
        total_emotions.plot(kind='pie', autopct='%1.1f%%', labels=['Feliz', 'Triste', 'Neutro','Surpreso','Medo','Nojo','Raiva'])
        plt.title('Distribuição Geral das Emoções')
        plt.ylabel('')  # Remove label do eixo Y
        plt.tight_layout()
        plt.savefig('graph_pizza.png')
        # plt.show()

    # Plotar os gráficos
    plot_stacked_bar_chart(df)
    plot_line_chart(df)
    plot_pie_chart(df)

    # Passo 4: Gerar o Relatório


    # Exemplo de template HTML
    template_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>[Relatório] Estatística da Aula</title>
    </head>
    <body>
        <h1>Relatório de Emoções dos Alunos</h1>
        <p><strong>Data:</strong> {{ data_aula }}</p>
        <p><strong>Nome do Aluno:</strong> {{ Nome_aluno }}</p>
        <p><strong>Professor:</strong> {{ professor }}</p>
        <p><strong>Instituição de Ensino:</strong> {{ Instituicao }}</p>
        <p><strong>Disciplina:</strong> {{ disciplina }}</p>
        
        <h2>Resumo Geral</h2>
        <p><strong>Duração da Aula:</strong> {{ duracao_aula }}</p>
        <p><strong>Emoção Predominante:</strong> {{ emocao_predominante }}</p>

        <h2>Distribuição de Emoções ao Longo da Aula</h2>
        <table border="1">
            <tr>
                <th>Imagens analisadas</th>
                <th>Feliz</th>
                <th>Triste</th>
                <th>Raiva</th>
                <th>Nojo</th>
                <th>Medo</th>
                <th>Surpreso</th>
                <th>Neutro</th>
            </tr>
            {% for row in distribuicao_emocoes %}
            <tr>
                <td>{{ row.Image }}</td>
                <td>{{ row.Feliz }}</td>
                <td>{{ row.Triste }}</td>
                <td>{{ row.Raiva }}</td>
                <td>{{ row.Nojo }}</td>
                <td>{{ row.Medo }}</td>
                <td>{{ row.Surpreso }}</td> 
                <td>{{ row.Neutro }}</td> 

            </tr>
            {% endfor %}
        </table>

        <!-- Imagens dos gráficos podem ser inseridas aqui -->
        <h2>Gráficos</h2>
        
        <img src="graph_barras.png" alt="Gráfico de Barras">
        <img src="graph_linhas.png" alt="Linha do Tempo">
        <img src="graph_pizza.png" alt="Gráfico de Pizza">

        <h2>Recomendações</h2>

        <h3>Para Manter o Aluno Feliz</h3>
        <ul>
            <li>Manter atividades interativas, como discussões em grupo e quizzes.</li>
            <li>Diversificar métodos de ensino, incluindo vídeos, demonstrações práticas e atividades participativas.</li>
            <li>Oferecer elogios e reconhecimento para manter o moral dos alunos alto.</li>
            <li>Promover um ambiente de aprendizado positivo e encorajador.</li>
            <li>Incorporar pausas curtas para atividades recreativas ou exercícios de alongamento.</li>
        </ul>

        <h3>Para Reduzir Tristeza</h3>
        <ul>
            <li>Simplificar explicações difíceis e usar exemplos práticos e analogias.</li>
            <li>Oferecer apoio adicional, como sessões de perguntas e respostas ou tutoriais complementares.</li>
            <li>Encourajar a comunicação aberta para que os alunos possam expressar dificuldades.</li>
            <li>Proporcionar feedback positivo e construtivo para melhorar a autoestima dos alunos.</li>
            <li>Implementar técnicas de ensino diferenciadas para atender diferentes estilos de aprendizagem.</li>
        </ul>

        <h3>Para Envolver o Aluno Neutro</h3>
        <ul>
            <li>Introduzir mais atividades colaborativas que incentivem a participação ativa.</li>
            <li>Fornecer feedback constante e individualizado para manter os alunos envolvidos.</li>
            <li>Usar tecnologia educativa, como aplicativos interativos, para aumentar o engajamento.</li>
            <li>Desafiar os alunos com problemas práticos e situações do mundo real.</li>
            <li>Criar metas claras e alcançáveis para motivar os alunos a participar ativamente.</li>
        </ul>

        <h2>Conclusão</h2>
        <p>Esse relatório visa proporcionar ao professor uma visão clara e objetiva sobre as emoções dos alunos durante a aula, permitindo identificar momentos chave e ajustar estratégias pedagógicas para melhorar a experiência de aprendizado.</p>
    </body>
    </html>
    """

    # Dados para preencher o template
    context = {
        'data_aula': datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M'),
        'professor': 'Prof. Claudionor',
        'disciplina': 'Processamento de Imagens  Visão Computacional',
        'Instituicao': 'Universidade Adventista de São Paulo',
        'Nome_aluno': 'DEVE SER VARIAVEL',
        'duracao_aula': '60 minutos',
        'emocao_predominante': 'DEVE SER VARIAVEL DE ACORDO COM A QUANTIADE DE IMAGENS QUE SERÃO PASSADA DO ALUNO',
        'distribuicao_emocoes': df.to_dict(orient='records'),

    }

    template = Template(template_html)
    report_html = template.render(context)

    # Salvar relatório como arquivo HTML
    with open('relatorio_emocoes.html', 'w', encoding='utf-8') as f:
        f.write(report_html)

def dataReport(original_data):

    # Inicializa o novo formato de dados
    data = {
        'Image': [],
        'Raiva': [],
        'Nojo': [],
        'Medo': [],
        'Feliz': [],
        'Triste': [],
        'Surpreso': [],
        'Neutro': []
    }

    # Mapeia as expressões para as colunas correspondentes
    expressions = ['Raiva', 'Nojo', 'Medo', 'Feliz', 'Triste', 'Surpreso', 'Neutro']

    # Popula o novo formato de dados
    for i, entry in enumerate(original_data):
        data['Image'].append(f'Image {i + 1}')
        
        # Inicializa todas as expressões com 0
        expression_dict = {expr: 0 for expr in expressions}
        
        # Atualiza a expressão correspondente com 1
        expression = entry['expressao']
        if expression in expression_dict:
            expression_dict[expression] = 1
        
        # Adiciona os valores ao dicionário de dados
        for key in expressions:
            data[key].append(expression_dict[key])

    # Exibe o resultado
    df = pd.DataFrame(data)
    print(df)

    buildReport(df)


if __name__ == '__main__':
    dados = [{'imagem': 'b09ac60b-2d9c-11ef-b2f8-80bf07906c97.jpg', 'expressao': 'Raiva'}, {'imagem': 'bc9fd905-2d9c-11ef-9252-80bf07906c97.jpg', 'expressao': 'Feliz'}, {'imagem': 'c2c8f9f4-2d9c-11ef-b14e-80bf07906c97.jpg', 'expressao': 'Medo'}]
    dataReport(dados)

