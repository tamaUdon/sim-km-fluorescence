from fluoro_uv_linear_eq import fluoro_uv
from fluoro_vl_linear_eq import fluoro_vl
import matplotlib.pyplot as plt


# ======== constatnts ======== #
STEP = 50
MIN = 300
MAX = 800 + 1

s = t = 0.5  # warining - 測定値ではない
u = r = 0.5

coumarine_fwl = [
    # クマリン蛍光の透過・反射 (励起|吸収スペクトル)
    0.1,  # 300nm
    0.8,  # 350nm
    0.5,  # 400nm
    0.2,  # 450nm
    0.1,  # 500nm
    0.0,  # 550nm
    0.0,  # 600nm
    0.0,  # 650nm
    0.0,  # 700nm
    0.0,  # 750nm
    0.0,  # 800nm
]

chlorophyll_fwl = [
    # クロロフィルa蛍光の透過・反射
    0.0,  # 300nm
    0.1,  # 350nm
    0.3,  # 400nm
    0.2,  # 450nm
    0.0,  # 500nm
    0.0,  # 550nm
    0.1,  # 600nm
    0.2,  # 650nm
    0.0,  # 700nm
    0.0,  # 750nm
    0.0,  # 800nm
]

non_fwl = [
    # 蛍光なしの透過・反射
    0.0,  # 300nm
    0.0,  # 350nm
    0.0,  # 400nm
    0.0,  # 450nm
    0.0,  # 500nm
    0.0,  # 550nm
    0.0,  # 600nm
    0.0,  # 650nm
    0.0,  # 700nm
    0.0,  # 750nm
    0.0,  # 800nm
]

d65_step50 = [
    # 昼光(D65)の波長ごとの強度
    0.0,  # 300nm
    0.4,  # 350nm
    0.8,  # 400nm
    1.0,  # 450nm
    0.9,  # 500nm
    0.88,  # 550nm
    0.78,  # 600nm
    0.7,  # 650nm
    0.6,  # 700nm
    0.58,  # 750nm
    0.5,  # 800nm
]

led_step50 = [
    # 青色LED+黄色蛍光体の波長ごとの強度
    0.0,  # 300nm
    0.0,  # 350nm
    0.0,  # 400nm
    1.0,  # 450nm
    0.1,  # 500nm
    0.65,  # 550nm
    0.6,  # 600nm
    0.3,  # 650nm
    0.1,  # 700nm
    0.02,  # 750nm
    0.0,  # 800nm
]
# ======== ==== ======== #

t_stars = r_stars = k_stars = [
    coumarine_fwl,
    chlorophyll_fwl,
    non_fwl,
]
I_0 = [d65_step50, led_step50]


def calculate_RT(
    t, r, t_star_l: list, k_star_l: list, i_0
) -> tuple[list, list, list, list]:
    Tuv, Ruv = [], []
    Tvl, Rvl = [], []
    I_2uv, J_3uv = [], []

    for i, wl in enumerate(range(MIN, MAX, STEP)):
        Tuv_, Ruv_, I_2uv_, J_3uv_ = fluoro_uv(t, r, t_star_l[i], i_0[i])
        Tuv.append(Tuv_)
        Ruv.append(Ruv_)
        I_2uv.append(I_2uv_)
        J_3uv.append(J_3uv_)

    I_2uv.reverse()  # 吸収波長を反転し, 蛍光波長とする
    J_3uv.reverse()

    for i, wl in enumerate(range(MIN, MAX, STEP)):
        Tvl_, Rvl_ = fluoro_vl(t, r, k_star_l[i], I_2uv[i], J_3uv[i], i_0[i])
        Tvl.append(Tvl_)
        Rvl.append(Rvl_)
    return Tuv, Ruv, Tvl, Rvl


def plot_graphs(Tuv, Ruv, Tvl, Rvl) -> None:
    # プロット
    wavelength = [wl for wl in range(MIN, MAX, STEP)]
    fig, ax = plt.subplots(1, 2, figsize=(8, 4))
    ax[0].plot(wavelength, Ruv, label="R(uv)", color="forestgreen")
    ax[0].plot(wavelength, Tuv, label="T(uv)")
    ax[1].plot(wavelength, Rvl, label="R(visible light)", color="orange")
    ax[1].plot(wavelength, Tvl, label="T(visible light)", color="plum")

    # 凡例表示
    ax[0].legend()
    ax[0].legend()
    ax[0].set_title("UV")  # Cl, Cm # D65, LED
    ax[0].set_xlabel("wavelength(nm)")
    ax[0].set_ylabel("a.u.")

    ax[1].legend()
    ax[1].legend()
    ax[1].set_title("VisibleLight")  # Cl, Cm # D65, LED
    ax[1].set_xlabel("wavelength(nm)")
    ax[1].set_ylabel("a.u.")

    print(f"Tuv={Tuv}")
    print(f"Ruv={Ruv}")
    print(f"Tvl={Tvl}")
    print(f"Rvl={Rvl}")

    plt.show()


def main():
    for i_0 in I_0:
        for k_star_l, t_star_l in zip(k_stars, t_stars):
            Tuv, Ruv, Tvl, Rvl = calculate_RT(t, r, t_star_l, k_star_l, i_0)
            plot_graphs(Tuv, Ruv, Tvl, Rvl)


if __name__ == "__main__":
    main()
