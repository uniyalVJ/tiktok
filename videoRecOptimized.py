
#N = 5, K = 3
#watch_time = [10, 20, 30, 40, 50]
#engagement = [1, 4, 2, 3, 1]
#

def videoRecOptimized(N, K, watch_time, engagement):
    
    
    total_value = 0
    for i in range(N):
        watch_time[i] = watch_time[i] * engagement[i]
        #print(watch_time[i])
        
    i = 0
    for i in range(N):
        for j in range(i+1, N):
            for g in range(j+1, N):
                if(watch_time[i] + watch_time[j] + watch_time[g]) >= total_value:
                    total_value = watch_time[i] + watch_time[j] + watch_time[g]
                    print(f"Selected videos: {i}, {j}, {g} with total value: {total_value}")
    
    return total_value
                    
        
    
videoRecOptimized(5, 3, [10, 20, 30, 40, 50], [1, 4, 2, 3, 1])