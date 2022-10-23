import tensorflow as tf
from src.loss.utils import KLDiv


class RegularizationLoss(tf.keras.losses.Loss):
    def __init__(self,
                 lambda_p: float, 
                 max_steps: int = 1000,
                 **kwargs
                 ):
        '''
        Parameters
        ----------
        lambda_p : float
            The success probability of geometric distribution. 
        max_steps : int, optional
            Highest N. 
            The default is 1000.
        '''
        super().__init__(**kwargs)
        not_halted = 1.0
        p_g_list = []
        for k in range(max_steps):
            p_g_list.append(not_halted * lambda_p)
            not_halted = not_halted * (1-lambda_p)
        p_g = tf.stack(p_g_list)
        self.p_g = tf.cast(tf.Variable(p_g,trainable=False,name='p_g'),dtype=tf.float64)
        self.kl_div = KLDiv()

    def __call__(self,p: tf.Tensor) -> tf.Tensor:
        p = tf.transpose(p,perm=[1,0])
        p_g = tf.broadcast_to(self.p_g[None,:tf.shape(p)[1]],shape = tf.shape(p))
        return self.kl_div(tf.math.log(p), p_g)