from dataclasses import dataclass
from typing import Dict, List, Optional, Set


input1 = """DGS)1HY
FYY)13C
RPN)9C5
NNV)CVR
BVN)BCH
39R)BPR
43R)CPB
XFB)J3X
LS3)D2Z
8KB)XX5
MDK)2YB
NFX)8GF
KV6)T6S
ZDP)163
CM4)453
FR8)ZV2
FQG)QXG
ZLY)G8X
81Q)GKB
V33)QBG
BXZ)724
T4W)XJ4
BM6)CW1
W5P)HWD
3LQ)1BF
7R1)GL2
1KM)R91
J19)55D
VW9)PFT
S9F)393
ZR3)TVM
KM9)K5D
B7P)ZFJ
G2Q)C7N
9C7)QTH
BS2)7NB
5QV)K91
L1Y)VX5
PBY)XFL
TC8)B7P
T7C)5WZ
6HZ)NRW
FPT)C75
FRK)R9F
RXL)WPB
LSG)SYB
WZ5)86T
6NG)C6C
VHQ)P2S
CCN)3PP
Y8H)ZLY
3V6)XBW
GGS)3HX
FK6)VTV
2M1)LNP
3WK)BVF
T2W)HRB
C2T)XSR
HVF)N5T
MPK)X68
X1H)HXJ
SD1)CG7
ZLL)T4W
VHS)2G7
HKC)CJF
DW1)F82
LWP)C3M
7KH)S8C
TTP)BVM
JCM)3HJ
RBT)9XB
7CG)7B6
Y8B)MX2
724)Z38
6V6)TR7
6CP)67M
DNV)9MG
Q83)2BQ
KX1)MJC
HDT)RSV
HG6)9NW
Y74)S14
N56)NRN
G8P)XH4
VK7)R7C
CB5)S7X
NFW)P89
8VG)RLN
GJB)JYR
BQX)G73
TWQ)Y74
K57)DGD
NLY)1SZ
VF8)BTV
JGX)489
MYZ)LVD
WXN)DJR
6G2)2BG
3M5)J4S
7BD)F3Q
W8M)6FC
6J4)4DD
7Y1)1P7
GMJ)46H
G5C)V86
147)WLR
TJM)FM7
DN4)QV6
V76)8HY
QCX)R5D
LNK)9ZP
TF7)JL3
9ZX)DV2
G5V)FYY
LJC)B88
6DW)2TB
LMT)THC
M61)R2B
8JL)QW1
5VP)6CP
TLL)RXL
422)2FG
9KG)ZLD
9ML)1WW
N38)PCP
PZ3)8K1
VV4)G6V
NWW)7MM
HSV)JBZ
XBM)XXQ
XSR)PND
LVD)17P
VNM)KJZ
K2Z)3Q3
ZZQ)86H
SQS)3FD
428)85T
G54)B62
V33)899
TRV)JKT
BDG)HJQ
HG6)DGX
1MB)6NY
6NY)P6P
VQQ)2ZJ
5G5)ZYJ
JP6)QV7
ZZN)85G
VRC)TFL
K7D)ZZQ
VSG)MJX
1TL)CYK
8HM)CWD
SQV)VRC
SYX)K5H
9MG)8HM
RSV)CMQ
TLH)KCF
THL)37P
WYW)4NQ
8ML)F2P
ZR1)SAN
4VB)52R
BPR)F5T
426)FBB
4B8)DKL
LYP)Q5B
HB2)VC7
93T)3PY
3HJ)B7D
6DH)7NY
8RZ)LVW
JL4)98M
4DD)HVH
M93)SCH
DRS)3R1
BTN)689
B7D)RB6
VX5)3SF
9KH)L26
BMT)NHG
HQW)4Z7
W5J)YTT
ZR3)DVT
V6W)S5W
NRN)MY4
FN5)HP6
THY)LL4
9SQ)425
6BJ)JDM
2TY)LX4
BKD)9BC
1R9)P1V
8K1)CR5
68H)72R
7H1)NWD
WQZ)MC2
T4W)1Z2
SPB)X7P
B4V)2R4
QG2)DZ9
BKD)WC1
V36)VLY
W9B)TMQ
ZG6)BJL
XS3)FB9
7B6)CQJ
KD4)HXB
DBM)1K5
82F)18S
M74)NJB
HJQ)G34
KVK)YYZ
L44)KDB
KNM)DD8
TVM)XC9
9SB)CRN
TR7)5VN
HYP)K6C
8BC)ZZN
WC1)SYL
P14)7LJ
1MP)11X
SYL)P6X
ZQ3)GD3
R6F)4WY
TRD)2SY
F2P)C4Z
DSW)VPL
KWN)8LG
45F)ZCL
MR5)LQT
DL1)DS4
KJZ)WWP
4SN)263
TT2)9W2
CVW)SLM
Y6Q)FXS
FN7)43F
MZ5)PX5
KTV)KLD
1N9)M1R
GHS)F73
6CJ)RTN
S9B)6SL
C7N)WBB
QKX)CHT
FP4)K1M
XZY)124
R7C)JXH
8TX)B17
7HP)F3R
KW2)6R9
6J4)P25
9RW)GH7
NRW)K2S
BBR)KM9
7BD)5SJ
WTQ)NNQ
L5S)KQG
GGW)GVM
94M)1MB
F2C)QWY
97N)ZCS
3VX)Y8H
51L)8LP
WXZ)YZ1
MJC)ZG6
8GW)SXR
PNR)6J4
G6V)W16
XNT)BDH
7QG)4PZ
QX4)75Z
5M5)CFS
BHN)HCS
2M1)NCD
43F)HYP
C45)Y7Y
LJK)THL
DW1)GJB
ZZZ)JMQ
DLM)T2F
38X)N6X
8VC)K6F
5CP)V59
RXL)3NN
7NB)LQY
QMB)G9R
NNQ)PMN
NZX)9H8
TCQ)2BF
1DD)SJ3
K6F)YN9
ZV2)MPW
VHQ)GN4
5K8)BM6
Y28)FK6
NPR)DKD
57N)M5N
15L)FHN
8DV)N56
3PP)BZY
5LC)4W7
K6C)9M1
CPT)6YS
LQ9)NYC
JXH)G7M
NWS)45F
Q9N)PHD
QH2)GJM
K93)SDT
3FD)YX6
8BD)SH6
QBG)X47
K2S)8VG
5D4)JPK
HL6)S9F
K3S)YBL
JP6)XCT
ZQ7)XT5
C7L)26C
YQ4)WVN
73F)LJC
HYF)KW2
N1M)426
ZVQ)K2Z
T6T)JS2
XXW)7NC
5DV)2RW
SXB)28F
XC9)NGM
LVW)JKV
7VP)4CB
PFT)1FL
VTV)1SP
163)MZ5
489)8P1
QRD)3V6
7XM)5JJ
VM5)86K
F3R)DSR
JG7)JKL
JJQ)KTV
CCD)2L8
55J)2GG
N6X)LYT
PPQ)B84
P5G)43R
2CL)TTP
QWF)2WD
YYW)3YT
9GL)VF8
VRH)1Q5
669)5BH
NWP)5V7
KV7)5XF
P9W)254
LKB)CPL
7FB)M2H
YH7)NL2
FBM)KK7
PJ9)SR6
SB4)BM3
LPR)MH9
41C)TLB
PBG)SMC
8N6)582
TQ4)D4C
2NJ)TZL
PKC)MYZ
427)YFZ
GMJ)BGP
FB9)1KM
NPR)6BQ
9C5)VJH
8MR)SPB
CTV)KNG
M2P)N85
BWJ)YBB
F97)HSV
XCT)D1G
1SP)HW1
V7Y)8X4
BZY)378
R42)9B8
G9R)7BD
WG6)1YC
W89)5MJ
1Z7)ZT9
5ZT)TC9
PY5)D4G
J4T)JYY
NWD)5CP
2FM)MP9
1S3)FF2
DGD)5WX
GWC)LPR
H98)GQF
WHD)NGP
85S)6Q4
WSL)2QH
3V6)W85
YVP)GFS
9NW)H57
BF8)MMH
F3Q)7XM
ZT9)7MP
ZCF)VHS
XPX)DPM
XSQ)W2G
B7D)9KH
79H)M2P
LZ8)77S
2JF)XTD
H47)2JF
LYT)SQV
3YQ)S58
8B8)85B
L49)KV7
3JF)D7F
96M)FMY
QQV)TRD
YVH)2KK
8KC)K3V
4D2)STW
1P7)HBH
9XB)M9M
Q99)8PN
JYY)WJW
4LC)GB6
2TR)Y4H
B4N)FGP
6PJ)5JB
SMG)Q9N
2YR)FMP
6ND)W5P
YYZ)GY4
Y7Q)251
H5R)YYW
1FY)Y7Q
SXR)5YG
PFL)NCT
D61)Z5K
2KL)V76
62F)6DW
J3Y)YOU
NGM)78Y
X7P)GKT
BTN)ZVQ
121)PQ6
MPK)W89
LV9)WVG
TZV)BXZ
3S3)LWP
CGQ)CZF
N6X)CCN
XJ4)3WK
SR6)1RV
GD3)F78
JW6)GKL
P8T)6K2
HZ7)WSH
6V5)PG9
R9C)J3Y
PJC)G3V
5Y4)63K
4M5)7W3
2BF)23M
LX6)TWM
526)KV6
LK7)YVH
576)9ML
6D9)4HZ
6VC)HQP
CFS)119
TC9)3BP
CBX)DSW
JMQ)LG6
QTB)8GW
VWD)JWN
3PY)JHL
ZZQ)TZV
6SL)BRX
GD7)51L
Y2T)9FS
TGF)976
6PP)WT1
JHL)9W9
SMJ)99W
ZL1)MJ5
RSW)6KQ
DD7)M86
SLM)2VQ
M9J)HMW
5VN)ZQ3
8G5)JPH
MFR)YVP
WXG)TWQ
2QH)LBP
15R)7YR
K17)7VX
QZQ)YQ4
QZF)WFT
2B1)D4Q
STW)V21
ZDX)669
8Y7)6V6
KDY)DN4
DVT)LHZ
2WD)6M5
S2B)YV7
3SF)3LQ
DCR)NG1
R91)CQW
MJQ)LMT
ST3)YDW
4T3)4Y4
3VT)26D
3HR)31P
BSF)HHP
VL2)3H4
TVM)C3Y
9M1)45N
PQ6)MR5
G6G)6F1
Y74)Z1Z
F5T)LSK
WV5)KPZ
2VQ)22G
582)KZQ
5RX)8M1
YFZ)F2C
QMV)DBM
THC)WHW
P2P)19H
DHM)2CL
PCP)XZ5
7NY)JGX
FR1)NBT
HHD)K11
31T)HVF
JCM)B2S
1QB)QQV
VPL)JF5
C4Z)YBN
5DH)74L
VY2)R8D
46H)MZ1
DTN)JG7
NY2)DZ8
KPZ)6G2
SZ3)RLZ
TMQ)NFW
HQH)4GR
MMC)TLH
B4N)4XK
2ZQ)JWW
2YM)QMT
G73)FN7
GN4)KJK
P6P)XNT
YFZ)C7L
P1V)GMK
P2S)2RB
QXG)2KL
W89)FQS
DLS)1MP
MHX)44H
C2T)3QM
W86)T6T
MCN)X9M
M2P)57N
SCH)GHP
XH4)576
9FS)PKC
R8D)D2N
ZQX)37J
LN8)BRM
HWD)ZK6
LBP)53C
YX6)7KF
5QW)SBM
LXH)KVK
263)G3L
B1G)XTY
3BP)FPT
CWD)5TM
TNB)L5S
6XC)WPS
7QK)G5V
CSR)B69
YHG)5XK
6K2)ZTH
C7T)QZQ
NBN)FVW
8P1)QJ6
GFS)SMJ
W2G)G6G
VDR)4YD
25M)MDK
YDW)QTB
LNN)FHY
DPM)2F8
899)S4M
F73)VHQ
5D3)6NG
F85)ST3
Q8N)81J
XBW)5LC
85M)51G
M1F)76Z
8LP)NY1
21C)P5K
T6T)41C
Z59)9H1
VC7)M8V
Q5B)CGQ
JYR)CBX
3RL)WKP
BQ2)LX1
8LL)TTM
MC7)3M5
L4Z)11N
RPZ)9DJ
119)DPY
XK7)SZ3
3CS)ZR3
3PN)WYW
LL4)5V9
HSJ)SKF
PTP)K17
MPW)X4Y
LRM)CFY
V3G)W9B
SBR)PJ6
KYQ)Q9S
WQ4)CCD
N25)2BZ
Z5K)XSQ
D4G)9V1
LX1)MW5
RB5)XJR
W29)LKV
CTG)HLP
3Q3)QZF
9BC)BTR
P9B)ZSN
PLY)Z4B
CBX)X1H
L64)QMW
T96)LGD
399)8G5
LG6)HQW
Y5J)31F
G8X)FCN
Y44)ZCF
8X4)B12
NL2)5G5
4YD)XK7
Z8K)CPT
LRH)6YQ
R9F)NHC
86T)K57
QLQ)HLJ
VKQ)YPQ
BC3)9VB
9F6)46L
74X)39R
Z1T)WVM
WXN)V3D
976)SYR
MW5)42P
LMT)P9W
JPK)H3J
ZCS)B6N
XTD)FXH
PHD)FP4
TCC)T7C
RJ3)QD6
PM7)VM5
K3V)2JH
HCS)3WZ
1HY)ZPY
VRL)HQL
HLH)BMT
4NW)ZQX
1M1)L4R
FVW)9KG
PKD)JL4
FCN)5QW
731)VG6
GP7)ZZZ
GCM)D8F
5DV)RVS
QJK)PB9
67M)KXH
VVD)B6S
ZLD)CXQ
5BP)N25
3NN)M93
SVJ)Y4C
TRW)VK7
LN9)85Z
Z9J)94M
9WS)85S
9V1)LX6
NY1)59Y
1RV)4K2
33D)3S3
3HX)9T1
9ZP)4BV
R5D)K6B
DLW)LJK
6YQ)CH7
QHQ)VSG
CG7)V36
85G)HPV
LQ9)9BR
7F2)VRR
29L)62F
Q9S)2D1
PWY)8DV
WPS)S8G
FB3)7HH
1YL)HG7
S8C)RPN
F57)WNY
YBL)HSJ
C75)QRD
WP9)LM1
HG7)QH2
N5R)6DH
TWM)LWS
LRH)FBM
78G)WVL
MH9)1N9
YS1)QJM
G3L)TCC
BTV)314
XDL)TCQ
6MW)389
MYZ)TQ6
CHT)BF8
37V)JQW
QKL)T2W
DJR)D4R
CRK)G2Q
S4M)B4V
NRN)9F6
BRM)465
5JJ)CFM
75Z)82F
W8Q)ZQ7
X68)31T
QW1)Q6V
PYY)1JW
6B4)NG5
NQ6)RL1
GHP)731
CQW)427
4W7)39N
XF7)VW9
MTY)1PP
BV1)S4Q
4CJ)JW6
52R)DTL
453)WBK
HPV)BLQ
JH9)DCR
JSF)NZX
FCG)W8Q
YJH)BC3
JKV)NQZ
RLZ)5D3
9H8)8BD
DGX)Q76
MJX)QZV
9SB)NL9
B7Y)5VP
689)9GR
NS5)Q83
K5D)9SQ
QJ6)L64
254)HHD
WYQ)J19
6BQ)QKX
6VC)6TY
5V7)4SS
378)NWP
L9B)VPH
JBZ)8KB
1SZ)F57
8T6)JSF
2D1)M74
HVH)1M1
446)7HP
9VB)DW1
9MM)RPZ
1PV)8T6
11N)121
WPB)YH7
MLD)DHM
VLK)D74
HJZ)9HP
53C)3GQ
MBB)SWM
SNN)5TN
CR5)BTN
1FL)YQP
PMN)PJC
R3J)68S
NG5)P5G
1X2)WT2
BPF)PW5
MX7)6ND
H57)CSR
CHJ)P14
P5D)YS1
QN6)ZQN
4SS)BQX
FG2)WQ4
HG3)5SS
SH6)S2W
Y4H)SYP
6TY)8TX
J4Z)TJM
STZ)WHD
2BQ)BMV
N56)1Z7
CZF)NJK
MJ5)5PZ
KK7)93T
CMQ)DLW
Z1Z)L1Y
8SM)NPR
5V9)L4Z
P7Q)5K8
NHC)CKH
X47)PNR
4J8)KPD
SZD)2ZQ
K48)7FB
FMP)39P
3XL)YJT
T3R)M2B
K11)P3F
NNK)5CV
J3X)BQ2
5JB)PY5
XHQ)R3S
9KH)GY8
7W1)VDQ
7MM)T2C
V59)K76
ZVN)RKJ
N6J)B7M
QZV)SBR
DPC)X6T
ZSD)SVJ
5PZ)NS5
DBH)V7Y
8J1)N1M
QNB)S5L
7LJ)DD7
SYR)NPS
CH7)Y2T
YMP)NNV
95P)G8P
7HH)LLJ
4MB)JXG
68S)P4Z
58H)J1L
P8R)B7Y
HXJ)5BP
MQJ)4XP
85B)TDZ
J1W)R42
D8F)7F2
T99)CVW
WK2)PBG
W16)W5J
CG7)LBK
JPH)Y6Q
B69)3YQ
ZFJ)JJQ
5XF)SS7
NBT)FBK
JXG)TNB
JL3)FR8
BHG)GHS
YZQ)GMJ
LN9)NWS
WHW)3NP
M2B)KT3
Z9L)J4T
R67)M4Y
GKT)M43
TF2)BV1
HMW)BWJ
ZJQ)HB2
WXR)SZD
8WX)5DH
BM3)KD4
WVG)RBT
YFD)ZKL
8C6)8VC
2JH)DJ5
NQZ)P7Q
86K)8LL
MHX)K48
1JW)STF
KQJ)6PP
NG1)3VT
C7T)VVD
N3W)2TY
5CV)GXR
CQJ)55J
J2T)526
RW8)LF3
CJF)PXW
4PZ)R4B
Y3T)W6T
X4Y)1QB
51L)5D4
Z4B)DL1
1PP)1W5
LLJ)5RX
5ZG)WK2
6PR)8KC
RB6)2ZV
R4R)B1G
Q76)W8M
5MJ)4LC
S58)1DN
5J4)B47
TTM)2YM
JF6)YYS
HL7)M37
XXQ)FG2
YN9)FGR
121)NJV
B6N)1DD
SWM)VQQ
MZN)LN8
B9X)GCM
NHP)6D9
JWW)PFL
D7F)LTG
BLQ)B16
6M5)9FC
WG9)WJK
GL2)5QV
1W5)VDT
GQF)QNB
Y7Q)446
LKV)VKQ
YQP)VS5
SDT)CTG
K91)XGP
9GR)CRD
F78)BVN
MB5)FR1
KT3)96M
GY4)WFX
2ZJ)LQB
251)3HR
9C5)BS2
MS2)QGV
1DN)2M1
ZMZ)BHG
TNX)PBY
FDH)LXH
2ZV)147
HHP)2BL
MRW)4NW
SYP)HQH
389)3PN
ZKL)33D
D4P)6MW
6YQ)QHQ
8Y8)S48
9W9)85M
LBK)MJS
GHB)DGS
G7M)MPK
HZG)399
P5K)DM4
72R)26Q
VVD)97N
4CB)BMD
5XW)R9C
7T3)6TP
BRX)W86
TQV)TNX
8K1)RSW
MJS)H5R
3HJ)QKL
WBK)4CZ
WFX)1TL
V76)TQ4
NCD)X5S
HTQ)428
TQ6)MLD
N85)R2D
DKW)25M
J4S)71W
BTR)JP6
124)QLQ
67M)ZVN
XV1)DLM
1Z2)15R
TDZ)112
JH9)CM4
YTT)WXZ
HRB)15L
65J)3KZ
CPB)L9B
JD3)V9J
3NN)1VC
2T5)XPX
KQG)VGD
LHZ)TLL
S7T)BPY
VDT)ZDX
1RW)21C
SBV)M9J
L1Y)V6W
CYK)T3R
YLM)N6J
XT2)9WQ
LTG)4B8
J3X)XVH
7YR)K32
ZSN)RGM
NYC)29L
P6X)HYF
7KM)7R1
58H)RMJ
JKT)WXR
FVW)V79
RL1)TRV
WT1)J7R
MKM)BPF
HW1)KX1
MP9)6X1
LQB)L6P
D4Q)Y44
5SJ)K7D
TZL)YZQ
DSR)3JF
17P)9C7
COM)KYQ
S14)LVB
DS4)FDH
KZQ)79H
71W)7QK
7HZ)CHJ
NGP)WRM
8M1)79F
YYS)Y28
RTN)PPQ
WT2)8Y7
YJT)R3J
3H4)1RW
T9Q)DLS
6GJ)WZ5
HBH)8BC
LNP)2TR
5TN)HMQ
2RB)NTV
GVM)YWL
SBM)1S3
BGP)QX4
WC1)LKB
J7R)BFX
2TB)9YC
2KK)GGW
WXR)LRH
V86)QHC
NPS)Z9L
18S)V33
CKH)MC7
5DH)BBR
2RW)SYX
CPL)MRW
ZTP)XLC
NFX)SD3
TRW)NQ6
WKP)Z8K
HHP)JCM
SVJ)VL2
TRZ)HG6
SKF)RJ3
FF8)Z9J
NT2)GHB
HLH)DPC
FGP)JD3
2G7)RB5
L4R)4VB
14D)5XW
XPR)9MQ
P3F)P5D
4JM)QCX
361)NXD
6SJ)8N6
393)68H
QKX)7CG
1V6)7KM
QMT)8B8
X5S)37V
FXH)HL7
NL9)K3S
WYW)BR6
K7C)168
9HP)VNM
S48)FB3
WBB)74X
DKL)LS3
SD3)JL5
6X1)Q99
WVN)2YR
G3V)QMV
4DD)9M6
4WY)MQJ
PWY)PYY
FF2)VLK
J1L)Q8G
B9X)WQZ
28F)DV3
K76)Y8B
TFL)PWY
HQP)WYQ
3R1)L9H
HQL)TF2
QW1)VV4
446)73F
4CZ)JXC
HPK)5ZT
S7X)3CS
KPD)CRK
3X8)FV7
G7G)5ZG
SMG)C7T
ZK6)4CJ
TL3)9RW
6SJ)LZ8
8XT)TF7
81J)839
LL4)B4N
ZQ7)S2B
8HY)3XJ
X6T)4MB
2JH)3VX
SYB)NLY
B62)1LD
9YC)6PB
2WP)WG6
MY4)RW8
13C)HDT
NHP)9WS
9PZ)BKD
NBQ)261
NJV)HPF
323)KNM
L26)SQS
NXD)422
SJ5)B1Q
JS2)DFL
7W3)1YS
QD6)MX7
HLP)D6F
Y5J)3RL
3YT)2B1
K5H)J2T
GH7)J1W
C3Y)G54
7RN)5J4
6YS)NFX
31P)LN9
P77)MKM
MMH)ZLL
HXB)9GL
59Y)FRK
RB5)LNN
MZ1)TT2
9W2)CCV
WNH)PTP
XFL)G9W
NFW)PJ9
K7D)M1F
GB6)T99
BMD)361
WNY)HNZ
P25)WNH
Q6V)YJH
S2W)7QG
QLQ)TQV
W85)NHP
CPP)8WX
M37)PZ3
XX5)2LQ
CY1)6HZ
PW5)7W1
5XK)SB4
CXQ)DKW
N38)WV5
M5N)Y5J
VRR)FP7
CFM)HZ7
NCD)6V5
NY1)P8R
51G)R67
168)L44
B84)4SN
3QM)Y77
RKJ)FN5
9MQ)GD7
JF5)VY2
BCH)TQ7
FM7)YMP
KCF)4J8
5WZ)VDR
44H)MJV
6SL)LNK
45N)QG2
B88)Y3T
QWY)7RN
FBB)6VC
9H1)WG9
VG6)PLY
15R)PKD
M43)9PZ
D2Z)38X
FHY)KDY
78Y)GZT
2SY)8JL
DPY)C4F
NJK)FCG
XTY)N5R
QY4)XF7
4HZ)ZTP
STF)VRL
11X)JF6
2GG)ZJQ
WRM)N4H
17X)XHQ
S5L)SNN
K9Z)SJ5
D74)6PJ
QMB)1X2
26C)2NJ
VLY)R6F
2BZ)CB5
46L)1YL
B2S)WP9
669)MHX
LF3)WHF
7NC)8SM
1NR)T56
DV3)Q8N
D72)S9B
TCD)GB9
3WZ)QN6
4LC)XXW
N5T)HTQ
GMP)323
K32)2Z6
DKL)XFB
2TR)ZSD
6PB)ZDP
L6G)TY9
FNX)58H
D4R)JH9
PG9)P8T
TQ7)ZL1
KM5)6KV
6DW)9ZX
H3J)8ML
7W1)V3G
LVB)SD1
2LQ)6CJ
HP6)3XL
99W)K9Z
YV7)5Y4
QTH)1NR
LQY)9MM
4BV)NNK
5ZT)LK7
LM1)K93
8LG)THY
LQT)Z2X
M4Y)B9X
JXC)NBQ
DKD)G5C
R9Y)2T5
PMN)8C6
XJR)MZN
839)7Y1
3KZ)78G
26D)RC9
XZ5)6GJ
PCP)TL3
1VC)8Y8
FXS)2FM
1YS)M78
85Z)GWC
GY8)S7T
PX5)TX2
NJB)8MR
2YB)PM7
GZT)WMC
1VL)R4R
SMC)785
S9B)CTV
2FG)H47
HMQ)1PV
FHN)C45
B17)WSL
GB9)ZR1
BFX)8XT
T49)KQJ
4NQ)G7G
4XK)S39
WT1)GMP
314)7H1
B16)TC8
JDM)QBT
CRN)NBN
CW1)6B4
T6S)6PR
KNG)MBB
2R4)YHG
VJH)GTX
3PH)XT2
J4Z)WXN
8GF)WTQ
JSF)4BM
6TP)14D
Z38)N38
BDH)HPK
4XP)BDG
QV7)NT2
2JF)WXG
WHD)DBH
WLR)XDL
9FS)XBM
NCT)DBV
JQW)HG3
GKL)6XC
B6S)TY1
H8R)2ZW
D1G)LQ9
YZ1)8J1
TY9)FF8
2L8)MMC
Z2X)3P6
F82)CY1
S39)LSG
GJM)MS2
TLB)DRS
KJK)D4P
9FC)K7C
GT6)QHR
9WQ)M61
BMV)D72
WVM)YFD
N4H)W29
ZV2)R9Y
QHR)GP7
465)X8K
X9M)2H7
4V3)LST
T2C)MCN
Y77)NY2
WVM)SXB
2Z6)FQG
1YC)22K
WSH)J4Z
Q8G)N3W
DJ5)NWW
4BM)TRZ
9M6)STZ
S5W)95P
WVL)P9M
KXH)KM5
2R1)7VP
DZ9)YLM
M1R)6KL
6KL)QY4
4K2)XV1
6FC)X7S
CFY)TRW
WHF)1VL
DV2)H8R
XGP)5DV
BVF)7KH
TC8)P2P
TX2)H98
TY1)4JM
FSN)VRH
XT5)TGF
XLC)3PH
T2F)YPT
YDW)SMG
LSK)KWN
77S)BSF
TX2)MJQ
QTB)4T3
MX2)HJZ
BJL)Z59
YBB)4V3
1LD)4M5
RVS)LRM
DBV)6BJ
3YQ)L49
K1M)6SJ
C6C)GT6
V79)D61
6Q4)Z1S
2BG)8RZ
SBV)HKC
WJK)QMB
X7S)C2T
D6F)7HZ
39N)17X
M1R)FSN
9BR)65J
7HP)ZMZ
M2H)VWD
DD8)T96
M78)4NB
FMY)HZG
19H)MTY
Q5B)LV9
4GR)DNV
WFT)8D1
HPF)HLH
PND)CPP
XVH)1R9
LWS)Z1T
HPK)BHN
63K)XPR
5SS)V93
V9J)F97
9MM)MFR
WWP)9SB
1WW)SBV
S4Q)3X8
W6T)P9B
22K)K8G
3XJ)5M5
8PN)2R1
SJ3)4D2
X7S)1V6
QV6)L6G
R3S)LYP
425)MB5
86H)HL6
31F)XZY
B7M)XS3
9DJ)7K5
DFL)F85
MJV)DTN
8LL)7T3
HDT)TCD
4Y4)2WP
GKB)QWF
98M)FNX
2ZW)81Q
4Z7)1FY
GXR)QJK
5YG)T49
C3M)R8R
4XK)P77
GMK)GGS
5BH)T9Q
"""


