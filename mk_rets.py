import pandas as pd
import event_study.config as cfg

def mk_ret_df(tic):
    locs = cfg.csv_locs(tic)
    pth = locs['prc_csv']
    df = pd.read_csv(pth,index_col='Date',parse_dates=['Date'])
    df = cfg.standardise_colnames(df)
    df = df.sort_index()
    df.loc[:,'ret'] = df.loc[:,'adj_close'].pct_change()
    ff_df = pd.read_csv(cfg.FF_FACTORS_CSV,index_col='Date',parse_dates=['Date'])
    cols = ['mkt','ret']
    df = df.join(ff_df,how='inner')[cols]
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    tic = 'TSLA'
    df = mk_ret_df(tic)
    print(df)
    df.info()