# Hash Tables
![hash table image](https://d33wubrfki0l68.cloudfront.net/87075beeda9ac5cf3bc104aaca45d231ef42aaea/56f14/img/blog/data-structures/hash-tables/hash-table.png)
### Overview
In previous presenatations, we covered the basic structure of hash tables and the utility of the hash function extensively. In our final presentation, we expand upon the topic of hash tables delving deeper into the hash function. We will demo a common use case in cybersecurity using the popular SHA-256 hash function.   

### Types and Qualities of Hash Functions 
There are generally two types of hash functions: **cryptographic** and **non-cryptographic**. The hash tables we have discussed until now have been implementing non-cryptographic hash functions, as we were only concerned with speed and didn't discuss security. Because non-cryptographic hash functions are meant for efficient search and retrieval, their main criteria are speed and collision resistance. Cryptogrpahic hash functions on the other hand, have more rigorous requirements. 

According to [Geekstogeeks.com](https://www.geeksforgeeks.org/cryptographic-hash-function-in-java/#), there are seven properties that make a cryptographic hash function effective:
1. Deterministic
2. Low computation time
3. Avalanche effect
4. One-way function
5. Collision resistant
6. Pre-image resistant
7. Second pre-image resistant

In our example, we use the SHA-256 hash function. 

### Code
Files:
- Hashing.ipynb: code demo
- common_passwords.txt
- hashes.txt
- input.txt (omitted from public repo: personal info)
- hash.png

In the Hashing.ipynb file, we explore some of the use cases for hashing, particularly with the common SHA-256. We hope to provide insight into how the data is stored, then shift gears to discuss how these measures may be outdone during security breaches and bring awareness to the cybersecurity implications and methods for protecting your personal information. 
