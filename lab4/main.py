from multiprocessing import freeze_support
import covsirphy as cs
import matplotlib.pyplot as plt


def main():
    data = cs.ODEScenario.auto_build(geo="Argentina", model=cs.SIRFModel)

    parameters = ["theta", "kappa", "rho", "sigma", "tau"]
    for param in parameters:
        data.compare_param(param)

    data.simulate(name="Baseline")

    future_days = [7, 30, 300]
    future_data = {}
    for days in future_days:
        data.build_with_template(name="Predicted", template="Baseline")
        data.predict(days=days, name="Predicted")
        simulated_df = data.simulate(display=False)
        future_data[days] = simulated_df

        plt.figure(figsize=(12, 6))
        plt.plot(simulated_df.index, simulated_df["Confirmed"], label=f"Інфіковані ({days} днів)", color='red')
        plt.plot(simulated_df.index, simulated_df["Fatal"], label=f"Летальні випадки ({days} днів)", color='black')
        plt.plot(simulated_df.index, simulated_df["Recovered"], label=f"Одужалі ({days} днів)", color='green')
        plt.title(f"Прогноз COVID-19 для Argentina - {days} днів")
        plt.xlabel("Дата")
        plt.ylabel("К-сть випадків")
        plt.legend()
        plt.grid()
        plt.show()

    df = future_data[300]
    peak_date = df["Confirmed"].idxmax()
    print(f"Дата піку захворюваності: {peak_date}")


if __name__ == '__main__':
    freeze_support()
    main()
