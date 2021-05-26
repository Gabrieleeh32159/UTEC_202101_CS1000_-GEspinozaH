print("Sistema Binario: De binario a decimal")
print("=" * 40)
num = '0b110'
decimal = int(num, 2)
print("{} en decimal es {}".format(num, decimal))
print()
print("Sistema Binario: De decimal a binario")
print("=" * 40)
num = 18
enBinario = bin(num)
print("{} en binario es {}".format(num, enBinario))
print()
print("Sistema octal: De octal a decimal")
print("=" * 40)
num = '0o10'
decimal = int(num, 8)
print("{} en decimal es {}".format(num[2:], decimal))
print()
print("Sistema Octal: De decimal a octal")
print("="*40)
num = 101
enOctal = oct(num)
print("{} en octal es {}".format(num, enOctal[2:]))
