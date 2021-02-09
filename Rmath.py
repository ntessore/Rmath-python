__all__ = []

from ctypes import cdll, c_double, c_uint, c_int
from glob import glob
from os import path
import sys

MATHLIB = cdll.LoadLibrary(glob(path.join(path.dirname(__file__), '_Rmath*.*'))[0])
MODULE = sys.modules[__name__]

def MATHIMPORT(restype, name, *argtypes):
    name, symbol = name if isinstance(name, tuple) else (name, name)
    func = getattr(MATHLIB, symbol)
    func.__name__ = name
    func.argtypes = argtypes
    func.restype = restype
    setattr(MODULE, name, func)
    __all__.append(name)

# Random Number Generators

MATHIMPORT(c_double, 'norm_rand')
MATHIMPORT(c_double, 'unif_rand')
MATHIMPORT(c_double, 'exp_rand')
MATHIMPORT(None, 'set_seed', c_uint, c_uint)
#MATHIMPORT(None, 'get_seed', c_uint*, c_uint*)

# Normal Distribution

MATHIMPORT(c_double, ('dnorm', 'dnorm4'), c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, ('pnorm', 'pnorm5'), c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, ('qnorm', 'qnorm5'), c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rnorm', c_double, c_double)
#MATHIMPORT(None, 'pnorm_both', c_double, c_double*, c_double*, c_int, c_int)

# Uniform Distribution

MATHIMPORT(c_double, 'dunif', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'punif', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qunif', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'runif', c_double, c_double)

# Gamma Distribution

MATHIMPORT(c_double, 'dgamma', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pgamma', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qgamma', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rgamma', c_double, c_double)

# Beta Distribution

MATHIMPORT(c_double, 'dbeta', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pbeta', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qbeta', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rbeta', c_double, c_double)

# Lognormal Distribution

MATHIMPORT(c_double, 'dlnorm', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'plnorm', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qlnorm', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rlnorm', c_double, c_double)

# Chi-squared Distribution

MATHIMPORT(c_double, 'dchisq', c_double, c_double, c_int)
MATHIMPORT(c_double, 'pchisq', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qchisq', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rchisq', c_double)

# Non-central Chi-squared Distribution

MATHIMPORT(c_double, 'dnchisq', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pnchisq', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qnchisq', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rnchisq', c_double, c_double)

# F Distibution

MATHIMPORT(c_double, 'df', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pf', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qf', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rf', c_double, c_double)

# Student t Distibution

MATHIMPORT(c_double, 'dt', c_double, c_double, c_int)
MATHIMPORT(c_double, 'pt', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qt', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rt', c_double)

# Binomial Distribution

MATHIMPORT(c_double, 'dbinom_raw', c_double, c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'dbinom', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pbinom', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qbinom', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rbinom', c_double, c_double)

# Multnomial Distribution

#MATHIMPORT(void, 'rmultinom', c_int, c_double*, c_int, c_int*)

# Cauchy Distribution

MATHIMPORT(c_double, 'dcauchy', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pcauchy', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qcauchy', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rcauchy', c_double, c_double)

# Exponential Distribution

MATHIMPORT(c_double, 'dexp', c_double, c_double, c_int)
MATHIMPORT(c_double, 'pexp', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qexp', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rexp', c_double)

# Geometric Distribution

MATHIMPORT(c_double, 'dgeom', c_double, c_double, c_int)
MATHIMPORT(c_double, 'pgeom', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qgeom', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rgeom', c_double)

# Hypergeometric Distibution

MATHIMPORT(c_double, 'dhyper', c_double, c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'phyper', c_double, c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qhyper', c_double, c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rhyper', c_double, c_double, c_double)

# Negative Binomial Distribution

MATHIMPORT(c_double, 'dnbinom', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pnbinom', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qnbinom', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rnbinom', c_double, c_double)

MATHIMPORT(c_double, 'dnbinom_mu', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pnbinom_mu', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qnbinom_mu', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rnbinom_mu', c_double, c_double)

# Poisson Distribution

MATHIMPORT(c_double, 'dpois_raw', c_double, c_double, c_int)
MATHIMPORT(c_double, 'dpois', c_double, c_double, c_int)
MATHIMPORT(c_double, 'ppois', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qpois', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rpois', c_double)

# Weibull Distribution

MATHIMPORT(c_double, 'dweibull', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pweibull', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qweibull', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rweibull', c_double, c_double)

# Logistic Distribution

MATHIMPORT(c_double, 'dlogis', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'plogis', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qlogis', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rlogis', c_double, c_double)

# Non-central Beta Distribution

MATHIMPORT(c_double, 'dnbeta', c_double, c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pnbeta', c_double, c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qnbeta', c_double, c_double, c_double, c_double, c_int, c_int)
#MATHIMPORT(c_double, 'rnbeta', c_double, c_double, c_double)

# Non-central F Distribution

MATHIMPORT(c_double, 'dnf', c_double, c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pnf', c_double, c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qnf', c_double, c_double, c_double, c_double, c_int, c_int)

# Non-central Student t Distribution

MATHIMPORT(c_double, 'dnt', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pnt', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qnt', c_double, c_double, c_double, c_int, c_int)

# Studentized Range Distribution

MATHIMPORT(c_double, 'ptukey', c_double, c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qtukey', c_double, c_double, c_double, c_double, c_int, c_int)

# Wilcoxon Rank Sum Distribution

MATHIMPORT(c_double, 'dwilcox', c_double, c_double, c_double, c_int)
MATHIMPORT(c_double, 'pwilcox', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qwilcox', c_double, c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rwilcox', c_double, c_double)

# Wilcoxon Signed Rank Distribution

MATHIMPORT(c_double, 'dsignrank', c_double, c_double, c_int)
MATHIMPORT(c_double, 'psignrank', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'qsignrank', c_double, c_double, c_int, c_int)
MATHIMPORT(c_double, 'rsignrank', c_double)

# Gamma and Related Functions
MATHIMPORT(c_double, 'gammafn', c_double)
MATHIMPORT(c_double, 'lgammafn', c_double)
#MATHIMPORT(c_double, 'lgammafn_sign', c_double, c_int*)
#MATHIMPORT(None, 'dpsifn', c_double, c_int, c_int, c_int, c_double*, c_int*, c_int*)
MATHIMPORT(c_double, 'psigamma', c_double, c_double)
MATHIMPORT(c_double, 'digamma', c_double)
MATHIMPORT(c_double, 'trigamma', c_double)
MATHIMPORT(c_double, 'tetragamma', c_double)
MATHIMPORT(c_double, 'pentagamma', c_double)

MATHIMPORT(c_double, 'beta', c_double, c_double)
MATHIMPORT(c_double, 'lbeta', c_double, c_double)

MATHIMPORT(c_double, 'choose', c_double, c_double)
MATHIMPORT(c_double, 'lchoose', c_double, c_double)

# Bessel Functions

MATHIMPORT(c_double, 'bessel_i', c_double, c_double, c_double)
MATHIMPORT(c_double, 'bessel_j', c_double, c_double)
MATHIMPORT(c_double, 'bessel_k', c_double, c_double, c_double)
MATHIMPORT(c_double, 'bessel_y', c_double, c_double)
#MATHIMPORT(c_double, 'bessel_i_ex', c_double, c_double, c_double, c_double*)
#MATHIMPORT(c_double, 'bessel_j_ex', c_double, c_double, c_double*)
#MATHIMPORT(c_double, 'bessel_k_ex', c_double, c_double, c_double, c_double*)
#MATHIMPORT(c_double, 'bessel_y_ex', c_double, c_double, c_double*)


# General Support Functions

MATHIMPORT(c_int, 'imax2', c_int, c_int)
MATHIMPORT(c_int, 'imin2', c_int, c_int)
MATHIMPORT(c_double, 'fmax2', c_double, c_double)
MATHIMPORT(c_double, 'fmin2', c_double, c_double)
MATHIMPORT(c_double, 'sign', c_double)
MATHIMPORT(c_double, 'fprec', c_double, c_double)
MATHIMPORT(c_double, 'fround', c_double, c_double)
MATHIMPORT(c_double, 'fsign', c_double, c_double)
MATHIMPORT(c_double, 'ftrunc', c_double)

# Accurate log(1+x) - x, {care for small x}
MATHIMPORT(c_double, 'log1pmx', c_double)
# accurate log(gamma(x+1)), small x (0 < x < 0.5)
MATHIMPORT(c_double, 'lgamma1p', c_double)

# Compute the log of a sum or difference from logs of terms, i.e.,
#
#     log (exp (logx) + exp (logy))
# or  log (exp (logx) - exp (logy))
#
# without causing overflows or throwing away too much accuracy:
#
MATHIMPORT(c_double, 'logspace_add', c_double, c_double)
MATHIMPORT(c_double, 'logspace_sub', c_double, c_double)
#MATHIMPORT(c_double, 'logspace_sum', const c_double*, c_int)
