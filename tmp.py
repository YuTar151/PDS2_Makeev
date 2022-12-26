# Протягом 30 днів вересня було 12 дощових днів
rainy_days = 12
# Протягом 30 днів вересня було 8 вітряних днів
windy_days = 8
# Протягом 30 днів вересня було 4 холодних дні
cold_days = 4
# Протягом 30 днів вересня було 5 дощових та вітряних днів
rainy_windy_days = 5
# Протягом 30 днів вересня було 3 дощових та холодних дні
rainy_cold_days = 3
# Протягом 30 днів вересня було 2 вітряних та холодних дні
windy_cold_days = 2
# Протягом 30 днів вересня було 1 дощовий, вітряний та холодний день
all_days = 1

# Скільки днів у вересні була гарна погода
good_weather_days = 30 - rainy_days - windy_days - cold_days - rainy_windy_days - rainy_cold_days - windy_cold_days - all_days

if good_weather_days < 0:
    good_weather_days = 0
    print(f"У вересні було {good_weather_days} днів з гарною погодою.")
else:
    print(f"У вересні було {good_weather_days} днів з гарною погодою.")
