# icedns-python

Script to reverse lookup an IP address against .iceland.rix.is to see if it resolves to be an Icelandic IP

---

## Requirements

Python >= 3.5

### Usage

```bash
python3 icedns.py ipaddress
chmod a+x icends.py
./icedns.py ipaddress
```

E.g: To see if 92.43.192.120 resolves against .iceland.rix.is

```bash
# Running this:
./icedns.py 92.43.192.120
# Returns:
92.43.192.120 is an .is IP
```
