# Auction-Based Conflict Management System

## Overview
This system provides a solution for resolving conflicts between xApps (cross applications) in a network environment. It utilizes an auction-based mechanism to determine the optimal parameter values for conflicting parameters, allowing xApps to submit bids for various values they desire to set.

## Features
- Allows xApps to submit multiple bids for conflicting parameters.
- Implements an auction algorithm to determine the final winner for each parameter.
- Supports multiple xApps with multiple conflicting parameters.
- Provides flexibility in defining objectives and parameters for each xApp.
Limitations
- The current auction algorithm is too simplistic and does not assure Incentive compatibility, individual rationality, and budget balance.
## Input Data
The input data for the auction algorithm is provided in a CSV file. Each row represents a bid submitted by an xApp for a particular parameter. The CSV file should have the following format:

- **Columns**:
  - `xApp`: Name of the xApp submitting the bid.
  - `ICP (Input Control Parameter)`: The parameter for which the bid is submitted.
  - `Desired Value`: The desired value for the parameter.
  - `Bid Amount`: The amount bid by the xApp for the desired value.

- **Example**:
    xApp,ICP (Input Control Parameter),Desired Value,Bid Amount
    MLB,TXP,10,50
    MLB,TXP,15,30
    MLB,TTT,5,20
    CCO,TXP,100,70
    CCO,TXP,90,40
    CCO,RET,10,60
    ES,TXP,50,80
    MRO,TXP,20,30
    MRO,TXP,25,50
    MRO,CIO,3,40

## Usage
1. **Input Data**: Define the bids data for xApps and their desired parameter values in a CSV file following the specified format.

2. **Auction Algorithm**: Run the provided Python notebook (`auction_conflict_resolution.py`). The notebook reads the bids data from the CSV file, conducts the auction, and determines the winning bids for each parameter.

3. **Output**: The auction algorithm outputs the winning bids for each parameter, along with the corresponding xApp name and bid amount. These results can be used to resolve conflicts between xApps effectively.

## Example
An example CSV file (`xapps_info.csv`) and Python notebook (`auction_conflict_resolution.py`) are provided to demonstrate the usage of the system. You can customize the bids data according to your network environment and objectives.
## References

- Abdul Wadud, Fatemeh Golpayegani, and Nima Afraz. "Conflict Management in the Near-RT-RIC of Open RAN: A Game Theoretic Approach." 2023. [arXiv:2311.13389](https://arxiv.org/abs/2311.13389)

## Contributing
If you would like to contribute to this project or have any suggestions for improvements, please feel free to open an issue or a pull request.


