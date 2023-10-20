from fuzzylogic.classes import Domain, Set, Rule
from fuzzylogic.functions import R, S, alpha
from fuzzylogic.functions import (
    trapezoid, triangular_sigmoid, rectangular, triangular)
from math import pi
import itertools
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(5, 5))

# Input Domain
# Proximity Domain
proximity = Domain('Proximity', -50, 1_600)
proximity.vn = S(0, 150)
proximity.n = trapezoid(0, 100, 300, 400)
proximity.sn = trapezoid(300, 400, 600, 700)
proximity.sf = trapezoid(600, 700, 900, 1000)
proximity.f = trapezoid(900, 1000, 1200, 1300)
proximity.vf = R(1200, 1300)

# proximity.vn.plot()
# proximity.n.plot()
# proximity.sn.plot()
# proximity.vf.plot()
# proximity.f.plot()
# proximity.sf.plot()

# Height Domain
height = Domain('Height', -550, 550)
height.vu = S(-530, -315)
height.su = triangular(-530, -120, c=-315)
height.u = trapezoid(-315, -210, -90, 0)
height.exact = triangular(-90, 80, c=0)
height.low = triangular(0, 160, c=80)
height.low_mid = triangular(80, 290, c=160)
height.mid = triangular(160, 375, c=290)
height.high_mid = triangular(255, 500, c=380)
height.high = R(380, 480)

# height.vu.plot()
# height.su.plot()
# height.u.plot()
# height.exact.plot()
# height.low.plot()
# height.low_mid.plot()
# height.mid.plot()
# height.high_mid.plot()
# height.high.plot()

# Output Domain
# Trajectory Domain
ONE = 23 * (pi / 180)
TWO = 45 * (pi / 180)
THREE = 68 * (pi / 180)
FOUR = 90 * (pi / 180)

trajectory = Domain('Trajectory', 0, 5)
trajectory.none = S(0, 1)
trajectory.low = triangular(0, 2, c=1)
trajectory.low_mid = triangular(1, 3, c=2)
trajectory.mid = triangular(2, 4, c=3)
trajectory.high_mid = triangular(3, 5, c=4)
trajectory.high = R(4, 5)

# trajectory.none.plot()
# trajectory.low.plot()
# trajectory.low_mid.plot()
# trajectory.mid.plot()
# trajectory.high_mid.plot()
# trajectory.high.plot()

# Magnitude Domain
magnitude = Domain('Magnitude', 0, 4)
magnitude.none = S(0, 1)
magnitude.weak = triangular(0, 2, c=1)
magnitude.ample = triangular(1, 3, c=2)
magnitude.strong = triangular(2, 4, c=3)
magnitude.powerful = R(3, 4)

# magnitude.none.plot()
# magnitude.weak.plot()
# magnitude.ample.plot()
# magnitude.strong.plot()
# magnitude.powerful.plot()

# Rule base
# Trajectory rules
t_ruleA1 = Rule({( proximity.vn, height.vu): trajectory.none })
t_ruleA2 = Rule({( proximity.vn, height.su): trajectory.none })
t_ruleA3 = Rule({( proximity.vn, height.u): trajectory.none })
t_ruleA4 = Rule({( proximity.vn, height.exact): trajectory.none})
t_ruleA5 = Rule({( proximity.vn, height.low): trajectory.high })
t_ruleA6 = Rule({( proximity.vn, height.low_mid): trajectory.high })
t_ruleA7 = Rule({( proximity.vn, height.mid): trajectory.high })
t_ruleA8 = Rule({( proximity.vn, height.high_mid): trajectory.high })
t_ruleA9 = Rule({( proximity.vn, height.high): trajectory.high })

t_ruleB1 = Rule({( proximity.n, height.vu): trajectory.high })
t_ruleB2 = Rule({( proximity.n, height.su): trajectory.high })
t_ruleB3 = Rule({( proximity.n, height.u): trajectory.none })
t_ruleB4 = Rule({( proximity.n, height.exact): trajectory.low_mid})
t_ruleB5 = Rule({( proximity.n, height.low): trajectory.high })
t_ruleB6 = Rule({( proximity.n, height.low_mid): trajectory.high })
t_ruleB7 = Rule({( proximity.n, height.mid): trajectory.high })
t_ruleB8 = Rule({( proximity.n, height.high_mid): trajectory.high })
t_ruleB9 = Rule({( proximity.n, height.high): trajectory.high  })

