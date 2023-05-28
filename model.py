def curve(use_rate):
    return market_table[use_rate]
def show_graph():
    plt.scatter(df['Danceability'], df['Energy'], c=df['Cluster'], cmap='viridis')
    plt.xlabel('Danceability')
    plt.ylabel('Energy')
    plt.title('K-means Clustering')
    plt.show()
def evaluation(lots_available, time, price_table):
    # monthly renting  fixed_income
    threshold = config.fixed_income + past_data(time) * lots_available * price_table(config.parking_lot)
    return threshold 