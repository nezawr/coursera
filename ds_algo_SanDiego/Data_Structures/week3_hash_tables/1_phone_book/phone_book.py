# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    phone_book = {}
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            if cur_query.number in phone_book:
                phone_book[cur_query.number].name = cur_query.name
            else: # otherwise, just add it
                phone_book[cur_query.number] = cur_query
        elif cur_query.type == 'del':
            if cur_query.number in phone_book:
                del phone_book[cur_query.number]
        else:
            response = 'not found'
            if cur_query.number in phone_book:
                response = phone_book[cur_query.number].name
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

