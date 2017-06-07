from sympy import symbols, Matrix, pi
from sympy.physics.mechanics import *
import numpy as np

# Modeling the system with Kane method

# Signals
x, th  = dynamicsymbols('x th')
v, w = dynamicsymbols('v w')
F = dynamicsymbols('F')
d = symbols('d')

# Constants
m, r = symbols('m r')
M = symbols('M')
g, t = symbols('g t')
Ic = symbols('Ic')

# Frames and Coord. system

# Car
Nf = ReferenceFrame('Nf')
C = Point('C')                         
C.set_vel(Nf, v*Nf.x)
Car = Particle('Car',C,M)

# Pendulum
A = Nf.orientnew('A','Axis',[th,Nf.z])
A.set_ang_vel(Nf,w*Nf.z)

P = C.locatenew('P',r*A.x)
P.v2pt_theory(C,Nf,A)
Pa = Particle('Pa', P, m)

I = outer (Nf.z, Nf.z)
Inertia_tuple = (Ic*I, P)
Bp = RigidBody('Bp', P, A, m, Inertia_tuple)

# Forces and torques
forces = [(C,F*Nf.x-d*v*Nf.x),(P,-m*g*Nf.y)]
frames = [Nf,A]
points = [C,P]

kindiffs = [x.diff(t)-v, th.diff(t) - w]
particles = [Car,Bp]

# Model
KM = KanesMethod(Nf,q_ind=[x,th],u_ind=[v,w], kd_eqs=kindiffs)
fr,frstar = KM.kanes_equations(forces,particles)

# Equilibrium point
eq_pt = [0.0, pi/2,0.0,0.0]
eq_dict = dict(zip([x,th,v,w], eq_pt))

# symbolically linearize about arbitrary equilibrium
MM, linear_state_matrix, linear_input_matrix, inputs = KM.linearize(new_method=True)

# sub in the equilibrium point and the parameters
f_A_lin = linear_state_matrix.subs(eq_dict)
f_B_lin = linear_input_matrix.subs(eq_dict)
MM = MM.subs(eq_dict)

# compute A and B
Atmp = MM.inv() * f_A_lin
Btmp = MM.inv() * f_B_lin

# Real parameters
Mpar = 0.4874257
mpar = 0.19211
rpar = 0.323
dpar = 1.6800357
Th =  0.0294049
gpar = 9.81
Icpar = Th - mpar*rpar**2
kt = 0.0603/1000
rp = 0.0286524
N = 1

# Get numerical matrices
pars = [M , m, r, d, Ic, g]
par_vals = [Mpar, mpar, rpar, dpar, Icpar, gpar]

par_dict = dict(zip(pars, par_vals))

# Matrices with identified values
Atmp = Atmp.subs(par_dict)
Btmp = Btmp.subs(par_dict)

A = np.matrix(Atmp)
B = np.matrix(Btmp)

A = A.astype('float64')
B = kt/rp*B.astype('float64')

C=[[1, 0, 0, 0], [0, 1, 0, 0]]    
D=[[0], [0]]

from supsictrl.ctrl_repl import *
from supsictrl.ctrl_utils import *
import numpy as np
import scipy as sp
from matplotlib.pyplot import *
from control import *
from control.matlab import *
from control.mateqn import *

# Continous system
sys = ss(A,B,C,D)

# discrete-time model
ts = 0.01
sysd = c2d(sys,ts,'zoh')

# LQR Controller design
##############################################################################
Q = np.diag([300,10,400,20]);
Q = np.diag([400,300,20,10]);
R = [4e-6];                    
[k_lqr, S, E] = dlqr(sysd.A,sysd.B,Q,R)

# Observer design parameters
##############################################################################
# Control design - Reduced order observer
(preg,pvect) = sp.linalg.eig(A-B*k_lqr)
rho=max(abs(preg));       # process spectral radius
rhoamp=10;                # amplification of observer poles

angle1 = 15*1j*np.pi/16
poles_c = rhoamp*rho*sp.exp([angle1, -angle1])
obs_poles = sp.exp(poles_c*ts)

T=[[0,0,1,0],[0,0,0,1]]
obs=red_obs(sysd,T,obs_poles)

# Put Observer and controller together (compact form)
ctr = comp_form(sysd,obs,k_lqr)

g = tf(kt/Mpar/rp,[1, dpar/Mpar,0])

###### Swing up

# Motor model
# Motor response for least square identification
from scipy.optimize import leastsq

def residuals(p, y, t):  
    [k,alpha] = p
    g = tf(k,[1,alpha,0])
    Y,T = step(g,t)
    err=y-Y
    return err

# Motore 1

kt = 60.3e-6
rp = 0.75/26.17585
N = 1

x = np.loadtxt('MOT');
t = x[200:264,0] 
y = x[200:264,1] 
t = t - t[0] 
y = y - y[0]
t = np.arange(0,ts*(len(t)),ts)

U0=1500  
p0=[1.,4.]
y1 = y/U0 
plsq = leastsq(residuals, p0, args=(y1, t))

M = kt/plsq[0][0]           # Motor Inertia
d = plsq[0][1]*M                 # Motor friction

g = tf([kt/M],[1,d/M,0])  # Transfer function

Y,T = step(g,t)
plot(T,Y)
plot(t,y1)
#show()

# Plant
A = [[0,1],[0,-d/M]]
B = [[0],[kt/M]]
C = [1,0]
D = [0];

Mot = ss(A,B,C,D)
Motd = c2d(Mot, ts, 'zoh')

# Control Design

wn=12
xi=np.sqrt(2)/2

cl_p1=[1,2*xi*wn,wn**2]
cl_p2=[1,wn]
cl_poly=sp.polymul(cl_p1,cl_p2)
cl_poles=sp.roots(cl_poly);  # Desired continous poles
cl_polesd=sp.exp(cl_poles*ts)  # Desired discrete poles

sz1=sp.shape(Motd.A);
sz2=sp.shape(Motd.B);

# Add discrete integrator for steady state zero error
Phi_f=np.vstack((Motd.A,-Motd.C*ts))
Phi_f=np.hstack((Phi_f,[[0],[0],[1]]))
G_f=np.vstack((Motd.B,zeros((1,1))))

kmot=place(Phi_f,G_f,cl_polesd)

#Reduced order observer
p_oc=-10*max(abs(cl_poles))
p_od=sp.exp(p_oc*ts);

T=[0,1]
r_obs=red_obs(Motd,T,[p_od])

contr_I=comp_form_i(Motd,r_obs,kmot)

Amp = 0.28
Tosc = 18.0/21


