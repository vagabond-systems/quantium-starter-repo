#!/usr/bin/env python3
"""
Soul Foods Data Processing Script
Processes transaction data to extract Pink Morsel sales by date and region.
"""

import pandas as pd
import sys
import os

def main():
    print("=" * 60)
    print("Soul Foods Data Processing")
    print("=" * 60)
    
    # Define the file names
    files_name = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
    
    # Check if data folder exists
    if not os.path.exists('data'):
        print("ERROR: 'data' folder not found!")
        print("Please ensure you're running this script from the correct directory.")
        sys.exit(1)
    
    try:
        # Read and combine all CSV files
        print("\n1. Reading CSV files...")
        data_frames = [pd.read_csv('data/' + file) for file in files_name]
        data_combined = pd.concat(data_frames, ignore_index=True)
        print(f"   ✓ Combined data shape: {data_combined.shape}")
        
        # Filter for Pink Morsel only
        print("\n2. Filtering for Pink Morsel...")
        data_filtered_by_product = data_combined[data_combined['product'].str.lower() == 'pink morsel']
        print(f"   ✓ Filtered data shape: {data_filtered_by_product.shape}")
        
        # Clean the price field (remove $ and commas, convert to float)
        print("\n3. Cleaning price data...")
        data_filtered_by_product = data_filtered_by_product.copy()
        data_filtered_by_product['price'] = data_filtered_by_product['price'].str.replace('$', '', regex=False).str.replace(',', '').astype(float)
        print("   ✓ Price data cleaned")
        
        # Calculate sales (price * quantity)
        print("\n4. Calculating sales...")
        data_filtered_by_product['sales'] = data_filtered_by_product['price'] * data_filtered_by_product['quantity']
        print("   ✓ Sales calculated")
        
        # Select only the required fields: sales, date, region
        print("\n5. Selecting required fields...")
        output_data = data_filtered_by_product[['sales', 'date', 'region']]
        print("   ✓ Fields selected: sales, date, region")
        
        # Save to output file
        print("\n6. Saving output file...")
        output_data.to_csv('data/pink_morsel_sales.csv', index=False)
        print("   ✓ Output saved to data/pink_morsel_sales.csv")
        
        # Display summary statistics
        print("\n" + "=" * 60)
        print("Processing Summary")
        print("=" * 60)
        print(f"Total rows processed: {output_data.shape[0]}")
        print(f"Total sales: ${output_data['sales'].sum():,.2f}")
        print(f"Average sale: ${output_data['sales'].mean():,.2f}")
        print(f"Regions: {', '.join(output_data['region'].unique())}")
        print(f"Date range: {output_data['date'].min()} to {output_data['date'].max()}")
        
        print("\n" + "=" * 60)
        print("✓ Processing complete!")
        print("=" * 60)
        
    except FileNotFoundError as e:
        print(f"\nERROR: File not found - {e}")
        print("Please ensure all CSV files are in the 'data' folder.")
        sys.exit(1)
    except Exception as e:
        print(f"\nERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()