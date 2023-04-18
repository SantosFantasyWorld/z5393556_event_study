import os
import toolkit_config as tk_cfg

DATADIR = tk_cfg.DATADIR
FF_FACTORS_CSV = os.path.join(DATADIR,'ff_daily.csv')
START = '1900-01-01'
END = '2020-12-31'

def csv_locs(tic):
    tic = tic.lower().replace('.', '_')
    rec_csv = os.path.join(DATADIR, f'{tic}_rec.csv')
    prc_csv = os.path.join(DATADIR, f'{tic}_prc.csv')
    return {
        'rec_csv': rec_csv,
        'prc_csv': prc_csv,
    }


def standardise_colnames(df):
    cols = set(df.columns)
    def _parse_name(colname):
        new_name = colname.lower().replace(' ', '_')
        if new_name == colname:
            return colname
        elif new_name in cols:
            return '_' + new_name
        else:
            return new_name
    return df.rename(columns=_parse_name)
