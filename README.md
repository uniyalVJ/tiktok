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