# envy
print environment variables

```bash
    python3 envy.py
```

OR

```bash
    ./envy.py
```


## Compile with nuitka && Install


### Install nuitka
```bash
    pip3 install nuitka 
```

### Compile && move to bin directory
```bash
    python3 -m nuitka envy.py --follow-imports --show-progress -o build/envy
    sudo mv build/envy /usr/bin
```

