<h1 align="center">
  <br>
  <a href="https://github.com/Pawan-Yaduveer/HashBreaker.git"><img src="https://image.ibb.co/bSwkMe/bitmap.png" alt="HashBreaker"></a>
  <br>
  HashBreaker
  <br>
</h1>

<h4 align="center">Why crack hashes when you can bust them?</h4>

<p align="center">
  <a href="https://github.com/s0md3v/Hash-Buster/releases">
    <img src="https://img.shields.io/github/release/s0md3v/Hash-Buster.svg">
  </a>
  <a href="https://github.com/s0md3v/Hash-Buster/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed-raw/s0md3v/Hash-Buster.svg">
  </a>
</p>

<!-- Center the demo image -->
<p align="center">
  <img src="https://i.ibb.co/6c7xpJXN/Screenshot-2025-04-28-014852.png" alt="demo">
</p>

## Features
- Automatic hash type identification
- Supports MD5, SHA1, SHA256, SHA384, SHA512
- Can extract & crack hashes from a file
- Can find hashes from a directory, recursively
- Multi-threading

## Insallation & Usage
> **Note:** HashBreaker isn't compatible with python2, run it with python3 instead.
> Also, HashBreaker uses some APIs for hash lookups, check the source code if you are paranoid.

HashBreaker can be run directly from the python script but I highly suggest you to install it with `make install`

After the installation, you will be able to access it with `buster` command.

### Cracking a single hash

You don't need to specify the hash type. HashBreaker will identify and *crack* it under 3 seconds.

**Usage:** `buster -s <hash>`
### Finding hashes from a directory

Yep, just specify a directory and HashBreaker will go through all the files and directories present in it, looking for hashes.

**Usage:** `buster -d /root/Documents`
### Cracking hashes from a file

HashBreaker can find your hashes even if they are stored in a file like this
```
simple@gmail.com:21232f297a57a5a743894a0e4a801fc3
{"json@gmail.com":"d033e22ae348aeb5660fc2140aec35850c4da997"}
surrondedbytext8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918surrondedbytext
```

**Usage:** `buster -f /root/hashes.txt`

### Specifiying number of threads

Multi-threading can incredibly minimize the overall speed when you have a lot of hashes to crack by making requests in parallel.

`buster -f /root/hashes.txt -t 10`

### License
HashBreaker is licensed under [MIT License](https://github.com/Pawan-Yaduveer/HashBreaker/blob/main/LICENSE).
