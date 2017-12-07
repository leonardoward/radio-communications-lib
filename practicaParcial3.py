# python3 practicaParcial3.py
import matplotlib.pyplot as plt
import RadiocomLib
from RadiocomLib import *
import printColors
import math

# AMPS
fc = 850            # MHz
population = 150000 # users
globalArea = 400    # Km^2

# Base Station
Ptx_BS = 30         # dBm
Srx_BS = -115       # dBm

# Mobile
Ptx_M = 26          # dBm
Srx_M = -112        # dBm

hAntena = 30        # M

userTraffic = 0.017 # Erlangs (Standard value)

# Cluster
voiceChannels_Cluster = 395     # channels/cluster
controlChannels_Cluster = 21    # channels/cluster
cells_Cluster = 7               # cells/cluster

# Sectors
sectorsPerCell = 3                                          # sectors/cell

clustersNumberArray = [3,6,9,12]

for x in range(len(clustersNumberArray)):

    clusterNumber = clustersNumberArray[x]

    printColors.printHeader("Clusters number = "+str(clusterNumber))
    print()

    # ##############################################################################
    # ##                            GOS (%)                                       ##
    # ##############################################################################

    printColors.printWarning("GOS (%)")
    print()

    # Cell
    voiceChannels_Cell = voiceChannels_Cluster/cells_Cluster       # channels/cell
    controlChannels_Cell = controlChannels_Cluster/cells_Cluster   # channels/cell

    # Sectors
    voiceChannels_sector = voiceChannels_Cell/sectorsPerCell    # channels/sector

    # Users
    marketPenetration = []                              # [0,1]
    globalUsers = []                                    # users
    users_cluster = []                                  # users/cluster
    users_cell = []                                     # users/cell
    users_sector = []                                   # users/sector
    traffic_sector = []                                 # Erlangs/sector

    i = 0
    while (i <= 100):
        marketPenetration.append(i/100)
        globalUsers.append(marketPenetration[i] * population)
        users_cluster.append(globalUsers[i]/clusterNumber)
        users_cell.append(users_cluster[i]/cells_Cluster)
        users_sector.append(users_cell[i]/sectorsPerCell)
        # Traffic
        traffic_sector.append(users_sector[i] * userTraffic)         # Erlangs/sector
        i = i + 1

    print("Sector's Voice Channels = " + str(voiceChannels_sector)+ " channels")
    print()
    printColors.printWarning("Sector")
    print("\tMarket Penetration = 20% -> Traffic = " + str(traffic_sector[20-1])+ " Erlangs")
    print("\tMarket Penetration = 40% -> Traffic = " + str(traffic_sector[40-1])+ " Erlangs")
    print("\tMarket Penetration = 60% -> Traffic = " + str(traffic_sector[60-1])+ " Erlangs")
    print("\tMarket Penetration = 80% -> Traffic = " + str(traffic_sector[80-1])+ " Erlangs")
    print("\tMarket Penetration = 100% -> Traffic = " + str(traffic_sector[100-1])+ " Erlangs")
    print()


    # ##############################################################################
    # ##                    Perimeter Coverage (%)                                ##
    # ##############################################################################

    printColors.printWarning("Perimeter Coverage (%)")
    print()

    # Sigma
    k = 1.2
    sigma = k + 1.3*math.log10(fc)

    # Area and cell's radius
    area_cluster = globalArea/clusterNumber     # Km²/cluster
    area_cell = area_cluster/cells_Cluster      # Km²/cell
    radius_cell = math.sqrt(area_cell/math.pi)

    # Trayectory Losses
    a_hm = 0
    Lb = 69.55 + 23.16*math.log10(fc) - 13.82*math.log10(hAntena) - a_hm + (44.9-6.55*math.log10(hAntena))*math.log10(radius_cell)  # dB

    # Downlink
    Prx_BS = Ptx_BS - Lb  # dBm
    z_down = (Srx_M - Prx_BS)/sigma      # dBm
    print("Downlink")
    print("\tz = " + str(z_down) + " dBm")
    print()

    # Uplink
    Prx_M = Ptx_M - Lb  # dBm
    z_up = (Srx_BS - Prx_M)/sigma      # dBm
    print("Uplink")
    print("\tz = " + str(z_up) + " dBm")
    print()

    # ##############################################################################
    # ##                              PLOTS                                       ##
    # ##############################################################################

    plt.figure()
    plt.subplot(2,1,1)
    plt.title('GOS Analysis with '+str(clusterNumber)+" clusters")
    plt.grid(True)
    plt.plot(marketPenetration, traffic_sector)
    # plt.title('Sector\'s traffic(Erlangs) vs Market Penetration')
    plt.xlabel('Market Penetration')
    plt.ylabel('Sector\'s traffic(Erlangs)')

    plt.subplot(2,1,2)
    plt.grid(True)
    plt.plot(marketPenetration, users_sector)
    # plt.title('Sector\'s users(hab) vs Market Penetration')
    plt.xlabel('Market Penetration')
    plt.ylabel('Sector\'s users(hab)')


plt.show()
