import math

def calculate_p(q):
    return 1 -q

def calculate_t(p, time):
    return -time / math.log(p)

def calculate_q(p):
    return 1 - p

def calculate_Qreserved( k, isLoaded, P_system, Q_system):
    if (isLoaded):
        return pow((1 - P_system), k + 1)

    return Q_system / math.factorial(k + 1)

def calculate_G (par1, par2):
    return par1 / par2

if __name__ == '__main__':
    P_system = 0.259204410758
    time = 2616
    Q_system = calculate_q(P_system)

    # k = 2
    # is_loaded = True

    k = 3
    is_loaded = False

    print("k = ", k)
    print("P = ", P_system)
    print("Q = ", calculate_q(P_system))
    print("Tsys = ", calculate_t(P_system, time))
    print("Qres = ", calculate_Qreserved(k, is_loaded, P_system, Q_system))
    print("Pres = ", calculate_p(calculate_Qreserved(k, is_loaded, P_system, Q_system)))
    print("Tres = ", calculate_t(calculate_p(calculate_Qreserved(k, is_loaded, P_system, Q_system)), time))
    print("Gq = ", calculate_G(calculate_Qreserved(k, is_loaded, P_system, Q_system), Q_system))
    print("Gp = ", calculate_G(calculate_p(calculate_Qreserved(k, is_loaded, P_system, Q_system)), P_system))
    print("Gt = ", calculate_G(calculate_t(calculate_p(calculate_Qreserved(k, is_loaded, P_system, Q_system)), time), time))

