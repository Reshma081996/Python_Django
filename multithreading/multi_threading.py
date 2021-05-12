
"""
        MULTI TASKING - SIMULETANEOUSLY EXCUTE MULTIPLE TASK AT A TIME AND FAST
TWO WAYS TO ACHIEVE MULTI TASKING
 1.MULTIPROCESSING--->different application(pycharm,notepad,chrome) run paralleling at the same time
                     multiple process excute simuletaneously

2.MULTI THREADING-->single process or program divided into different subprocess and thread excuting them simulatenously
                ---->fast
                """

import threading
print(threading.currentThread().getName())