class DataClass:

    import pandas as pds

    list_csv_files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']

    list_data_frames = []

    for input_data in list_csv_files:

        data_frame = pds.read_csv(input_data)

        data_frame = data_frame[data_frame['product'].isin(['pink morsel'])]

        data_frame['price'] = data_frame['price'].str.replace('$', '')

        data_frame['price'] = data_frame['price'].astype(float)

        data_frame['quantity'] = data_frame['quantity'].astype(float)

        data_frame = data_frame.sort_values(by='date', ascending=True)

        data_frame.insert(loc=3, column='sales', value=data_frame['price'] * data_frame['quantity'])

        data_frame['price'] = '$' + data_frame['price'].astype(str)

        data_frame['sales'] = '$' + data_frame['sales'].astype(str)

        data_frame = data_frame[['sales', 'date', 'region']]

        data_frame = data_frame.reset_index(drop=True)

        list_data_frames.append(data_frame)

    combined_data_frame = pds.concat(objs=list_data_frames, axis=0)  # axis=0 means vertical stack || axis=1 means horizontal join
    combined_data_frame = combined_data_frame.reset_index(drop=True)
    print(combined_data_frame.to_csv(sep='|'))
        
    # Optional: Implement separate data_frames per region
    data_frame_north = data_frame[data_frame['region'].isin(['north'])]

    data_frame_south = data_frame[data_frame['region'].isin(['south'])]

    data_frame_east = data_frame[data_frame['region'].isin(['east'])]

    data_frame_west = data_frame[data_frame['region'].isin(['west'])]

    regionalised_data_frames = [data_frame_north, data_frame_south, data_frame_east, data_frame_west]

    for individual_table in regionalised_data_frames:

        individual_table = individual_table.reset_index(drop=True)

        #print(individual_table.to_string())

        new_csv_files = individual_table.to_csv()