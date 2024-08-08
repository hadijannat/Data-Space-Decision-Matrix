import matplotlib.pyplot as plt
import numpy as np

class DecisionMatrix:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.setup_matrix()

    def setup_matrix(self):
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.set_xlabel('Number of Partners')
        self.ax.set_ylabel('Data Complexity')
        self.ax.set_title('Data Space Decision Matrix')

        # Add quadrant labels
        self.ax.text(2.5, 2.5, 'Traditional\nData Sharing', ha='center', va='center')
        self.ax.text(7.5, 2.5, 'Consider\nData Space', ha='center', va='center')
        self.ax.text(2.5, 7.5, 'Consider\nData Space', ha='center', va='center')
        self.ax.text(7.5, 7.5, 'Strongly Consider\nData Space', ha='center', va='center')

        # Add dividing lines
        self.ax.axvline(x=5, color='k', linestyle='--')
        self.ax.axhline(y=5, color='k', linestyle='--')

    def plot_point(self, partners, complexity):
        self.ax.plot(partners, complexity, 'ro')
        
    def save_matrix(self, filename='decision_matrix.png'):
        self.fig.savefig(filename)

    def show_matrix(self):
        plt.show()

if __name__ == "__main__":
    matrix = DecisionMatrix()
    matrix.plot_point(7, 8)  # Example point
    matrix.show_matrix()
