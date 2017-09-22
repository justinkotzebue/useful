import os
import glob


folder = r"\\ncr104\d$\NAER\S2\unzipped"


glob.glob(os.path.join(folder,'*201709[1]*'))
glob.glob(os.path.join(folder,'*201709[1][2-9]*'))

glob.glob(os.path.join(folder,'*201709{12..31}*'))
