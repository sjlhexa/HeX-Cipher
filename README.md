# HeX-Cipher

Encrypt and decrypt messages with a simple substitution cipher

Supports both GUI as well as CLI


## Authors

- [@sjlhexa](https://www.github.com/sjlhexa)


## Deployment

GUI =>
```bash
  python main.py
```

CLI =>
```bash
  python main.py <password> <shift> [option (if not encrypt)]
```

Options:
```bash

  -h, --help          show this help message and exit
  -u, --unscramble    Unscramble a message
  -s, --super-sneaky  Replace spaces with $@
  encrypt : by default 
```
## Input

* TEXT to Encode/Decode
* Magic Number(by default 7)
* Want to remove spaces or not



## Screenshots

![HeX Cipher](https://github.com/user-attachments/assets/5f0e0f85-3e47-4205-aebe-53e558a74483)

## Example CLI:

Encrypt a message:

```bash
    python3 main.py "Hello, World!" 7
```

Decrypt a message:
```bash
    python3 main.py "Olssv, Dvysk!" 7 -u
```

Use super sneaky mode (replace spaces):
```bash
    python3 main.py "Hello World" 7 -s
```

Get help:
```bash
    python3 main.py -h
```
