import matplotlib.pyplot as plt


def plot_line(x, y, xlabel, ylabel, title, out_path=None, xticks=None):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o')
    if xticks is not None:
        plt.xticks(xticks)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(alpha=0.3)
    if out_path:
        plt.tight_layout()
        plt.savefig(out_path)
        plt.close()
    else:
        plt.show()
