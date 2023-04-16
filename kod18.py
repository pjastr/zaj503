class Test:
    def __getitem__(self, items):
        print(type(items), items)

        
test = Test()
test[4]
test[5:65:5]
test['Olsztyn']