var PublicKey = "CF87D7B4C864F4842F1D337491A48FFF54B73A17300E8E42FA365420393AC0346AE55D8AFAD975DFA175FAF0106CBA81AF1DDE4ACEC284DAC6ED9A0D8FEB1CC070733C58213EFFED46529C54CEA06D774E3CC7E073346AEBD6C66FC973F299EB74738E400B22B1E7CDC54E71AED059D228DFEB5B29C530FF341502AE56DDCFE9";
var RSA = new RSAKey();
RSA.setPublic(PublicKey, "10001");
var PublicTs="1466840867";

var Res = RSA.encrypt(S('pp').value + '\n' + document.form1.ts.value + '\n');
if (Res )
{
if (document.form1.chg.value == 1)
{
document.form1.p.value = hex2b64(Res);
}
else
{
if (document.form1.ppp.value != "")
{
document.form1.p.value = document.form1.ppp.value;
}
else
{
document.form1.p.value = hex2b64(Res);
}
}
}