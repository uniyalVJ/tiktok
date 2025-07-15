
#N = 5, K = 3
#watch_time = [10, 20, 30, 40, 50]
#engagement = [1, 4, 2, 3, 1]
#

def videoRecOptimized(N, K, watch_time, engagement):
    
    
    total_value = 0
    
    values = [watch_time[i] * engagement[i] for i in range(N)]
    desc_values = [(values[i], i) for i in range(N)]
    desc_values.sort(reverse=True)
    #print(desc_values[0][0])
    #print("K value: ", K)
    for i in range(K):
        #print(i)
        #print(desc_values[i][0])
        total_value += desc_values[i][0]
        #print("Total value: ", total_value)
        
    print("Final Total Value: ", total_value)
    return total_value
    
                    
        
    
videoRecOptimized(5, 3, [10, 20, 30, 40, 50], [1, 4, 2, 3, 1])