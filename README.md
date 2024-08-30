![image](https://github.com/user-attachments/assets/979be605-4705-4b8c-942b-62a9de7c20cc)



# Empe Desktop Wallet

## Project Description:

This project allows users to quickly create a wallet on the Empeiria network, log in with existing wallets, transfer tokens, and perform delegation transactions to active validators.

## Features:

- **Create New Wallet:** You can create a new Empe wallet with a single click.
- **Log In with Existing Wallet:** Log in to your wallet using an existing private key.
- **Transfer Between Wallets:** Perform token transfers to another Empe wallet.
- **Validator Delegation:** Browse the list of active validators and make delegations.

## Installation Guide

This guide provides step-by-step instructions on how to install and run the application.

### 1. Prerequisites

- **Python 3.10 or above:** Python version 3.10 or higher is required to run this application.
- **pip:** The Python package manager, pip, should also be installed. It typically comes with Python.

### 2. Required Libraries

The following Python libraries are required for this project:

- **tkinter:** Python's GUI interface module (comes by default).
- **requests:** Used for sending HTTP requests.
- **httpx:** A fast and modern HTTP client.
- **cosmospy-protobuf:** Used for handling transactions on Cosmos SDK-based blockchains.
- **mospy:** Used for managing wallets and transactions on the Empe network.

### 3. Installation Steps

**Clone the Repository:**

```bash
git clone https://github.com/username/Empe-Desktop-Wallet.git
cd Empe-wallet
```
### Install Required Libraries:

You can install all the necessary libraries with the following command:

```bash
pip install -r requirements.txt

```
The content of the requirements.txt file may look like this:

```bash
requests
httpx
cosmospy-protobuf
mospy


```
### 4. Run the Wallet Application
Run the application from the terminal or command line with the following command:

```bash
python main.py

```
This command will start the wallet application and allow the user to interact with the graphical user interface (GUI).

# Python File Descriptions

## `main.py`
- **Function**: The entry point of the application. Creates the main window and presents the user with options to create a new wallet or log in with an existing wallet.

## `mainscreen.py`
- **Function**: Manages the main screen of the application. Users can create a new wallet or log in with an existing wallet from here.

## `newwallet.py`
- **Function**: Creates a new Empe wallet for the user and displays the wallet address and private key.

## `login_prvtkey.py`
- **Function**: Allows the user to log in with an existing private key. If the private key is valid, access to the user's wallet is granted.

## `walletaction.py`
- **Function**: Manages the main operations related to the wallet (updates balances, performs transfer transactions, and makes delegations to validators). Defines buttons and functions for various operations in the user interface.

## `delegate.py`
- **Function**: Allows the user to delegate tokens to a specific validator address.

## `transfer.py`
- **Function**: Enables the user to transfer tokens to another wallet.

## `logo.png`
- **Function**: The logo of the application, displayed in the graphical user interface.
