import glob
import os

import pandas as pd

if __name__ == "__main__":

    final_df = pd.DataFrame()

    for f in sorted(glob.glob("files/*.xlsx")):
        df = pd.read_excel(f, index_col=0)
        df.columns = [ f"{c} ({os.path.basename(f)})" for c in df.columns.values]
        final_df = pd.concat([final_df, df.iloc[:, 0]], axis=1)

    final_df.to_excel("output/output.xlsx")
