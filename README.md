# Obfuscator for Python

*This code is a work-in-progress prototype! Proper documentation is not yet written!*

For now it is able to rename local variables, definitions, attributes, parameters
that can be assumed to be private to the module (all their uses should be inside the
obfuscated script and can be renamed as well). The idea is to remove some degree of
information from the script without changing its behaviour. The obfuscated script can
be published to allow execution without making it unnecessarily easy to understand and
modify it.

There are some limitations:

 - `getattr()`/`setattr()`/`hasattr()` etc. will not work for renamed attributes
 - Access to namespaces and attribute dictionaries will see the renamed identifiers.
   This affects `locals()`, `globals()`, `__dict__` etc.
 - Removing a local variable (with `del`) to access a variable with the same name in a
   parent scope will not work.
 - ... there is more to be written!