test1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""


@dataclass
class Node:
    name: str
    children: List["Node"]
    parent: Optional["Node"] = None

    def __init__(self, name: str):
        self.name = name
        self.parent = None
        self.children = []

    def __repr__(self):
        return f"{self.name} ({self.parent.name if self.parent else None})"

    def __hash__(self) -> int:
        return hash(self.name)


def parse1(inp: str) -> Dict[str, Node]:
    nodes = {}
    for line in inp.splitlines():
        parent, child = line.split(")")

        if parent not in nodes:
            nodes[parent] = Node(parent)
        if child not in nodes:
            nodes[child] = Node(child)

        nodes[child].parent = nodes[parent]
        if nodes[parent].children is None:
            nodes[parent].children = []

        nodes[parent].children.append(nodes[child])
    return nodes


# print(parse1(test1))


def count_orbits(nodes: Dict[str, Node]) -> int:
    total = 0
    for node in nodes.values():
        while node.parent:
            total += 1
            node = node.parent
    return total


print(count_orbits(parse1(input1)))

# part 2

test2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""


def find_path(nodes: Dict[str, Node], end1: str, end2: str) -> int:
    chain1: Set[str] = set()
    chain2: Set[str] = set()

    node1 = nodes[end1]
    c1 = 0
    counts1 = {}

    node2 = nodes[end2]
    c2 = 0
    counts2 = {}

    while node1.parent or node2.parent:
        if node1.parent:
            node1 = node1.parent
            counts1[node1] = c1
            c1 += 1
            chain1.add(node1.name)
        if node2.parent:
            node2 = node2.parent
            counts2[node2] = c2
            c2 += 1
            chain2.add(node2.name)

        inter = chain1.intersection(chain2)
        if inter != set():
            x = inter.pop()
            return counts1[nodes[x]] + counts2[nodes[x]]

    return 0


print(find_path(parse1(input1), "YOU", "SAN"))
