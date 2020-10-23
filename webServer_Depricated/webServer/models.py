class ControllerInformation():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.x = 0
        self.y = 0
        self.lt = 0
        self.rt = 0
        self.lb = 0
        self.rb = 0
        self.u = 0
        self.d = 0
        self.l = 0
        self.r = 0
        self.lsx = 0
        self.lsy = 0
        self.rsx = 0
        self.rsy = 0
        self.st = 0
        self.se = 0

    def __str__(self):
        return "a: {}, b: {}, x: {}, y:{}\nlt: {}, rt: {}, lb: {}, rb: {}\nu: {}, d: {}, l: {}, r: {}\nlsx: {}, lsy: {}, rsx: {}, rsy: {}\nst: {}, se: {}".format(
            self.a, self.b, self.x, self.y, self.lt, self.rt, self.lb, self.rb, self.u, self.d, self.l, self.r, self.lsx, self.lsy, self.rsx, self.rsy, self.st, self.se
        )

    def toDict(self):
        return {
            'a': self.a, 'b': self.b, 'x': self.x, 'y': self.y, 
            'u': self.u, 'd': self.d, 'l': self.l, 'r': self.r,
            'lt': self.lt, 'rt': self.rt, 'lb': self.lb, 'rb': self.rb, 
            'lsx': self.lsx, 'lsy': self.lsy, 'rsx': self.rsx, 'rsy': self.rsy,
            'st': self.st, 'se': self.se
        }

    def updateController(self, updateDict):
        try:
            self.a = updateDict['a']
            self.b = updateDict['b']
            self.x = updateDict['x']
            self.y = updateDict['y']
            self.lt = updateDict['lt']
            self.rt = updateDict['rt']
            self.lb = updateDict['lb']
            self.rb = updateDict['rb']
            self.u = updateDict['u']
            self.d = updateDict['d']
            self.l = updateDict['l']
            self.r = updateDict['r']
            self.lsx = updateDict['lsx']
            self.lsy = updateDict['lsy']
            self.rsx = updateDict['rsx']
            self.rsy = updateDict['rsy']
            self.st = updateDict['st']
            self.se = updateDict['se']
        except Exception as e:
            print("ERROR updating controller...")
            return e
        return ''