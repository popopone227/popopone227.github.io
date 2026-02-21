# レアリティごとの値段
price = {
    "common": 1,
    "uncommon": 3,
    "rare": 10,
    "epic": 250,
    "mythical": 5000,
    "legendary": 15000,
    "gem": 30000,
    "special": 6000,
}

# 捕まえた数を入力
common_total = 0  # コモンの総所持数

while True:
    common = int(input("捕まえたcommonの数（終了は0）: "))
    if common == 0:
        break

    common_total += common
    print("現在のcommon総数:", common_total)

uncommon_total = 0

while True:
    uncommon = int(input("捕まえたuncommonの数（終了は0）: "))
    if uncommon == 0:
        break

    uncommon_total += uncommon
    print("現在のuncommon総数:", uncommon_total)

rare_total = 0
while True:
    rare = int(input("捕まえたrareの数（終了は0）: "))
    if rare == 0:
        break

    rare_total += rare
    print("現在のrareの総数", rare_total)

epic_total = 0
while True:
    epic = int(input("捕まえたepicの数（終了は0）: "))
    if epic == 0:
        break

    epic_total += epic
    print("現在のepicの総数", epic_total)

mythical_total = 0
while True:
    mythical = int(input("捕まえたmythicalの数（終了は0）: "))
    if mythical == 0:
        break

    mythical_total += mythical
    print("現在のmythicalの総数", mythical_total)

legendary = int(input("legendaryの数は？: "))
gem = int(input("gemの数は？: "))
special = int(input("specialの数は？: "))

# 合計金額を計算
total = (
    common_total * price["common"] +
    uncommon_total * price["uncommon"] +
    rare_total * price["rare"] +
    epic_total * price["epic"] +
    mythical_total * price["mythical"] +
    legendary * price["legendary"] +
    gem * price["gem"] +
    special * price["special"]

)

print("合計金額:", total, "円")

