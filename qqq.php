<html>
<head>
<meta http-equiv="Content-Language" content="ar-ma">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1256">
<CENTER><img src="cnd.gif" alt="Le Centre National de Documentation" border="0" WIDTH="775" HEIGHT="79"></a></td>
</CENTER>
<?php

$err=0;
?>
<title>COLLECTE/PERIODIQUE </title>
</head>
<body background="back.gif" text="#0c3173" link="#FFFFFF" vlink="#FFFFFF" alink="#00bb00" >


<table width="100%">
<tr>
<td width="30%"><center><h3><b><a href="index.php3"><font color="#0c3173">Accueil</a></b></h3></center></td>
<td width="40%"><center><h3><b><a href="view.php3"><font color="#0c3173">Editer</a></b></h3></center></td>
<td width="30%"><center><h3><b><a href="recherche.php3"><font color="#0c3173">Recherche</a></b></h3></center></td>
</tr>
</table>


<form method="post" action="search.php3" name="form">
<table width="100%" border="0" >
<tr>
<td width="20%">Titre de contr�le</td>
<td width="50%">
<input type="text" name="titr" size="80" maxlength="255"></td>
<td width="30"><input type="submit" name="ok"
value="Chercher"></td>
</tr>
</table >
</form>
<hr size=2 >
<table width="100%">
<tr>
<td width=90%>
<center><FONT SIZE=5 > <b>ARTICLE</b></font><center></td>
<td width=10% align="right"><a href="nperiodique.php3" ><font color="#0c3173">Non&nbsp;Periodique>></a></td>
</tr>
</table><br><br>

<?php

require("config.php3");
require("functions.php3");


//connexion a la base
$db=mysql_connect($dbhost,$dblogin,$dbpass) or die("Connexion impossible");
mysql_select_db($dbname,$db);


