import tkinter as tk
from tkinter import messagebox
import pandas as pd
import bech32
import cosmospy
import mainscreen
import walletaction

def generate_empe_wallet():
    wallet = cosmospy.generate_wallet()
    private_key_hex = wallet["private_key"].hex()
    empe_address = convert_address(wallet["address"], "empe")
    return private_key_hex, empe_address

def convert_address(cosmos_address, new_prefix):
    _, data = bech32.bech32_decode(cosmos_address)
    if data is None:
        raise ValueError("Invalid address")
    empe_address = bech32.bech32_encode(new_prefix, data)
    return empe_address

def create_new_wallet(root):
    mainscreen.clear_content(root)
    frame = tk.Frame(root, bg='#1F0021')
    frame.pack(fill='both', expand=True)

    logo = tk.PhotoImage(file="logo.png")
    logo_label = tk.Label(frame, image=logo, bg='#1F0021')
    logo_label.image = logo
    logo_label.pack(pady=(20, 0))

    developer_info_label = tk.Label(frame, text="This application is developed by Coinsspor", font=('Arial', 10), bg='#1F0021', fg='white')
    developer_info_label.pack(pady=(0, 20))

    priv_key, empe_address = generate_empe_wallet()

    # Global değişkenlere cüzdan bilgilerini ve private key'i aktar
    walletaction.empe_address = empe_address
    walletaction.private_key = priv_key

    # Label styles
    label_style = {'font': ('Arial', 12), 'bg': '#1F0021', 'fg': 'white', 'anchor': 'center'}
    title_style = {**label_style, 'font': ('Arial', 12, 'bold', 'underline')}

    # Private Key
    tk.Label(frame, text="Private Key:", **{**title_style, 'fg': 'blue'}).pack(fill='x')
    tk.Label(frame, text=priv_key, **label_style).pack(fill='x')

    # empe Address
    tk.Label(frame, text="Empe Address:", **{**title_style, 'fg': 'orange'}).pack(fill='x')
    tk.Label(frame, text=empe_address, **label_style).pack(fill='x')

    # Buttons
    copy_button = tk.Button(frame, text="Copy Information", bg='#027bfe', fg='white', font=('Arial', 14, 'bold'), command=lambda: copy_info(root, priv_key, empe_address))
    copy_button.pack(fill='x', pady=10)

    back_button = tk.Button(frame, text="Back", bg='#027bfe', fg='white', font=('Arial', 14, 'bold'), command=lambda: mainscreen.show_main_screen(root))
    back_button.pack(side='left', fill='x', expand=True, padx=20, pady=20)

    next_button = tk.Button(frame, text="Next", bg='#027bfe', fg='white', font=('Arial', 14, 'bold'), command=lambda: walletaction.wallet_actions(root, empe_address, priv_key))
    next_button.pack(side='right', fill='x', expand=True, padx=20, pady=20)

def copy_info(root, priv_key, empe_address):
    info_text = f"Private Key: {priv_key}\nEmpe Address: {empe_address}"
    root.clipboard_clear()
    root.clipboard_append(info_text)
    messagebox.showinfo("Copied", "Wallet information copied to clipboard!")
