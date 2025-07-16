def videoProcessing(N, videos):
    # This function is a placeholder for video processing logic.
    # It can be used to handle video files, apply filters, or perform any other video-related tasks.
    videos.sort(key=lambda x: (-x[2], x[1]))
    print(videos)
    optimal = []
    for i in range(N):
        #print({videos[i][0]})
        optimal.append(videos[i][0])
    
    print("Optimal Videos: ", optimal)
    return optimal



N = 4
videos = [
    ["v1", 3, 1],
    ["v2", 1, 2], 
    ["v3", 4, 1],
    ["v4", 2, 2]
]

videoProcessing(N, videos)