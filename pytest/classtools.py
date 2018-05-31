class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s: %s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':
    class Toptest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = Toptest.count
            self.attr2 = Toptest.count + 1
            Toptest.count += 2
    class SubTest(Toptest):
        pass

    X, Y = Toptest(), SubTest()
    print(X)
    print(Y)
