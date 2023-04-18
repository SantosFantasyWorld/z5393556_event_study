from event_study import download
from event_study import mk_rets
from event_study import mk_events
from event_study import mk_cars
from event_study import test_hypo

def main(tic,update_csv=True):
    if update_csv is True:
        download.get_data(tic)
    else:
        print('skipping download')
    # step1
    ret_df = mk_rets.mk_ret_df(tic)

    # step2
    event_df = mk_events.mk_event_df(tic)

    # step3
    cars_df = mk_cars.mk_cars_df(ret_df,event_df)

    # step4
    res = test_hypo.calc_tstats(cars_df)
    print(res)

if __name__ == "__main__":
    tic = 'TSLA'
    update_csv = False
    main(tic=tic, update_csv=update_csv)