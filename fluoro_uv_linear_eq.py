import sympy

# 蛍光色素が吸収する波長つきで連立方程式を解く

I_1 = sympy.Symbol("I_1")
I_2 = sympy.Symbol("I_2")
I_3 = sympy.Symbol("I_3")
I_4 = sympy.Symbol("I_4")
I_5 = sympy.Symbol("I_5")

J_1 = sympy.Symbol("J_1")
J_2 = sympy.Symbol("J_2")
J_3 = sympy.Symbol("J_3")
J_4 = sympy.Symbol("J_4")
J_5 = sympy.Symbol("J_5")


def fluoro_uv(t, r, t_star, I_0) -> tuple[float, float, float, float]:
    """
    - t_star = r_starとする
    - I_0 = Insident light, 入射光の波長ごとの強さ, 規定値は1
    - 背面からの入射光は0とする
    """

    if I_0 == 0.0:  # 入射光が0
        return 0.0, 0.0, 0.0, 0.0

    # Iの式 (蛍光吸収)
    equation1 = I_1 - 1
    equation2 = (-t * I_1) + (I_2) + (-r * J_2)
    equation3 = ((t_star - t) * I_2) + (I_3) + (-r * J_3)
    equation4 = (-t * I_3) + (I_4) + (-r * J_4)
    equation5 = (-t * I_4) + (I_5) + (-r * J_5)

    # Jの式 (蛍光発光)
    equation6 = (-r * I_1) + (J_1) + (-t * J_2)
    equation7 = (-r * I_2) + (J_2) + ((t_star - t) * J_3)
    equation8 = (-r * I_3) + (J_3) + (-t * J_4)
    equation9 = (-r * I_4) + (J_4) + (-t * J_5)
    equation10 = J_5 - 0

    solved = sympy.solve(
        [
            equation1,
            equation2,
            equation3,
            equation4,
            equation5,
            equation6,
            equation7,
            equation8,
            equation9,
            equation10,
        ]
    )

    Ta, Ra = None, None
    Tb, Rb = None, None

    if float(solved[J_5]) > 0.0:  # 背面から光を当てる場合
        Tb = solved[J_1] / solved[J_5] * I_0
        Rb = solved[I_5] / solved[J_5] * I_0

    Ta = (solved[I_5] / solved[I_1]) * I_0
    Ra = (solved[J_1] / solved[I_1]) * I_0
    I_2uv = solved[I_2] * I_0
    J_3uv = solved[J_3] * I_0

    return Ta, Ra, I_2uv, J_3uv  # Tb, Rb
