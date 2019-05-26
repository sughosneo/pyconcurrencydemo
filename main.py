from pyconcurrencydemo.SingleThreadSample import *
from pyconcurrencydemo.MultiThreadingSample import *
from pyconcurrencydemo.MultiProcessingSample import *
from pyconcurrencydemo.AsyncIOSample import *

if __name__ == '__main__':

    # '''
    #     Video thumbnail creation process - with normal single thread sync execution.
    # '''
    # singleThreadSample = SingleThreadSample()
    # singleThreadSample.process()
    #
    # '''
    #     Video thumbnail creation process - with multi-threading in place
    # '''
    # multiThreadSample = MultiThreadingSample()
    # multiThreadSample.process()
    #
    # '''
    #     Video thumbnail creation process - with multi-processing
    # '''
    # multiProcessSample = MultiProcessingSample()
    # multiProcessSample.process()

    '''
        Video thumbnail creation process - with Async/Wait
    '''
    asyncIOProcessSample = AsyncIOSample()
    asyncIOProcessSample.process()

