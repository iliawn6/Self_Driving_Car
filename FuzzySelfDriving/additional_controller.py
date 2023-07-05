import numpy as np

class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    # fuzzify

    def front_dist(self, x):
        membership_func_close_f = 0
        membership_func_moderate_f = 0
        membership_func_far_f = 0

        if x <= 0:
            membership_func_close_f = 0
        elif x > 0 and x <= 50:
            membership_func_close_f = -0.02 * x + 1
        # close -- done

        if x >= 40 and x <= 50:
            membership_func_moderate_f = 0.1 * x - 4
        elif x > 50 and  x <= 100:
            membership_func_moderate_f = -0.02 * x + 2 
        # moderate --- done

        if x >= 90 and x <= 200:
            membership_func_far_f = 0.0090 * x - 0.8181
        elif x > 200:
            membership_func_far_f = 1
        # far --- done

        return [membership_func_close_f, membership_func_moderate_f, membership_func_far_f]

    def gas(self, x):
        membership_func_low = 0
        membership_func_med = 0
        membership_func_high = 0

        if x <= 0:
            membership_func_low = 0
        elif x > 0 and x <= 5:
            membership_func_low = 0.2 * x + 0
        elif x > 5 and x <= 10:
             membership_func_low = -0.2 * x + 2
        # close -- done

        if x >= 0 and x < 15:
            membership_func_med = 0.0666 * x + 0
        elif x >= 15 and  x <= 30:
            membership_func_med = -0.0666 * x + 2 
        # moderate --- done

        if x >= 25 and x <= 30:
            membership_func_high = 0.2 * x - 5
        elif x > 30 and x <= 90:
            membership_func_high = -0.0166 * x + 1.5   
        elif x > 90: membership_func_high = 0 
        # far --- done

        return [membership_func_low, membership_func_med, membership_func_high]


    # inference

    def inference(self, forward_dist):
        gas_low = forward_dist[0]
        gas_mid = forward_dist[1]
        gas_high = forward_dist[2]

        return [gas_low, gas_mid, gas_high]
    

    # defuzzify 
    
    def defuzzify(self, speed):
        soorat = 0.0
        makhraj = 0.0
        X=np.linspace(0, 200, 1000)
        delta = X[1] - X[0]
        for i in X:
            temp = self.gas(i)
            m = max(min(temp[0], speed[0]), min(temp[1], speed[1]), min(temp[2], speed[2]))
            soorat = soorat + m * i * delta
            makhraj = makhraj + m * delta
        center = 0.0
        if not makhraj == 0:
            center = 1.0 * float(soorat) / float(makhraj)

        return center        




    
    def __init__(self):
        pass
        

    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """

        #fuzzify
        dist = self.front_dist(center_dist)

        #inference
        inf = self.inference(dist)
        
        res = self.defuzzify(inf)

        return res
    