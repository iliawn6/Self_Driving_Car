import numpy as np

class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """
    #fuzzify
    
    def d_L(self, x):
        membership_func_close_L = 0
        membership_func_moderate_L = 0
        membership_func_far_L = 0

        if x <= 0:
            membership_func_close_L = 1
        elif x > 0 and x <= 50:
            membership_func_close_L = -0.02 * x + 1
        # close_L -- done

        if x >= 35 and x <= 50:
            membership_func_moderate_L = 0.0666666 * x - 2.3333333
        elif x > 50 and  x <= 65:
            membership_func_moderate_L = -0.0666666 * x + 4.3333333 
        # moderate_L --- done

        if x >= 50 and x <= 100:
            membership_func_far_L = 0.02 * x - 1
        elif x > 100:
            membership_func_far_L = 1
        # far_L --- done

        return [membership_func_close_L, membership_func_moderate_L, membership_func_far_L]



    def d_R(self, x):        
        membership_func_close_r = 0
        membership_func_moderate_r = 0
        membership_func_far_r = 0
        if x <= 0:
            membership_func_close_r = 1
        elif x >= 0 and x <= 50:
            membership_func_close_r = -0.02 * x + 1
        # close_L -- done

        if x >= 35 and x <= 50:
            membership_func_moderate_r = 0.0666 * x - 2.3333
        elif x >= 50 and  x <= 65:
            membership_func_moderate_r = -0.0666 * x + 4.3333 
        # moderate_L --- done

        if x >= 50 and x <= 100:
            membership_func_far_r = 0.02 * x - 1
        elif x >= 100:
            membership_func_far_r = 1
        # far_L --- done

        return [membership_func_close_r, membership_func_moderate_r, membership_func_far_r]

    def rotate(self, x):
        membership_func_high_right = 0
        membership_func_low_right = 0
        membership_func_nothing = 0
        membership_func_low_left = 0
        membership_func_high_left = 0
         
        if x >= -50 and x <= -20:
             membership_func_high_right = 0.0333 * x + 1.6666
        elif x >= -20 and x < -5:
             membership_func_high_right = -0.0666 * x - 0.3333
        # high_right --- done
        
        if x >= -20 and x <= -10:
            membership_func_low_right = 0.1 * x + 2
        elif x >= -10 and x <= 0:
            membership_func_low_right = -0.1 * x + 0
        # low_right --- done

        if x >= -10 and x <= 0:
            membership_func_nothing = 0.1 * x + 1
        elif x >= 0 and x <= 10:
            membership_func_nothing = -0.1 * x + 1
        # nothing --- done 

        if x >= 0 and x <= 10:
            membership_func_low_left = 0.1 * x + 0
        elif x >= 10 and x <= 20:
            membership_func_low_left = -0.1 * x + 2
        # low_left --- done

        if x >= 5 and x <= 20:
            membership_func_high_left = 0.0666 * x - 0.3333
        elif x >= 20 and x <= 50:
            membership_func_high_left = -0.0333 * x + 1.6666
        # high_left --- done

        return[membership_func_high_right, membership_func_low_right, membership_func_nothing,
                membership_func_low_left, membership_func_high_left]   

    def inference(self, left_dist, right_dist):
        low_right = min(left_dist[0], right_dist[1])      
        high_right = min(left_dist[0], right_dist[2])
        low_left = min(left_dist[1], right_dist[0])
        high_left = min(left_dist[2], right_dist[0])
        nothing = min(left_dist[1], right_dist[1])

        rotation = [high_right, low_right, nothing, low_left, high_left]

        return rotation
    

    def defuzzify(self, rotation):
        soorat = 0.0
        makhraj = 0.0
        X=np.linspace(-50, 50, 1000)
        delta = X[1] - X[0]
        for i in X:
            temp = self.rotate(i)
            m = max(min(temp[0], rotation[0]), min(temp[1], rotation[1]), min(temp[2], rotation[2]),
                     min(temp[3], rotation[3]), min(temp[4], rotation[4]))
            soorat = soorat + m * i * delta
            makhraj = makhraj + m * delta
        center = 0.0
        if not makhraj == 0:
            center = 1.0 * float(soorat) / float(makhraj)

        return center        






    def __init__(self):
        pass


    def decide(self, left_dist, right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """
        # fuzzify

        d_l = self.d_L(left_dist)
        d_r = self.d_R(right_dist)

        # inference

        rot = self.inference(d_l,d_r)

        # defuzzify

        result = self.defuzzify(rot)

        return result
    