t_ruleC1 = Rule({( proximity.sn, height.vu): trajectory.none })
t_ruleC2 = Rule({( proximity.sn, height.su): trajectory.none })
t_ruleC3 = Rule({( proximity.sn, height.u): trajectory.high })
t_ruleC4 = Rule({( proximity.sn, height.exact): trajectory.low_mid})
t_ruleC5 = Rule({( proximity.sn, height.low): trajectory.mid })
t_ruleC6 = Rule({( proximity.sn, height.low_mid): trajectory.high_mid })
t_ruleC7 = Rule({( proximity.sn, height.mid): trajectory.high_mid })
t_ruleC8 = Rule({( proximity.sn, height.high_mid): trajectory.high_mid })
t_ruleC9 = Rule({( proximity.sn, height.high): trajectory.high })

t_ruleD1 = Rule({( proximity.sf, height.vu): trajectory.high })
t_ruleD2 = Rule({( proximity.sf, height.su): trajectory.high_mid })
t_ruleD3 = Rule({( proximity.sf, height.u): trajectory.low })
t_ruleD4 = Rule({( proximity.sf, height.exact): trajectory.mid })
t_ruleD5 = Rule({( proximity.sf, height.low): trajectory.high })
t_ruleD6 = Rule({( proximity.sf, height.low_mid): trajectory.high_mid })
t_ruleD7 = Rule({( proximity.sf, height.mid): trajectory.high })
t_ruleD8 = Rule({( proximity.sf, height.high_mid): trajectory.high_mid })
t_ruleD9 = Rule({( proximity.sf, height.high): trajectory.high })

t_ruleE1 = Rule({( proximity.f, height.vu): trajectory.low_mid })
t_ruleE2 = Rule({( proximity.f, height.su): trajectory.low_mid })
t_ruleE3 = Rule({( proximity.f, height.u): trajectory.none })
t_ruleE4 = Rule({( proximity.f, height.exact): trajectory.low })
t_ruleE5 = Rule({( proximity.f, height.low): trajectory.high_mid })
t_ruleE6 = Rule({( proximity.f, height.low_mid): trajectory.high_mid })
t_ruleE7 = Rule({( proximity.f, height.mid): trajectory.mid })
t_ruleE8 = Rule({( proximity.f, height.high_mid): trajectory.high_mid })
t_ruleE9 = Rule({( proximity.f, height.high): trajectory.high })

t_ruleF1 = Rule({( proximity.vf, height.vu): trajectory.none })
t_ruleF2 = Rule({( proximity.vf, height.su): trajectory.low_mid })
t_ruleF3 = Rule({( proximity.vf, height.u): trajectory.mid })
t_ruleF4 = Rule({( proximity.vf, height.exact): trajectory.low_mid })
t_ruleF5 = Rule({( proximity.vf, height.low): trajectory.low_mid })
t_ruleF6 = Rule({( proximity.vf, height.low_mid): trajectory.high_mid })
t_ruleF7 = Rule({( proximity.vf, height.mid): trajectory.high })
t_ruleF8 = Rule({( proximity.vf, height.high_mid): trajectory.high_mid })
t_ruleF9 = Rule({( proximity.vf, height.high): trajectory.high_mid  })

TRAJECTORY_RULES = t_ruleA1 | t_ruleA2 | t_ruleA3 | t_ruleA4 | t_ruleA5 | t_ruleA6 | t_ruleA7 | t_ruleA8 | t_ruleA9 | \
t_ruleB1 | t_ruleB2 | t_ruleB3 | t_ruleB4 | t_ruleB5 | t_ruleB6 | t_ruleB7 | t_ruleB8 | t_ruleB9 | \
t_ruleC1 | t_ruleC2 | t_ruleC3 | t_ruleC4 | t_ruleC5 | t_ruleC6 | t_ruleC7 | t_ruleC8 | t_ruleC9 | \
t_ruleD1 | t_ruleD2 | t_ruleD3 | t_ruleD4 | t_ruleD5 | t_ruleD6 | t_ruleD7 | t_ruleD8 | t_ruleD9 | \
t_ruleE1 | t_ruleE2 | t_ruleE3 | t_ruleE4 | t_ruleE5 | t_ruleE6 | t_ruleE7 | t_ruleE8 | t_ruleE9 | \
t_ruleF1 | t_ruleF2 | t_ruleF3 | t_ruleF4 | t_ruleF5 | t_ruleF6 | t_ruleF7 | t_ruleF8 | t_ruleF9

