from colors import red
import logging

def plot_simulation_results(results, nb_simul, nb_workers):
    """Plots a time series chart of a simulation."""

    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
    except ImportError:
        print red('>>> Info: matplotlib is required for charting.  Please install using `pip install matplotlib`')
        return None

    l_list=len(results[0])
    h_list=len(results)

    x_data=[x for x in range(l_list)]

    # add sub processes results to chart.  Can be one or more lists
    for sub_proc_results in results:
        plt.plot(x_data,sub_proc_results,'black')

    # merged results
    merged_results=[sum(results[i][j] for i in range(h_list)) / h_list for j in range(l_list)]
    plt.plot(x_data,merged_results,'r-',linewidth=3)

    # display final result
    plt.text(l_list, merged_results[l_list - 1], '{0:.2%}'.format(merged_results[l_list - 1]), color='red')

    # legends
    red_patch = mpatches.Patch(color='red', label='consolidated results',linewidth=2)
    black_patch = mpatches.Patch(color='black', label='workers results',linewidth=1)

    # determine best place to put legend on screen
    if (merged_results[l_list - 1]/plt.get_current_fig_manager().canvas.figure.axes[0].dataLim.y1)<0.4:
        location=1 # legend on top right corner
    else:
        location=4 # legend on bottom right corner
    plt.legend(handles=[black_patch,red_patch],loc=location)

    plt.title('Simulation Stages\n({:,} simulations dispatched to {} workers)'.format(nb_simul,nb_workers),fontsize=12,fontweight='bold')
    plt.xlabel('simulations ({}s)'.format(collect_frequency(nb_simul)),fontsize=12,fontweight='bold')
    plt.ylabel('odds (%)',fontsize=12,fontweight='bold')

    # styling
    plt.style.use('ggplot')

    # display chart
    plt.show()


def collect_frequency(simulations):
    """
    Calculates the frequency at which sub processes should collect intermediary results for plotting
    This is done to ensure that the total number of data points loaded in the charts do not exceed
    a breaking limit which, based on our tests seems to be about 7,000 data points
    """

    max_data_points_to_load = 5000     # the max number of data points we allow in the charts

    # The + 100 at the end is added to ensure that the frequency is rounded to the higher 100s
    # to ensure the total number of collections cannot be higher than 5000
    cf = ((simulations / max_data_points_to_load)/100)*100 + 100
    return cf
