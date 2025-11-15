import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).parent

def load_vgid(filename: str):
    """
    vgid_*.log から (Vg, |Id|) を返す。
    1列目: Vg, 最終列: Id という前提。
    """
    path = BASE_DIR / filename
    data = np.loadtxt(path)

    vg = data[:, 0]          # 1列目 = Vg
    id_raw = data[:, -1]     # 最後の列 = Id
    id_abs = np.abs(id_raw)

    print(
        f"{filename}: shape={data.shape}, "
        f"Vg[min,max]=({vg.min():.3g},{vg.max():.3g}), "
        f"|Id|[min,max]=({id_abs.min():.3e},{id_abs.max():.3e})"
    )

    return vg, id_abs


def fit_vth(vg, id_abs, id_cut=1e-6):
    """
    √Id–Vg の直線部分を一次近似して Vth を求める。
    - id_cut 以上の Id をフィットに使う。
    戻り値:
      vth, (m, b, vg_fit, sqrt_id_fit)
    """
    mask = id_abs > id_cut
    if mask.sum() < 5:
        idx = np.argsort(id_abs)[-10:]
        vg_fit = vg[idx]
        sqrt_id_fit = np.sqrt(id_abs[idx])
    else:
        vg_fit = vg[mask]
        sqrt_id_fit = np.sqrt(id_abs[mask])

    m, b = np.polyfit(vg_fit, sqrt_id_fit, 1)
    vth = -b / m
    return vth, (m, b, vg_fit, sqrt_id_fit)


def main():
    # --- ログ読み込み ---
    vg_n, id_n = load_vgid("vgid_nmos.log")
    vg_p, id_p = load_vgid("vgid_pmos.log")

    # --- Vth フィット ---
    vth_n, (m_n, b_n, vgfit_n, sqfit_n) = fit_vth(vg_n, id_n)
    vth_p, (m_p, b_p, vgfit_p, sqfit_p) = fit_vth(vg_p, id_p)

    print(f"nMOS Vth ≒ {vth_n:.3f} V")
    print(f"pMOS Vth ≒ {vth_p:.3f} V")

    # --- プロット ---
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # ① Id–Vg（線形）
    ax = axes[0]
    ax.plot(vg_n, id_n * 1e6, ".", label="nMOS")
    ax.plot(vg_p, id_p * 1e6, ".", label="pMOS")
    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("Id [µA]")
    ax.set_title("Id–Vg (linear)")
    ax.grid(True)
    ax.legend()

    # ② Id–Vg（y軸ログ）
    ax = axes[1]
    ax.semilogy(vg_n, id_n, ".", label="nMOS")
    ax.semilogy(vg_p, id_p, ".", label="pMOS")
    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("Id [A]")
    ax.set_title("Id–Vg (log scale)")
    ax.grid(True, which="both")
    ax.legend()

    # ③ √Id–Vg ＋ フィット直線 ＋ Vth 線
    ax = axes[2]
    eps = 1e-20
    sqrt_id_n = np.sqrt(np.clip(id_n, eps, None))
    sqrt_id_p = np.sqrt(np.clip(id_p, eps, None))

    ax.plot(vg_n, sqrt_id_n, ".", label="nMOS data")
    ax.plot(vg_p, sqrt_id_p, ".", label="pMOS data")

    vg_line_n = np.linspace(vgfit_n.min(), vgfit_n.max(), 100)
    vg_line_p = np.linspace(vgfit_p.min(), vgfit_p.max(), 100)
    ax.plot(vg_line_n, m_n * vg_line_n + b_n, "C0--", label="nMOS fit")
    ax.plot(vg_line_p, m_p * vg_line_p + b_p, "C1--", label="pMOS fit")

    ax.axvline(vth_n, color="C0", linestyle=":", label=f"Vth_n={vth_n:.3f}V")
    ax.axvline(vth_p, color="C1", linestyle=":", label=f"Vth_p={vth_p:.3f}V")

    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("sqrt(Id) [A^0.5]")
    ax.set_title("sqrt(Id)–Vg & Vth")
    ax.grid(True)
    ax.legend()

    plt.tight_layout()

    # ここがポイント：必ず PNG を保存する
    out_path = BASE_DIR / "vgid_all.png"
    plt.savefig(out_path)
    print(f"Saved figure to: {out_path}")

    # ウィンドウはおまけ（出なくても PNG があればOK）
    # plt.show()


if __name__ == "__main__":
    main()
