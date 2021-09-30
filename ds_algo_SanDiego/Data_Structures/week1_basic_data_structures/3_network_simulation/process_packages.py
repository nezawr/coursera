# python3

from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.finish_time = deque()
        self.time = 0

    def process(self, request):
        # write your code here
        while self.finish_time and self.finish_time[0] <= request.arrived_at:
            self.finish_time.popleft()

        if len(self.finish_time) >= self.max_size:
            return Response(True, -1)

        else:
            start_time = max(request.arrived_at, self.finish_time[-1] if self.finish_time else 0)
            self.finish_time.append(start_time + request.time_to_process)
            return Response(False, start_time)
        


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses

def process_packets(requests, buffersize):
    buffer = deque(maxlen=buffersize)

    start_times = [None] * len(requests)

    for i, (arrival, duration) in enumerate(requests):

        while buffer and buffer[0] <= arrival:
            buffer.popleft()

        if len(buffer) >= buffersize:
            start_times[i] = -1

        else:
            start_times[i] = max(arrival, buffer[-1] if buffer else 0)
            buffer.append(start_times[i] + duration)

    return start_times


    return

def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)
    
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
