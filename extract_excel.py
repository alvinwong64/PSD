import pandas as pd
import os
from tqdm import tqdm

# Assuming your data is in a DataFrame df
# You can read your Excel file into a DataFrame using pd.read_excel('your_file.xlsx')
# For this example, let's create a sample DataFrame

main_dir = r"D:\alvin\ultralytics\runs\segment\PSD_scrach"
result = r"filter3.xlsx"
files= "results.csv"
# columns = ['   metrics/precision(M)',
#        '      metrics/recall(M)', '     metrics/mAP_0.5(M)',
#        'metrics/mAP_0.5:0.95(M)']
columns = ['   metrics/precision(B)',
       '      metrics/recall(B)', '       metrics/mAP50(B)',
       '    metrics/mAP50-95(B)']
df_out = pd.DataFrame()
df_out1 = pd.DataFrame()
df_out2 = pd.DataFrame()
df_out3 = pd.DataFrame()
check=False
for folder_path, _, file_names in os.walk(main_dir):


    for filename in tqdm(file_names):

        if filename == files:
            
            check=True
            file_path = os.path.join(folder_path, filename)
            print(file_path)
            df = pd.read_csv(file_path)
            # print(df)
            # print(df.columns)
            indices_to_extract = [i for i in range(9, len(df)+1, 10)]
            result_df1 = df.loc[indices_to_extract,columns[0]]
            result_df2 = df.loc[indices_to_extract,columns[1]]
            result_df3 = df.loc[indices_to_extract,columns[2]]
            result_df4 = df.loc[indices_to_extract,columns[3]]

            df_out =pd.concat([df_out, result_df1], ignore_index=True,axis=1)
            df_out1 =pd.concat([df_out1, result_df2], ignore_index=True,axis=1)
            df_out2 =pd.concat([df_out2, result_df3], ignore_index=True,axis=1)
            df_out3 =pd.concat([df_out3, result_df4], ignore_index=True,axis=1)

    # print(df_out)
    # print(df_out1)
    # print(df_out2)
    # print(df_out3)
    if check:
        result_path= file_path.replace(files,result)
        with pd.ExcelWriter(result_path) as writer:
            df_out.to_excel(writer, sheet_name='Precision', index=False , header=False)
            df_out1.to_excel(writer, sheet_name='Recall', index=False, header=False)
            df_out2.to_excel(writer, sheet_name='map50', index=False, header=False)
            df_out3.to_excel(writer, sheet_name='map50-95', index=False, header=False)




# Extract rows with indices 1, 10, 20, ...
# df_out.to_csv(result_path, index=False)


# Print the result
# print(result_df)
