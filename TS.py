from bit import Key

# สร้างคีย์จาก private key
private_key = "YOUR_PRIVATE_KEY"
key = Key(private_key)

# ส่ง Bitcoin
tx_hash = key.send([("RECIPIENT_ADDRESS", 0.001, "btc")])

print(f"Transaction sent! TX ID: {tx_hash}")