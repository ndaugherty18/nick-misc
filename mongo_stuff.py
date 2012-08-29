from pymongo import ReplicaSetConnection, Connection, ReadPreference

mongo_connection = Connection()
db = mongo_connection.adserver_sync_database
'''
imp_stats_ads = db.impression_stats.find({"ad_id" : {"$in" : ["02c3402dce70cf4dabed1791c92824fd91e709973d26b18015f6a12735efeae8", "f96ce80a80fb6427fe45e227136a1a1d84f6b3cc6f4d155619ac0717c17ece1d", "b8e2951cae3e20fd28b81c26bf51ca9963aad419ecca0d76ef5c6b1fccbfa543", "c2e15ea0d6f9249e486bf17a5035d7ad57124e6b1f7cb810617e332ca7f7190c"]}, "page_id" : { '$in' : ["YGzA6", "R0dhy", "0Iatk", "O2dqc", "None"]}})
imp_totals_ads = {}
for stat in imp_stats_ads:
    if stat["ad_id"] in imp_totals_ads:
        imp_totals_ads[stat["ad_id"]] += stat["value"]
    else:
        imp_totals_ads[stat["ad_id"]] = stat["value"]
print imp_totals_ads["02c3402dce70cf4dabed1791c92824fd91e709973d26b18015f6a12735efeae8"]

imp_stats_ads2 = db.impression_stats.find({"_id.ad" : {"$in" : ["02c3402dce70cf4dabed1791c92824fd91e709973d26b18015f6a12735efeae8", "f96ce80a80fb6427fe45e227136a1a1d84f6b3cc6f4d155619ac0717c17ece1d", "b8e2951cae3e20fd28b81c26bf51ca9963aad419ecca0d76ef5c6b1fccbfa543", "c2e15ea0d6f9249e486bf17a5035d7ad57124e6b1f7cb810617e332ca7f7190c"]}, "_id.type" : {"$in" : ["gallery", "None"]}})
imp_totals_ads2 = {}
for stat in imp_stats_ads2:
    if stat["_id"]["ad"] in imp_totals_ads2:
        imp_totals_ads2[stat["_id"]["ad"]] += stat["value"]
    else:
        imp_totals_ads2[stat["_id"]["ad"]] = stat["value"]
print imp_totals_ads2

imp_totals_ads2["02c3402dce70cf4dabed1791c92824fd91e709973d26b18015f6a12735efeae8"] = imp_totals_ads["02c3402dce70cf4dabed1791c92824fd91e709973d26b18015f6a12735efeae8"]
combine_imp_stats = 0
for stat in imp_totals_ads2:
    combine_imp_stats += imp_totals_ads2[stat]
print combine_imp_stats/4
'''
'''
click_stats_ads = db.click_stats.find({"ad_id" : {"$in" : ["02c3402dce70cf4dabed1791c92824fd91e709973d26b18015f6a12735efeae8", "f96ce80a80fb6427fe45e227136a1a1d84f6b3cc6f4d155619ac0717c17ece1d", "b8e2951cae3e20fd28b81c26bf51ca9963aad419ecca0d76ef5c6b1fccbfa543", "c2e15ea0d6f9249e486bf17a5035d7ad57124e6b1f7cb810617e332ca7f7190c"]}})
click_totals_ad = {}
for stat in click_stats_ads:
    if stat["ad_id"] in click_totals_ad:
        if stat["type"] in click_totals_ad[stat["ad_id"]]:
            click_totals_ad[stat["ad_id"]][stat["type"]] += stat["value"]
        else:
            click_totals_ad[stat["ad_id"]][stat["type"]] = stat["value"]
    else:
        click_totals_ad[stat["ad_id"]] = {}
        click_totals_ad[stat["ad_id"]][stat["type"]] = stat["value"]
print click_totals_ad

click_stats_ads2 = db.click_stats.find({"_id.ad" : {"$in" : ["02c3402dce70cf4dabed1791c92824fd91e709973d26b18015f6a12735efeae8", "f96ce80a80fb6427fe45e227136a1a1d84f6b3cc6f4d155619ac0717c17ece1d", "b8e2951cae3e20fd28b81c26bf51ca9963aad419ecca0d76ef5c6b1fccbfa543", "c2e15ea0d6f9249e486bf17a5035d7ad57124e6b1f7cb810617e332ca7f7190c"]}})
click_totals_ad2 = {}
for stat in click_stats_ads2:
    if stat["_id"]["ad"] in click_totals_ad2:
        if stat["_id"]["type"] in click_totals_ad2[stat["_id"]["ad"]]:
            click_totals_ad2[stat["_id"]["ad"]][stat["_id"]["type"]] += stat["value"]
        else:
            click_totals_ad2[stat["_id"]["ad"]][stat["_id"]["type"]] = stat["value"]
    else:
        click_totals_ad2[stat["_id"]["ad"]] = {}
        click_totals_ad2[stat["_id"]["ad"]][stat["_id"]["type"]] = stat["value"]
print click_totals_ad2
click_totals_ad2["02c3402dce70cf4dabed1791c92824fd91e709973d26b18015f6a12735efeae8"] = click_totals_ad["02c3402dce70cf4dabed1791c92824fd91e709973d26b18015f6a12735efeae8"]
click_totals_ad2["02c3402dce70cf4dabed1791c92824fd91e709973d26b18015f6a12735efeae8"]["comment"] = 96
click_totals_ad2["f96ce80a80fb6427fe45e227136a1a1d84f6b3cc6f4d155619ac0717c17ece1d"]["comment"] = 160
click_totals_ad2["c2e15ea0d6f9249e486bf17a5035d7ad57124e6b1f7cb810617e332ca7f7190c"]["comment"] = 133
click_totals_ad2["b8e2951cae3e20fd28b81c26bf51ca9963aad419ecca0d76ef5c6b1fccbfa543"]["comment"] = 154

click_totals = {}
for stat in click_totals_ad2:
    click_totals[stat] = 0
    for t in click_totals_ad2[stat]:
        #if t != "gallery":
        click_totals[stat] += click_totals_ad2[stat][t]

print click_totals
'''
'''
all_imps = db.impression_stats.find({"e_secs" : {"$gte":1344236400, "$lt":1344322800}, "page_type" : "gallery", "page_id" : {"$ne" : "None"}})
all_imps_stats = {}
for stat in all_imps:
    if stat["page_id"] in all_imps_stats:
        all_imps_stats[stat["page_id"]] += stat["value"]
    else:
        all_imps_stats[stat["page_id"]] = stat["value"]

all_list = []
for k,v in all_imps_stats.iteritems():
    all_list.append((v,k))
all_list.sort()
all_list.reverse()

top_list = []
for v in all_list[:10]:
    top_list.append(v[1])


all_clicks = db.click_stats.find({"e_secs" : {"$gte":1344236400, "$lt":1344322800}, "page_type" : "gallery", "page_id" : { "$in" : top_list}})
all_clicks_stats = {}
for stat in all_clicks:
    if stat["page_id"] in all_clicks_stats:
        if stat["type"] in all_clicks_stats[stat["page_id"]]:
            all_clicks_stats[stat["page_id"]][stat["type"]] += stat["value"]
        else:
            all_clicks_stats[stat["page_id"]][stat["type"]] = stat["value"]
    else:
        all_clicks_stats[stat["page_id"]] = {}
        all_clicks_stats[stat["page_id"]][stat["type"]] = stat["value"]


all_clicks_avg = {}
page_count = 30
for stat in all_clicks_stats:
    for t in all_clicks_stats[stat]:
        if t in all_clicks_avg:
            all_clicks_avg[t] += all_clicks_stats[stat][t]
        else:
            all_clicks_avg[t] = all_clicks_stats[stat][t]

print all_clicks_avg, page_count

for stat in all_clicks_avg:
    all_clicks_avg[stat] = float(all_clicks_avg[stat])/page_count
print all_clicks_avg
'''

'''
imps = db.impression_stats.find({"e_secs" : { "$gte" :  1343026800, "$lt" : 1343113200}})
imp_obj = {}
for stat in imps:
    if stat["page_id"] in imp_obj:
        imp_obj[stat["page_id"]] += stat["value"]
    else:
        imp_obj[stat["page_id"]] = stat["value"]

top_list = []
for k,v in imp_obj.iteritems():
    top_list.append((v,k))
top_list.sort()
top_list.reverse()
print top_list[:3]
'''


domains = db.impression_domains.find({"page_id" : "lVAEf", "e_secs" : { "$gte" :  1343026800, "$lt" : 1343113200}})
total = 0
obj = {}
for stat in domains:
    if stat["from_domain"] in obj:
        obj[stat["from_domain"]] += stat["value"]
        total += stat["value"]
    else:
        obj[stat["from_domain"]] = stat["value"]
        total += stat["value"]

top_list = []
for k,v in obj.iteritems():
    top_list.append((v,k))
top_list.sort()
top_list.reverse()
print top_list[:100]
print "TOTAL", total

