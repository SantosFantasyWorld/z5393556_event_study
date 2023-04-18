import os
import pandas as pd
import yfinance as yf
import toolkit_config as tk_cfg

TIC = 'tsla'
PRC_CSV = os.path.join(tk_cfg.DATADIR , 'tsla_prc.csv')
START = '1900-01-01'
END = '2020-12-31'


def get_data0(tic):
    df = yf.download(tic,
                     start=START,
                     end=END,
                     ignore_tz=True
                     )
    df.to_csv(PRC_CSV)

def get_data1(tic):
    filename = f'{tic}_prc.csv'
    pth = os.path.join(tk_cfg.DATADIR,filename)
    df = yf.download(tic,
                     start=START,
                     end=END,
                     ignore_tz=True
                     )
    df.to_csv(pth)

def load_prc0(tic):
    filename = f'{tic}_prc.csv'
    pth = os.path.join(tk_cfg.DATADIR,filename)
    df = pd.read_csv(pth)
    print(df)

def load_prc1(tic):
    filename = f'{tic}_prc.csv'
    pth = os.path.join(tk_cfg.DATADIR,filename)
    df = pd.read_csv(pth)
    lower_columns_name = {column:column.lower() for column in df.columns}

    df = df.rename(columns=lower_columns_name)
    df.info()


if __name__ == "__main__":
    # get_data0(tic=TIC)
    get_data1(tic=TIC)
    # load_prc0(tic=TIC)
    load_prc1(tic=TIC)