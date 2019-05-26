import cProfile,pstats, io

def timeStatsProfiler(func):

    def profile(*args,**kwargs):

        # In outer section of code
        pr = cProfile.Profile()

        # In section you want to profile
        pr.enable()

        func(*args,**kwargs)

        #code of interest
        pr.disable()

        # Back in outer section of code
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s)
        ps.print_stats()
        print(s.getvalue())

    return profile