

def eux(a, b):
    if a % b == 0:
        m, n, gcd = 0, 1, b
        return m, n, gcd

    # m and n for the smaller pair (b, a % b)
    m_small, n_small, gcd = eux(b, a % b)

    # convert them into m and n for (a, b)
    m = n_small
    n = m_small - n_small * (a // b)
    return m, n, gcd