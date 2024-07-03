import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    fig.suptitle('Gráfica de Pastel')  # Agregar un título a la figura
    plt.savefig('pie.png')
    plt.close()