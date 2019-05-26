# Concurrency And Parallelism In Python - ***`pyconcurrencydemo`*** (Still in Construction)

This project actually shows all respective example(s) of concurrency and multiprocessing in python.
In this sample project we have `ThumbnailMgr.py` library which actually creates thumbnail provided video URL in it's `generateThumbnails()` method.
Also, in this method we have put some delay intentionally so that we time this function in different scenario we should see be able to see clear different in terms of numbers. 

We have video URL constant defined under `Constant.py` class. To run this locally in their machine someone has to change this 
video file path. This could be any video of any size.

Now, there are 4 types of sample test script which is used primarily test out concurrency and parallelism in below manner.
All the libraries gets called from `main.py`. This script is the entry point for this entire project.

1. ***`SingleThreadSample.py`*** -  
    
    This is how any sample program would have ran synchronously to generate thumbnail from 2 videos each after other.
    When we timed it it came as per below.
    
    ```python
    
    Extracting frames from video ....
    Generating and save thumbnails ...
    success
    Extracting frames from video ....
    Generating and save thumbnails ...
    success
    Done!
             11331 function calls (11329 primitive calls) in 157.986 seconds
    
       Random listing order was used
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        12/10    0.000    0.000    0.011    0.001 C:\Users\sugho\AppData\Local\Programs\Python\Python36-32\lib\os.py:195(makedirs)
           12    0.000    0.000    0.000    0.000 C:\Users\sugho\AppData\Local\Programs\Python\Python36-32\lib\ntpath.py:121(splitdrive)
           12    0.000    0.000    0.000    0.000 C:\Users\sugho\AppData\Local\Programs\Python\Python36-32\lib\ntpath.py:199(split)
           12    0.000    0.000    0.000    0.000 C:\Users\sugho\AppData\Local\Programs\Python\Python36-32\lib\ntpath.py:33(_get_bothseps)
           10    0.000    0.000    0.004    0.000 C:\Users\sugho\AppData\Local\Programs\Python\Python36-32\lib\genericpath.py:16(exists)
            1    0.001    0.001  157.986  157.986 D:/projects/pyconcurrencydemo/SingleThreadSample.py:4(process)
            2    0.055    0.027    3.077    1.539 D:\projects\pyconcurrencydemo\ThumbnailMgr.py:37(__getVideoFrames)
            2  154.790   77.395  157.985   78.993 D:\projects\pyconcurrencydemo\ThumbnailMgr.py:6(generateThumbnails)
           10    0.000    0.000    0.001    0.000 D:\projects\pyconcurrencydemo\ThumbnailMgr.py:64(__convertImageToThumbs)

   
    ```  
2. ***`MultiThreadingSample`*** - 
    
    Using thread we tried to improve the performance but it came out almost same.
    
    ```python
    
    Extracting frames from video ....
    Extracting frames from video ....
    Generating and save thumbnails ...
    Generating and save thumbnails ...
    Done!
             83 function calls in 154.466 seconds
    
       Random listing order was used
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            2    0.000    0.000    0.000    0.000 C:\Users\sugho\AppData\Local\Programs\Python\Python36-32\lib\_weakrefset.py:38(_remove)
            2    0.000    0.000    0.000    0.000 C:\Users\sugho\AppData\Local\Programs\Python\Python36-32\lib\_weakrefset.py:81(add)
            1    0.000    0.000  154.466  154.466 D:/projects/pyconcurrencydemo/MultiThreadingSample.py:5(process)
            2    0.000    0.000    0.000    0.000 C:\Users\sugho\AppData\Local\Programs\Python\Python36-32\lib\threading.py:215(__init__)

    ``` 
  
These above 2 behaviours are likely to be expected. As we had created 2 thread, we thought it would run in parallel 
but only one thread can hold the GIL at a time. One thread must wait for another one to release. 


3. ***`Multiprocessing`*** - 
    
    In this example we tried to create 2 different process and tried to run in parallel and that actually brought up the performance quite a bit.
    When we timed it here how it looks like - 
    
    ```python
    
    Extracting frames from video ....
    Extracting frames from video ....
    Generating and save thumbnails ...
    Generating and save thumbnails ...
    Done!
             1838 function calls (1783 primitive calls) in 98.175 seconds
    
       Random listing order was used

 
    ```

    
4. ***`Async IO`***
    
    This is another approach which people like to do bring in concurrency model in python programming.
    Async IO got introduced after python 3.4+ and we can use quite easily to bring in concurrency in your program. 
    
    

Though remember concurrency and parallelism is quite a different but somewhat releated as well.

#### References :

[1] - `Multithreading`  - - https://hackernoon.com/concurrent-programming-in-python-is-not-what-you-think-it-is-b6439c3f3e6a

[2] - `Multiprocessing` - https://www.geeksforgeeks.org/multiprocessing-python-set-1/

[3] - `Parallel Programming` - https://realpython.com/async-io-python/        
        
[4] - `Async Programming` - https://www.youtube.com/watch?v=BI0asZuqFXM

Disclaimer :
------------

This project has been tested against ***python 3.7.3*** version.