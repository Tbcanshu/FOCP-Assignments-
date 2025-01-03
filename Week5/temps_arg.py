import sys

if len(sys.argv) > 1:
    temperatures = []
    for arg in sys.argv[1:]:
        try:
            temperatures.append(float(arg))
        except ValueError:
            continue  

    if temperatures:
        print(f"Max: {max(temperatures)}")
        print(f"Min: {min(temperatures)}")
        print(f"Mean: {sum(temperatures) / len(temperatures)}")
    else:
        print("No valid temperature readings provided.")
else:
    print("No temperatures provided.")