import pandas as pd

url = "https://www.guttmacher.org/state-policy/explore/sex-and-hiv-education"

tables = pd.read_html(url)

df = tables[0]

# Replace 'X' with 1 and blanks with 0 in yes/no columns
df["Sex ed mandated"] = df["Sex ed mandated"].replace("X", 1)
df["Sex ed mandated"] = df["Sex ed mandated"].fillna(0)
df["Sex ed mandated"] = df["Sex ed mandated"].replace("", 0)

df["HIV ed mandated"] = df["HIV ed mandated"].replace("X", 1)
df["HIV ed mandated"] = df["HIV ed mandated"].fillna(0)
df["HIV ed mandated"] = df["HIV ed mandated"].replace("", 0)

df["Ed must be medically accurate"] = df["Ed must be medically accurate"].replace("X", 1)
df["Ed must be medically accurate"] = df["Ed must be medically accurate"].fillna(0)
df["Ed must be medically accurate"] = df["Ed must be medically accurate"].replace("", 0)

df["Ed must be age-appropriate"] = df["Ed must be age-appropriate"].replace("X", 1)
df["Ed must be age-appropriate"] = df["Ed must be age-appropriate"].fillna(0)
df["Ed must be age-appropriate"] = df["Ed must be age-appropriate"].replace("", 0)

df["Ed must include contraception"] = df["Ed must include contraception"].replace("X", 1)
df["Ed must include contraception"] = df["Ed must include contraception"].fillna(0)
df["Ed must include contraception"] = df["Ed must include contraception"].replace("", 0)

df["Ed must cover consent"] = df["Ed must cover consent"].replace("X", 1)
df["Ed must cover consent"] = df["Ed must cover consent"].fillna(0)
df["Ed must cover consent"] = df["Ed must cover consent"].replace("", 0)

df["Ed must cover healthy relationships"] = df["Ed must cover healthy relationships"].replace("X", 1)
df["Ed must cover healthy relationships"] = df["Ed must cover healthy relationships"].fillna(0)
df["Ed must cover healthy relationships"] = df["Ed must cover healthy relationships"].replace("", 0)


df.to_csv("Sex_Policies.csv", index=False)

