

conv_type = input("Enter conversion type: ")
source_value = float(input("Enter source value: "))

match conv_type:
    case "C":
        print(f'Temperature is {(1.8 * source_value) + 32} Ferhenheit')
    case "F":
        print(f'Temperature is {(source_value - 32) / 1.8} Celsius')
    case "MPH":
        print(f'Speed is {source_value / 3.6} km/h')
    case "KPH":
        print(f'Speed is {source_value * 3.6} mph')
    case "kg":
        print(f'Weight is {source_value / 6.35029} stone & {source_value * 2.20462} lbs')
    case "stone":
        print(f'Weight is {source_value * 6.35029} kg & {source_value * 14} lbs')
    case "lbs":
        print(f'Weight is {source_value / 2.20462} kg & {source_value / 14} stone')
