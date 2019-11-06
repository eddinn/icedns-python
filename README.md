# icedns-python

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0f1758b92be64207902ecc324608372b)](https://www.codacy.com/manual/Eddinn/icedns-python?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=eddinn/icedns-python&amp;utm_campaign=Badge_Grade) [![CircleCI](https://circleci.com/gh/eddinn/icedns-python.svg?style=svg)](https://circleci.com/gh/eddinn/icedns-python) ![GitHub](https://img.shields.io/github/license/eddinn/icedns-python)

Script to reverse lookup an IP address against .iceland.rix.is to see if it resolves to be an Icelandic IP

---

## Requirements

Python >= 3.3

### Usage

```bash
python3 icedns.py ipaddress

# OR

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
