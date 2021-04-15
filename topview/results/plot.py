import matplotlib.pyplot as plt


def plot_acc(ax, dist, acc, name):
    '''
    acc: (K, num)
    dist: (K, )
    name: (K, )
    '''
    assert(acc.shape[0] == len(name))

    for i in range(len(name)):
        ax.plot(dist, acc[i], label=name[i])

    ax.legend()
    ax.grid(True)
    ax.set_xlabel('Maximum allowed distance to GT (m)')
    ax.set_ylabel('Fraction of samples within distance')


def plot_mean_err(ax, mean_err, name):
    '''
    mean_err: (K, )
    name: (K, )
    '''
    plt.ylim([0, 0.5])
    ax.grid(True)
    ax.bar(name, mean_err)