T_RULES = []

T_RULES.append( t_ruleA1 ) 
T_RULES.append( t_ruleA2 )
T_RULES.append( t_ruleA3 )
T_RULES.append( t_ruleA4 )
T_RULES.append( t_ruleA5 )
T_RULES.append( t_ruleA6 )
T_RULES.append( t_ruleA7 )
T_RULES.append( t_ruleA8 )
T_RULES.append( t_ruleA9 )
T_RULES.append( t_ruleB1 ) 
T_RULES.append( t_ruleB2 )
T_RULES.append( t_ruleB3 )
T_RULES.append( t_ruleB4 )
T_RULES.append( t_ruleB5 )
T_RULES.append( t_ruleB6 )
T_RULES.append( t_ruleB7 )
T_RULES.append( t_ruleB8 )
T_RULES.append( t_ruleB9 )
T_RULES.append( t_ruleC1 ) 
T_RULES.append( t_ruleC2 )
T_RULES.append( t_ruleC3 )
T_RULES.append( t_ruleC4 )
T_RULES.append( t_ruleC5 )
T_RULES.append( t_ruleC6 )
T_RULES.append( t_ruleC7 )
T_RULES.append( t_ruleC8 )
T_RULES.append( t_ruleC9 )
T_RULES.append( t_ruleD1 ) 
T_RULES.append( t_ruleD2 )
T_RULES.append( t_ruleD3 )
T_RULES.append( t_ruleD4 )
T_RULES.append( t_ruleD5 )
T_RULES.append( t_ruleD6 )
T_RULES.append( t_ruleD7 )
T_RULES.append( t_ruleD8 )
T_RULES.append( t_ruleD9 )
T_RULES.append( t_ruleE1 ) 
T_RULES.append( t_ruleE2 )
T_RULES.append( t_ruleE3 )
T_RULES.append( t_ruleE4 )
T_RULES.append( t_ruleE5 )
T_RULES.append( t_ruleE6 )
T_RULES.append( t_ruleE7 )
T_RULES.append( t_ruleE8 )
T_RULES.append( t_ruleE9 )
T_RULES.append( t_ruleF1 ) 
T_RULES.append( t_ruleF2 )
T_RULES.append( t_ruleF3 )
T_RULES.append( t_ruleF4 )
T_RULES.append( t_ruleF5 )
T_RULES.append( t_ruleF6 )
T_RULES.append( t_ruleF7 )
T_RULES.append( t_ruleF8 )
T_RULES.append( t_ruleF9 )

# Magnitude rules
m_ruleA1 = Rule({( proximity.vn, height.vu): magnitude.none })
m_ruleA2 = Rule({( proximity.vn, height.su): magnitude.none })
m_ruleA3 = Rule({( proximity.vn, height.u): magnitude.none })
m_ruleA4 = Rule({( proximity.vn, height.exact): magnitude.none})
m_ruleA5 = Rule({( proximity.vn, height.low): magnitude.weak })
m_ruleA6 = Rule({( proximity.vn, height.low_mid): magnitude.ample })
m_ruleA7 = Rule({( proximity.vn, height.mid): magnitude.ample })
m_ruleA8 = Rule({( proximity.vn, height.high_mid): magnitude.strong })
m_ruleA9 = Rule({( proximity.vn, height.high): magnitude.powerful })

m_ruleB1 = Rule({( proximity.n, height.vu): magnitude.weak })
m_ruleB2 = Rule({( proximity.n, height.su): magnitude.weak })
m_ruleB3 = Rule({( proximity.n, height.u): magnitude.weak })
m_ruleB4 = Rule({( proximity.n, height.exact): magnitude.weak})
m_ruleB5 = Rule({( proximity.n, height.low): magnitude.weak })
m_ruleB6 = Rule({( proximity.n, height.low_mid): magnitude.ample })
m_ruleB7 = Rule({( proximity.n, height.mid): magnitude.ample })
m_ruleB8 = Rule({( proximity.n, height.high_mid): magnitude.strong })
m_ruleB9 = Rule({( proximity.n, height.high): magnitude.strong })

