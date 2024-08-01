def TemperatureAssurance(batch_temperatures):
    # Initializing the cut temperature
    cut = 26
    rejected_batches = []

    # Iterating the temperatures and checking if they all meet the criteria
    for i in batch_temperatures:
        if i >= cut:
            print(str(i) + " is ok")
        else:
            rejected_batches.append(i)
            print(str(i) + " is rejected")

    # Print all rejected batches if any
    if rejected_batches:
        print("Rejected batches:", rejected_batches)

TemperatureAssurance([40, 26, 39, 30, 25, 21])