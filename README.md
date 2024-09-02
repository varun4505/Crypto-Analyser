# Crypto Analyser Readme

## Overview
Crypto Analyser is a Python-based cryptocurrency price tracker and data visualization tool. This project uses the `cryptocompare` API to fetch live cryptocurrency data and `matplotlib` for real-time graph plotting. The tool provides insights into various cryptocurrencies, including current prices, visual trends, and answers to frequently asked questions.

## Features
- **About Crypto Analyser:** Provides an overview of the project and explains how it functions.
- **Current Prices:** Allows users to check the current price of a cryptocurrency in USD.
- **Frequently Asked Questions (FAQs):** Offers information about common cryptocurrency concepts like blockchain, public/private keys, and investing in cryptocurrencies.
- **Data Visualization:** Displays live price graphs for selected cryptocurrencies such as Bitcoin, Ethereum, Dogecoin, and others.
- **Price Comparison:** Plots real-time bar graphs comparing prices of different cryptocurrencies.
- **Trading Profit Calculator:** (To be added) Helps users calculate potential trading profits based on price differences.

## Prerequisites
- **Python 3.6+**
- **Libraries:** `cryptocompare`, `matplotlib`
  - Install the necessary libraries using:
    ```bash
    pip install cryptocompare matplotlib
    ```

## How to Use
1. **Run the Script:**
   Start the script, and the main menu will appear:
   ```
   =============================================
              CRYPTO ANALYSER
   *********************************************
   1 - About Cryptoanalyser
   2 - Current Prices
   3 - Frequently Asked Questions
   4 - Data Visualisation
   5 - Price Comparison with Bar graph
   6 - Trading Profit Calculator
   7 - Exit
   =============================================
   ```

2. **Select an Option:**
   - **Option 1: About Crypto Analyser**
     - Displays a brief description of the project.
   
   - **Option 2: Current Prices**
     - Enter the name of a cryptocurrency (e.g., BTC, ETH) to display its current price in USD and its full name.

   - **Option 3: FAQs**
     - Provides answers to frequently asked cryptocurrency questions. Topics include blockchain, cryptocurrency basics, public and private keys, and investment tips.

   - **Option 4: Data Visualization**
     - Visualizes live cryptocurrency price graphs for multiple coins (Bitcoin, Ethereum, Dogecoin, etc.). Prices update in real-time every second.
     
   - **Option 5: Price Comparison with Bar Graph**
     - (To be added) Graphically compares prices of different cryptocurrencies.

   - **Option 6: Trading Profit Calculator**
     - (To be added) Calculates potential profits based on trading activity.
   
   - **Option 7: Exit**
     - Closes the application.

## Usage Example

To visualize the live price of Bitcoin:

1. Start the program.
2. Select `4 - Data Visualisation` from the menu.
3. Choose `1 - Bitcoin Live Price Graph`.
4. A live updating graph of Bitcoin prices in USD will be displayed.

## FAQ Section Details
Crypto Analyser includes an extensive FAQ section with information on various cryptocurrency-related topics. This can be accessed by selecting option `3` from the main menu.

## Known Issues
- Ensure stable internet connection for fetching live data from the cryptocompare API.
- The program might experience delays if there are network issues or high API response times.

## License
This project is licensed under the MIT License.
