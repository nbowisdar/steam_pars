from multiprocessing import Process
from steam_pars.database.mongo_db.lootfarm_db import get_loot_inst
from steam_pars.database.mongo_db.tradegg_db import get_trade_gg_inst
from steam_pars.src.calculate import main
from steam_pars.src.pulling import start_pulling
from time import sleep

def test():
    while True:
        print('hello')
        sleep(1)

if __name__ == '__main__':

    # get mongo_db instances
    loot = get_loot_inst()
    trade = get_trade_gg_inst()
    # creating two main process
    pulling_proc = Process(target=start_pulling)
    calculating_proc = Process(target=main, args=(loot, trade))
    #calculating_proc = Process(target=test)


    # starting them
    pulling_proc.start()
    calculating_proc.start()

    pulling_proc.join()
    calculating_proc.join()

