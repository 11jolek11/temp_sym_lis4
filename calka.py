import random
import math


class MonteCarlo:
    """
    Integrating using Monte Carlo method.
    Supports some of elementary functions.
    Extended numerical integration avoiding 'h' finding problem
    """
    def __init__(self, xp:float, xk:float, formula:str, n:int=1000000):
        self.formula = formula
        for _ in self.formula:
            self.formula.replace('\n', '')
        self.n = n
        self.xp = xp
        self.xk = xk
        # self.dx = (self.xk - self.xp)/n
        self.dx = self.xk - self.xp

    def fx(self):
        """
        Function fx represents function f(x) provided by user
        """
        return eval("lambda x:" + self.formula, math.__dict__)

    def start(self):
        """
        Starts calculating value.
        """
        s = 0
        # i = 0
        func = self.fx()
        for i in range(self.n):
            if i <= self.n-2:
                temp = s
                r = random.uniform(self.xp, self.xk)
                s = temp + func(r)
            else:
                s = (s/self.n)*self.dx
        return s

class MonteCarlo2:
    """
    Integrating using Monte Carlo method.
    Supports some of elementary functions.
    """
    # FIXME: nie radzi sobie z xp < 0
    # FIXME: nie działa w 100%
    def __init__(self, xp:float, xk:float, g:float, d:float, formula:str, n:int=1000000):
        self.formula = formula
        for _ in self.formula:
            self.formula.replace('\n', '')
        self.n = n
        self.xp = xp
        self.xk = xk
        self.g = g
        self.d = d
        self.dx = (self.xk - self.xp)
        self.h = (self.g - self.d)
        self.inside = 0

    def fx(self):
        """
        Function fx represents function f(x) provided by user
        """
        return eval("lambda x:" + self.formula, math.__dict__)

    def start(self):
        """
        Starts calculating value.
        """
        func = self.fx()
        l_plus = 0
        for i in range(self.n):
            xi = random.uniform(self.xp, self.xk)
            yi = random.uniform(self.d, self.g)
            r = func(xi)
            if r > 0 and r >= yi:
                l_plus += 1
            elif r < 0 and r < yi:
                l_plus -=1
            else:
                l_plus += 0
        return (l_plus/self.n)*self.h*self.dx



if __name__ == "__main__":
    test_object = MonteCarlo(0, 1, "exp((-1*(x**2))/2)")
    print(test_object.start())
    test = MonteCarlo2(xp=0, xk=1, g=1.1, d=0, formula="exp((-1*(x**2))/2)")
    print(test.start())
