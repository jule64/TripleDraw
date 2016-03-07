import_ploting_libs_ok=True

from colors import red
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
except Exception:
    import_ploting_libs_ok=False

def plot_simulation_results(results, nb_simul, nb_workers):
    if(not import_ploting_libs_ok):
        print red('>>> Warning: matplotlib is required for charting.  Please install using `pip install matplotlib`')
        return

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
    red_patch = mpatches.Patch(color='red', label='Merged stages',linewidth=2)
    black_patch = mpatches.Patch(color='black', label='Per-worker stages',linewidth=1)
    plt.legend(handles=[black_patch,red_patch],loc=4)
    plt.title('Simulation Stages\n({:,} simulations dispatched to {} workers)'.format(nb_simul,nb_workers),fontsize=12,fontweight='bold')
    plt.xlabel('simulations (100s)',fontsize=12,fontweight='bold')
    plt.ylabel('odds (%)',fontsize=12,fontweight='bold')

    # styling
    plt.style.use('ggplot')
    # plt.xscale('log')

    # display chart
    plt.show()