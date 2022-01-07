"""
CodeLibrary.hashlib_eg
~~~~~~~~~~~~~~~~~~~~~~~

Function: 用于加密相关的操作，代替了md5模块和sha模块，主要提供md5(), sha1(), sha224(), sha256(), sha384(), and sha512()算法

Crater: lin
CreateDate: 2021-12-30
"""

import hashlib

# ######## md5 ########
hash = hashlib.md5()
# help(hash.update)
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())
print(hash.digest())


######## sha1 ########

hash = hashlib.sha1()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha256 ########

hash = hashlib.sha256()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())


# ######## sha384 ########

hash = hashlib.sha384()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())


##### 加盐 ######
# ######## md5 ########

hash = hashlib.md5(bytes('898oaFs09f',encoding="utf-8"))
hash.update(bytes('admin',encoding="utf-8"))
print(hash.hexdigest())

#python内置还有一个 hmac 模块，它内部对我们创建 key 和 内容 进行进一步的处理然后再加密

import hmac

h = hmac.new(bytes('898oaFs09f',encoding="utf-8"))
h.update(bytes('admin',encoding="utf-8"))
print(h.hexdigest())
