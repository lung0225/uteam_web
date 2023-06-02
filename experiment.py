from model import curve
def experiment():
    
def show_graph():
    plt.scatter(df['Danceability'], df['Energy'], c=df['Cluster'], cmap='viridis')
    plt.xlabel('Danceability')
    plt.ylabel('Energy')
    plt.title('K-means Clustering')
    plt.show()