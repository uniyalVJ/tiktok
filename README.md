Practice/Interviewing questions for Tiktok


1. Video Reccomendation Optimization
Problem:
TikTok wants to optimize their recommendation algorithm. Given a user's viewing history and a list of available videos, find the maximum total watch time you can achieve by recommending exactly K videos to the user.
Details:

You have N videos available, each with a predicted watch time watch_time[i] and engagement score engagement[i]
You must recommend exactly K videos
The total value is calculated as: sum(watch_time[i] * engagement[i]) for selected videos
You cannot recommend the same video twice

Example:
N = 5, K = 3
watch_time = [10, 20, 30, 40, 50]
engagement = [1, 4, 2, 3, 1]
Constraints:

1 ≤ N ≤ 1000
1 ≤ K ≤ N
1 ≤ watch_time[i] ≤ 100
1 ≤ engagement[i] ≤ 10

Your task: Write a function that returns the maximum total value possible.



Question 2: Real-time Stream Processing
Problem:
TikTok needs to process live video stream metadata to detect trending hashtags. You need to implement a sliding window system that tracks hashtag frequency over the last T seconds.
Details:

Events arrive as (timestamp, hashtag) pairs
You need to support two operations:

addEvent(timestamp, hashtag) - add a new hashtag event
getTrending(timestamp, T) - get the most frequent hashtag in the window [timestamp-T, timestamp]


Events can arrive out of order (but within reasonable bounds)
If there's a tie in frequency, return the lexicographically smallest hashtag

Example:
pythonprocessor = TrendingProcessor()

# Add events
processor.addEvent(1, "fyp")
processor.addEvent(2, "dance")  
processor.addEvent(3, "fyp")
processor.addEvent(4, "viral")
processor.addEvent(5, "fyp")
processor.addEvent(6, "dance")

# Query trending hashtags
print(processor.getTrending(5, 3))  # Window [2,5] -> "fyp" (appears 2 times)
print(processor.getTrending(6, 2))  # Window [4,6] -> "dance" or "viral" (tie, return "dance")
Constraints:

1 ≤ timestamp ≤ 10^9
1 ≤ T ≤ 10^6
Hashtag length ≤ 20 characters
Up to 10^5 events total
Up to 10^4 queries

Your task: Implement the TrendingProcessor class with both methods.


Question 3: Video Processing Pipeline
Problem:
TikTok's video processing system needs to handle video uploads efficiently. Given a list of video upload requests, each with a processing time and priority, determine the optimal order to process them to minimize total waiting time.
Details:

Each video has: processing_time and priority (higher number = higher priority)
Videos with the same priority should be processed in order of shortest processing time first
Return the order of video IDs that minimizes total waiting time
Total waiting time = sum of (waiting_time + processing_time) for each video

Example:
pythonvideos = [
    {"id": "v1", "processing_time": 3, "priority": 1},
    {"id": "v2", "processing_time": 1, "priority": 2}, 
    {"id": "v3", "processing_time": 4, "priority": 1},
    {"id": "v4", "processing_time": 2, "priority": 2}
]

# Expected output: ["v2", "v4", "v1", "v3"]
# Reasoning: Priority 2 first (v2, v4), then priority 1 (v1, v3)
# Within same priority, shortest processing time first
Input Format:

First line: integer N (number of videos)
Next N lines: video_id, processing_time, priority

Output Format:

List of video IDs in optimal processing order

Constraints:

1 ≤ N ≤ 10^5
1 ≤ processing_time ≤ 100
1 ≤ priority ≤ 10
video_id is a string of length ≤ 20

Sample Input:
4
v1 3 1
v2 1 2
v3 4 1
v4 2 2
Sample Output:
["v2", "v4", "v1", "v3"]