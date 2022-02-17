## Metachange

A very simple script and template for making use of metaboss for updating Metaplex metadata.

* metaboss - https://metaboss.rs
* Python 3

### Download metadata
```metaboss snapshot mints -c <candy-machine-address> -o metadata```

### Make Changes to metadata template
Edit metachange.py

### Start Metachange
```python metachange.py```

### Update ALL
```metaboss update data-all --keypair <keypair> --data-dir build --rpc <rpc> -t 120```

### Update 1
```metaboss update data --keypair <keypair> --account BLpAXt8RoJeAwPzAjsognQKA3GbBRQBWrCi7NJzzjEjs --new-data-file <metadata> --rpc <rpc>```

### Legend
```
<rpc> -> https://api.devnet.solana.com
<keypair> -> ./path/to/keypair
<metadata> -> ./metadata/address.json
```


### FAQ

1. Getting errors because of RPC response?
lease a node from quiknode.pro
