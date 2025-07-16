

class TrendingProcessor:
    def __init__(self):
        self.events = []  # List to store events in order
        self.hashtag_position = {}  # Hashmap: hashtag -> list of indices in event array "fyp": [0,2,4]


    def addEvent(self, timestamp, hashtag):
        self.events.append((timestamp, hashtag))
        event_index = len(self.events) - 1
        #print(event_index)
        #print(self.events)
        if hashtag not in self.hashtag_position:
            self.hashtag_position[hashtag] = []
        self.hashtag_position[hashtag].append(event_index)
        #print(self.hashtag_position)


    def getTrending(self, timestamp, T):
        #getTrending(5,3) = [2,5]
        #
        window_start = timestamp - T
        window_end = timestamp
        hashtag_count = {}  # Dictionary to count occurrences of hashtags in the window
        #I need events between window_start and window_end
        for i in range(len(self.events)):
            event_timestamp = self.events[i][0]
            event_hashtag = self.events[i][1]
            
            if window_start <= event_timestamp <= window_end:
                #print(f"Event at index {i} with timestamp {event_timestamp} and hashtag '{event_hashtag}' is within the window [{window_start}, {window_end}]")
                if event_hashtag not in hashtag_count:
                    hashtag_count[event_hashtag] = 0
                hashtag_count[event_hashtag] += 1
        
        max_count = max(hashtag_count.values(), default=0)
        max_trending = [hashtag for hashtag, count in hashtag_count.items() if count == max_count]
        result = min(max_trending)  # Get lexicographically smallest
        print(result)
            
            
        
        
        return










processor = TrendingProcessor()

# Add events (timestamp, hashtag)
processor.addEvent(1, "fyp")
processor.addEvent(2, "dance")  
processor.addEvent(3, "fyp")
processor.addEvent(4, "viral")
processor.addEvent(5, "fyp")
processor.addEvent(6, "dance")
processor.addEvent(7, "music")
processor.addEvent(8, "fyp")

# Queries
processor.getTrending(5, 3)   # Query 1
processor.getTrending(6, 2)   # Query 2
processor.getTrending(8, 4)   # Query 3
processor.getTrending(10, 5)  # Query 4