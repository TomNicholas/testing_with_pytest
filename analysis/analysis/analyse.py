import numpy as np


def check_temperature(T, melting_point=3000):
    """
    Check if an instantaneous temperature will melt the divertor.
    """
    if T > melting_point:
        print("Destroyed divertor!")
        melted = True

    elif T <= 0:
        raise ValueError("Unphysical temperature value!")

    else:
        melted = False

    return melted


def reactor_survived(temp_time_series):
    """
    Check that the divertor survived a whole shot.
    """
    survived = True
    for T in temp_time_series:
        if check_temperature(T):
            survived = False

    return survived
