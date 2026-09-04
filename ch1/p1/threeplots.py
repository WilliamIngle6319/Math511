# threeplots.py
#   Create all three types of systems of linear equastions in two dimensions

import matplotlib.pyplot as plt
import numpy as np

def main():
    threeplots()

def threeplots():
    titletext = [ 'Independent', 'Dependent', 'Inconsistent' ]

    fig, axs = plt.subplots(1, 3)

    for i, ax in enumerate(axs):
        ax.spines[['left', 'bottom']].set_position('center')
        ax.spines[['top', 'right']].set_color('none')

        ax.plot([-2, 2], [-2, 2], 'b')
        ax.title.set_text(titletext[i])

        match i:
            case 0:
                ax.plot([-1,2], [2,-2], 'b')
            case 1:
                ax.plot([-2,2], [-2,2], 'b')
            case 2:
                ax.plot([-2,1], [-1,2], 'b')
        
    fig.align_labels()  # same as fig.align_xlabels(); fig.align_ylabels()

    plt.show()

main()