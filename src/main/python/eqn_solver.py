from scipy.optimize import fsolve
from numpy import sin, cos, tan, pi, sqrt

def solve(d1, d2, d3, d4, ver1, ver2, hor1, hor2):
    def eqn(p):
        x, y, z, u, v = p
        v1 = (d1*cos(u*pi/180)*sin(z*pi/180)-y)/(d1*cos(u*pi/180)*cos(z*pi/180)-x) - tan(hor1*pi/180)
        v2 = (d2*cos(u*pi/180)*sin(z*pi/180)-y)/(d2*cos(u*pi/180)*cos(z*pi/180)-x) - tan(hor2*pi/180)
        v3 = d4 - sqrt(((d2*cos(u*pi/180)*sin(z*pi/180)-y))**2+((d2*cos(u*pi/180)*cos(z*pi/180)-x))**2+(d2*sin(u*pi/180)-v)**2)
        v4 = (d1*sin(u*pi/180)-v)/d3 - sin(ver1 * pi / 180)
        v5 = (d2*sin(u*pi/180)-v)/d4 - sin(ver2 * pi / 180)
        return (v1, v2, v3, v4, v5)
    
    return fsolve(eqn, (0, 0, 0, 0, 0))
