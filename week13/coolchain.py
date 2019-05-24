from pwn import *
import sys
from paddingoracle import BadPaddingException, PaddingOracle

iv=0x7dc4885cc38ef6fd0181b78f8f484873
print(str(iv).decode('hex'))
cipher=0xf4a60fdec121df64f0dca2abcb8cb82507b20ee6da804da255714b7b588329b8b095d3e121caad3fe044d4bea33b1c600a542b01bd344fe3126bb129fd26dc979fee0375461ef6fb5652862f3076a207bffa826624260b1bb9b0d4d41a2b8622981c965fcfd72bb13f31b51b150c3e92097a4b408b43dd776ec0c56ccdf30ec5a3581c381e5faafbe2d16d1a24351c204f05bcefae6067aab54b9e34ed681f48ad9bd926102e5f54c6815c6bbf138df7467406287f8569fe1847e379834ae2efe36cf4adff20aca81469861841939b64cb3a448889f2346975cd17ab2580499f4e42bba9503bc443527493328169afc4dfb27dc2de1037603bb7b8126556d38253d3784ea861e0426d2b10214a5a3677e8fa408132b40cf114317acff054d23f17eb2c9ead82b0cac51104f4cfb728c06e978638fa3a896a692bb9435d198537600dd6cc17056dade427a75f1e8ac3026fe378795be2781c01e1e65786a3accfc9bc185e0d43f75c016abeea2234d35360f044d3a68efd6b66fc71e21326d3c33fa1ebd9245238941ac1dfea165f212882d7bd7f16241e8f9d1c06637013ab08a8c58e1e71fbae95c77466cfafcca51b0c7696971636fc56df0436b06e5118b72eeead10766750879c370ca13978b07a69abda0667eb6da93d63cbe8056e2ee382d16f6ac8d9ab86096d463a67570c7c7b48f217c86471285bc5dd1a768c09f9563ae75b0174febec4ac8b959f4f4df8f6e6fe93eb433055a2bcf80097420eb48f84d7524dfc6a3800f21f3c1c9098d6a047447510f41cbc4b6839e577f1f39728fe242dfea3ceec2303ff96d9b0cb5b1bc90304d217bdb6ff2576173619b9c4027864b1d772978015ebb7ac9ef9125e9fb326a5c2d184107c1796fba3cdfe8b8b43d24b02f0038bfb9c8d4486ad50b8bb1511dc330d6758d64608c3a95e1ad6b3634b98b546dfda4f2b25a2397014820ae8a9fb6b0d51d70a6e770bc047822f82e8169063172d4036124496ccfb0b5629154028eee810c897b0c487532d6d3122a8c359cdab89bb8b9f0d239648b1e3ea63543391362efa8bab6b9f2b6beef7713bf7d4f39421e8005553fcd72bbf565946c22d3c421a2ce28e431b145fe0c7d0dccd8705e8d8566161ff25d8a3549773cc172d92aa37ee568f68eaa2762ad73b9c1cb0ea2dbe1915c54824379a459e16863b515ac8c0c424b6d773bb8e0b1e3b25d61bee2d2afb6306a65c68864a5490b30d2a57ee67f7eec4e455422ff331245c1cbfa7763f7135d66d8c30b51be3dd760d3bf4dfdf134d68ce84dc92d78a6f11414e145521822c7b9cb843db656e

REMOTE = 1

if REMOTE:
    p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1478)
    print(p.recvuntil(":"))
    p.sendline("joe215")
    print(p.recvuntil("Gimme a message:"))
    p.sendline(str(iv) + str(cipher))
    print(p.recvline())