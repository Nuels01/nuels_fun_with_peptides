from pyteomics import achrom
import matplotlib.pyplot as plt

def predict_lc_retention_times(peptides):
    """
    Calculates the retention time of each peptide

    Parameters
    ----------
    peptides: list of lists, list of strings, string
            contains the peptide sequences

    Returns
    -------
    dic
            each peptide connected with ther predicted retention time
    """
    pep_retention_times = {}
    if type(peptides) == str:
        pep_retention_times[peptides] = round(achrom.calculate_RT(peptides, achrom.RCs_guo_ph7_0),2)
    else:
        for peptide in peptides: 
          if type(peptide) == list:
           for pep_list in peptide:
                pep_retention_times[pep_list] = round(achrom.calculate_RT(pep_list, achrom.RCs_guo_ph7_0), 2)
          else:
                pep_retention_times[peptide] = round(achrom.calculate_RT(peptide, achrom.RCs_guo_ph7_0),2)

    return pep_retention_times


def plot_retention_time(retention_times, resolution=30):
    """
    Plots the retention time of the peptides as a histogram

    Parameters
    ----------
    retention_times: dic
            contains the peptides with their retentiontime 
    
    resolution: int 
            determines how many histogram bins are shown
    Returns
    -------
            None
    """
    if type(retention_times) == dict:
        plt.hist(retention_times.values(),resolution)
    elif type(retention_times) == list:
        plt.hist(retention_times, resolution)
    else: 
        return "Nice you destroyed the function! Maybe it was a wrong datatype"
    plt.xlabel("retention times")
    plt.ylabel("number of peptides")
    plt.show()


def select_retention_time_window(peptide_rt_map, lower_ret_time, upper_ret_time):
    """
    Searches and select all peptides that are in the given range.

    Parameters
    ----------
    peptide_rt_map: dic
            holds the sequences and the time 
    
    lower_ret_time: float
            the minimal time that is selected
        
    upper_ret_time: float
            the maximal time that is selected
    Returns
    -------
    list: 
            contains all selected peptides
    """
    selected_peptides = []
    if type(peptide_rt_map) == dict: 
        for peptide, time in peptide_rt_map.items(): 
            if time >= lower_ret_time and time <= upper_ret_time:
                selected_peptides.append(peptide)
            else: 
                continue
        return selected_peptides
    else: 
        return "Nice try but wrong type of data"