m_ruleC1 = Rule({( proximity.sn, height.vu): magnitude.weak })
m_ruleC2 = Rule({( proximity.sn, height.su): magnitude.weak })
m_ruleC3 = Rule({( proximity.sn, height.u): magnitude.ample })
m_ruleC4 = Rule({( proximity.sn, height.exact): magnitude.ample })
m_ruleC5 = Rule({( proximity.sn, height.low): magnitude.ample })
m_ruleC6 = Rule({( proximity.sn, height.low_mid): magnitude.strong })
m_ruleC7 = Rule({( proximity.sn, height.mid): magnitude.strong })
m_ruleC8 = Rule({( proximity.sn, height.high_mid): magnitude.strong })
m_ruleC9 = Rule({( proximity.sn, height.high): magnitude.strong })

m_ruleD1 = Rule({( proximity.sf, height.vu): magnitude.strong })
m_ruleD2 = Rule({( proximity.sf, height.su): magnitude.ample })
m_ruleD3 = Rule({( proximity.sf, height.u): magnitude.ample })
m_ruleD4 = Rule({( proximity.sf, height.exact): magnitude.ample })
m_ruleD5 = Rule({( proximity.sf, height.low): magnitude.strong })
m_ruleD6 = Rule({( proximity.sf, height.low_mid): magnitude.strong })
m_ruleD7 = Rule({( proximity.sf, height.mid): magnitude.powerful })
m_ruleD8 = Rule({( proximity.sf, height.high_mid): magnitude.strong })
m_ruleD9 = Rule({( proximity.sf, height.high): magnitude.strong })

m_ruleE1 = Rule({( proximity.f, height.vu): magnitude.ample })
m_ruleE2 = Rule({( proximity.f, height.su): magnitude.ample })
m_ruleE3 = Rule({( proximity.f, height.u): magnitude.powerful })
m_ruleE4 = Rule({( proximity.f, height.exact): magnitude.strong })
m_ruleE5 = Rule({( proximity.f, height.low): magnitude.strong })
m_ruleE6 = Rule({( proximity.f, height.low_mid): magnitude.strong })
m_ruleE7 = Rule({( proximity.f, height.mid): magnitude.strong })
m_ruleE8 = Rule({( proximity.f, height.high_mid): magnitude.powerful })
m_ruleE9 = Rule({( proximity.f, height.high): magnitude.powerful })

m_ruleF1 = Rule({( proximity.vf, height.vu): magnitude.strong })
m_ruleF2 = Rule({( proximity.vf, height.su): magnitude.strong })
m_ruleF3 = Rule({( proximity.vf, height.u): magnitude.strong })
m_ruleF4 = Rule({( proximity.vf, height.exact): magnitude.strong })
m_ruleF5 = Rule({( proximity.vf, height.low): magnitude.strong })
m_ruleF6 = Rule({( proximity.vf, height.low_mid): magnitude.powerful })
m_ruleF7 = Rule({( proximity.vf, height.mid): magnitude.powerful })
m_ruleF8 = Rule({( proximity.vf, height.high_mid): magnitude.powerful })
m_ruleF9 = Rule({( proximity.vf, height.high): magnitude.powerful })

MAGNITUDE_RULES = m_ruleA1 | m_ruleA2 | m_ruleA3 | m_ruleA4 | m_ruleA5 | m_ruleA6 | m_ruleA7 | m_ruleA8 | m_ruleA9 | \
m_ruleB1 | m_ruleB2 | m_ruleB3 | m_ruleB4 | m_ruleB5 | m_ruleB6 | m_ruleB7 | m_ruleB8 | m_ruleB9 | \
m_ruleC1 | m_ruleC2 | m_ruleC3 | m_ruleC4 | m_ruleC5 | m_ruleC6 | m_ruleC7 | m_ruleC8 | m_ruleC9 | \
m_ruleD1 | m_ruleD2 | m_ruleD3 | m_ruleD4 | m_ruleD5 | m_ruleD6 | m_ruleD7 | m_ruleD8 | m_ruleD9 | \
m_ruleE1 | m_ruleE2 | m_ruleE3 | m_ruleE4 | m_ruleE5 | m_ruleE6 | m_ruleE7 | m_ruleE8 | m_ruleE9 | \
m_ruleF1 | m_ruleF2 | m_ruleF3 | m_ruleF4 | m_ruleF5 | m_ruleF6 | m_ruleF7 | m_ruleF8 | m_ruleF9

