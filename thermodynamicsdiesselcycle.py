import numpy as np
from matplotlib import pyplot as plt


def volume(d, s, l, r, theta):
    Vs = (np.pi / 4) * d**2 * s
    Vc = Vs / (r - 1)

    term1 = 1 / (r - 1)
    term2 = 1 + (2 / s) - np.cos(theta)
    term3 = np.sqrt((2 / s) ** 2 + (np.sin(theta)) ** 2)

    V = Vs * (term1 + 0.5 * (term2 - term3))

    return V


d = 0.1
s = 0.1
l = 0.15
r = 15

p1 = 101.3
t1 = 300
gamma = 1.4
t3 = 2500

Vs = (np.pi / 4) * d**2 * s
Vc = Vs / (r - 1)

V1 = Vs + Vc
V2 = Vc
V4 = V1
P2 = p1 * r**gamma
t2 = t1 * r ** (gamma - 1)
P3 = P2

V3 = V2 * t3 / t2

P4 = P3 * (V3 / V4) ** gamma

# pv**gamma = const p1v1**gamma = p2v2**gamma

P2 = p1 * (r) ** gamma
P3 = P2
t2 = t1 * r ** (gamma - 1)
# When P is constant V/T = constant, (V2/T2 = V3/T3)

V3 = V2 * t3 / t2

P4 = P3 * (V3 / V4) ** gamma

theta = 0

while theta < np.pi:
    theta += 0.001
    v_theata = volume(d, s, l, r, theta)
    if 0 < (v_theata - V3) < 0.001:
        break
    print(theta * 180 / np.pi)

v_comp = volume(d, s, l, r, np.linspace(0, np.pi, 180))
P_comp = (p1 * V1**gamma) / v_comp**gamma

V_exp = volume(d, s, l, r, np.linspace(np.pi, theta, 180))
P_exp = (P3 * V3**gamma) / V_exp**gamma

plt.figure(figsize=(7.5, 7.5))

plt.plot(v_comp, P_comp)
plt.plot([V2, V3], [P2, P3])
plt.plot(V_exp, P_exp)
plt.plot([V4, V1], [P4, p1])

plt.title("PV Diagram Dielse cycle", fontsize=13)
plt.xlabel("Volume", fontsize=13)
plt.ylabel("Pressure", fontsize=13)
plt.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))
plt.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

plt.show()