if(isset($envoyer)){

//Calculer l'erreur
if($isbn==NULL)
 $err=2;
else{
 $query_string  = "SELECT * FROM doc WHERE n_enregistrement= \"$isbn\" ";
 $result = mysql_query($query_string,$db);
 if (mysql_num_rows($result)!=0)
 $err=1;
 }


if($err)
{

// Debut formulaire
if($err==2)
 echo"<font color=red size=4>Vous avez oublie de remplir le N d'enregistrement, veuillez le remplir?</font>";

if($err==1)
echo"<font color=red size=4>le N d'enregistrement que vous avez entre  existe deja,veuillez le changer?</font>";

$srchnames = explode('\\', "$src");
$src="";
$n=count($srchnames);
for($i=0;$i<$n;$i++)
{
$src=$src."$srchnames[$i]";
}
?>
<form method="post" action="periodique.php3" name="form12">
<input type=hidden name=radio1 value=p> </td></tr>

<table width="100%" border="0" >

<tr>
<td width="11%">N� Enregistrement</td>
<td width="55%">
<input type="text" name="isbn" maxlength="12"
size="12"> /2003
</td>
</tr>

<tr>
<td width="11%">Titre Article*</td>
<td width="55%">
<input type="text" name="stitre" size="100"
maxlength="255" value="<?php echo"$stitre"; ?>">
</td>
</tr>

<tr>
<td width="11%">Auteur/Collectivite</td>
<td width="55%">
<input type="text" name="auteur" maxlength="255"
size="100" value="<?php echo"$auteur"; ?>">
</td>
</tr>

<tr>
<td width="11%">Titre Source** </td>
<td width="55%">
<input type="text" name="titre" size="100" maxlength="255" value="<?php echo"$titre"; ?>"><br>Titre du document generique</td>
</tr>

<tr>
<td width="11%">Volume</td>
<td width="55%">
<table width="20%" border="0" >
<tr>
<td  width="9%"  align="right"><input type="text" name="vol" size="10" maxlength="25" value=<?php echo"$vol"; ?>></td>
<td  width="9%" align="right">Tome</td>
<td  width="9%" ><input type="text" name="tom" size="10" maxlength="25" value=<?php echo"$tom"; ?>></td>
<td  width="9%" align="right">N�</td>
<td  width="9%" > <input type="text" name="num"  size="10" maxlength="25" value=<?php echo"$num"; ?>></td>
</tr>
</table>
</td></tr>



<tr>
<td width="11%" >Date d'edition</td>
<td width="55%" align="left"><input type="text" name="dat_edit" size=10 maxlength="10" value=<?php echo"$dat_edit"; ?>>(ex: 2003-01-01)</td>
</tr>

<tr>
<td width="11%">Pagination   <b>p.</b></td>
<td width="55%" align="left"><input type="text" name="pages" size="30" maxlength="30" value=<?php echo"$pages"; ?>>
(ex: 20-25)</td>
</tr>

<tr>
<td width="11%">Domaine:</td>
<td width="55%"><?php  domaine_select($db, 'critere',"$critere") ?></td>
</tr>
<tr>
<td width="11%">Langue:</td>
<td width="55%"><?php  lang1_select('lang',"$lang") ?></td>
</tr>
<tr>
<td width="11%">Source Exp�ditrice</td>
<td width="55%">
<?php  sourceo_select($db, 'src',"$src")?> </td>
</tr>
<tr>
<td width="11%">Type d'acquisition</td>
<td width="55%"><?php type_select($db,'type',"$type") ?></td>
</tr>

<tr>
<td width="11%">Date de reception</td>
<td width="55%">
<input type="text" name="dat_recep" size="10"
maxlength="10" value=<?php echo"$dat_recep"; ?>>(ex: 2003-01-01)</td>
</tr>

<tr>
<td width="11%">Responsable de saisie</td>
<td width="55%">
<input type="text" name="saisi" maxlength="100"
size="50" value="<?php echo"$saisi"; ?>">
</td>
</tr>

<tr>
<td width="11%">Date de saisie</td>
<td width="55%">
<input type="text" name="dat_saisi" size="10"
maxlength="10" value=<?php echo"$dat_saisi"; ?> >(ex: 2003-01-01)</td>
</tr>

<tr>
<td width="11%">Date d'envoi au traitement</td>
<td width="55%">
<input type="text" name="dat_envoi" size="10"
maxlength="10"  value=<?php echo"$dat_envoi"; ?>>(ex: 2003-01-01)</td>
</tr>


</table>
<br><br>
<table width="100%" border="0">
<tr>
<td width="45%">
<div align="center">
<input type="reset" name="reset"
value="Effacer">
</div>
</td>

<td align="right">
<input type="submit" name="envoyer"
value="Ajouter"> </form>
</td>

</tr>
</table>
</body>
</html>
<?php
}
else
{

//Requete d'insertion
$requete1="INSERT INTO
doc(n_enregistrement,titre,titre_article,periodicite,vol,tom,num,n_periodique,pages,domaine,statut,lang)
VALUES('$isbn','$titre','$stitre','$radio1','$vol','$tom','$num','$nperio','$pages','$critere','collecte','$lang')";
$verif1 = mysql_query($requete1,$db);

$requete2="INSERT INTO suivi
(n_enregistrement,datenvoi_t) VALUES ('$isbn','$dat_envoi')";
$verif2 = mysql_query($requete2,$db);


$tab=explode("/",$auteur);
$n=count($tab);
for($i=0;$i<$n;$i++)
{

$requete3="INSERT INTO ecriture(auteur,n_enregistrement)VALUES('$tab[$i]','$isbn')";
$verif3 = mysql_query($requete3,$db);
}
$requete4="INSERT INTO edition(editeur,n_enregistrement,date_edition,ville_edition)VALUES('$editeur','$isbn','$dat_edit','$ville')";
$verif4 = mysql_query($requete4,$db);

$requete5="INSERT INTO fournit(source,n_enregistrement,date_reception,obligation)VALUES('$src','$isbn','$dat_recep','$type')";
$verif5= mysql_query($requete5,$db);

$requete6="INSERT INTO collecte(nomrc,n_enregistrement,datsaisi_c)VALUES('$saisi','$isbn','$dat_saisi')";
$verif6= mysql_query($requete6,$db);
}
}
if($err==0)  {
?>
<form method="post" action="periodique.php3" name="form10">

<input type=hidden name=radio1 value=p>
<table width="100%" border="0" >
<tr>
<td width="11%">N� Enregistrement</td>
<td width="55%">
<input type="text" name="isbn" maxlength="12"
size="12"> /2003
</td>
</tr>

<tr>
<td width="11%">Titre Article*</td>
<td width="55%">
<input type="text" name="stitre" size="100"
maxlength="255">
</td>
</tr>

<tr>
<td width="11%">Auteur/Collectivite</td>
<td width="55%">
<input type="text" name="auteur" maxlength="255"
size="100">
</td>
</tr>

<tr>
<td width="11%">Titre Source**</td>
<td width="55%">
<input type="text" name="titre" size="100" maxlength="255"><br>Titre du document g�nerique</td>
</tr>

<tr>
<td width="11%">Volume</td>
<td width="55%">
<table width="20%" border="0" >
<tr>
<td  width="9%"  align="right"><input type="text" name="vol" size="10" maxlength="25"></td>
<td  width="9%" align="right">Tome</td>
<td  width="9%" ><input type="text" name="tom" size="10" maxlength="25" ></td>
<td  width="9%" align="right">N�</td>
<td  width="9%" > <input type="text" name="num"  size="10" maxlength="25"></td>
</tr>
</table>
</td></tr>

<tr >
<td width="11%" >Date d'edition</td>
<td width="55%" align="left">
<input type="text" name="dat_edit" size=10 maxlength="10">(ex: 2003-01-01)
</td></tr>
<tr>
<td width="11%">Pagination      <b>p.</b></td>
<td width="55%" align="left">
<input type="text" name="pages" size="30" maxlength="30"> (ex: 20-25)
</td>
</tr>

<tr>
<td width="11%">Domaine:</td>
<td width="55%"><?php domaine_select($db, 'critere','-1') ?></td>
</tr>

<tr>
<td width="11%">Langue:</td>
<td width="55%"><?php  lang1_select('lang','-1') ?></td>
</tr>

<tr>
<td width="11%">Source Exp�ditrice</td>
<td width="55%">
<?php  sourceo_select($db, 'src') ?> </td>
</tr>

<tr>
<td width="11%">Type d'acquisition</td>
<td width="55%"><?php type_select($db,'type') ?></td>
</tr>

<tr>
<td width="11%">Date de reception</td>
<td width="55%">
<input type="text" name="dat_recep" size="10"
maxlength="10" >(ex: 2003-01-01)</td>
</tr>

<tr>
<td width="11%">Responsable de Saisie</td>
<td width="55%">
<input type="text" name="saisi" maxlength="100"
size="50">
</td>
</tr>


<tr>
<td width="11%">Date de Saisie</td>
<td width="55%">
<input type="text" name="dat_saisi" size="10"
maxlength="10" >(ex: 2003-01-01)</td>
</tr>

<tr>
<td width="11%">Date d'envoi au traitement</td>
<td width="55%">
<input type="text" name="dat_envoi" size="10"
maxlength="10" >(ex: 2003-01-01)</td>
</tr>

</table>
<br><br>
<table width="100%" border="0">
<tr>
<td width="45%">
<div align="center">
<input type="reset" name="reset"
value="Effacer">
</div>
</td>

<td align="right">
<input type="submit" name="envoyer"
value="Ajouter" ></table> </form>
<?php
}
?>
<table >
<tr>
<th ALIGN="left">* :</th><td> -Extrait d'ouvrage collectif<br>
    -Extrait d'acte de congres<br>-Extrait de periodique
  </td>
<th ALIGN="left">** :</th><td>-Titre periodique<br>-Titre d'acte de congres<br>
-Titre monographie<br> -Titre d'ouvrage collectif<br>

  </td></tr>
  </table>