M_RULES = []

M_RULES.append( m_ruleA1 ) 
M_RULES.append( m_ruleA2 )
M_RULES.append( m_ruleA3 )
M_RULES.append( m_ruleA4 )
M_RULES.append( m_ruleA5 )
M_RULES.append( m_ruleA6 )
M_RULES.append( m_ruleA7 )
M_RULES.append( m_ruleA8 )
M_RULES.append( m_ruleA9 )
M_RULES.append( m_ruleB1 ) 
M_RULES.append( m_ruleB2 )
M_RULES.append( m_ruleB3 )
M_RULES.append( m_ruleB4 )
M_RULES.append( m_ruleB5 )
M_RULES.append( m_ruleB6 )
M_RULES.append( m_ruleB7 )
M_RULES.append( m_ruleB8 )
M_RULES.append( m_ruleB9 )
M_RULES.append( m_ruleC1 ) 
M_RULES.append( m_ruleC2 )
M_RULES.append( m_ruleC3 )
M_RULES.append( m_ruleC4 )
M_RULES.append( m_ruleC5 )
M_RULES.append( m_ruleC6 )
M_RULES.append( m_ruleC7 )
M_RULES.append( m_ruleC8 )
M_RULES.append( m_ruleC9 )
M_RULES.append( m_ruleD1 ) 
M_RULES.append( m_ruleD2 )
M_RULES.append( m_ruleD3 )
M_RULES.append( m_ruleD4 )
M_RULES.append( m_ruleD5 )
M_RULES.append( m_ruleD6 )
M_RULES.append( m_ruleD7 )
M_RULES.append( m_ruleD8 )
M_RULES.append( m_ruleD9 )
M_RULES.append( m_ruleE1 ) 
M_RULES.append( m_ruleE2 )
M_RULES.append( m_ruleE3 )
M_RULES.append( m_ruleE4 )
M_RULES.append( m_ruleE5 )
M_RULES.append( m_ruleE6 )
M_RULES.append( m_ruleE7 )
M_RULES.append( m_ruleE8 )
M_RULES.append( m_ruleE9 )
M_RULES.append( m_ruleF1 ) 
M_RULES.append( m_ruleF2 )
M_RULES.append( m_ruleF3 )
M_RULES.append( m_ruleF4 )
M_RULES.append( m_ruleF5 )
M_RULES.append( m_ruleF6 )
M_RULES.append( m_ruleF7 )
M_RULES.append( m_ruleF8 )
M_RULES.append( m_ruleF9 )

def getCOG(x, y):
    coords = {proximity: x, height: y}

    t_cog = TRAJECTORY_RULES(coords)
    m_cog = MAGNITUDE_RULES(coords)

    # for i in range(len(T_RULES)):
    #     print(f'Rule {chr(ord("a") + int(i / 9))}{i % 9 + 1}: {T_RULES[i](coords)}')

    # print('***')

    # for i in range(len(M_RULES)):
    #     print(f'Rule {chr(ord("a") + int(i / 9))}{i % 9 + 1}: {M_RULES[i](coords)}')

    # for s, v in proximity(x).items():
    #     if v == 0: continue

    #     print(str(s) + ' ' + str(v))

    # print('***')

    # for s, v in height(y).items():
    #     if v == 0: continue
        
    #     print(str(s) + ' ' + str(v))

    # print('***')

    # print(f'Trajectory COG: {t_cog}')
    # print(f'Magnitude COG: {m_cog}')

    # for s, v in trajectory(t_cog).items():
    #     if v == 0: continue

    #     print(str(s) + ' ' + str(v))
    
    # print('***')

    # for s, v in magnitude(m_cog).items():
    #     if v == 0: continue

    #     print(str(s) + ' ' + str(v))

    # print('***')

    # print(t_cog / 5)
    # print(m_cog / 4)
    return [pi / 2 * (t_cog / 5), 2 * m_cog / 4]