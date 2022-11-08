from pylab import *

def processor(
    control_path,
    sample_path,
    thickness
    ):
    con_nm, con_t = loadtxt(control_path, unpack = True)
    sam_nm, sam_t = loadtxt(sample_path, unpack = True)
    samnonneg_t = [] 
    for i in range(len(sam_t)):
        a = sam_t[i]

        # Check for negative values
        if a < 0: 
            a = a 
        samnonneg_t.append(a)

        # Normalized thickness 
    norm_t = [m/n for m,n in zip(samnonneg_t, con_t)]

        # Calculate the absorption coefficient
    alpha = -np.log(norm_t) / (
        thickness * 1e-7)
        
        # Return the values 
    return sam_nm, alpha
    
def conprocessor(
    con_filepath,
    con_thickess #350 microm
    ):

    con_nm, con_t = loadtxt(con_filepath, unpack = True)
    alpha = -np.log(con_t) / (
        con_thickess * 1e-7
    )
    return con_nm, alpha