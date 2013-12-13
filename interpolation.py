class TimeSeries(object):
    '''takes a parameter, data, of the form x,y tuples'''
   
    def __init__(self, data):
         '''this is to store the time_series data in self.data'''
        self.data = data

   
    def get(self, x):
         '''if the variable is matching one of the data points, return the corresponding y value'''
        for (xi,yi) in self.data:
            if xi == x:
                return yi
        
        raise Exception("Didn't find the value")
    
    def view(self):
        '''function to view the data, but empty function right now'''
        pass


    
class StepFunctionTimeSeries(TimeSeries):
    def get(self, x):
        '''if the new data point is closer to x than the last point, it becomes the new closest point'''
        closest_point = None
        for (xi, yi) in self.data:
            if closest_point is None:
                closest_point = (xi, yi)
            else:
                cx, cy = closest_point
                if abs(xi-x) < abs(cx-x):
                    closest_point = (xi, yi)
        return closest_point[1]
	#Meow, Meow, Meow, Meow, Meow, Meow, Woof

    
class LinearTimeSeries(TimeSeries):
    def __init__(self, data):
        '''the data needs to be sorted. is called from a previous class to avoid mistakes''' 
        TimeSeries.__init__(self, data)
        self.data.sort()
    
    def get(self, x):
         '''Method to find two closest data points to x and linearly
    interpolate between them to estimate the y value'''
        # if it's out of range to the left,
        # return the first value
        if x < self.data[0][0]:
            return self.data[0][1]
        # if it's out of range to the right,
        # return the last value
        elif x > self.data[-1][0]:
            return self.data[-1][1]
        # otherwise, it's within the range
        for (n, (xi, yi)) in enumerate(self.data):
            if xi == x:
                return yi
            elif xi > x:
                n1, n2 = n-1, n
                x1, x2 = self.data[n1][0], self.data[n2][0]
                y1, y2 = self.data[n1][1], self.data[n2][1]
                d1, d2 = abs(x-x1), abs(x-x2)
                total_weight = float(d1 + d2)
                w1 = y1 * (total_weight-d1) / total_weight
                w2 = y2 * (total_weight-d2) / total_weight
                return w1 + w2


		#I love code
