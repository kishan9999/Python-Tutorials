import numpy as np

class LinearRegression:
    
    def fit(self, X, y):
        n = X.shape[0]
        sx = np.sum(X)
        sy = np.sum(y)
        sx2 = np.sum(np.multiply(X, X)) 
        sy2 = np.sum(np.multiply(y, y))
        sxy = np.sum(np.multiply(X, y))
        self.intercept_ = (sy*sx2-sx*sxy)/(n*sx2-sx*sx)
        self.coef_ = (n*sxy-sx*sy)/(n*sx2-sx*sx)
        
    def predict(self, x):
        y1 = self.coef_*x+self.intercept_
        return y1
        

