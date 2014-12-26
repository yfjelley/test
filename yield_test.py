def test_yield():
    print "test yield"
    says = (yield)
    print says
if __name__ == "__main__":
    client = test_yield()
    client.next()
    client.send("hello world!")
