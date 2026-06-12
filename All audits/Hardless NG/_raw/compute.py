PRICE = 150.0  # blended avg price for whole-house filter / softener-alternative segment

# Monthly data: [imp_b, imp_t, clk_b, clk_t, atc_b, atc_t, pur_b, pur_t, search_vol]
# Order: May25..Apr26
T1 = [
 [39502,1991005,725,26381,40,3027,2,534,78960],
 [44433,1910164,872,26196,52,3163,2,534,76493],
 [61378,2597890,1061,31989,76,3899,5,634,101935],
 [57921,2385493,1039,29080,69,3255,3,511,91446],
 [61263,2027207,1274,25650,85,3072,3,528,78265],
 [51629,2288696,933,29194,55,3189,1,554,88574],
 [27268,2566625,367,31828,14,3596,0,583,99843],
 [35734,2325984,524,31428,27,3265,1,576,88861],
 [32389,2623253,465,35945,29,4271,2,680,100613],
 [29542,2294200,377,29938,32,3663,1,625,88042],
 [21534,2342600,237,33211,14,3659,1,650,89758],
 [22508,2186824,300,30219,14,3412,0,575,83332],
]
T2 = [
 [7471,2136148,119,31879,8,5208,0,1903,79967],
 [4821,2020953,60,30303,2,4703,0,1825,77098],
 [7533,2594199,90,37628,7,5793,0,2170,97436],
 [4745,2363303,59,33665,2,5117,0,1972,85992],
 [6319,2084689,92,30822,8,4901,1,1790,78492],
 [4723,2458742,56,34454,7,5305,0,1942,90681],
 [1710,2559515,18,34288,0,5177,0,1740,94043],
 [8290,2273451,69,30722,3,4689,1,1700,81728],
 [1838,2551949,31,35343,2,5171,0,1796,90691],
 [1404,2334343,15,32265,0,4995,0,625,82252],
 [917,2529189,11,34785,0,5707,0,2097,90255],
 [1132,2367513,14,31947,2,5159,1,1940,82714],
]
T3 = [
 [11011,15903619,177,223422,11,64518,0,25023,646931],
 [7806,16487156,149,229024,11,68279,0,24783,675091],
 [11156,21128849,168,279695,16,80405,0,28865,833681],
 [8266,19291216,126,258438,10,73493,0,27872,756778],
 [7377,16743470,157,229380,12,67648,0,26140,665575],
 [6872,17488138,130,235018,9,68636,0,27164,687411],
 [3807,18861395,54,241075,4,70086,0,26762,729830],
 [8865,17432558,114,229831,4,67638,1,26432,676056],
 [2056,19605122,35,265733,3,82659,0,31628,764027],
 [1404,16499722,15,227675,3,70406,0,27574,640263],
 [2204,15368225,36,185873,1,58079,0,22258,594445],
 [2438,13863959,43,172901,3,51815,0,21034,535741],
]

def agg(rows):
    s = [sum(r[i] for r in rows) for i in range(9)]
    return s

def block(name, rows, cap):
    n = len(rows)
    s = agg(rows)
    imp_b,imp_t,clk_b,clk_t,atc_b,atc_t,pur_b,pur_t,sv = s
    print(f"\n=== {name} ({n} months) ===")
    print(f"avg monthly search volume: {sv/n:,.0f}")
    print(f"avg monthly market cart-adds: {atc_t/n:,.0f}")
    print(f"avg monthly market purchases: {pur_t/n:,.0f}")
    print(f"est market size $/mo (ATC x ${PRICE:.0f}): ${(atc_t/n)*PRICE:,.0f}")
    print(f"-- shares (vol-weighted) --")
    print(f"impression share: {imp_b/imp_t*100:.2f}%  (cap ~{cap})")
    print(f"click share:      {clk_b/clk_t*100:.2f}%")
    print(f"cart share:       {atc_b/atc_t*100:.2f}%")
    print(f"purchase share:   {pur_b/pur_t*100:.2f}%")
    print(f"-- rates brand vs industry (vol-weighted) --")
    print(f"CTR:  {clk_b/imp_b*100:.2f}% vs {clk_t/imp_t*100:.2f}%")
    print(f"ATC:  {atc_b/clk_b*100:.2f}% vs {atc_t/clk_t*100:.2f}%")
    print(f"CVR:  {pur_b/clk_b*100:.3f}% vs {pur_t/clk_t*100:.2f}%")
    print(f"base: clk_b={clk_b} atc_b={atc_b} pur_b={pur_b}")

print("################ 12-MONTH (May25-Apr26): market sizing + annual rates ################")
block("TIER 1 (salt-free softener)", T1, "8-9% (1 product)")
block("TIER 2 (whole house filter)", T2, "8-9% (1 product)")
block("TIER 3 (broad filter/purifier)", T3, "8-9% (1 product)")

print("\n\n################ 3-MONTH (Feb-Apr26): current share + blocker rates ################")
block("TIER 1 (salt-free softener)", T1[-3:], "8-9%")
block("TIER 2 (whole house filter)", T2[-3:], "8-9%")
block("TIER 3 (broad filter/purifier)", T3[-3:], "8-9%")

print("\n\n################ TIER 1 monthly impression share trend ################")
for i,r in enumerate(T1):
    lbl = ["May25","Jun25","Jul25","Aug25","Sep25","Oct25","Nov25","Dec25","Jan26","Feb26","Mar26","Apr26"][i]
    print(f"{lbl}: imp_share={r[0]/r[1]*100:.2f}%  CTR={r[2]/r[0]*100:.2f}%")

# Total P0 (all tiers) 12-mo
print("\n\n################ TOTAL P0 (all 3 tiers, 12-mo avg) ################")
allrows = T1+T2+T3
# sum per-month across tiers isn't right for search volume (different queries, additive ok since no overlap)
s1,s2,s3 = agg(T1),agg(T2),agg(T3)
tot_sv = (s1[8]+s2[8]+s3[8])/12
tot_atc = (s1[5]+s2[5]+s3[5])/12
tot_pur = (s1[7]+s2[7]+s3[7])/12
print(f"avg monthly search volume: {tot_sv:,.0f}")
print(f"avg monthly market cart-adds: {tot_atc:,.0f}")
print(f"avg monthly market purchases: {tot_pur:,.0f}")
print(f"est total market size $/mo: ${tot_atc*PRICE:,.0f}")
