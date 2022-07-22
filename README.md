# Normal-Random-Variables-Comparison
This script takes two independent normal distributions as input (namely their mean and variance), computes the probability that a random variable distributed according to the first one will be larger than the second one and plots both densities for visualisation purposes.

The `NormalCDF(value, N)` function yields the value of the cumulative density function of the normal distribution for a given variable by using the following taylor series approximation:

$$\Phi (x)\approx {\frac {1}{2}}+{\frac {1}{\sqrt {2\pi }}}\sum _{k=0}^{N}{\frac {\left(-1\right)^{k}x^{\left(2k+1\right)}}{2^{k}k!\left(2k+1\right)}.}$$

Obviously, the more iterations of `N` the more accurate our result will be, but we need to be aware of the computational cost it implies, given that we are taking its factorial. I have found that setting `N=100` returns a very accurate approximation while remaining feasible.

To figure out the probability, we employ the fact that $P(X>Y)=P(X-Y>0)$, and define $Z=X-Y$ to be a new distribution. Therefore, we now need to find $P(Z>0)$, which is done by employing the CDF.
Note that $E(Z)=E(X)-E(Y)$, $Var(Z)=Var(X)+Var(Y)$ (because they are independent). Thus, $P(D>0)=1-\Phi\left(\frac{-E(Z)}{\sqrt{Var(Z)}}\right)$.

Let's provide an example. Assume that we have a pair of stocks X and Y, and that their yearly returns are normally distributed. I'm aware that this is not the most accurate PDF to model stock returns due to its tails, in fact, it is part of [summer research topic](https://github.com/lluissalvat/Research-Reading-List); but I shall use it regardless, for simplication purposes.
Furthermore, assume we have found that their expected returns are 10 and 11, and that their standard deviations are 3 and 5, respectively (in units of percentage). We want to find out what stock we should invest in, so we run the script and find that there is a 43.19% chance that Stock X will yield a higher return than Stock Y, so we will start a position in Y. Feel free to tweak the parameters and to use the script in a field other than finance, such as physics or demography.
