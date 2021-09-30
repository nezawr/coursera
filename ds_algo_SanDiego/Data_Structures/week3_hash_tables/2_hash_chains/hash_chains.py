# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for i in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            if 0 <= query.ind < self.bucket_count:
                self.write_chain(cur for cur in reversed(self.elems[query.ind]))
            else:
                print('Invalid index')
        else:

            outer_ind = -1
            inner_ind = -1
            hash_value = self._hash_func(query.s)
            for i, element in enumerate(self.elems[hash_value]):
                    if element == query.s:
                        outer_ind = hash_value
                        inner_ind = i

            if query.type == 'find':
                self.write_search_result(outer_ind != -1)
            elif query.type == 'add':
                if inner_ind == -1:
                    self.elems[hash_value].append(query.s)
            else:
                if inner_ind != -1:
                    self.elems[hash_value].pop(inner_ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
