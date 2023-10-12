# Hash Tables
![hash table image](https://d33wubrfki0l68.cloudfront.net/87075beeda9ac5cf3bc104aaca45d231ef42aaea/56f14/img/blog/data-structures/hash-tables/hash-table.png)
### Overview
In previous presenatations, we covered the basic structure of hash tables and the utility of the hash function extensively.
In our final presentation, we expand upon the topic of hash tables delving deeper into the hash function. Because there are an infinite amount of hash functions, there are equally as many use cases for them. We will demo a common use case in cybersecurity using the popular SHA-256 hash function.   

### Types and Qualities of Hash Functions 
There are generally two types of hash functions: **cryptographic** and **non-cryptographic**. The hash tables we have discussed until now have been implementing non-cryptographic hash functions, as we were only concerned with speed and didn't discuss security. Because non-cryptographic hash functions are meant for efficient search and retrieval, their main criteria are speed and collision resistance. Cryptogrpahic hash functions on the other hand, have more rigorous requirements. 

According to [Geekstogeeks.com](https://www.geeksforgeeks.org/cryptographic-hash-function-in-java/#), there are six criteria for a cryptographic hash function:
1. It is deterministic
2. 

### The Code
File structure:
- Hashing.ipynb: code demo
- common_passwords.txt
- hashes.txt
- input.txt (omitted from public repo: personal info)
- hash.png
Our demo 
Hashing.ipynb seeks to explore some of the use cases for hashing, particularly with the common SHA-256. It provides insight into how the data is stored, but then shifts gears to talk about how these measures may not help during security breaches and bring awareness to the cybersecurity implications.
