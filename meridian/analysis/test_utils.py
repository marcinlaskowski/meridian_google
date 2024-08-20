# Copyright 2024 The Meridian Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Helper functions and constants for Analysis module unit tests.

These constants are meant to be used in the end-to-end-like unit tests. They
were generated by running the model in a colab. The model was initialized with
random data (using seed=0), using same settings as the test Colab notebook.
"""

from collections.abc import Mapping, Sequence
from xml import etree as et

from meridian import constants as c
import numpy as np
import pandas as pd
import xarray as xr


__all__ = []


INC_IMPACT_MEDIA_AND_RF_USE_PRIOR = np.array([[
    [250.93, 914.95, 1488.56, 2499.96, 194.59],
    [323.77, 766.39, 499.36, 218.52, 536.27],
    [454.30, 381.87, 274.42, 812.97, 316.66],
    [216.75, 581.56, 565.30, 391.46, 161.34],
    [279.34, 2646.60, 2225.99, 454.78, 612.63],
    [421.48, 689.09, 408.15, 941.84, 114.84],
    [1383.32, 810.77, 511.27, 598.21, 283.58],
    [717.54, 192.93, 249.84, 240.15, 1106.14],
    [194.41, 55.73, 432.67, 126.29, 162.53],
    [252.09, 52.38, 297.78, 125.89, 226.06],
]])
INC_IMPACT_MEDIA_AND_RF_USE_POSTERIOR = np.array([
    [
        [582.06, 636.00, 170.72, 131.45, 747.25],
        [576.95, 628.67, 171.09, 131.47, 761.42],
        [579.18, 635.11, 174.04, 132.01, 759.44],
        [565.29, 639.10, 177.51, 131.00, 754.27],
        [560.16, 635.52, 173.50, 131.34, 761.65],
        [558.92, 646.11, 176.58, 130.95, 746.63],
        [552.30, 657.84, 170.02, 130.94, 748.13],
        [560.61, 664.25, 171.13, 131.26, 740.95],
        [552.71, 659.69, 170.69, 130.04, 738.11],
        [553.07, 660.30, 170.71, 130.10, 738.35],
    ],
    [
        [79.00, 164.46, 53.80, 495.31, 159.67],
        [79.02, 164.46, 53.79, 495.32, 159.69],
        [79.02, 164.52, 53.80, 495.09, 159.11],
        [79.04, 164.57, 53.95, 494.78, 159.33],
        [78.69, 164.55, 53.93, 494.57, 159.17],
        [78.78, 164.59, 53.89, 494.68, 159.05],
        [79.10, 164.85, 53.85, 495.01, 159.23],
        [79.85, 164.75, 53.78, 495.48, 160.84],
        [79.86, 164.61, 53.71, 494.85, 160.99],
        [79.84, 164.81, 53.60, 495.19, 161.18],
    ],
])
INC_IMPACT_MEDIA_ONLY_USE_PRIOR = np.array([[
    [551.34, 1071.77, 600.61],
    [416.56, 220.16, 302.47],
    [328.12, 191.68, 108.85],
    [858.76, 480.41, 163.72],
    [156.49, 216.55, 871.51],
    [2208.06, 752.48, 60.76],
    [212.20, 85.28, 20.00],
    [160.69, 642.43, 651.54],
    [1335.38, 513.54, 181.51],
    [147.56, 426.27, 354.36],
]])
INC_IMPACT_MEDIA_ONLY_USE_POSTERIOR = np.array([
    [
        [341.47, 4323.64, 1198.80],
        [70.05, 7476.11, 69.56],
        [1124.28, 6274.36, 693.93],
        [60.03, 5857.76, 263.23],
        [77.94, 3465.37, 143.75],
        [2336.68, 2529.21, 277.47],
        [625.78, 5145.63, 268.51],
        [592.20, 6010.15, 1035.03],
        [503.91, 6103.16, 358.96],
        [833.23, 1976.09, 124.21],
    ],
    [
        [87.94, 1695.98, 99.80],
        [87.93, 1695.97, 99.80],
        [87.94, 1696.01, 99.80],
        [87.94, 1696.01, 99.81],
        [87.94, 1695.97, 99.81],
        [87.93, 1695.96, 99.80],
        [87.93, 1696.37, 99.81],
        [87.89, 1697.92, 99.89],
        [87.84, 1692.52, 100.31],
        [87.72, 1696.20, 100.65],
    ],
])
INC_IMPACT_RF_ONLY_USE_PRIOR = np.array([[
    [646.24, 318.49],
    [441.57, 256.74],
    [1331.16, 97.92],
    [168.89, 601.37],
    [299.61, 297.77],
    [1382.17, 487.59],
    [318.69, 159.89],
    [812.50, 1734.59],
    [257.95, 871.77],
    [162.43, 675.57],
]])
INC_IMPACT_RF_ONLY_USE_POSTERIOR = np.array([
    [
        [386.06, 1037.53],
        [385.36, 1039.23],
        [382.93, 1037.09],
        [382.42, 1041.15],
        [383.14, 1039.56],
        [383.37, 1034.98],
        [384.68, 1039.13],
        [382.77, 1040.12],
        [381.06, 1042.39],
        [379.17, 1035.06],
    ],
    [
        [1181.46, 353.52],
        [1193.12, 340.00],
        [1096.41, 341.53],
        [1329.99, 347.21],
        [1429.17, 333.79],
        [1425.08, 329.34],
        [1497.22, 306.80],
        [1625.06, 304.85],
        [1622.44, 305.77],
        [2081.52, 317.14],
    ],
])

MROI_MEDIA_AND_RF_USE_PRIOR = np.array([[
    [0.3399, 1.7045, 3.1300, 2.7845, 0.3523],
    [0.4540, 1.3445, 0.9966, 0.2985, 0.4917],
    [0.7575, 0.3504, 0.5767, 1.0278, 0.8805],
    [0.3337, 0.4499, 0.6881, 0.3966, 0.1746],
    [0.3649, 2.8715, 3.3528, 0.7638, 0.8069],
    [0.8379, 1.6386, 0.7886, 1.8928, 0.3080],
    [2.8982, 1.9764, 1.2727, 1.1683, 0.2494],
    [1.4771, 0.4279, 0.5875, 0.4700, 1.1623],
    [0.3116, 0.1210, 0.4312, 0.1828, 0.2387],
    [0.5794, 0.0999, 0.6654, 0.2890, 0.3041],
]])
MROI_MEDIA_AND_RF_USE_PRIOR_BY_REACH = np.array([[
    [0.3399, 1.7045, 3.1300, 9.1854, 0.6759],
    [0.4540, 1.3445, 0.9966, 0.8028, 1.8628],
    [0.7574, 0.3504, 0.5767, 2.9870, 1.1000],
    [0.3337, 0.4499, 0.6881, 1.4383, 0.5605],
    [0.3649, 2.8715, 3.3528, 1.6709, 2.1280],
    [0.8379, 1.6386, 0.7886, 3.4605, 0.3989],
    [2.8982, 1.9764, 1.2727, 2.1979, 0.9851],
    [1.4771, 0.4279, 0.5875, 0.8823, 3.8424],
    [0.3116, 0.1210, 0.4312, 0.4640, 0.5646],
    [0.5794, 0.0999, 0.6654, 0.4625, 0.7852],
]])
MROI_MEDIA_AND_RF_USE_POSTERIOR = np.array([
    [
        [1.6876, 1.9684, 0.5030, 0.0934, 0.1623],
        [1.6734, 1.9471, 0.5040, 0.0958, 0.1645],
        [1.6799, 1.9672, 0.5139, 0.0969, 0.1641],
        [1.6378, 1.9834, 0.5252, 0.1009, 0.1620],
        [1.6236, 1.9732, 0.5131, 0.1012, 0.1631],
        [1.6196, 2.0069, 0.5218, 0.0993, 0.1604],
        [1.6011, 2.0436, 0.5036, 0.1036, 0.1613],
        [1.6256, 2.0625, 0.5077, 0.1045, 0.1597],
        [1.6034, 2.0482, 0.5070, 0.1037, 0.1592],
        [1.6045, 2.0500, 0.5069, 0.1039, 0.1591],
    ],
    [
        [0.2256, 0.3251, 0.1359, 0.1392, 0.1424],
        [0.2256, 0.3250, 0.1359, 0.1392, 0.1424],
        [0.2256, 0.3253, 0.1360, 0.1394, 0.1419],
        [0.2258, 0.3255, 0.1364, 0.1371, 0.1421],
        [0.2247, 0.3255, 0.1363, 0.1370, 0.1420],
        [0.2250, 0.3256, 0.1362, 0.1375, 0.1419],
        [0.2260, 0.3264, 0.1362, 0.1343, 0.1424],
        [0.2282, 0.3266, 0.1359, 0.1343, 0.1436],
        [0.2283, 0.3265, 0.1358, 0.1349, 0.1437],
        [0.2282, 0.3271, 0.1354, 0.1335, 0.1442],
    ],
])
MROI_MEDIA_AND_RF_USE_POSTERIOR_BY_REACH = np.array([
    [
        [1.6876, 1.9684, 0.5030, 0.4830, 2.5956],
        [1.6734, 1.9471, 0.5040, 0.4830, 2.6450],
        [1.6799, 1.9672, 0.5139, 0.4850, 2.6381],
        [1.6378, 1.9834, 0.5252, 0.4813, 2.6201],
        [1.6236, 1.9732, 0.5131, 0.4825, 2.6458],
        [1.6196, 2.0069, 0.5218, 0.4811, 2.5936],
        [1.6011, 2.0436, 0.5036, 0.4811, 2.5988],
        [1.6256, 2.0625, 0.5077, 0.4822, 2.5739],
        [1.6034, 2.0482, 0.5070, 0.4778, 2.5640],
        [1.6045, 2.0500, 0.5069, 0.4780, 2.5648],
    ],
    [
        [0.2256, 0.3251, 0.1359, 1.8198, 0.5546],
        [0.2256, 0.3250, 0.1359, 1.8199, 0.5547],
        [0.2256, 0.3253, 0.1360, 1.8191, 0.5527],
        [0.2258, 0.3255, 0.1364, 1.8179, 0.5534],
        [0.2247, 0.3255, 0.1363, 1.8171, 0.5529],
        [0.2250, 0.3256, 0.1362, 1.8175, 0.5525],
        [0.2260, 0.3264, 0.1362, 1.8187, 0.5531],
        [0.2282, 0.3266, 0.1359, 1.8205, 0.5587],
        [0.2283, 0.3265, 0.1358, 1.8181, 0.5592],
        [0.2282, 0.3271, 0.1354, 1.8194, 0.5598],
    ],
])
MROI_MEDIA_ONLY_USE_PRIOR = np.array([[
    [1.0740, 1.3019, 0.7984],
    [0.8990, 0.4201, 0.7120],
    [0.1340, 0.4114, 0.2389],
    [1.1974, 0.9624, 0.3721],
    [0.2613, 0.3995, 2.0881],
    [2.7704, 0.8456, 0.1207],
    [0.4953, 0.0424, 0.0423],
    [0.2991, 0.4112, 0.7823],
    [0.4918, 1.0556, 0.3962],
    [0.1665, 1.0178, 0.3253],
]])
MROI_MEDIA_ONLY_USE_POSTERIOR = np.array([
    [
        [0.4422, 9.3207, 2.3945],
        [0.1470, 12.8182, 0.1610],
        [1.0377, 13.3305, 1.8174],
        [0.0568, 14.6320, 0.4360],
        [0.1162, 5.4620, 0.2345],
        [4.7597, 5.0803, 0.2372],
        [1.1496, 11.8842, 0.4796],
        [0.9482, 12.9420, 1.6867],
        [0.8706, 14.3139, 0.5490],
        [1.6256, 4.4582, 0.1215],
    ],
    [
        [0.1977, 5.3532, 0.3220],
        [0.1976, 5.3530, 0.3220],
        [0.1977, 5.3534, 0.3220],
        [0.1977, 5.3533, 0.3220],
        [0.1977, 5.3531, 0.3220],
        [0.1977, 5.3531, 0.3220],
        [0.1977, 5.3543, 0.3219],
        [0.1973, 5.3592, 0.3223],
        [0.1977, 5.3426, 0.3237],
        [0.1973, 5.3541, 0.3248],
    ],
])
MROI_RF_ONLY_USE_PRIOR = np.array([[
    [0.5429, 0.3957],
    [0.4478, 0.2091],
    [1.9448, 0.2493],
    [0.2426, 1.0238],
    [0.4595, 0.5257],
    [1.4106, 0.5619],
    [0.6273, 0.1139],
    [1.8461, 2.2882],
    [0.5036, 0.8826],
    [0.2506, 0.7252],
]])
MROI_RF_ONLY_USE_PRIOR_BY_REACH = np.array([[
    [2.3753, 1.1037],
    [1.6244, 0.8928],
    [4.8863, 0.3513],
    [0.6133, 2.0871],
    [1.0978, 1.0359],
    [5.0919, 1.7021],
    [1.1755, 0.5495],
    [2.9831, 6.0266],
    [0.9513, 3.0227],
    [0.5975, 2.3417],
]])
MROI_RF_ONLY_USE_POSTERIOR = np.array([
    [
        [1.1980, 0.6598],
        [1.2059, 0.6493],
        [1.1873, 0.6377],
        [1.1821, 0.6507],
        [1.2059, 0.6492],
        [1.2163, 0.6443],
        [1.2193, 0.6353],
        [1.2197, 0.6444],
        [1.2144, 0.6423],
        [1.2055, 0.6393],
    ],
    [
        [1.6838, 1.0183],
        [1.6449, 0.2891],
        [1.8734, 0.6988],
        [1.8439, 0.2740],
        [2.2058, 0.5334],
        [1.7365, 0.3025],
        [1.8021, 0.5561],
        [3.3720, 0.3345],
        [2.6666, 0.5455],
        [2.8244, 0.3173],
    ],
])
MROI_RF_ONLY_USE_POSTERIOR_BY_REACH = np.array([
    [
        [1.4183, 3.6023],
        [1.4208, 3.6155],
        [1.3974, 3.5974],
        [1.4042, 3.6202],
        [1.4139, 3.6172],
        [1.4103, 3.5999],
        [1.4261, 3.5983],
        [1.4050, 3.6211],
        [1.4014, 3.6159],
        [1.4058, 3.5957],
    ],
    [
        [4.3477, 1.2222],
        [4.3790, 1.1917],
        [4.0231, 1.1834],
        [4.8855, 1.2039],
        [5.2465, 1.1637],
        [5.2446, 1.1340],
        [5.5086, 1.0636],
        [5.9674, 1.0501],
        [5.9643, 1.0677],
        [7.6481, 1.0991],
    ],
])

SAMPLE_ROI = np.array([
    [
        [1.5295, 1.0948],
        [0.6959, 0.2681],
        [3.6885, 1.9717],
    ],
    [
        [2.5433, 1.4539],
        [0.1932, 0.5897],
        [6.6965, 2.3686],
    ],
    [
        [2.7188, 0.4426],
        [1.0201, 0.2100],
        [7.4064, 0.6906],
    ],
    [
        [2.3552, 1.1502],
        [0.4632, 0.4780],
        [6.6092, 1.8199],
    ],
    [[1.2903, 1.5795], [0.4716, 0.5527], [3.0709, 2.6449]],
    [
        [2.0644, 1.1582],
        [0.6929, 0.6849],
        [4.1972, 1.6350],
    ],
])
SAMPLE_MROI = np.array([
    [
        [0.8354, 0.9310],
        [0.3215, 0.2250],
        [2.2587, 1.6802],
    ],
    [
        [1.0984, 1.1655],
        [0.1094, 0.3251],
        [2.4685, 2.0506],
    ],
    [
        [1.2490, 0.3233],
        [0.4967, 0.1358],
        [3.2525, 0.5220],
    ],
    [[0.9274, 0.1185], [0.2306, 0.0957], [2.3833, 0.1392]],
    [
        [0.4968, 0.1521],
        [0.2034, 0.1419],
        [1.0355, 0.1641],
    ],
    [
        [0.9120, 0.5455],
        [0.3138, 0.1945],
        [1.5988, 0.8988],
    ],
])
SAMPLE_CPIK = np.array([
    [
        [2.8592, 6.6402],
        [0.9368, 1.5922],
        [4.5142, 11.7104],
    ],
    [
        [4.4769, 3.3190],
        [0.6124, 1.2901],
        [15.9312, 5.3240],
    ],
    [
        [1.8077, 9.7881],
        [0.4410, 4.5464],
        [3.0791, 14.9515],
    ],
    [
        [2.8703, 4.1234],
        [0.5804, 1.7252],
        [6.7785, 6.5684],
    ],
    [
        [3.7490, 3.3789],
        [1.1116, 1.1799],
        [6.8440, 5.5822],
    ],
    [
        [2.1109, 3.2354],
        [0.7490, 1.9020],
        [4.4865, 4.5707],
    ],
])
SAMPLE_EFFECTIVENESS = np.array([
    [
        [3.0950e-01, 2.2154e-01],
        [1.4081e-01, 5.4255e-02],
        [7.4636e-01, 3.9898e-01],
    ],
    [
        [5.1542e-01, 2.9465e-01],
        [3.9163e-02, 1.1952e-01],
        [1.3570e00, 4.8001e-01],
    ],
    [
        [5.4621e-01, 8.8930e-02],
        [2.0495e-01, 4.2191e-02],
        [1.4879e00, 1.3875e-01],
    ],
    [
        [1.9593e-04, 9.5685e-05],
        [3.8535e-05, 3.9767e-05],
        [5.4982e-04, 1.5140e-04],
    ],
    [
        [1.0622e-04, 1.3003e-04],
        [3.8824e-05, 4.5498e-05],
        [2.5280e-04, 2.1773e-04],
    ],
    [
        [4.2322e-04, 2.3743e-04],
        [1.4204e-04, 1.4041e-04],
        [8.6045e-04, 3.3518e-04],
    ],
])
SAMPLE_SPEND = np.array([293.807, 278.854, 255.744, 272.165, 287.876, 1388.448])
SAMPLE_PCT_OF_SPEND = np.array([21.160, 20.083, 18.419, 19.602, 20.733, 100.0])
SAMPLE_INCREMENTAL_IMPACT = np.array([
    [
        [449.3971, 321.6781],
        [204.4690, 78.7793],
        [1083.7236, 579.3290],
    ],
    [
        [709.2308, 405.4423],
        [53.8891, 164.4619],
        [1867.3624, 660.5021],
    ],
    [
        [695.3375, 113.2083],
        [260.9031, 53.7094],
        [1894.1516, 176.6288],
    ],
    [
        [641.0110, 313.0473],
        [126.0751, 130.1054],
        [1798.8108, 495.3362],
    ],
    [
        [371.4706, 454.7283],
        [135.7712, 159.1129],
        [884.0682, 761.4331],
    ],
    [
        [2866.4497, 1608.1071],
        [962.0666, 951.0228],
        [5827.7158, 2270.1303],
    ],
])
SAMPLE_BASELINE_EXPECTED_IMPACT = np.array([
    [11180.9931, 20127.6386],
    [-24876.6487, 13877.7523],
    [55426.2115, 26502.3695],
])
SAMPLE_PCT_OF_CONTRIBUTION = np.array([
    [
        [3.1991, 1.4799],
        [1.4555, 0.3624],
        [7.7147, 2.6653],
    ],
    [
        [5.0488, 1.8653],
        [0.3836, 0.7566],
        [13.2932, 3.0387],
    ],
    [
        [4.9499, 0.5208],
        [1.8573, 0.2471],
        [13.4839, 0.8126],
    ],
    [
        [4.5631, 1.4402],
        [0.8974, 0.5985],
        [12.8052, 2.2789],
    ],
    [
        [2.6444, 2.0920],
        [0.9665, 0.7320],
        [6.2934, 3.5031],
    ],
    [
        [20.4054, 7.3984],
        [6.8486, 4.3753],
        [41.4859, 10.4442],
    ],
])
SAMPLE_BASELINE_PCT_OF_CONTRIBUTION = np.array([
    [79.5945, 92.6015],
    [-177.0902, 63.8475],
    [394.5644, 121.9298],
])
ADSTOCK_DECAY_CI_HI = np.array([1.0, 1.0, 0.8295, 0.9728, 0.6880])
ADSTOCK_DECAY_CI_LO = np.array([1.0, 1.0, 0.8128, 0.6194, 0.6607])
ADSTOCK_DECAY_MEAN = np.array([1.0, 1.0, 0.8214, 0.8359, 0.6748])
HILL_CURVES_CI_HI = np.array([0.0, 0.0, 0.00098, 0.00895, 0.00195])
HILL_CURVES_CI_LO = np.array([0.0, 0.0, 0.00085, 0.00322, 0.00169])
HILL_CURVES_MEAN = np.array([0.0, 0.0, 0.00091, 0.00606, 0.00183])
HILL_CURVES_COUNT_HISTOGRAM = np.array(
    [34.55127961, 34.55127961, 51.82691941, 51.82691941, 17.2756398]
)
HILL_CURVES_SCALED_COUNT_HISTOGRAM = np.array(
    [0.06667, 0.06667, 0.09999999, 0.09999999, 0.03333]
)
HILL_CURVES_START_INTERVAL_HISTOGRAM = np.array(
    [0.00445, 0.00468, 0.004898, 0.00512, 0.00534]
)
HILL_CURVES_END_INTERVAL_HISTOGRAM = np.array(
    [0.00468, 0.004898, 0.00512, 0.00534, 0.00557]
)

PREDICTIVE_ACCURACY_NO_HOLDOUT_ID_NO_GEOS_OR_TIMES = np.array(
    [-2.785, -5.832, 10.677, 0.696, 1.001, 0.596]
)
PREDICTIVE_ACCURACY_NO_HOLDOUT_ID_GEOS_NO_TIMES = np.array(
    [-4.295, -4.705, 3.646, 1.158, 1.083, 0.820]
)
PREDICTIVE_ACCURACY_NO_HOLDOUT_ID_TIMES_NO_GEOS = np.array(
    [-1.394, -0.814, 2.242, 0.992, 1.177, 0.608]
)
PREDICTIVE_ACCURACY_NO_HOLDOUT_ID_TIMES_AND_GEOS = np.array(
    [-13.597, -7.360, 1.634, 0.887, 0.990, 0.757]
)
PREDICTIVE_ACCURACY_HOLDOUT_ID = np.array([
    -2.907,
    -2.356,
    -2.784,
    -3.267,
    -1.431,
    -5.836,
    2.481,
    46.381,
    10.724,
    0.729,
    63.022,
    0.696,
    0.994,
    1.038,
    1.001,
    0.633,
    0.906,
    0.596,
])
SAMPLE_IMPRESSIONS = np.array([
    1.4520000e03,
    1.3760000e03,
    1.2730000e03,
    3.2716225e06,
    3.4970928e06,
    6.7728160e06,
])
SAMPLE_PCT_OF_IMPRESSIONS = np.array([
    2.143865e-02,
    2.031651e-02,
    1.879573e-02,
    4.830520e01,
    5.163425e01,
    1.000000e02,
])
SAMPLE_CPM = np.array([
    2.023468e02,
    2.026558e02,
    2.008992e02,
    8.318969e-02,
    8.231886e-02,
    2.050032e-01,
])


def generate_model_fit_data(
    geo: Sequence[str] | None = None,
    time: Sequence[str] | None = None,
    actual: Sequence[Sequence[int]] | None = None,
) -> xr.Dataset:
  """Helper method to generate simulated model fit analyzed data."""
  metric = [c.MEAN, c.CI_LO, c.CI_HI]
  if geo:
    n_geos = len(geo)
  else:
    n_geos = 5
    geo = [f"geo {i}" for i in range(n_geos)]
  if time:
    n_time = len(time)
  else:
    n_time = 52
    time = pd.date_range("2023-01-01", freq="W-SUN", periods=n_time).format(
        formatter=lambda x: x.strftime("%Y-%m-%d")
    )

  np.random.seed(0)
  expected = abs(np.random.lognormal(10, 1, size=(n_geos, n_time, 3)))
  baseline = abs(np.random.lognormal(10, 1, size=(n_geos, n_time, 3)))
  if not actual:
    actual = abs(np.random.lognormal(10, 1, size=(n_geos, n_time)))

  return xr.Dataset(
      data_vars={
          c.EXPECTED: (
              [c.GEO, c.TIME, c.METRIC],
              expected,
          ),
          c.BASELINE: (
              [c.GEO, c.TIME, c.METRIC],
              baseline,
          ),
          c.ACTUAL: ([c.GEO, c.TIME], actual),
      },
      coords={
          c.GEO: geo,
          c.TIME: time,
          c.METRIC: metric,
      },
      attrs={c.CONFIDENCE_LEVEL: 0.9},
  )


def generate_predictive_accuracy_table(
    with_holdout: bool = False, column_var: str | None = None
) -> pd.DataFrame:
  """Helper method to simulate predictive accuracy DataFrame for Summarizer."""
  metric = [c.R_SQUARED, c.MAPE, c.WMAPE]
  geo_granularity = [c.GEO, c.NATIONAL]
  evaluation_set = [c.TRAIN, c.TEST, c.ALL_DATA]

  shape = [len(metric), len(geo_granularity)]
  dims = [c.METRIC, c.GEO_GRANULARITY]
  coords = {
      c.METRIC: ([c.METRIC], metric),
      c.GEO_GRANULARITY: ([c.GEO_GRANULARITY], geo_granularity),
  }
  if with_holdout:
    shape.append(len(evaluation_set))
    dims.append(c.EVALUATION_SET_VAR)
    coords[c.EVALUATION_SET_VAR] = (
        [c.EVALUATION_SET_VAR],
        evaluation_set,
    )
  np.random.seed(0)
  value = np.random.lognormal(0, 1, size=shape)
  ds = xr.Dataset(
      data_vars={
          c.VALUE: (dims, value),
      },
      coords=coords,
  )
  df = ds.to_dataframe().reset_index()
  if not column_var:
    return df
  coords = list(ds.coords)
  if column_var not in coords:
    raise ValueError(
        f"The DataFrame cannot be pivoted by {column_var} as it does not"
        " exist in the DataFrame."
    )
  indices = coords.copy()
  indices.remove(column_var)
  pivoted_df = (
      df.pivot(
          index=indices,
          columns=column_var,
          values=c.VALUE,
      )
      .reset_index()
      .rename_axis(None, axis=1)
  )
  # The 2-Pager displays the national predictive accuracy metric data only.
  national_table = pivoted_df[pivoted_df[c.GEO_GRANULARITY] == c.NATIONAL]
  return national_table


def generate_media_summary_metrics() -> xr.Dataset:
  """Helper method to generate simulated media summary metrics data."""
  channel = [f"ch_{i}" for i in range(3)] + [f"rf_ch_{i}" for i in range(2)]
  channel.append(c.ALL_CHANNELS)
  metric = [c.MEAN, c.CI_LO, c.CI_HI]
  distribution = [c.PRIOR, c.POSTERIOR]

  np.random.seed(0)
  shape = (len(channel), len(metric), len(distribution))
  pct_of_spend = np.random.randint(low=0, high=100, size=len(channel))
  spend = np.random.randint(low=10, high=1000, size=len(channel))
  impressions = np.random.randint(low=10, high=1000, size=len(channel))
  cpm = np.random.random(size=len(channel))
  roi = np.random.lognormal(1, 1, size=shape)
  mroi = np.random.lognormal(0, 1, size=shape)
  cpik = np.random.lognormal(0, 1, size=shape)
  incremental_impact = np.random.lognormal(10, 1, size=shape)
  effectiveness = np.random.lognormal(1, 1, size=shape)
  pct_of_contribution = np.random.randint(low=0, high=50, size=shape)
  pct_of_impressions = np.random.randint(low=0, high=100, size=len(channel))

  return xr.Dataset(
      data_vars={
          c.IMPRESSIONS: ([c.CHANNEL], impressions),
          c.PCT_OF_IMPRESSIONS: ([c.CHANNEL], pct_of_impressions),
          c.SPEND: ([c.CHANNEL], spend),
          c.PCT_OF_SPEND: ([c.CHANNEL], pct_of_spend),
          c.CPM: ([c.CHANNEL], cpm),
          c.INCREMENTAL_IMPACT: (
              [c.CHANNEL, c.METRIC, c.DISTRIBUTION],
              incremental_impact,
          ),
          c.PCT_OF_CONTRIBUTION: (
              [c.CHANNEL, c.METRIC, c.DISTRIBUTION],
              pct_of_contribution,
          ),
          c.ROI: (
              [c.CHANNEL, c.METRIC, c.DISTRIBUTION],
              roi,
          ),
          c.EFFECTIVENESS: (
              [c.CHANNEL, c.METRIC, c.DISTRIBUTION],
              effectiveness,
          ),
          c.MROI: (
              [c.CHANNEL, c.METRIC, c.DISTRIBUTION],
              mroi,
          ),
          c.CPIK: (
              [c.CHANNEL, c.METRIC, c.DISTRIBUTION],
              cpik,
          ),
      },
      coords={
          c.CHANNEL: channel,
          c.METRIC: metric,
          c.DISTRIBUTION: distribution,
      },
      attrs={c.CONFIDENCE_LEVEL: 0.9},
  )


def generate_response_curve_data(
    n_channels: int = 5, spend_multiplier: Sequence[int] | None = None
) -> xr.Dataset:
  """Helper method to generate simulated response curve data."""
  channels = [f"channel {i}" for i in range(n_channels)]
  metric = [c.MEAN, c.CI_LO, c.CI_HI]
  spend_multiplier = (
      list(np.arange(0, 2, 0.05))
      if spend_multiplier is None
      else spend_multiplier
  )

  np.random.seed(0)
  shape = (
      len(spend_multiplier),
      len(channels),
      len(metric),
  )
  spend = np.random.lognormal(
      25, 1, size=(len(spend_multiplier), len(channels))
  )
  incremental_impact = np.random.lognormal(10, 1, size=shape)

  xarray = xr.Dataset(
      data_vars={
          c.SPEND: (
              [c.SPEND_MULTIPLIER, c.CHANNEL],
              spend,
          ),
          c.INCREMENTAL_IMPACT: (
              [c.SPEND_MULTIPLIER, c.CHANNEL, c.METRIC],
              incremental_impact,
          ),
      },
      coords={
          c.CHANNEL: channels,
          c.METRIC: metric,
          c.SPEND_MULTIPLIER: spend_multiplier,
      },
      attrs={c.CONFIDENCE_LEVEL: 0.9},
  )
  return xarray


def generate_predictive_accuracy_data(holdout_id: bool = False) -> xr.Dataset:
  """Helper method to generate simulated predictive accuracy data."""

  np.random.seed(0)

  xr_dims = [c.METRIC, c.GEO_GRANULARITY]
  xr_coords = {
      c.METRIC: (
          [c.METRIC],
          [c.R_SQUARED, c.MAPE, c.WMAPE],
      ),
      c.GEO_GRANULARITY: (
          [c.GEO_GRANULARITY],
          [c.GEO, c.NATIONAL],
      ),
  }
  rsquared_arr = [np.random.uniform(0.0, 1.0) for _ in range(2)]
  mape_arr = [np.random.uniform(0.0, 1.0) for _ in range(2)]
  wmape_arr = [np.random.uniform(0.0, 1.0) for _ in range(2)]

  if not holdout_id:
    stacked_metric_values = np.stack([rsquared_arr, mape_arr, wmape_arr])
    xr_data = {c.VALUE: (xr_dims, stacked_metric_values)}
  else:
    geo_train = [np.random.uniform(0.0, 1.0) for _ in range(3)]
    national_train = [np.random.uniform(0.0, 1.0) for _ in range(3)]
    geo_test = [np.random.uniform(0.0, 1.0) for _ in range(3)]
    national_test = [np.random.uniform(0.0, 1.0) for _ in range(3)]
    geo_all_data = [np.random.uniform(0.0, 1.0) for _ in range(3)]
    national_all_data = [np.random.uniform(0.0, 1.0) for _ in range(3)]

    stacked_train = np.stack([geo_train, national_train], axis=-1)
    stacked_test = np.stack([geo_test, national_test], axis=-1)
    stacked_all_data = np.stack([geo_all_data, national_all_data], axis=-1)
    stacked_total = np.stack(
        [stacked_train, stacked_test, stacked_all_data], axis=-1
    )

    xr_dims.append(c.EVALUATION_SET_VAR)
    xr_coords[c.EVALUATION_SET_VAR] = (
        [c.EVALUATION_SET_VAR],
        list(c.EVALUATION_SET),
    )
    xr_data = {c.VALUE: (xr_dims, stacked_total)}

  return xr.Dataset(data_vars=xr_data, coords=xr_coords)


def generate_optimal_frequency_data(
    channel_prefix: str = c.RF_CHANNEL,
    num_channels: int = 5,
    use_roi: bool = True,
) -> xr.Dataset:
  """Helper method to generate simulated optimal frequency data."""
  frequency = list(np.arange(1, 7.05, 0.1))
  rf_channel = [f"{channel_prefix}_{i}" for i in range(num_channels)]
  metric = [c.MEAN, c.CI_LO, c.CI_HI]

  np.random.seed(0)
  metric_by_frequency = np.random.lognormal(
      1, 1, size=(len(frequency), len(rf_channel), len(metric))
  )
  optimal_frequency = np.random.lognormal(1, 1, size=(len(rf_channel)))
  optimized_effectiveness = np.random.lognormal(
      1, 1, size=(len(rf_channel), len(metric))
  )
  optimized_incremental_impact = np.random.lognormal(
      1, 1, size=(len(rf_channel), len(metric))
  )
  optimized_pct_of_contribution = np.random.lognormal(
      1, 1, size=(len(rf_channel), len(metric))
  )
  optimized_roi = np.random.lognormal(1, 1, size=(len(rf_channel), len(metric)))
  optimized_mroi_by_reach = np.random.lognormal(
      1, 1, size=(len(rf_channel), len(metric))
  )
  optimized_mroi_by_frequency = np.random.lognormal(
      1, 1, size=(len(rf_channel), len(metric))
  )
  optimized_cpik = np.random.lognormal(
      1, 1, size=(len(rf_channel), len(metric))
  )

  metric_name = c.ROI if use_roi else c.CPIK
  data_vars = {
      metric_name: (
          [c.FREQUENCY, c.RF_CHANNEL, c.METRIC],
          metric_by_frequency,
      ),
      c.OPTIMAL_FREQUENCY: (
          [c.RF_CHANNEL],
          optimal_frequency,
      ),
      c.OPTIMIZED_EFFECTIVENESS: (
          [c.RF_CHANNEL, c.METRIC],
          optimized_effectiveness,
      ),
      c.OPTIMIZED_INCREMENTAL_IMPACT: (
          [c.RF_CHANNEL, c.METRIC],
          optimized_incremental_impact,
      ),
      c.OPTIMIZED_PCT_OF_CONTRIBUTION: (
          [c.RF_CHANNEL, c.METRIC],
          optimized_pct_of_contribution,
      ),
  }

  if use_roi:
    data_vars[c.OPTIMIZED_ROI] = (
        (c.RF_CHANNEL, c.METRIC),
        optimized_roi,
    )
    data_vars[c.OPTIMIZED_MROI_BY_REACH] = (
        (c.RF_CHANNEL, c.METRIC),
        optimized_mroi_by_reach,
    )
    data_vars[c.OPTIMIZED_MROI_BY_FREQUENCY] = (
        (c.RF_CHANNEL, c.METRIC),
        optimized_mroi_by_frequency,
    )
  else:
    data_vars[c.OPTIMIZED_CPIK] = (
        (c.RF_CHANNEL, c.METRIC),
        optimized_cpik,
    )

  return xr.Dataset(
      data_vars=data_vars,
      coords={
          c.FREQUENCY: frequency,
          c.RF_CHANNEL: rf_channel,
          c.METRIC: metric,
      },
  )


def generate_hill_curves_dataframe() -> pd.DataFrame:
  """Helper method to generate simulated hill curve data."""
  channel_names = [f"ch_{i}" for i in range(3)] + [
      f"rf_ch_{i}" for i in range(2)
  ]
  channel_array = []
  channel_type_array = []
  for i, channel in enumerate(channel_names):
    for _ in range(100):
      channel_array.append(channel)
      if i <= 3:
        channel_type_array.append(c.MEDIA)
      else:
        channel_type_array.append(c.RF)

  np.random.seed(0)
  media_units_array = [
      np.random.uniform(0, 1000) for _ in range(len(channel_array))
  ]
  distribution_array = [
      c.POSTERIOR if i % 2 == 0 else c.PRIOR for i in range(len(channel_array))
  ]
  ci_hi_array = [np.random.rand() for _ in range(len(channel_array))]
  ci_lo_array = [np.random.rand() for _ in range(len(channel_array))]
  mean_array = [np.random.rand() for _ in range(len(channel_array))]

  one_channel_impressions_hist = [
      np.random.rand() if i == 0 else None for i in range(100)
  ]
  one_channel_start_interval_hist = [
      np.random.uniform(0, 1000) if i == 0 else None for i in range(100)
  ]
  one_channel_end_interval_hist = [
      np.random.uniform(0, 1000) if i == 0 else None for i in range(100)
  ]

  scaled_count, start_interval, end_interval = [], [], []

  for _ in range(len(channel_names)):
    scaled_count.extend(one_channel_impressions_hist)
    start_interval.extend(one_channel_start_interval_hist)
    end_interval.extend(one_channel_end_interval_hist)

  data_hill = {
      c.CHANNEL: channel_array,
      c.MEDIA_UNITS: media_units_array,
      c.DISTRIBUTION: distribution_array,
      c.CI_HI: ci_hi_array,
      c.CI_LO: ci_lo_array,
      c.MEAN: mean_array,
      c.CHANNEL_TYPE: channel_type_array,
      c.SCALED_COUNT_HISTOGRAM: scaled_count,
      c.START_INTERVAL_HISTOGRAM: start_interval,
      c.END_INTERVAL_HISTOGRAM: end_interval,
  }

  return pd.DataFrame(data_hill).reset_index(drop=True)


def generate_adstock_decay_data() -> pd.DataFrame:
  """Helper method to generate simulated adstock decay data."""
  channel_names = [f"ch_{i}" for i in range(3)] + [
      f"rf_ch_{i}" for i in range(2)
  ]

  channel_array, time_units_array = [], []
  np.random.seed(0)

  for channel in range(len(channel_names)):
    for _ in range(100):
      channel_array.append(channel)
    time_units_array.extend(np.linspace(0, 20, 100))

  distribution_array = [
      c.PRIOR if i % 2 == 0 else c.POSTERIOR for i in range(len(channel_array))
  ]
  mean_array = [np.random.rand() for _ in range(len(channel_array))]
  ci_lo_array = [np.random.rand() for _ in range(len(channel_array))]
  ci_hi_array = [np.random.rand() for _ in range(len(channel_array))]

  data_hill = {
      c.TIME_UNITS: time_units_array,
      c.CHANNEL: channel_array,
      c.DISTRIBUTION: distribution_array,
      c.MEAN: mean_array,
      c.CI_LO: ci_lo_array,
      c.CI_HI: ci_hi_array,
  }

  return pd.DataFrame(data_hill).reset_index(drop=True)


def get_child_element(
    root: et.ElementTree.Element,
    path: str,
    attribs: Mapping[str, str] | None = None,
) -> et.ElementTree.Element:
  """Searches for a descendant element under `root` with the given path.

  Args:
    root: The top-level element to search from.
    path: Path fom the root to search.
    attribs: Optional attribute match to search for.

  Returns:
    ElementTree Element found from the path and attribute match.
  Raises:
    AssertionError if not found.
  """
  for div in root.findall(path):
    if attribs:
      if not (attribs.items() <= div.attrib.items()):
        continue
    return div
  raise AssertionError(
      f"Cannot find child element {path} under {root} "
      + (f"with {attribs}" if attribs else "")
  )


def get_table_row_values(
    tr: et.ElementTree.Element, row_element="td"
) -> Sequence[str]:
  row_values = []
  for row in tr.findall(row_element):
    row_values.append(row.text or "")
  return row_values


def generate_selected_times(start: str, periods: int) -> Sequence[str]:
  return pd.date_range(start, freq="W-SUN", periods=periods).format(
      formatter=lambda x: x.strftime("%Y-%m-%d")
  )
