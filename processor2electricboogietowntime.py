from cProfile import label
from pylab import *
from matplotlib import pyplot as plt 
import numpy as np 
def processor(
    control_path, 
    sample_path_list, 
    sample_name_list,
    thickness_list, 
    control_thickness,
    control_name,
    title,
    upperlimit,
    lowerlimit
    ):
    # Create list that we can append all the values to if we want 
    processed_list = []
    # Import control values as lists to normalize data with 
    con_nm, con_t = loadtxt(control_path, unpack = True)
    processed_list.append(con_nm)
    for i in range(len(sample_path_list)):
        # Preallocate memory and clear datam from lists 
        sam_nm  = []
        sam_t = []
        # Memory for values 
        sample_path = sample_path_list[i]
        thickness = thickness_list[i]
        sample_name = sample_name_list[i]
        # Import data 
        sam_nm, sam_t = loadtxt(sample_path, unpack = True)
        # Normalize the data 
        norm_t =  [m/n for m,n in zip(sam_t, con_t)]
        # Make all values positive
        norm_t = [abs(number) for number in norm_t]
        # Absorption coefficient
        alpha = -np.log(norm_t) / (
            thickness * 1e-7)
        # Append to list 
        processed_list.append(alpha)
        # Plot the values 
        plt.plot(sam_nm, alpha, label = sample_name)
    con_t = [abs(number) for number in con_t]
    alpha_c = -np.log(con_nm) / (
        control_thickness * 1e-7
    )
    plt.plot(con_nm, alpha_c, label = control_name)
    plt.yscale('log')
    plt.legend()
    plt.title(title)
    plt.xlim(lowerlimit,upperlimit)
    plt.show()

    return processed_list

