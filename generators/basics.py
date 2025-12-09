def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))

print(get_chai_list())