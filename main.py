import pandas as pd
from prettytable import PrettyTable 

def printTable(df):
    table = PrettyTable()
    headers = []
    for cols in df.columns:
        headers.append(cols)
    table.field_names = headers
    for i in range(0, len(df)):
        row = df.loc[i].values.flatten().tolist()
        table.add_row(row)
    print(table)

def getWinners(df, n):
    sub_df = df[['Rank', 'NFT Name', 'Kills']]
    w_df = sub_df.iloc[0:n]
    return w_df

def changeName(df, i):
    #0xf954 = MFER
    #0x555d = WG
    nft = df.at[i, "NFT"]
    nft_type = nft[0:6]
    nft_name = ""
    end = len(nft) - 1
    while nft[end] != "/":
        nft_name += nft[end]
        end-=1
    nft_name = nft_name[::-1]
   
    if nft_type == "0xf954":
        nft_type = "MFER "

    elif nft_type == "0x555d":
        nft_type = "WG "

    else:
        nft_type = "Unknown "
    
    name = nft_type + "#" + nft_name
    return name

def formatting(df):
    df.rename(columns={"Game": "Rank"}, inplace = True) #renames Games column to rank
    
    for i in range(len(df)):
        df.at[i, "Rank"] = i+1

        if str(df.at[i, "NFT Name"]) == "nan":
            df.at[i, "NFT Name"] = changeName(df, i)
            df.at[i, "Tier"] = "Passport"
    
def main():
    df = pd.read_csv("24_may.csv", skiprows= 0, nrows=100) #load pit game CSV
    formatting(df)

    df.to_csv("Game_Results_Full_24_MAY.csv", encoding='utf-8', index=False) #saves the formatted data frame to a csv
    #Change the file name as you wish (file name is first arg)
    
    w_df = getWinners(df, 10)
    w_df.to_csv("Game_Results_24_MAY.csv", encoding='utf-8', index=False)

    printTable(w_df) #print ascii table of winners then just copy and paste into webhook webiste with embedd

if __name__ == "__main__":
    main()