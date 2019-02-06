param (
[string]$customer
)
$cred  = New-Object System.Management.Automation.PsCredential("domain\user", (ConvertTo-SecureString "password" -AsPlainText -Force))
$ou = Get-ADOrganizationalUnit -identity $customer 
$ouu = Set-ADObject -ProtectedFromAccidentalDeletion:$false -PassThru $ou
Remove-ADOrganizationalUnit -Confirm:$false -Recursive $ouu 